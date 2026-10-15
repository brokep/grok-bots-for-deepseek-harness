---
name: routine-daily-prospects
description: "Scheduled routine: Disabled by default. Weekday mornings at 7am in the user's timezone. Queues new prospects that match the confirmed ICP onto the tracker, up to the saved daily cap. Quiet when the cap is already filled."
---

# Daily prospects

Part of the Sequencer agent preset.

Schedule, as written by the template author: Disabled by default. Weekday mornings at 7am in the user's timezone. Queues new prospects that match the confirmed ICP onto the tracker, up to the saved daily cap. Quiet when the cap is already filled.

## What to do on each run

# Daily prospects

This routine ships disabled. Before enabling, confirm the timezone, the weekday morning cadence, the confirmed ICP, the ownership scope, the tracker, the daily cap, and the quiet-when-full behaviour.

When enabled:
1. Read `/workspace/sequencer/state.md` for ICP, title winners, owner filter, daily cap, and the tracker reference. If ICP is not confirmed, do nothing and say so once.
2. Count rows already queued or active for today. If the cap is filled, stay quiet.
3. Run prospect-queue against the sources the user actually has.
4. Dedupe against the tracker, recent sent mail, and CRM activity.
5. Append rows with region, channel_allowlist, status queued, next_due_at, and a source with a date. Leave any unsourced field blank.
6. Report only when rows were added: how many, from where, how many were dropped as duplicates, how many have no email.

This run is unattended. It writes rows to the tracker and nothing else. It never sends anything, never contacts anyone, never writes to the CRM, and never invents an email, a phone, or a title. Drafting happens in sequencer-daily.

Fires on:
- cron `0 7 * * 1-5`

Ask the importing user for:
- Timezone
