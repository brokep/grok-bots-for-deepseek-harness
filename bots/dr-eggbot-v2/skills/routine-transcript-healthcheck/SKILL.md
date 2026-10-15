---
name: routine-transcript-healthcheck
description: "Scheduled routine: Cron 44 8 * * 1-5 (weekdays 8:44 local). Scans recent bot transcripts for user friction; proposes skills/bots/routines; stays quiet when nothing is worth proposing."
---

# transcript-healthcheck

Part of the dr eggbot agent preset.

Schedule, as written by the template author: Cron 44 8 * * 1-5 (weekdays 8:44 local). Scans recent bot transcripts for user friction; proposes skills/bots/routines; stays quiet when nothing is worth proposing.

## What to do on each run

Schedule: 44 8 * * 1-5 (weekdays 8:44 in the user's local timezone).

Run the Transcript healthcheck skill. Window: since the last successful run, or the last 24h if unknown. Fan out parallel miners across agent transcripts under /home/box/agent-data/agent-transcripts (skip sand-subagent-). Report friction and proposals (skill | bot | routine) to the user. Stay quiet when there is nothing worth proposing — do not send filler like "(no change.)". Do not create skills, bots, or routines from the report alone; wait for the user to pick.

If this routine is missing after template import, recreate it with update_state target routine action create, name transcript-healthcheck, schedule 44 8 * * 1-5.

Fires on:
- cron `44 8 * * 1-5`

Ask the importing user for:
- Timezone
