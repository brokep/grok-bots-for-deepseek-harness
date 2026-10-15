---
name: competitor-page-diff
description: "Use when you need to find what changed across the watch list since the last run, on demand or from a routine."
---

# Competitor page diff

Part of the Competitor Watch agent preset.

Inputs: the watch list, the most recent saved snapshot, and the user's material bar.

Default material bar, used unless the user gave you their own: a price, plan, or limit change, a new tier, a new product or feature, a shift in the headline pitch or category, funding, a new customer logo, and job posts that point somewhere new. Noise to ignore: testimonial rotation, image swaps, nav and footer edits, blog ordering, and word churn that does not change meaning.

1. Read the watch list, then the latest snapshot. Never diff from memory.
2. Fetch every tracked page. Post a running list of pages checked so the user sees movement inside a minute.
3. Save this run's text for each page as the new snapshot before you analyze. That is what the next run compares against.
4. Compare new against old per page and pull out what was added, removed, or reworded. Quote the change in the shortest form that still makes sense.
5. Sort each difference into material or noise.
6. Date every material find. Use the source's own date when it has one and say the date is approximate when it does not.

Output: material changes with competitor, page, what changed, source URL, and date, plus the pages with nothing material and the pages you could not read.

Fallbacks: a page you cannot fetch keeps its old snapshot and gets named in the output. An export from a page watcher or an intel tool the user already pays for counts as one more source when they paste it.

Save the new snapshot under competitors, then hand the findings to the brief.
