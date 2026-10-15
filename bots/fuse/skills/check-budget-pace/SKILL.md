---
name: check-budget-pace
description: "Use when the user asks whether they are on pace, how much budget is left, where the month lands, or where the remaining money should go, and when the Monday pace routine runs."
---

# Check budget pace

Part of the Ad Spend Watch agent preset.

Inputs: the numbers ledger and the monthly plan behind every account.

Steps:
1. Per account: month-to-date spend, the share of the plan it has used, days elapsed against days in the month, and where the month lands if the current daily rate holds.
2. Flag any account projected to pass its plan, and give the daily rate it would take to land on plan instead. Give the same number for any account underspending by more than 15%, because budget left on the table is a miss too.
3. Total across accounts, with the projected overshoot or shortfall in their currency.
4. When they ask where the remaining money should go, rank campaigns above the quiet floor by the metric they said they are judged on, and split them into earning it, holding, and not earning it. Name the two you would move money toward and the two you would move it away from, with the number behind each. This is a recommendation. Do not move anything.
5. Missing dates in the ledger get named, and you ask for that export rather than projecting across a gap.

Output: one line per account, then the total, then the recommendation when they asked for one. Under 150 words unless they asked for a table.

Save the pace read dated under ad spend watch.
