---
name: routine-weekend-sports-preview
description: "Scheduled routine: Every Friday evening, the weekend and the week after it with the collisions, what to prepare, and everything still owed."
---

# Weekend preview

Part of the Tradbot agent preset.

Schedule, as written by the template author: Every Friday evening, the weekend and the week after it with the collisions, what to prepare, and everything still owed.

## What to do on each run

Run every Friday at 6pm in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Friday evening is the point, there is still time to buy the gift, sign the form, or find a sitter. Read the calendar from Saturday through the end of next week, the watch list, and the open loops list. Send four short parts. The weekend, one line per day with who is where and when, covering sports, classes, outings, pool, parties, and travel, then next week in a line with the heaviest day named. Collisions, the days where two things overlap or one person cannot be in both places, each with the fix you would make. Prep, what has to be bought, signed, printed, paid, or packed before a date, with two days of lead time. Still owed, the forms, RSVPs, bills, and appointments open in the ledger, soonest first. A clear weekend gets three lines. Never move, add, or delete a calendar event, never RSVP, and never send anything from this run, offer the draft instead. Name anything you could not read rather than guessing at it.

Fires on:
- cron `0 18 * * 5`

Ask the importing user for:
- Timezone
