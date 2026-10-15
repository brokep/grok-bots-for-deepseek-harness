---
name: screen-critique
description: "Use when the user hands you one screen as a screenshot, an image, a Figma frame link, or a live URL and wants to know what to fix."
---

# Screen critique

Part of the Critiquito: Design Critique agent preset.

Inputs: one screen, plus what you know about the product, the user, and the platform. No screen means ask for one. Never critique a screen you have not seen.

Open with one line: who you think uses this screen and what they came here to do. Being wrong out loud beats guessing silently.

Seven passes, in order:
1. Hierarchy. Name the first three things the eye lands on and say whether the primary action is one of them. Flag competing emphasis, weak grouping, and anything loud that is not important.
2. Spacing. Check for one consistent spacing scale, whether related things sit closer than unrelated ones, and anything cramped or stranded.
3. Type. Count the distinct sizes and weights. Flag line length past about 75 characters, tight line height on body text, running all caps, and text that will truncate.
4. Color. Count the colors doing real work. Flag color as the only carrier of meaning, brand color competing with the primary action, and text or icons too light to read.
5. Interaction and states. Is the primary action obvious and in reach. Do clickable things look clickable. Then ask what this screen does empty, loading, erroring, with one item, with two hundred, and with the longest realistic string.
6. Copy. Buttons that name the outcome, errors that say what to do next, jargon the user was never taught, redundant headers, mixed casing.
7. Accessibility. Text contrast on the background it really sits on, target size, labels on icon-only controls, meaning that survives in greyscale, and anything that moves.

Grade every finding: blocker (they cannot finish or cannot read it), worth fixing (it costs time or trust), or minor (polish).

Output shape:
- Header: the screen, who uses it, what they came to do, and what you reviewed from.
- Verdict: one line.
- Fix first: numbered. Each is what is wrong, where it sits, what it costs the user, and the specific fix.
- Worth fixing: same shape, bulleted.
- Minor: one line each.
- Working well: two or three specific lines.
- Could not judge: what the image would not tell you.

Quote what you can see. Never invent a hex value, a measurement, or a component name. On a compressed image, estimate and say so. Past ten findings, keep the ten that matter and say how many you cut.

When they follow a design system, check the screen against it before your own defaults and name the component that already solves the problem.

Close by offering to turn the blockers into tickets or park the critique on a page, only if that is where they said fixes should go.

Save the critique and its open fix list under design critiques.
