#!/usr/bin/env python3
"""Render the social preview from a live wxiu.com Browser capture."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "wxiu-kof98-live.jpg"
OUTPUT = ROOT / "assets" / "promo-codex-wxiu-v0.2.0.png"
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)


def main() -> None:
    canvas = Image.new("RGB", (1600, 900), "#0b0d12")
    draw = ImageDraw.Draw(canvas)

    draw.rectangle((0, 0, 1600, 72), fill="#171a21")
    draw.line((0, 71, 1600, 71), fill="#343946", width=1)
    draw.text((34, 20), "CODEX", font=font(28, bold=True), fill="white")
    draw.text((1402, 24), "Built-in Browser", font=font(20), fill="#b8c0cc")

    draw.rounded_rectangle((28, 108, 354, 856), radius=18, fill="#151922", outline="#343946", width=2)
    draw.text((54, 140), "wxiu-game-launcher", font=font(22, bold=True), fill="white")

    draw.rounded_rectangle((54, 207, 326, 279), radius=12, fill="#232a37", outline="#3d4657", width=2)
    draw.text((72, 228), "Open King of Fighters '98", font=font(20), fill="#e9edf5")

    draw.rounded_rectangle((54, 312, 326, 406), radius=12, fill="#17264a")
    draw.text((72, 335), "Opening it in the", font=font(21), fill="#bcd0ef")
    draw.text((72, 367), "built-in Browser...", font=font(21), fill="#bcd0ef")

    draw.text((72, 500), "ARCADE COMPANION", font=font(17, bold=True), fill="#9ba8ba")
    for y, label in ((542, "Live lobby radar"), (578, "Game roulette"), (614, "Daily challenges"), (650, "Streaks + badges")):
        draw.ellipse((72, y + 7, 80, y + 15), fill="#38bdf8")
        draw.text((94, y), label, font=font(20), fill="#dbe5f5")

    draw.text((72, 778), "OPEN SOURCE", font=font(17, bold=True), fill="#7dd3fc")

    game = Image.open(SOURCE).convert("RGB")
    game.thumbnail((1140, 642), Image.Resampling.LANCZOS)
    frame = Image.new("RGB", (1140, 642), "#090b10")
    frame.paste(game, ((1140 - game.width) // 2, (642 - game.height) // 2))
    canvas.paste(frame, (400, 145))
    draw.rounded_rectangle((399, 144, 1541, 788), radius=10, outline="#4c566a", width=2)
    draw.text((420, 104), "wxiu.com  /  King of Fighters '98", font=font(23), fill="#e5e7eb")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUTPUT, optimize=True)
    print(OUTPUT)


if __name__ == "__main__":
    main()
