---
name: routine-confirm-notes
description: "Scheduled routine: Disabled by default. Hourly on weekdays: confirm-note drafts for calls about an hour out."
---

# Confirm notes

Part of the Sell Bot agent preset.

Schedule, as written by the template author: Disabled by default. Hourly on weekdays: confirm-note drafts for calls about an hour out.

## What to do on each run

This routine ships disabled. Before enabling, confirm the timezone and the calls to watch.

When enabled:
1. Read memory and setup.md in my folder (MY FOLDER fact). No fact, no file, or Confirm notes not under Routines on: stop silently.
2. Read today's calendar for watched calls starting 50 to 110 minutes from now, not canceled, and add any missing from calls.csv.
3. For each with confirm empty, draft the note per @prep-page and @draft-email, mark confirm, and send one line: "Confirm note for <name> at <time> is ready", plus where it is.
4. Nothing due: quiet. Never send the note or change the event.

Fires on:
- cron `5 7-17 * * 1-5`

Ask the importing user for:
- Timezone
