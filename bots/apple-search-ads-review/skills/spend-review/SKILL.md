---
name: spend-review
description: "Use when the user hands over a fresh Apple Search Ads export, asks how spend is tracking against target, or when the weekday spend check routine runs."
---

# Spend review

Part of the Apple Search Ads Review agent preset.

Inputs: the newest export, the targets sheet, and the last review.

1. Say which columns you found before you change anything. Map their headers onto spend, impressions, taps, tap-through rate, installs or conversions, new downloads and redownloads, cost per tap, cost per install, and conversion rate. Note the level each row sits at: account, campaign, ad group, keyword, search term, or creative set.
2. Name the date range, the storefront, and the currency from the file. Never mix currencies or storefronts in one table.
3. Roll up to the level the targets sheet uses, then compute actual cost per install per group and the gap to target in percent and in money.
4. Report five blocks:
   - Over target. Rows past the tolerance band, sorted by money above target, not by percent. Give spend, taps, installs, cost per tap, actual cost per install, the target, and the money.
   - Winners. Rows at or under target with real volume, and how much budget headroom is left.
   - Spending with nothing to show. Rows with spend and zero installs over the range. Usually the fastest money to stop.
   - Where the leak is. For each over-target row, say whether the cost per tap rose or the conversion rate fell, because those two need opposite fixes. A high cost per tap is a bid problem. A low conversion rate is a relevance, storefront, or product page problem.
   - Could not read. Rows, columns, or files you skipped, and why.
5. Check daily caps. Any campaign that spent its cap most days is capped, not optimized, and its numbers understate what it could do.
6. Finish with the three moves you would make first, each with the number behind it: a bid cut, a budget shift from an over target group into a winner, a pause, or a negative keyword.
7. Compare against the last review and say what moved since then.

Rules: a handful of installs proves nothing, so say when a row is too thin to judge and name the range you would want instead. Never invent a metric that is not in the export.

Save the export and the dated review under the Apple Search Ads folder, then attach the review.
