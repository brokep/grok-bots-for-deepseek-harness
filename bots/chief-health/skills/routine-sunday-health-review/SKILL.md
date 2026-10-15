---
name: routine-sunday-health-review
description: "Scheduled routine: Sunday 5:00pm local. Five-line week review."
---

# Sunday health review

Part of the Chief Health agent preset.

Schedule, as written by the template author: Sunday 5:00pm local. Five-line week review.

## What to do on each run

Five lines only. Sessions hit, sessions missed, sleep if a wearable is connected, one new lab or wearable trend if data landed, one change for next week. No dashboard essay. Never invent numbers that were not pulled from a connected source. Do not diagnose. Never prescribe.

Fires on:
- cron `0 17 * * 0`

Ask the importing user for:
- Timezone
