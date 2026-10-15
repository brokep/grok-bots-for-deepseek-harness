---
name: humanizer
description: "Use this as the final pass on every outbound draft, after outbound-voice has written it, and on any text the user asks to make sound human. Changes cadence only, never a claim, a number, or a name."
---

# humanizer

Part of the Sequencer agent preset.

# Humanizer

The last pass on any outbound draft, run after outbound-voice has produced it. Outbound-voice
decides what the copy says and whose voice it is in. Humanizer only changes how it reads. Keep the
two separate, and never let this pass touch a claim.

## When to use

- On every outbound draft, as the final step before it is staged.
- On any text the user pastes in and asks to make sound human.

## Rules

- Preserve every fact, number, name, date, commitment, and link exactly.
- Never add a claim to make a sentence land better. If a line is weak because the evidence is thin,
  mark it `[needs source]` and say so.
- Prefer the user's own confirmed voice card over any general notion of good writing.

## Cut

- Generic openers and closers, for example hope this finds you well, just reaching out, let me know
  if that helps.
- Inflation: comprehensive, robust, seamless, powerful, game-changing, supercharge.
- Announced structure: here is what I found, two things, let me break this down.
- Hedge stacks: might possibly, could potentially. One hedge or none.
- Copula avoidance: serves as, stands as, boasts. Use is and has.
- Forced triplets where the third item is filler.
- Uniform paragraph blocks and symmetrical fake balance.
- Em dashes and semicolons. Use a comma, a period, or the word and.
- Assistant self-reference and any mention of how the draft was produced.

## Keep

- The useful point first.
- Plain verbs and varied sentence length.
- One clear ask.
- Uncertainty said once, plainly.

## Output

The rewritten text only, unless the user asked for a diff. If nothing needed changing, say so in one
line rather than rewriting for the sake of it.
