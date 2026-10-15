---
name: design-token-audit
description: "Use when the user asks about their variables, styles, or design tokens: hardcoded values, near-duplicates, missing modes, contrast, or drift against the code."
---

# Design token audit

Part of the figma bro agent preset.

Inputs: the file's variables and styles, or a pasted token export such as JSON, a Style Dictionary file, a Tailwind config, or a block of CSS variables.

1. Pull every color, type, spacing, radius, and shadow token with its name and value, and note which collections and modes exist (light, dark, density, brand).
2. Find hardcoded values: colors, type sizes, and spacings used raw where a token already exists. Report the value, where it is used, and the token it should be.
3. Find near-duplicates: two colors a hair apart, three spacing values inside 2px of each other, type styles that differ only in line height. These are what quietly break a system.
4. Check the modes. A token present in one mode should exist in the others. Name every gap.
5. Check text against its background for contrast. Give the ratio and whether it clears 4.5:1 for body text and 3:1 for large text. Never say a pair passes without the number.
6. When the code side is available through a repo, a Tailwind config, or a paste, diff the Figma names and values against the code ones and list what does not match in either direction.

Output: the token table, the hardcoded list, the near-duplicate list, the mode gaps, the contrast failures, and a short rename or merge plan ordered by what it fixes.

Fallback: a file with no variables gets its styles audited instead, plus one plain line on what staying off variables costs them.

Save under design handoff.
