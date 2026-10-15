---
name: houseplant-care-card
description: "use this when making a generalized species care card after the owner named the plant and said yes, including first-run when render.py did not copy"
---

# Houseplant care card

Part of the Flora agent preset.

---
name: Houseplant care card
description: >-
  use this when making a generalized species care card after the owner named the
  plant and said yes, including first-run when render.py did not copy
---
# Houseplant care card

Use this when making a generalized species care card after the owner has named the plant (or accepted an ID guess) and said yes to a card. The helper script does not copy with a template. On first-run, write `render.py` from this skill if it is missing. Do not generate a card until they ask.

## Size and files

- Portrait **1080×1440** (3:4), PNG
- Save as `/workspace/plants/cards/<slug>.png`
- Reuse that file if the same species already has a card
- Helper: `/workspace/notes/templates/flora-care-card/render.py` (write it from this skill if missing)
- Blank layout: `/workspace/plants/cards/_template.png` (created by running the helper with no portrait)

## Look

Cream paper `#f6f0e6`, terracotta header bar with the words CARE CARD, one rounded plant portrait on top, typeset facts below in DejaVu Serif. Same colors as the private journal. Not a spreadsheet. Not a poster slogan card.

## What is on the card (species, not this owner's log)

1. Common name they use
2. Scientific name if looked up
3. Light
4. Water
5. Fertilizer
6. Soil / mix (ask if unknown; never invent)
7. Winter
8. Watch for (short, from the source)
9. Source line (Wikipedia, RHS, or the named page)

Do **not** put last-watered, their window, or their city on the card. That belongs in the journal.

## How to generate

1. Look up the species on a named source. Missing source ≠ invented fact.
2. Ask if they want a care card. If no, stop.
3. Warn that a card uses more weekly usage than a text note. No dollar amount.
4. Generate **only the plant portrait** with the built-in image generator: 1:1 or 4:3, no letters, no watermark, cream/terracotta/leaf-green, the species as a simple houseplant illustration. Do not draw care text in the generated image (models mangle letters).
5. If `render.py` is missing, write it from the helper source below.
6. Run `render.py` to typeset the facts onto 1080×1440 and drop the portrait into the top slot.
7. Save under `cards/`, show the PNG, and add it to the journal page.
8. No extra plugin. Higgsfield is optional and not required. Do not generate unasked cards or a fake ID photo.

## Helper source

This Python file does not copy with a template. If it is missing, write it to `/workspace/notes/templates/flora-care-card/render.py` exactly.

```python
#!/usr/bin/env python3
"""Compose a 1080x1440 Flora care card. Portrait is a generated image; all type is real text."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1440
PAPER = (246, 240, 230)
INK = (28, 24, 20)
MUTED = (107, 94, 82)
POT = (193, 95, 42)
LEAF = (61, 107, 50)
LINE = (226, 213, 196)
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

FIELDS = (
    ("Light", "light"),
    ("Water", "water"),
    ("Fertilizer", "fertilizer"),
    ("Soil", "soil"),
    ("Winter", "winter"),
    ("Watch for", "watch"),
)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    words = (text or "—").split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or ["—"]


def render(card: dict, portrait_path: str | None, out_path: str) -> Path:
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 88), fill=POT)
    title_f = font(SERIF_B, 36)
    tw = d.textlength("CARE CARD", font=title_f)
    d.text(((W - tw) / 2, 24), "CARE CARD", font=title_f, fill=(255, 250, 243))

    slot = (48, 112, W - 48, 112 + 520)
    d.rounded_rectangle(slot, radius=24, fill=(232, 221, 207))
    if portrait_path and Path(portrait_path).exists():
        port = Image.open(portrait_path).convert("RGB")
        box_w, box_h = slot[2] - slot[0], slot[3] - slot[1]
        port = port.resize((box_w, box_h), Image.Resampling.LANCZOS)
        mask = Image.new("L", (box_w, box_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, box_w, box_h), radius=24, fill=255)
        im.paste(port, (slot[0], slot[1]), mask)
    else:
        f = font(SERIF, 28)
        msg = "Plant portrait"
        d.text((W / 2 - d.textlength(msg, font=f) / 2, 340), msg, font=f, fill=LEAF)

    y = 660
    name_f = font(SERIF_B, 44)
    sci_f = font(SERIF, 26)
    name = card.get("common_name") or "Plant"
    d.text((56, y), name, font=name_f, fill=INK)
    y += 58
    sci = card.get("scientific_name") or ""
    if sci:
        d.text((56, y), sci, font=sci_f, fill=MUTED)
        y += 44
    y += 8
    d.line((56, y, W - 56, y), fill=LINE, width=2)
    y += 24

    label_f = font(SANS, 20)
    body_f = font(SERIF, 28)
    max_w = W - 112
    for label, key in FIELDS:
        val = card.get(key) or "—"
        d.text((56, y), label.upper(), font=label_f, fill=POT)
        y += 28
        for line in wrap(d, val, body_f, max_w)[:3]:
            d.text((56, y), line, font=body_f, fill=INK)
            y += 36
        y += 10
        if y > H - 120:
            break

    src = card.get("source") or "Named source required"
    d.line((56, H - 88, W - 56, H - 88), fill=LINE, width=2)
    d.text((56, H - 68), src, font=font(SANS, 20), fill=MUTED)

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "PNG")
    return out


if __name__ == "__main__":
    sample = {
        "common_name": "Species name",
        "scientific_name": "Scientific name if known",
        "light": "Bright, indirect light. Named source, not a guess.",
        "water": "When the top of the mix is dry. Empty the saucer.",
        "fertilizer": "Growing season only, from a named mix. Skip in winter unless the source says otherwise.",
        "soil": "Ask if unknown. Do not invent a mix.",
        "winter": "Water less unless a named source says otherwise.",
        "watch": "Yellow leaves, soggy mix, stretch toward a window.",
        "source": "Source: Wikipedia or RHS — replace with the real page.",
    }
    p = render(sample, None, "/workspace/plants/cards/_template.png")
    print("wrote", p, p.stat().st_size)
```
