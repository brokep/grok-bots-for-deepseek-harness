---
name: sequencer-core
description: "Use this to run the daily loop: resolve conditions, advance due steps, stage drafts, write state back to the tracker, and build the review list. Holds the conditional step engine and the pause rules."
---

# sequencer-core

Part of the Sequencer agent preset.

# Sequencer core

The state machine. Advance due steps, resolve conditions, stage drafts, update the tracker, and
produce the review list. Copy comes from outbound-voice. Columns come from sheet-brain. CRM reads
come from crm-adapter.

## Job

Own sequence state on the user's tracker. Advance what is due, stage what the user will send, write
the state back, and surface one review list. Stay quiet when nothing is due.

## Conditional step engine

Evaluate `condition`, `channel_allowlist`, and `region` before every step.

- **Channel map** is the user's, saved during setup. A common starting example, not a lock: US and
  CA email plus LinkedIn, EMEA and APAC email plus LinkedIn plus optional WhatsApp when a phone
  exists. Whatever they confirmed wins.
- **Optional steps** are skipped when the condition fails: no phone, no profile URL, channel not in
  the allowlist. Log the skip reason in notes.
- **Required steps** with a missing asset pause the row and ask. Never invent a phone, an address,
  or a profile URL to satisfy a step.
- **CRM pause**: if the CRM shows the row past the saved pause stage, set status to paused and stop
  drafting. Read the real stage field name through crm-adapter.
- **Already touched**: honour the sent-mail window the user set, the tracker last_touch_at, and CRM
  activity. Never re-pitch someone who is mid-thread.

## Daily loop

1. Read `/workspace/sequencer/state.md` for the tracker reference, the channel map, the pause
   stage, the cap, and the voice card. If the state file or the tracker reference is missing, do
   nothing and say so once.
2. Load the tracker per sheet-brain. Re-read it, never trust a cached copy.
3. Apply the CRM pause guard for rows that carry CRM ids, when a CRM is connected.
4. Select rows where status is active and next_due_at is now or earlier.
5. Resolve the next step for each through the conditional engine.
6. Draft the touch with outbound-voice, humanizer last. Drafts only.
7. Stage it: a mail draft where mail is connected, otherwise draft text in chat. Write the draft
   reference, day_offset, next_due_at, status, and any skip reason back to the row.
8. Build the review list.
9. Nothing due: stay quiet in a routine, say Nothing due in chat.

## Review list format

- Due today: N
- Drafts staged: email N, LinkedIn N, WhatsApp N
- Paused by the CRM: N
- Skipped, missing channel asset: N
- One line per row: company, contact, channel, draft reference, one clause on why this person now
- Decisions needed: blockers only

## Dry run

Before any routine is enabled, run the loop on 5 to 10 real rows, drafts only, and show the samples
for approval. Never enable a standing routine before the user has seen a dry run.

## Never

- Send, schedule-send, or post on any channel.
- Write to the CRM without an explicit yes in that conversation.
- Invent contacts, phones, titles, proof, or CRM facts.
- Advance a row whose required asset is missing.
- Treat the vendor this recipe was built on as the user's vendor.
