---
name: search-terms-and-negatives
description: "Use when the user wants to cut wasted search spend, harvest new keywords, or build a negative keyword list on Apple Search Ads."
---

# Search terms and negatives

Part of the Apple Search Ads Review agent preset.

Inputs: the search term report, the keyword report, and the targets sheet.

Search terms arrive from three places on Apple Search Ads: keywords the user bought on exact, keywords on broad, and Search Match picking queries on its own. Say which one fed each term where the export tells you, because the fix differs.

1. Split search terms into three piles: converting at or under target, converting above target, and spending with zero installs.
2. Harvest. Terms converting at or under target that are not already exact keywords go on the add list with a starting bid, priced from the cost per tap they already pay and the target cost per install. Put each one in the campaign that matches its intent, not wherever it was found.
3. Close the loop. Every term harvested out of a discovery or broad campaign gets added as an exact negative in the campaign it came from, so discovery stops bidding against the exact keyword you just created. Skipping this is the most common way an account competes with itself.
4. Cut. Terms with spend and zero installs across a range long enough to matter get a negative recommendation, with the range and the spend it saves. Never negate a term off two taps.
5. Trim. Terms converting above target get a bid cut sized to the gap rather than a pause, unless the spend is large and the gap is wide.
6. Check the usual wrong intent buckets before you finish: competitor and other app names, free, hack, mod, or crack, refunds and cancellations, support and login queries, jobs, and anything about a different product with a similar name.
7. Pick the level and the match type for each negative. Exact negative for one specific query, broad negative for a pattern. Campaign level when it should never run anywhere, ad group level when one group should stop bidding on it and another should keep going.

Output: an add list, a negative list, and a bid change list, each line carrying the term, the number behind it, the campaign and ad group it goes in, and the match type.

Rules: never negate a brand term without asking. Never harvest a term you cannot see in the export. Mark anything with only a few taps as too early to judge. A broad negative can silently kill a converting query, so name what else each broad negative would block.

Save under the Apple Search Ads folder with the review date.
