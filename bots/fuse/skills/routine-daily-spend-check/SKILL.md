---
name: routine-daily-spend-check
description: "Scheduled routine: Every weekday morning, checks the newest ad numbers against your thresholds and flags what broke, with the one change to make on each urgent line."
---

# Daily spend and performance check

Part of the Ad Spend Watch agent preset.

Schedule, as written by the template author: Every weekday morning, checks the newest ad numbers against your thresholds and flags what broke, with the one change to make on each urgent line.

## What to do on each run

Run every weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Include weekends only if the user asked for them. Pull the freshest numbers first from any connected sheet, warehouse query, or report mail, then read the threshold set and the numbers ledger. Evaluate every threshold row against its window and skip campaigns under the quiet floor. Post breaches in three groups, urgent, watch, and note, sorted by spend inside each, with priority accounts breaking ties. Every line carries the campaign, the metric, the number now, the number the row allowed, and the spend at risk. Name the one change you would make on each urgent line. Write the check to the alert log and deliver it to the destination the user picked. Stay quiet when every row is inside its limit and the ledger is current. Speak up when the freshest numbers are more than two days old, because a stale ledger means nothing is being watched, and ask for an export in one line. Never invent a number. Never pause a campaign, move a budget, or touch the platform, and never post anywhere the user did not pick.
