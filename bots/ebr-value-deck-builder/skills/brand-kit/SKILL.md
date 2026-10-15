---
name: brand-kit
description: "Learns the owner's visual brand once from a sample deck or website (palette, type, logo rules, slide shapes) and applies it to every deck without asking again."
---

# brand-kit

Part of the EBR & Value Deck Builder agent preset.

# brand-kit

## When to use

During `getting-started`, when the owner uploads a new template, or when a deck comes back "off brand".

## Learn

From an uploaded pptx or PDF: extract the color palette (primary, secondary, accent, background, text), the fonts and their roles (title, body, caption), the logo variants and where they sit, the title-slide and content-slide layouts, chart styling, and any footer or confidentiality text. From a website: palette and type from the CSS, logo from the header, tone from the copy.

Ask the owner two things only: which logo file to use for light and dark backgrounds, and whether decks are customer-facing by default.

Store the result as one "Brand" profile memory: palette hex values, fonts, logo rules, layout notes, and the default footer.

## Apply

Every deck this bot builds reads the Brand memory before generating. Defaults when nothing is stored: a neutral palette, one sans-serif face, no logo, and a note to the owner that the brand is unset.

## Logo contrast rule

Dark logo on light slides, light logo on dark slides. Never a light logo on a light background or a dark logo on a dark one. If only one logo variant exists, keep every slide background on the side that variant reads on.

## Rules

- Never pull brand assets from a third party's site for the owner's own deck.
- Charts use the palette in order, one series per color, labels on the axes, the data source in the caption.
- No gradients, no drop shadows, no clip art, no emojis on slides.
