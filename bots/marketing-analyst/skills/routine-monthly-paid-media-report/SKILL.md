---
name: routine-monthly-paid-media-report
description: "Scheduled routine: Disabled by default. The 1st of the month in the user's timezone. Builds the closed month's report with the three month trend, the campaign rollup, and budget pacing when a budget is on file. Draft only."
---

# Monthly paid media report

Part of the Marketing Analyst agent preset.

Schedule, as written by the template author: Disabled by default. The 1st of the month in the user's timezone. Builds the closed month's report with the three month trend, the campaign rollup, and budget pacing when a budget is on file. Draft only.

## What to do on each run

# Monthly paid media report

This routine ships disabled. Confirm the timezone, the hour on the 1st, the monthly budget if there is one, the destination, and that nothing gets sent before enabling.

When enabled:
1. Cover the month that just closed. Read memory for the platform accounts, the export location, the column map, the currency, the monthly budget, and the destination. If no platform is signed in and no column map exists, do nothing and say so once.
2. Run ingest-exports, which reads every signed-in platform live first and the exports second, then read metrics-history.csv for the two months before the one being reported.
3. Run the monthly-report skill end to end: totals per platform against the prior month, the three month trend for spend and CPA, the campaigns that carried spend, budget pacing when a budget is on file, the one paragraph read, and what to do next as questions.
4. Render the charts per evidence-media and build the report per html-report. Verify the file before attaching it.
5. Save the report dated, update metrics-history.csv, attach the HTML and the charts, and deliver to the saved destination as a draft.
6. When a platform is missing, ask once for the sign in or the export, then build the rest without it and say which platform and which date range is absent from every total.
7. Never invent spend, conversions, or budget figures, never present a partial month as closed, never touch a campaign or a budget, and never send without an explicit yes.

Fires on:
- cron `0 9 1 * *`

Ask the importing user for:
- Timezone
