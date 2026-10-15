---
name: promise-tracker
description: "Lists every commitment made on a call by either side with an owner and a due date, and keeps the open ones until they are closed."
---

# promise-tracker

Part of the Call Follow-Ups agent preset.

# promise-tracker

## When to use

Part of every post-call pack, and on demand ("what do I still owe Acme", "what are we waiting on from them").

## Steps

1. From the transcript, extract each commitment as: who promised, what, to whom, by when (explicit date, or "unspecified"). Both directions: what we owe them and what they owe us.
2. Merge with the open commitments for this account stored in memory. Mark as closed any commitment the call or the email history shows was delivered.
3. Store the updated list for the account as a log memory, one line per open commitment, with the call date it came from.

## Output

Two short lists: "We owe" and "They owe", each line as `what, owner, due date, source call`. If a due date was not said, write "date not set" and suggest one in the recap email.

Offer to create CRM tasks for our side. Create them only after the owner says yes.

## Rules

- A commitment is something someone said they would do. Do not infer commitments from tone.
- Read-only until approval, never nags the customer directly.
