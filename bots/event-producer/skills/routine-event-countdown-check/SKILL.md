---
name: routine-event-countdown-check
description: "Scheduled routine: Every weekday morning, what is due, what is late, and what is still unconfirmed, with the days-out count, registrations against target, and the guest gaps that get expensive late."
---

# Event countdown check

Part of the Event Producer agent preset.

Schedule, as written by the template author: Every weekday morning, what is due, what is late, and what is still unconfirmed, with the days-out count, registrations against target, and the guest gaps that get expensive late.

## What to do on each run

Run every weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the event brief, the run of show, the vendor tracker, the guest list, and the guest travel sheet for the active event. Post a short check in five parts: days out from the event, what is due today or already overdue with the owner on each line, what is still unconfirmed inside the next two weeks, registered against target with the number you actually expect through the door, and the guest gaps that cost money late, missing dietary answers, unnamed plus-ones, and any hotel cutoff inside seven days. One line per item, no preamble. Stay quiet when nothing is due, nothing is late, and nothing changed since the last run. Speak up when something is late even if nothing else moved. Never invent a confirmation, a headcount, a quote, or a date. Do not mail a vendor or a guest from this run, hand the user a draft instead. When there is no active event, say so in one line and stop.
