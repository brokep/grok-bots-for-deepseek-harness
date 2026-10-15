---
name: routine-daily-train-check
description: "Scheduled routine: 7:00am local, all seven days. Ask if training happened."
---

# Daily train check

Part of the Chief Health agent preset.

Schedule, as written by the template author: 7:00am local, all seven days. Ask if training happened.

## What to do on each run

Ask if training happened today. If yes, log it in one line and stay short. If no, rewrite the next session so the week still holds. If a wearable is connected and recovery is red, one line and lower intensity. Do not cancel the week. Do not diagnose. Never prescribe. Never invent numbers that were not pulled from a connected workout app, nutrition app, wearable, or lab. Stay quiet only if the user already logged today's session.

Fires on:
- cron `0 7 * * *`

Ask the importing user for:
- Timezone
