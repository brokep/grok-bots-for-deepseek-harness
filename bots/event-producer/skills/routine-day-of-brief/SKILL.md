---
name: routine-day-of-brief
description: "Scheduled routine: On the morning of the event, the run of show with owners, vendor arrival times with phone numbers, the guest and dietary counts, and everything still open."
---

# Day-of brief

Part of the Event Producer agent preset.

Schedule, as written by the template author: On the morning of the event, the run of show with owners, vendor arrival times with phone numbers, the guest and dietary counts, and everything still open.

## What to do on each run

Run on the morning of the event at the hour the user picked, in the timezone saved in memory. Take the event date from the event brief, compute the cron from that date and timezone, and recompute it whenever the event date changes. Read the run of show, the vendor tracker, the day-of checklist, the guest list, and the guest travel sheet. Post the day in five parts: the hour-by-hour run of show with an owner on every row, vendor arrival times with a phone number on every line, the guest numbers with registered against the count to actually expect plus the dietary and access counts the venue needs today, who is arriving from out of town and who is meeting them, and whatever is still unconfirmed or open. Add the what-if list as one short block at the end. Keep it scannable, this gets read on a phone in a loading dock. Never invent an arrival time, a phone number, a dietary need, or a confirmation. Do not mail or message a vendor, a guest, or the crew from this run, hand the user a draft instead.
