---
name: bids-and-budgets
description: "Use when the user wants to know what to bid, how much to change a bid by, where to move budget, or why a campaign is capped."
---

# Bids and budgets

Part of the Apple Search Ads Review agent preset.

Inputs: the keyword and campaign export, the targets sheet, and the last review.

The bid on Apple Search Ads is a maximum cost per tap, not a cost per install. So every bid recommendation goes through the conversion rate.

1. Compute per keyword: cost per tap, tap-through rate, conversion rate from taps to installs, and cost per install.
2. Size the bid. The bid that lands on target is roughly the target cost per install times that keyword's conversion rate. Show the math on every line so they can argue with it.
3. Cap the move. Do not recommend a change larger than 30 percent in one step on a keyword with real history. Big swings reset delivery and you lose the read on what the last change did.
4. Only change one lever at a time on any one keyword. A bid cut and a match type change on the same keyword in the same week means neither result is readable.
5. Low volume keywords. When a keyword has too few taps to trust its conversion rate, price the bid off the campaign or ad group conversion rate instead and say that is what you did.
6. Budgets. Separate the daily cap from the campaign total budget. A campaign hitting its daily cap before the day ends is constrained, so the right move is more budget if it is under target and a bid cut if it is over. Never raise a budget on a group that is already over target.
7. Reallocate. Name the exact money moving out of each over-target group and into each under-target group with headroom, and keep the total flat unless they say otherwise.
8. If they use a cost per acquisition goal field, say plainly that it throttles delivery to hit that number and can starve a campaign. Recommend it only where volume is healthy.
9. Set the check date. Most changes need several days of data before the result is readable, so name the date and the number that would tell them it worked.

Output: one line per change with the current value, the new value, the math, and the check date.

Rules: no bid without a number from the export. Never quote a bid you have not derived on the line. Say when the data is too thin instead of guessing a bid.

Save under the Apple Search Ads folder with the review date.
