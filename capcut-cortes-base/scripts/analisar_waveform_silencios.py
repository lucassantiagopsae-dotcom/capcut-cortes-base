from __future__ import annotations

import argparse
import csv
import json
import math
import subprocess
import sys
from array import array
from datetime import datetime
from pathlib import Path
from typing import Any


def parse_seconds(value: str | None) -> float | None:
    if not value:
        return None
    value = value.strip()
    if ":" not in value:
        return float(value)
    parts = [float(part) for part in value.split(":")]
    if len(parts) == 2:
        minutes, seconds = parts
        return minutes * 60 + seconds
    if len(parts) == 3:
        hours, minutes, seconds = parts
        return hours * 3600 + minutes * 60 + seconds
    raise ValueError(f"Timecode invalido: {value}")


def extract_audio_f32le(video_path: Path, start: float | None, end: float | None, sample_rate: int) -> array:
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error"]
    if start is not None:
        cmd.extend(["-ss", f"{start:.6f}"])
    cmd.extend(["-i", str(video_path)])
    if start is not None and end is not None:
        cmd.extend(["-t", f"{max(0.0, end - start):.6f}"])
    elif end is not None:
        cmd.extend(["-t", f"{end:.6f}"])
    cmd.extend(["-vn", "-ac", "1", "-ar", str(sample_rate), "-f", "f32le", "-"])
    raw = subprocess.check_output(cmd)
    samples = array("f")
    samples.frombytes(raw)
    if sys.byteorder != "little":
        samples.byteswap()
    return samples


def window_dbfs(samples: array, sample_rate: int, window_ms: int) -> list[dict[str, float]]:
    window = max(1, round(sample_rate * window_ms / 1000))
    rows: list[dict[str, float]] = []
    for start in range(0, len(samples), window):
        chunk = samples[start : start + window]
        if not chunk:
            continue
        square_sum = sum(float(value) * float(value) for value in chunk)
        rms = math.sqrt(square_sum / len(chunk))
        dbfs = 20 * math.log10(max(rms, 1e-9))
        rows.append(
            {
                "start": start / sample_rate,
                "end": min(len(samples), start + window) / sample_rate,
                "dbfs": dbfs,
            }
        )
    return rows


def detect_low_energy(
    windows: list[dict[str, float]],
    threshold_db: float,
    min_silence_ms: int,
    offset_seconds: float,
) -> list[dict[str, float]]:
    spans: list[dict[str, float]] = []
    current_start: float | None = None
    current_end: float | None = None
    db_values: list[float] = []
    min_duration = min_silence_ms / 1000

    for window in windows:
        if window["dbfs"] <= threshold_db:
            if current_start is None:
                current_start = window["start"]
                db_values = []
            current_end = window["end"]
            db_values.append(window["dbfs"])
            continue

        if current_start is not None and current_end is not None:
            duration = current_end - current_start
            if duration >= min_duration:
                spans.append(
                    {
                        "start": current_start + offset_seconds,
                        "end": current_end + offset_seconds,
                        "duration": duration,
                        "avg_dbfs": sum(db_values) / len(db_values),
                    }
                )
        current_start = None
        current_end = None
        db_values = []

    if current_start is not None and current_end is not None:
        duration = current_end - current_start
        if duration >= min_duration:
            spans.append(
                {
                    "start": current_start + offset_seconds,
                    "end": current_end + offset_seconds,
                    "duration": duration,
                    "avg_dbfs": sum(db_values) / len(db_values),
                }
            )
    return spans


def fmt(seconds: float) -> str:
    millis = round(seconds * 1000)
    total_seconds, ms = divmod(millis, 1000)
    minutes, sec = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{sec:02d}.{ms:03d}"


def safe_stem(path: Path) -> str:
    return "".join(char if char.isalnum() or char in "-_" else "-" for char in path.stem).strip("-") or "video"


def write_outputs(
    video_path: Path,
    spans: list[dict[str, float]],
    config: dict[str, Any],
    out_dir: Path,
) -> dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    base = out_dir / f"{safe_stem(video_path)}_waveform_silencios_{stamp}"
    json_path = base.with_suffix(".json")
    csv_path = base.with_suffix(".csv")
    md_path = base.with_suffix(".md")

    json_path.write_text(
        json.dumps({"video": str(video_path), "config": config, "spans": spans}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["start", "end", "duration", "avg_dbfs", "start_tc", "end_tc"])
        writer.writeheader()
        for span in spans:
            writer.writerow(
                {
                    "start": f"{span['start']:.6f}",
                    "end": f"{span['end']:.6f}",
                    "duration": f"{span['duration']:.6f}",
                    "avg_dbfs": f"{span['avg_dbfs']:.2f}",
                    "start_tc": fmt(span["start"]),
                    "end_tc": fmt(span["end"]),
                }
            )

    lines = [
        f"# Analise de waveform - {video_path.name}",
        "",
        f"- Video: `{video_path}`",
        f"- Threshold: `{config['threshold_db']} dBFS`",
        f"- Janela: `{config['window_ms']}ms`",
        f"- Silencio minimo: `{config['min_silence_ms']}ms`",
        f"- Trechos candidatos: `{len(spans)}`",
        "",
        "| # | Inicio | Fim | Duracao | Media dBFS | Uso no corte |",
        "|---:|---|---|---:|---:|---|",
    ]
    for index, span in enumerate(spans, start=1):
        lines.append(
            f"| {index} | `{fmt(span['start'])}` | `{fmt(span['end'])}` | "
            f"`{span['duration']:.3f}s` | `{span['avg_dbfs']:.1f}` | candidato a revisar |"
        )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    return {"json": str(json_path), "csv": str(csv_path), "md": str(md_path)}


def main() -> None:
    parser = argparse.ArgumentParser(description="Detecta trechos de baixa energia em video/audio.")
    parser.add_argument("video")
    parser.add_argument("--start", default=None, help="Inicio em segundos ou HH:MM:SS.mmm")
    parser.add_argument("--end", default=None, help="Fim em segundos ou HH:MM:SS.mmm")
    parser.add_argument("--out-dir", default=None, help="Pasta de saida. Padrao: ./waveform_analises")
    parser.add_argument("--sample-rate", type=int, default=16000)
    parser.add_argument("--window-ms", type=int, default=20)
    parser.add_argument("--threshold-db", type=float, default=-42.0)
    parser.add_argument("--min-silence-ms", type=int, default=180)
    args = parser.parse_args()

    video_path = Path(args.video).expanduser().resolve()
    if not video_path.is_file():
        raise FileNotFoundError(video_path)

    start = parse_seconds(args.start)
    end = parse_seconds(args.end)
    offset = start or 0.0
    out_dir = Path(args.out_dir).expanduser().resolve() if args.out_dir else Path.cwd() / "waveform_analises"

    samples = extract_audio_f32le(video_path, start, end, args.sample_rate)
    windows = window_dbfs(samples, args.sample_rate, args.window_ms)
    spans = detect_low_energy(windows, args.threshold_db, args.min_silence_ms, offset)
    config = {
        "start": start,
        "end": end,
        "sample_rate": args.sample_rate,
        "window_ms": args.window_ms,
        "threshold_db": args.threshold_db,
        "min_silence_ms": args.min_silence_ms,
    }
    paths = write_outputs(video_path, spans, config, out_dir)
    print(json.dumps({"spans": len(spans), "paths": paths}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

