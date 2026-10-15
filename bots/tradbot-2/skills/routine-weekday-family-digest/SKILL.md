---
name: routine-weekday-family-digest
description: "Scheduled routine: Every weekday morning, one short brief of the household things that need you today, and quiet when nothing does."
---

# Weekday family digest

Part of the Tradbot agent preset.

Schedule, as written by the template author: Every weekday morning, one short brief of the household things that need you today, and quiet when nothing does.

## What to do on each run

Run every weekday at 6:30am in the timezone saved in memory, or at the hour the user picked instead. Compute the cron from that timezone and never assume Pacific or UTC. Skip weekends unless the user asked for them. Read the watch list and the open loops list first, then personal email since the last run and the calendar for today and the next seven days. Keep only what clears the bar in the Household inbox scan skill, or the user's own bar when they set one. Send one short tactical chat message: what is on today and who is doing it, what needs them with the date and the action that closes it, the rest of the week in a line, and anything you already drafted. Write new items and closures back to the open loops list. A morning with nothing material gets one line saying it is clear, and a quiet morning with something overdue still names the overdue thing. Never invent an appointment, a date, or an amount. Do not send mail, RSVP, submit anything, or touch the calendar from this run, draft instead and say the draft is waiting. Say in one line when you could not read the inbox or the calendar. This is NOT the kitchen newspaper. Do not attach or merge the printable page into this message.

Fires on:
- cron `30 6 * * 1-5`

Ask the importing user for:
- Timezone
