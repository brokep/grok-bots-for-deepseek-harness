---
name: run-the-spend-and-performance-check
description: "Use when the user asks whether anything is off, right after new numbers land, or when the daily check routine runs."
---

# Run the spend and performance check

Part of the Ad Spend Watch agent preset.

Inputs: the threshold set, the numbers ledger, and the plan behind each account.

Steps:
1. Read the threshold set and the ledger. Never check from memory.
2. Say the range you are checking and the freshest date in the ledger. When that date is more than two days behind today, lead with it, because a stale ledger means nothing is being watched.
3. Evaluate every row against the window it names. A campaign under the quiet floor goes in the too small to judge list.
4. Per breach: the campaign, the metric, the number now, the number the row allowed, the trend across the window, and the spend at risk if it keeps going.
5. Sort by money. Urgent first, then watch, then note, and inside each one the biggest spend first. Priority accounts break ties.
6. For every urgent breach, name the one change you would make and what it would save, then wait. Do not pause anything, do not move a budget, do not touch the platform.

Output shape:

Urgent
- Campaign, metric, now against allowed, spend at risk, the change you would make

Watch
- Campaign, metric, now against allowed, what you are waiting to see

Note
- One line each

Too small to judge
- One line with the count

Everything inside the lines gets one sentence saying so and the date of your next check. Never pad a check to look busy.

Hand any urgent breach you cannot explain to the diagnosis skill in the same reply. When they say yes to a change, go to the fix list skill.

Save the check dated under ad spend watch.
