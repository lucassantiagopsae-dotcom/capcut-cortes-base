#!/usr/bin/env python3
"""Audit long low-energy spans in final short-form videos with FFmpeg."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


SILENCE_END = re.compile(
    r"silence_end:\s*(?P<end>[0-9.]+)\s*\|\s*silence_duration:\s*(?P<duration>[0-9.]+)"
)


def media_duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def detect_silences(path: Path, noise_db: float, minimum: float) -> list[dict[str, float]]:
    result = subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-i",
            str(path),
            "-af",
            f"silencedetect=n={noise_db}dB:d={minimum}",
            "-f",
            "null",
            "NUL",
        ],
        capture_output=True,
        text=True,
    )
    output = result.stderr + "\n" + result.stdout
    spans = []
    for match in SILENCE_END.finditer(output):
        end = float(match.group("end"))
        duration = float(match.group("duration"))
        spans.append({"start": end - duration, "end": end, "duration": duration})
    return spans


def collect_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    return sorted(path for path in target.rglob("*.mp4") if path.is_file())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path)
    parser.add_argument("--noise-db", type=float, default=-35.0)
    parser.add_argument("--review-seconds", type=float, default=0.60)
    parser.add_argument("--block-seconds", type=float, default=0.90)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--fail-on-block", action="store_true")
    args = parser.parse_args()

    files = collect_files(args.target)
    if not files:
        raise SystemExit(f"No MP4 files found in {args.target}")

    reports = []
    for path in files:
        duration = media_duration(path)
        silences = detect_silences(path, args.noise_db, args.review_seconds)
        blocked = [span for span in silences if span["duration"] >= args.block_seconds]
        review = [span for span in silences if span["duration"] < args.block_seconds]
        reports.append(
            {
                "file": str(path.resolve()),
                "duration": duration,
                "status": "block" if blocked else ("review" if review else "pass"),
                "longest_silence": max((span["duration"] for span in silences), default=0.0),
                "blocked_spans": blocked,
                "review_spans": review,
                "note": "Low energy is a candidate, not proof that an expressive pause should be cut.",
            }
        )

    payload = {
        "noise_db": args.noise_db,
        "review_seconds": args.review_seconds,
        "block_seconds": args.block_seconds,
        "files": reports,
    }
    rendered = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered)
    return 2 if args.fail_on_block and any(item["status"] == "block" for item in reports) else 0


if __name__ == "__main__":
    raise SystemExit(main())
