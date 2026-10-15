---
name: routine-monthly-parent-note
description: "Scheduled routine: On the first of each month, local events worth considering plus age-adjusted development and parenting notes."
---

# Monthly parent note

Part of the Tradbot agent preset.

Schedule, as written by the template author: On the first of each month, local events worth considering plus age-adjusted development and parenting notes.

## What to do on each run

Run on the 1st of every month at 9:00am in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the watch list for city, kids' first names, ages, and grades. Do not guess a birth year. Run the Monthly parent note skill: look up real local events for the next 4–6 weeks that fit those ages, plus age-adjusted development notes and parenting tactics. Do not invent events or milestones. Send one short chat note. Do not merge this into the weekday digest or the kitchen newspaper. Never send mail, RSVP, or add calendar events from this run. If ages are still unset, ask for ages once, then still send whatever local events you can.

Fires on:
- cron `0 9 1 * *`

Ask the importing user for:
- Timezone
