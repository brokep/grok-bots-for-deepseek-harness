---
name: routine-routine-healthcheck
description: "Scheduled routine: Cron 49 8 * * 1 (Mondays 8:49 local). Audits fleet routines for token waste; reports fixes; stays quiet when nothing is worth proposing."
---

# routine-healthcheck

Part of the dr eggbot agent preset.

Schedule, as written by the template author: Cron 49 8 * * 1 (Mondays 8:49 local). Audits fleet routines for token waste; reports fixes; stays quiet when nothing is worth proposing.

## What to do on each run

Schedule: 49 8 * * 1 (Mondays 8:49 in the user's local timezone).

Run the Routine healthcheck skill. Scan every bot's scheduled and event routines for token waste (too frequent, recurring on a long chat, noisy empty runs, dead or duplicate). Report a short list: bot, routine, flag, suggested fix. Stay quiet when there is nothing worth proposing — do not send filler like "(no change.)". Do not edit another bot's routines unless the user says to.

If this routine is missing after template import, recreate it with update_state target routine action create, name routine-healthcheck, schedule 49 8 * * 1.

Fires on:
- cron `49 8 * * 1`

Ask the importing user for:
- Timezone
