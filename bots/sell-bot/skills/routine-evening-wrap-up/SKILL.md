---
name: routine-evening-wrap-up
description: "Scheduled routine: Disabled by default. Weekdays 5:45pm: wrap-ups and the digest for today's calls."
---

# Evening wrap-up

Part of the Sell Bot agent preset.

Schedule, as written by the template author: Disabled by default. Weekdays 5:45pm: wrap-ups and the digest for today's calls.

## What to do on each run

This routine ships disabled. Before enabling, confirm the timezone and the notes source.

When enabled:
1. Read memory and setup.md in my folder (MY FOLDER fact). No fact, no file, or Evening wrap-up not under Routines on: stop silently.
2. Run @call-wrap for each watched call that ended in the last 3 weekdays with wrap empty.
3. Send the @call-wrap digest as one message. Notes not ready: say so, the next run retries. No watched calls: quiet. Drafts only.

Fires on:
- cron `45 17 * * 1-5`

Ask the importing user for:
- Timezone
