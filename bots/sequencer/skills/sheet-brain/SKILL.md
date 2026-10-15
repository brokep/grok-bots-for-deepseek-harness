---
name: sheet-brain
description: "Use this when creating or mapping the tracker, when writing state back, or when the sheet connector is missing and a CSV has to carry the sequence. Holds the column schema and the write rules."
---

# sheet-brain

Part of the Sequencer agent preset.

# Sheet brain

The tracker is the sequence state machine. A live sheet is the best version of it. A CSV works on
day one. The user names which, and that choice is theirs, not the recipe's.

## Create or map, once

If they already have a list, map their headers to these columns and add only what is missing. If
they have nothing, create the sheet and show the header row you wrote.

| Column | Purpose |
|---|---|
| sequence_id | Stable row id |
| company | Account name |
| contact_name | Person |
| email | Email if known, blank if not |
| profile_url | LinkedIn or other profile if known |
| phone | Phone if known, for optional WhatsApp or call steps |
| region | Region code used by the channel map |
| channel_allowlist | Channels allowed on this row |
| day_offset | Day in the sequence |
| step_type | email, linkedin, whatsapp, call, other |
| step_required | required or optional |
| condition | Skip rule, for example has_phone, has_profile, region_in |
| copy_key | Template or voice arc key |
| email_draft_ref | Draft id or reference for the staged mail draft |
| linkedin_draft_ref | Chat or doc reference for the LinkedIn draft text |
| whatsapp_draft_ref | Chat or doc reference for the WhatsApp draft text |
| priority | Rank |
| status | queued, active, paused, replied, booked, skipped, done |
| crm_account_id | CRM account id when a CRM is mapped |
| crm_contact_id | CRM contact id when a CRM is mapped |
| owner | Owner filter |
| last_touch_at | Last touch timestamp |
| next_due_at | Next due timestamp |
| source | Where this row came from, with a date |
| notes | Freeform, including skip reasons |

## Rules

- I own the state. The user reviews and sends, they do not live in the sheet.
- Write the draft reference on the row the moment a draft is staged, so nothing is drafted twice.
- Every added row carries a source and a date. A blank field stays blank. Never fill one to make
  the row look complete.
- Re-read the tracker at the start of every run. A user edit beats my last write.
- Log every skip with its reason in notes, so the review list can explain itself.
- One row per contact per sequence. Dedupe on email first, then profile URL, then name plus company.

## Fallbacks, in order

1. A live sheet the user names or asks me to create. Best, because state survives between runs.
2. A CSV they upload, which I return updated after every run. Say plainly that state lives in the
   file they hold.
3. A pasted table, for a one-off dry run only. Do not promise sequencing on a paste.

If the sheet connector is not connected, all of this still works on a CSV. Say which one is in use
in the first line of every review list.

## Quality checks before writing

- Header row matches the mapping saved in `/workspace/sequencer/state.md`. If the user renamed a
  column, re-map, do not overwrite.
- No duplicate sequence_id, no duplicate contact inside one sequence.
- next_due_at is in the future for every active row.
- Any row missing a required channel asset is paused, not silently skipped.

## Never

- Delete a row. Set status instead.
- Overwrite a column the user filled in by hand.
- Write contact data I did not source.
- Store credentials or API keys anywhere in the tracker.
