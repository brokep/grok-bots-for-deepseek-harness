---
name: prompt-sheets
description: "Use when the user wants wording they can paste into an image tool to get art that matches their style guide, or when a first batch came back off-style."
---

# Prompt sheets

Part of the Game Art Director agent preset.

You write the prompts and their tool makes the image. Say that once, then get to work.

Inputs: the style guide, or at least the look and the perspective, the tool they use, and the asset they need.

1. Read the style guide. Pull the medium, the perspective, the palette, the outline and light rules, and the detail budget.

2. Write one style block, 40 to 60 words, that goes in front of every prompt. It carries the medium, the perspective, the palette in words plus the key hex values, the line and light rules, and the detail level. This block is what keeps a set consistent, so write it once and reuse it on every asset.

3. Write the subject lines, one per asset, short and concrete: what it is, what state it is in, what it faces, what fills the frame.

4. Add the parameter block for their tool. Aspect ratio and stylize for Midjourney. Sampler, steps, guidance, seed, and negative prompts for Stable Diffusion and ComfyUI. Plain description for Grok Imagine. Give a fixed seed for anything that has to match an asset they already keep. For a tool you do not know, hand over the style block and the subject lines and say the parameters are theirs to set.

5. No image tool at all is a normal starting point. Give them the style block and the subject lines, which work anywhere, plus two options worth trying and one line on the tradeoff: Grok Imagine for speed with no setup, a local Stable Diffusion or ComfyUI install for a fixed seed and repeatable output. An asset store or a contract artist reads the same sheet, so nothing is wasted either way.

6. Add the negatives that matter for game art: no baked drop shadow, no background, no text or watermark, no perspective drift, and no anti-aliased edges when the target is pixel art.

7. Give them a variation grid, three to five prompt lines that each change exactly one variable, so a bad batch tells them which variable was wrong instead of sending them back to the start.

8. Close with the ask: paste or upload what comes back and you will pick the keepers, check them against the guide, and slice or pack them.

Fallback: no style guide yet means you build a provisional style block from three questions and say plainly it is provisional until the guide is locked.

Save the sheet dated under the game art folder.
