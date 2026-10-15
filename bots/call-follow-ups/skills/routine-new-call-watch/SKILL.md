---
name: routine-new-call-watch
description: "Scheduled routine: Every 30 minutes on weekdays, find calls the owner hosted that finished since the last run and stage the post-call pack for approval."
---

# New call watch

Part of the Call Follow-Ups agent preset.

Schedule, as written by the template author: Every 30 minutes on weekdays, find calls the owner hosted that finished since the last run and stage the post-call pack for approval.

## What to do on each run

# New call watch

Runs unattended every 30 minutes between 07:00 and 20:00 on weekdays in the owner's timezone.

1. Ask every connected recorder (Gong, Granola, or both) for calls where the owner was a participant that ended since the last run and have a processed transcript. Remember the ids you have already handled so a call is processed exactly once, and deduplicate a meeting that both recorders captured.
2. Skip internal-only calls (every participant on an internal domain stored in memory).
3. For each remaining call run, in order: `recap-email` (saved to Drafts), `next-steps-note`, `crm-update-proposal` (diff only), `promise-tracker`.
4. Deliver one message per call to the owner in this chat or their Slack DM: the draft link, the note, the CRM diff, and the open commitments. End with the plain-text question "Apply the CRM changes?".
5. Apply nothing during the run. Writes happen only when the owner answers yes in the conversation.
6. If nothing finished since the last run, stay silent.

Unattended runs never ask clarifying questions; if a call cannot be matched to an opportunity, say so in the message and list the candidates. This routine never sends email and never writes to the CRM on its own.

## Schedule

Create this routine paused, on cron `*/30 7-20 * * 1-5` read in the owner's timezone.
That is the default; if the owner named a different day or hour while setting up,
use theirs instead. Turn it on only when the owner says yes.
