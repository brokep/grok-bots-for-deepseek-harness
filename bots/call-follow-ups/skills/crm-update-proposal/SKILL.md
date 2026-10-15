---
name: crm-update-proposal
description: "Proposes CRM field changes after a call as a before/after diff (stage, dates, next step, contacts, qualification fields) and applies them only after the owner approves."
---

# crm-update-proposal

Part of the Call Follow-Ups agent preset.

# crm-update-proposal

## When to use

After every processed call, or when the owner says "update the CRM from that call".

## Steps

1. Resolve the opportunity: match the call's account and attendees to an open opportunity in the CRM. If there are several, list them and ask which one. If there is none, propose creating one only if the call clearly opened a deal, and ask first.
2. Read the current values of every field the owner asked to maintain (from memory): next step, next step date, stage, close date, amount, qualification fields, contact roles.
3. From the call read, propose new values. Only propose a change when the call supports it:
   - Stage: only move forward when the stage criteria were met on the call; never move a stage backward without saying why.
   - Close date: only if the customer stated a timeline.
   - Amount: only if seats, scope, or budget were discussed.
   - Next step and date: always, from `next-steps-note`.
   - Contacts: attendees who are not in the CRM, with title and role from the call. Never invent an email address.
   - Qualification fields: fill only what the transcript evidences, and quote the line that supports each.
4. Log the call as an activity with the summary if the CRM does not already have it from the recorder.

## Output

A diff table: Field, Before, After, Evidence (quote or source). Then one plain-text question: "Apply these changes? You can say yes, or name the rows to skip."

## Apply

Only after an explicit yes in this conversation. Apply exactly the approved rows, then confirm with links to the updated records. If a write fails, report which row failed and leave the rest applied.

## Rules

- Never write without approval, never in an unattended run. The routine stages the diff; the owner applies it.
- Never delete records or clear a field the owner did not ask to change.
- If the CRM connection is missing or read-only (a Salesforce MCP pointed at a reads-only server), say so and hand the owner the diff to apply by hand.
