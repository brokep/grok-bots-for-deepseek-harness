---
name: copy-review
description: "Use to score a piece of copy against the principles doc and the voice profile, whether this bot wrote it or not. Eight dimensions scored 1 to 5 with the deciding line quoted, a verdict, the three edits that move it most, and a rewrite of the weakest section only."
---

# copy-review

Part of the Product Marketer agent preset.

# Copy review

## When to use
Use when the user wants a piece scored against the principles: their own live page, a draft from someone else, an email, an ads set, or copy this bot wrote against an older rev.

## Inputs
The piece, pasted, linked, or a page to read. The current principles doc and the voice profile. When the piece is a live page, read it and screenshot it before scoring.

## Steps
1. Re-read /workspace/marketing/principles.md, /workspace/marketing/voice-profile.md, and the banned-word list. Read the anti-slop skill for the banned shapes.
2. Score the piece 1 to 5 on each of these, with one line of reason each, quoting the line that decided it:
   - Leads with the customer promise, not with the company
   - Follows the hierarchy: brand line, customer promise, supporting lines
   - Concrete product observations over brand adjectives
   - Every claim has a source in the principles doc or on the site
   - Voice matches the voice profile, rule by rule
   - Slop: banned words, banned shapes from anti-slop, hype with no evidence. Count them and list them.
   - Length and format fit the placement, including platform limits for ads
   - One clear action, in the right place
3. Total the score out of 40 and say in one line whether this ships as is, needs the three edits below, or needs a rewrite.
4. Name the three edits that move it most, each with the exact line before and after.
5. Rewrite only the single weakest section, in full. Never rewrite the whole piece unless the user asks.
6. Run the anti-slop skill over the rewritten section and over the after lines in step 4 before delivering. Every review pass ends there.

## Output
The scores with reasons, the verdict line, the three edits, the one rewritten section, and the screenshot when there was a page.

## Never
Score against your taste instead of the doc and the voice profile. Soften a failing score. Rewrite everything unasked. Invent a fact to patch a claim that has no source.
