---
name: routine-weekly-facilities-digest
description: "Scheduled routine: Every Monday morning, the open facilities issues grouped by severity with owners and days open."
---

# Weekly facilities digest

Part of the Office Ops Desk agent preset.

Schedule, as written by the template author: Every Monday morning, the open facilities issues grouped by severity with owners and days open.

## What to do on each run

Run Monday mornings at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the facilities log and fold in anything the user sent since the last digest. Recompute days open for every issue. Post four groups, each sorted oldest first: urgent, waiting on a vendor, routine, and no owner yet, with location, issue, owner or vendor, days open, and the last update. Group inside each bucket by site when the user tracks more than one. Flag anything open past seven days with no update. End with one line on what closed since the last digest. Keep it under 200 words. Save the digest with today's date in the filename and write the recomputed log back. An empty list gets one line saying it is clear. Never invent a ticket, an owner, or a vendor commitment. Do not post to a channel, file a ticket, or send mail unless the user asks for it in this run.
