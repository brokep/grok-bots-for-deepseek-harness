---
name: monthly-paid-media-report
description: "Use when the user asks for a monthly report, a month-over-month read, or a budget pacing check, or when the monthly report routine runs."
---

# Monthly paid media report

Part of the Paid Media Report Desk agent preset.

Inputs: the mapped exports for the month that closed, the metrics history for the two months before it, the monthly budget when the user gave you one, and the headline metrics.

1. Report closed months only. When they ask mid-month, say so and offer a month-to-date read against the same days of last month instead.
2. Compute the month's totals per platform and in total, then the same figures for the prior month, using the definitions in memory.
3. Build the three-month trend for spend, CPA, and ROAS where you have it, so a one-month swing shows up as either a blip or a direction.
4. Roll up to campaign level: the campaigns that took the most spend, the ones that moved most on CPA, and anything that started or stopped during the month.
5. Pacing: compare spend against the budget they gave you and give the share of budget used against the share of the period elapsed. Drop this section when there is no budget on file rather than inventing one.
6. Write the commentary through What moved and why, then one short list of what to change next month, each item tied to a number in the report.

Output shape:
- Headline: the month, total spend, and the two figures worth knowing.
- Table: one row per platform and a total row, prior month alongside.
- Three-month trend: one line per metric.
- Campaigns: the spend leaders and the movers.
- Pacing: budget used against period elapsed, when a budget exists.
- Next month: three to five items, each with the number behind it.
- Gaps: what was missing and what you could not compute.

Fallbacks: a missing platform gets one ask, then the report goes out without it and says so. A month where the column map changed gets a note naming the figures that are not comparable.

Save dated under paid media reports, update the metrics history, and attach it. Delivery to a channel or an inbox goes as a draft.
