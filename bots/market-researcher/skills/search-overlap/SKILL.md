---
name: search-overlap
description: "Use this when you need to know who shares the results with the user on their core terms. Public paid and organic SERP checks, title and meta movement, brand-term defense, and the Search Console consequence when it is signed in."
---

# search-overlap

Part of the Market Researcher agent preset.

# Search overlap

Where the user and their competitors collide in search results, paid and
organic, on the terms that matter.

## When to use
Every weekly brief. On demand when the user asks who is outranking or outbidding
them.

## Core terms
Take 8 to 15 terms from the baseline: the category terms, the two or three
problem phrases the user's own hero uses, their brand term, and their brand plus
"alternative" and "vs". Save them as CORE TERMS in `_us/core-terms.md` and
confirm the list with the user once, then never re-ask.

## The check, every run
For each core term, run a plain public search and capture:
1. **Paid**: which advertisers appear above and beside the results, in order,
   with the ad headline and the landing destination. Screenshot the whole
   above-the-fold block, ads included.
2. **Organic**: the first ten results in order, marking the user's own position
   and every watched competitor's position.
3. **Page furniture**: featured snippet owner, People Also Ask entries, any
   review-site or roundup page that outranks everyone, and whether an AI answer
   box is present and who it cites.
4. Store as `_us/search/<date>/<term-slug>.md` plus the screenshot. Diff against
   the previous run: positions gained and lost, advertisers in and out, snippet
   owner changes.

## Title and meta movement
For every watched competitor, capture the title tag, meta description, and H1 of
home, pricing, and any page ranking for a core term. A rewrite here usually
comes before a visible repositioning, so log it with the date in
`<competitor>/serp-copy.md` and quote both versions when it changes.

## Did it cost us anything
When Search Console is signed in, pair every position change with the user's own
numbers for that query: clicks, impressions, and average position for the last
28 days against the prior 28. Screenshot the view. A competitor climbing on a
query the user never earned clicks from is a note. One climbing on a query that
just lost the user clicks is a finding, and it leads the brief. When Search
Console is not signed in, say the effect is unmeasured. Never assert a traffic
loss without the number behind it.

## Brand defense
Check every run whether anyone is bidding on the user's brand term, and whether
a competitor's compare page or an affiliate roundup outranks the user's own
answer to it. Both are their own line in the brief when true.

## Output
A table of core terms with the user's paid and organic position, each watched
competitor's, and the change since last run. Then the advertiser set that moved,
the title and meta rewrites, the brand-term status, and the Search Console
consequence where it exists. Nothing if nothing moved.

## Never
Click a competitor's paid result. Use a rank-tracking claim you cannot
screenshot. Report a position as a fact without the date and the screenshot,
since results vary by location and personalization. Say so once when it matters.
