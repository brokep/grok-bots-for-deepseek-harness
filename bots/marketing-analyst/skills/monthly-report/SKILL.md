---
name: monthly-report
description: "Use for the monthly routine or when the user asks for a closed month. Everything the weekly report does, plus the three month trend, budget pacing against the budget on file, the campaigns that carried spend, and a one paragraph read of the month."
---

# monthly-report

Part of the Marketing Analyst agent preset.

# Monthly report

## When to use
On the monthly routine, or when the user asks for a closed month.

## Inputs
Everything weekly-report uses, plus metrics-history for the two months before the one being
reported, plus the monthly budget and daily plan when the user saved them.

## Steps
1. Run ingest-exports, which reads every signed-in platform live first and the exports second.
   Cover the month that just closed, complete. If one platform is missing, ask once for the sign
   in or the export, then build the rest of the report without it and say plainly which platform
   and which date range is absent from every total.
2. Everything in weekly-report steps 2 through 5, with the month against the prior month instead
   of week against week.
3. Trend: spend, conversions, and CPA per month across the trailing 3 months, at account level and
   for the 5 campaigns with the most spend in the reported month.
4. Budget pacing, only when a monthly budget is on file: spend to date against the budget, the
   percent of budget used, the implied daily rate for the month that closed, and the projection
   for the current month at the trailing 7 day rate. Say whether the month landed over, under, or
   on plan, with both numbers. Without a budget on file, skip the section and say it is skipped
   because no budget was given.
5. Campaigns that carried spend: every campaign above 5 percent of month spend, with its share,
   its CPA, and its direction against the prior month.
6. The read: one paragraph, 4 to 6 sentences, on what the month says. Every sentence carries a
   number. It answers where the money went, what it returned, what changed against the prior
   month, and what the trend implies if nothing changes.
7. Charts per evidence-media: 3 month spend and CPA trend, spend share by campaign, month against
   prior month by campaign, and budget pacing when a budget exists.
8. Build the HTML report per html-report and verify it before delivering.

## Structure
TLDR, header with the sources and their read dates, account table month against prior month,
campaign table, trend, budget pacing, top movers, the one paragraph read, what to do next as
questions, gaps, could not read. Source labels follow the weekly-report rule: every number says
live or export, with its date, and a period assembled from both says mixed.

## Deliver
Save to /workspace/analytics/reports/<date>-monthly.md and the HTML beside it. Update
metrics-history.csv. Attach the HTML and the charts with 6 lines in chat. Deliver to the saved
destination as a draft.

## Never
Invent spend, conversions, or a budget figure. Project a month from fewer than 7 days of data
without labeling it as that. Present a partial month as closed. Put a number in the report
without its source label. Send without an explicit yes.
