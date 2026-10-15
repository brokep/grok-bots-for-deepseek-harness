---
name: accessibility-pass
description: "Use when the user asks for an accessibility review, or when a critique turned up contrast, target size, or labeling problems worth a closer look."
---

# Accessibility pass

Part of the Critiquito: Design Critique agent preset.

Inputs: one screen or flow, and the platform. Web, iOS, and Android have different target size rules.

Check in this order:
1. Text contrast against the background it actually sits on. Body text needs 4.5 to 1. Text at 18pt, or 14pt bold, and above needs 3 to 1. Give the ratio you measured or estimated.
2. Non-text contrast. Icons, input borders, focus rings, and chart colors need 3 to 1.
3. Target size. About 44 by 44 points on iOS, 48 by 48 dp on Android, and enough space between adjacent targets anywhere.
4. Color-only meaning. Read the screen in greyscale. Anything that only made sense in color is a finding.
5. Labels. Icon-only buttons need a name. Form fields need a visible label that stays visible, so a placeholder standing in for a label is a finding.
6. Errors. Tied to the field, written in words, never carried by color alone.
7. Text scaling. What breaks at 200 percent, and whether anything that carries meaning truncates.
8. Motion. Autoplay, parallax, and looping animation with no way to stop it.

What a static image cannot tell you: focus order, keyboard traps, screen reader output, and the real semantics underneath. Say so plainly instead of guessing. With a live URL you can check focus order and keyboard access directly, so ask for one when it matters.

Output shape: one line per check marked pass, fail, or not testable. Every fail carries the measured or estimated value, the requirement it missed, and a specific fix, for example a darker value for a label rather than "improve contrast". Close with the two failures that block the most people.

Save under design critiques with the screen name.
