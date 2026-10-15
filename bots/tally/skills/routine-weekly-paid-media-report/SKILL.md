---
name: routine-weekly-paid-media-report
description: "Scheduled routine: Once a week, builds last week's paid media report from the exports on hand, or names exactly which export it still needs."
---

# Weekly paid media report

Part of the Paid Media Report Desk agent preset.

Schedule, as written by the template author: Once a week, builds last week's paid media report from the exports on hand, or names exactly which export it still needs.

## What to do on each run

Run once a week on the morning the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the column map and the exports on hand. When you have last week's data for every platform they report on, build the report with the Weekly paid media report skill: the headline, the per-platform table with last week alongside, the top movers, three to five lines on what moved and why, and the gaps. Save it dated, write the figures to the metrics history, attach it here, and deliver it to the destination they picked as a draft they approve before it posts. When an export is missing or stops before the week ends, send one short message instead: the platforms and the exact date range you need, and the export path for each. Then build the report the moment the files arrive. Never invent a number to fill a gap, never carry a previous week's figure forward as if it were new, and never post or send without an explicit yes.
