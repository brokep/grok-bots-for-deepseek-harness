---
name: weekly-paid-media-report
description: "Use when the user asks for a weekly report or a week-over-week read, or when the weekly report routine runs."
---

# Weekly paid media report

Part of the Paid Media Report Desk agent preset.

Inputs: the mapped exports covering the week you are reporting and the week before it, the headline metrics from memory, and the currency.

1. Fix the period first and say it out loud: the seven days you are reporting and the seven you are comparing against. Never compare a partial week to a full one. Say it plainly when an export stops mid-week.
2. Check coverage before you compute anything: which platforms you have, and which days. A platform with no export gets named in the report, never dropped quietly.
3. Compute per platform and in total, using the definitions in memory: spend, impressions, clicks, CTR, CPC, conversions, CPA, and conversion value and ROAS when a value column exists.
4. Compare every figure to the prior week in both absolute and percent terms. Money rounds to whole units, rates to one decimal.
5. Pick the top movers: the three to five campaigns with the biggest change in spend or CPA, each with the number that moved.
6. Hand the figures to What moved and why for the commentary. Do not write the commentary twice.

Output shape:
- Headline: the period, total spend, and the one metric that moved most.
- Table: one row per platform and a total row, with last week alongside each figure.
- Top movers: campaign, platform, and what changed.
- What I would look at: three to five lines from the commentary skill.
- Gaps: platforms or days missing, and metrics your columns cannot support.

Fallbacks: one platform exported means you build it for that one and name what is missing. No prior week means you build the baseline and say the comparisons start next week.

Save the report dated under paid media reports, write the period's figures to the metrics history, and attach it here. Anything that posts or emails goes out as a draft first.
