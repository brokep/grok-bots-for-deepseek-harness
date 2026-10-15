---
name: ui-copy-pass
description: "Use when the user wants the words on a screen rewritten: buttons, headers, empty states, error messages, tooltips, or onboarding text."
---

# UI copy pass

Part of the Critiquito: Design Critique agent preset.

Inputs: the screen, and who is reading it. A first-timer and a daily user need different words.

1. List every string on the screen with where it sits. Missing strings count too, an empty state with no words is a finding.
2. Rewrite against these rules:
   - A button names the outcome. "Send invite" beats "Submit". "Delete 3 files" beats "OK".
   - An error says what happened and what to do next, in the user's words, with no codes unless support needs them.
   - Cut jargon the product never taught them. Internal model and feature names are the usual offender.
   - One voice and one casing convention. Sentence case unless their system says otherwise.
   - An empty state says what goes here and how to add the first one.
   - Keep the rewrite close to the original length so the layout still holds. Say when a fix needs more room.
3. Never change what a control does to make its label read better. Flag the mismatch instead.
4. Mark the strings you would cut. Most screens carry a line explaining something already obvious.

Output shape: a table with the location, the original string, your rewrite, and one clause on why. Then the strings to cut, and any string you could not read from the image.

When they have a voice guide or a design system, ask for it once and follow it over these rules.

Save the rewrite under design critiques with the screen name.
