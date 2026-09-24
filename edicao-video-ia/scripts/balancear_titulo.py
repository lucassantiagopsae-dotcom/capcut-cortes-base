import argparse
import itertools
import json
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


DANGLING_ENDINGS = {
    "a",
    "ao",
    "aos",
    "com",
    "da",
    "das",
    "de",
    "do",
    "dos",
    "e",
    "em",
    "na",
    "nas",
    "no",
    "nos",
    "ou",
    "para",
    "por",
    "que",
    "se",
}


def partitions(words, line_count):
    for cuts in itertools.combinations(range(1, len(words)), line_count - 1):
        boundaries = (0, *cuts, len(words))
        yield [
            " ".join(words[boundaries[index] : boundaries[index + 1]])
            for index in range(line_count)
        ]


def score_layout(lines, widths):
    widest = max(widths)
    narrowest = min(widths)
    counts = [len(line.split()) for line in lines]
    score = ((widest - narrowest) / max(widest, 1)) * 1000
    score += ((max(counts) - min(counts)) / max(max(counts), 1)) * 180
    if counts[-1] == 1:
        score += 5000
    if widths[-1] < widest * 0.55:
        score += 1800
    for line in lines[:-1]:
        ending = line.lower().rstrip(".,:;!?\"").split()[-1]
        if ending in DANGLING_ENDINGS:
            score += 900
    return score


def choose_layout(text, font_path, min_font, max_font, max_width, padding_x):
    words = re.sub(r"\s+", " ", text).strip().split(" ")
    if not words or words == [""]:
        raise ValueError("O titulo nao pode ficar vazio")

    scratch = Image.new("RGBA", (10, 10), (0, 0, 0, 0))
    draw = ImageDraw.Draw(scratch)
    line_counts = [1, 2] if len(words) <= 3 else [2, 3, 4]
    content_width = max_width - padding_x * 2

    for line_count in line_counts:
        if line_count > len(words):
            continue
        for font_size in range(max_font, min_font - 1, -1):
            font = ImageFont.truetype(str(font_path), font_size)
            candidates = []
            for lines in partitions(words, line_count):
                boxes = [draw.textbbox((0, 0), line, font=font) for line in lines]
                widths = [box[2] - box[0] for box in boxes]
                if max(widths) <= content_width:
                    candidates.append((score_layout(lines, widths), lines, boxes, widths))
            if candidates:
                _, lines, boxes, widths = min(candidates, key=lambda item: item[0])
                return font, font_size, lines, boxes, widths

    raise ValueError(
        f"O titulo nao cabe entre {min_font} px e {max_font} px em ate quatro linhas"
    )


def render_png(path, font, lines, boxes, widths, padding_x, padding_y, line_gap):
    heights = [box[3] - box[1] for box in boxes]
    width = max(widths) + padding_x * 2
    height = sum(heights) + line_gap * (len(lines) - 1) + padding_y * 2
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    y = padding_y
    for line, box, line_width, line_height in zip(lines, boxes, widths, heights):
        x = (width - line_width) / 2
        draw.text((x, y - box[1]), line, font=font, fill=(255, 255, 255, 255))
        y += line_height + line_gap
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)
    return width, height


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True)
    parser.add_argument("--font", type=Path, required=True)
    parser.add_argument("--min-font", type=int, default=72)
    parser.add_argument("--max-font", type=int, default=88)
    parser.add_argument("--max-width", type=int, default=900)
    parser.add_argument("--padding-x", type=int, default=18)
    parser.add_argument("--padding-y", type=int, default=18)
    parser.add_argument("--line-gap", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.min_font > args.max_font:
        parser.error("--min-font nao pode ser maior que --max-font")
    if args.max_width <= args.padding_x * 2:
        parser.error("--max-width precisa comportar o padding horizontal")
    if not args.font.is_file():
        parser.error(f"Fonte nao encontrada: {args.font}")

    font, size, lines, boxes, widths = choose_layout(
        args.text,
        args.font,
        args.min_font,
        args.max_font,
        args.max_width,
        args.padding_x,
    )
    width = max(widths) + args.padding_x * 2
    height = None
    if args.output:
        width, height = render_png(
            args.output,
            font,
            lines,
            boxes,
            widths,
            args.padding_x,
            args.padding_y,
            args.line_gap,
        )

    print(
        json.dumps(
            {
                "font_size": size,
                "lines": lines,
                "line_widths": widths,
                "box_width": width,
                "box_height": height,
                "output": str(args.output) if args.output else None,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
