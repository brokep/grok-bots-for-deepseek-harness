---
name: routine-monthly-paid-media-report
description: "Scheduled routine: On the first business day of the month, builds the closed month's report with the three-month trend, campaign rollup, and budget pacing."
---

# Monthly paid media report

Part of the Paid Media Report Desk agent preset.

Schedule, as written by the template author: On the first business day of the month, builds the closed month's report with the three-month trend, campaign rollup, and budget pacing.

## What to do on each run

Run on the first business day of the month at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Cover the month that just closed. Read the column map, the exports on hand, and the metrics history for the two months before it. Build the report with the Monthly paid media report skill: totals per platform against the prior month, the three-month trend for spend and CPA, the campaigns that carried the spend, budget pacing when a budget is on file, four to six lines on what moved and why, and a short list of what to change next month. Save it dated, update the metrics history, attach it here, and deliver it to the destination they picked as a draft. When a platform's export is missing, ask once for that platform and date range, then build the rest without it and say so rather than waiting. Never invent spend, a conversion, or a budget figure, and never send or post without an explicit yes.
