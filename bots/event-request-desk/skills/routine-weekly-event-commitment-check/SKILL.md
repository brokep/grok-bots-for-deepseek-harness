---
name: routine-weekly-event-commitment-check
description: "Scheduled routine: Every Thursday morning, what the team still owes organizers for events already said yes to, with anything overdue first."
---

# Weekly commitment check

Part of the Event Request Desk agent preset.

Schedule, as written by the template author: Every Thursday morning, what the team still owes organizers for events already said yes to, with anything overdue first.

## What to do on each run

Run Thursday mornings at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the commitments list and the queue. For every committed event, recompute days to the event date and days to each deliverable due date. Post overdue first, then anything due inside seven days, then the rest of the next month. One line each with the event, what is owed, who owns it, the due date, and the status. Flag any committed event with nothing listed against it yet, and any deliverable with no owner. When an event is inside two weeks and the contract, the artwork, or the shipping address is still owed, say so on its own line. Stay quiet when nothing is overdue and nothing is due inside seven days. Never message an organizer, never mark something delivered on the user's behalf, and never invent a deliverable the organizer did not ask for. When something is blocked on a person the user named, say who it is waiting on rather than chasing them.
