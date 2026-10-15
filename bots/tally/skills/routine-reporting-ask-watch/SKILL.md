---
name: routine-reporting-ask-watch
description: "Scheduled routine: Through the working day, checks the channels you named for paid media reporting asks and brings you a drafted reply to approve."
---

# Reporting ask watch

Part of the Paid Media Report Desk agent preset.

Schedule, as written by the template author: Through the working day, checks the channels you named for paid media reporting asks and brings you a drafted reply to approve.

## What to do on each run

Run once an hour on weekdays during the working hours the user saved, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the channels the user named and look for asks about paid media numbers: spend, CPA, ROAS, a campaign, a platform, or how last week went. Skip anything you have already logged. For each new ask, draft the reply with the Answer a reporting ask skill, using the column map, the latest mapped exports, and the metrics history. Send the user one message with the ask, the channel, who asked, and the draft, then wait. When the exports on hand cannot answer it, name the export and the date range you need instead of guessing, and offer a two-line holding reply. Nothing new means send nothing at all. Never post, reply in a thread, or react without an explicit yes, and never invent a number to make a reply land faster.
