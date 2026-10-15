---
name: weekly-report
description: "Use for the weekly routine or when the user asks how a week went. Builds spend, conversions, CPA, CTR, and CPC by campaign against the prior week, with top movers, commentary carrying the number behind every sentence, a source label on every number, and next steps as questions."
---

# weekly-report

Part of the Marketing Analyst agent preset.

# Weekly report

## When to use
On the weekly routine, or when the user asks for last week, a named week, or "how did we do".

## Inputs
metrics-history.csv and ledger.csv after a fresh ingest-exports run, which reads every signed-in
platform live first and the exports second, plus the ACCOUNTS entry, the column map, the
thresholds, and the headline metrics from memory. The week runs Monday to Sunday unless the user
saved a different week start.

## Steps
1. Run ingest-exports first. If the week that closed is not fully covered, do not build the full
   report. Send one short message naming the platform, whether it needs a sign in or an export,
   and the exact date range still needed, and offer to build the report on the partial range with
   the range labeled.
2. Pull the closed week and the week before it, per platform, per campaign.
3. Compute spend, conversions, CPA, CTR, CPC, and ROAS where conversion value exists, for both
   weeks, at account level and per campaign.
4. Top movers: rank campaigns by absolute change in spend and by absolute change in conversions,
   then keep the 3 to 5 that moved most in either direction. A campaign under the quiet floor for
   the week is listed as low volume and not called a mover.
5. Write the commentary. Every sentence carries the number behind it. "Brand search took 38
   percent of spend at 412 dollars, up from 260 dollars, and CPA fell from 41 dollars to 29
   dollars on 14 conversions" is the register. "Performance improved" is not.
6. Render the charts per evidence-media: spend by campaign for both weeks, CPA by campaign, and
   the account spend trend across the weeks in history.
7. Build the HTML report per html-report and verify it before delivering.

## Structure
- **TLDR**, 3 to 4 bullets: what was done, what matters, the key numbers, what worked against what
  did not, and what to do next.
- **Header**: week covered, prior week compared, platforms, currency, and the sources: each
  platform read live with the view and the read date, each export file with its ingest date.
- **Source labels**: every number in every table and every sentence carries its source in short
  form, `live <platform> <read date>` or `export <file> <ingest date>`. A table gets a source
  column, a chart gets it in the caption, a sentence gets it in brackets. A figure that mixes a
  live read and an export across the period says mixed and the header says which days came from
  which.
- **Account table**: spend, conversions, CPA, CTR, CPC, ROAS where available, this week against
  last week, with the change in absolute terms and in percent.
- **Campaign table**: the same columns, one row per campaign, sorted by spend, with the change
  against the prior week.
- **Top movers**: 3 to 5 lines, each the campaign, the metric, the two numbers, and the change.
- **Commentary**: 3 to 5 lines on what moved and why, each tied to a number in the tables above.
  Where the cause is not in the export, say what would show it rather than naming a cause.
- **What to do next**: 2 to 4 questions the user answers, each with the number that raises it. For
  example "Shift the 180 dollars in the two campaigns at 0 conversions this week into brand
  search, which returned 14 conversions at 29 dollars?" Never phrase these as instructions and
  never act on them.
- **Gaps**: platforms or dates missing, one line each, saying whether a sign in or an export
  would close it.
- **Could not read**: any source that failed this run, including an expired platform session.

## Deliver
Save to /workspace/analytics/reports/<date>-weekly.md and the HTML beside it. Write the week's
figures to metrics-history.csv. Attach the HTML and the charts with 5 lines in chat: week, spend,
conversions, CPA against last week, and the one thing worth deciding. Deliver to the saved
destination as a draft the user approves before anything is posted or sent.

## Never
Invent a number or a cause. Carry a prior week's figure forward as new. Report a week the data
does not cover. Put a number in the report without its source label. Post or send without an
explicit yes.
