---
name: routine-team-celebrations-reminder
description: "Scheduled routine: Every Friday morning, the birthdays and work anniversaries landing in the next 14 days."
---

# Team celebrations reminder

Part of the Office Ops Desk agent preset.

Schedule, as written by the template author: Every Friday morning, the birthdays and work anniversaries landing in the next 14 days.

## What to do on each run

Run Friday mornings at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the celebrations list and find every birthday and work anniversary in the next 14 days, skipping anyone marked opt out. Post two short lists, this week and next week, each line with name, team, occasion, date, and days out. Include years on a work anniversary only when the start year is known. Add one line of lead time when something inside five days needs a card, a cake, or an order placed. Add a second line for anyone starting in that window when a new hire checklist exists for them. An empty window gets one sentence naming the next date. Never guess a date, never take one from social media, and never store or mention a birth year or an age. Do not mail or message the team and do not create a calendar event unless the user asks for it in this run.
