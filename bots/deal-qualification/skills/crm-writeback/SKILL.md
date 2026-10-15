---
name: crm-writeback
description: "Turns an audit into a before/after diff of qualification fields, stage, and an audit note, and applies it only after the owner approves."
---

# crm-writeback

Part of the Deal Inspector agent preset.

# crm-writeback

## When to use

After `stage-gate-audit`, when the owner wants the CRM to reflect what the transcripts support.

## Steps

1. Read the current value of each qualification field, the stage, the next step, and the close date.
2. Build the diff from the scorecard: fill a field only when the criterion is Met (quote the evidence in the note), clear or flag a field that the transcript contradicts, propose the stage the verdict supports, and attach the audit summary as an activity or note dated today.
3. Present the diff as a table: Field, Before, After, Evidence. Then ask in plain text: "Apply these changes? Say yes, or name the rows to skip."

## Apply

Only after an explicit yes in this conversation, never in an unattended run. Apply exactly the approved rows and confirm with links. If the CRM connection is read-only, hand the owner the diff to apply by hand and say so.

## Rules

- Never delete records. Never change ownership, amount, or close date unless the transcript stated them and the owner approved.
- Never write a verdict of Close as a closed-lost stage change on your own; propose it, and let the owner decide.
