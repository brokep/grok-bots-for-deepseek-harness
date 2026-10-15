---
name: pipeline-health-report
description: "Use when the user asks how the pipeline is doing, or when the weekly pipeline report routine runs."
---

# Pipeline health report

Part of the Lead Pipeline Desk agent preset.

Inputs: the lead ledger, the previous report when there is one, and the lead goal from memory when they set one.

1. Re-read the ledger and fold in anything that arrived since the last report.
2. Counts. New leads this period by source, with the change against the period before.
3. Quality. The split across tiers A, B, C, and D, and the share of new leads that landed in A or B.
4. Movement. What moved from new to working, working to qualified, and qualified to converted, plus the median days each step took.
5. Stuck. Leads with no owner, leads past their response window, and anything sitting in one status for more than 14 days. Name the oldest five with the owner on each.
6. Hygiene. Duplicates merged, rows still missing an email or a company, and how much of the list is complete.
7. Pacing, when they gave you a goal. Where they are against it, the run rate, and one line on whether the month lands.

Output shape: a short paragraph on what actually changed, then the numbers in that order, then a "needs a person" list of three to five items with a name against each.

Rules: every number comes from the ledger. Write "unclear" when a move has no cause you can support from the data. A quiet week is one line saying so plus the stuck list, not a padded report.

Save the report dated under the lead desk folder and attach it here, then send it to the destination they picked. Anything that posts to a channel goes to them as a draft first.
