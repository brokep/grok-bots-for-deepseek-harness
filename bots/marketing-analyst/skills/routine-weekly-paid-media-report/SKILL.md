---
name: routine-weekly-paid-media-report
description: "Scheduled routine: Disabled by default. Monday mornings in the user's timezone. Builds last week's paid media report from the exports on hand, or names exactly which export and which date range is still missing. Draft only."
---

# Weekly paid media report

Part of the Marketing Analyst agent preset.

Schedule, as written by the template author: Disabled by default. Monday mornings in the user's timezone. Builds last week's paid media report from the exports on hand, or names exactly which export and which date range is still missing. Draft only.

## What to do on each run

# Weekly paid media report

This routine ships disabled. Confirm the timezone, the Monday morning schedule, the platforms to cover, the destination, and that nothing gets sent before enabling.

When enabled:
1. Read memory for the platform accounts, the export location, the column map, the headline metrics, the currency, and the destination. If no platform is signed in and no column map exists, do nothing and say so once.
2. Run ingest-exports, which reads every signed-in platform live first and the exports second. Report the counts in one line, and name any platform whose session has expired without retrying anything.
3. When the closed week is covered for every platform the user reports on, run the weekly-report skill end to end: TLDR, account and campaign tables against the prior week, top movers, commentary with the number behind every sentence, a source label on every number, what to do next as questions, and gaps.
4. Render the charts per evidence-media and build the report per html-report. Verify the file in the browser before attaching it.
5. Save the report dated, write the week's figures to metrics-history.csv, attach the HTML and the charts, and deliver to the saved destination as a draft the user approves before anything is posted or sent.
6. When a platform is missing, send one short message naming it, whether a sign in or an export would close it, and the exact date range needed, and nothing else.
7. Never invent a number, never carry a previous week's figure forward as new, never touch a campaign or a budget, and never post or send without an explicit yes.

Fires on:
- cron `0 9 * * 1`

Ask the importing user for:
- Timezone
