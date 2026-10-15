---
name: messaging-matrix
description: "Use this when the user asks how they compare, for research on their own product, for a homepage screenshot, or for the first step a marketer takes when planning a campaign. Their claims beside the user's on the same dimensions, then gaps and marketing counter-moves."
---

# messaging-matrix

Part of the Market Researcher agent preset.

# Messaging matrix

Their claims beside the user's claims, on the same dimensions, so the difference
is visible instead of argued.

## Cues that fire this skill
Any version of:
- "do a research exercise on the product we are working on"
- "grab a screenshot of our product and tell me what you see"
- "kick off the first step every marketer does when planning a campaign"
- "study the product, identify competitors, do positioning analysis, find the
  gaps in competitor positioning that inform our marketing strategy and GTM"
- "where do we stand in this market"
- "how do we compare to <competitor>"

## Hard rule on how the product is described
Treat the user's product as a live, real product. Never call it a concept,
fictional, pre-launch, or waitlist-only. Never say its proofs are not shipped.
If a claim on their site cannot be verified, say the claim is unverified, not
that the product is not real.

## Steps
1. Open with a live screenshot of the user's own homepage, taken now. Attach it
   as the first thing in the reply, before any text about the product.
2. One-liner in their words from the hero, plus who it is for.
3. Market in three lines: the category as a buyer would name it, the 2 to 4
   things buyers actually compare on, and where the money moves. When Google Ads
   is signed in, the auction list says who is really competing for demand and it
   beats a category roundup. When Search Console is signed in, the query set
   says which part of the category the user already owns.
4. **The matrix.** Rows are dimensions, columns are us and each competitor, 3 to
   5 competitors. Use the dimensions the market actually buys on, and keep them
   stable between runs so the matrix is comparable over time. Typical rows:
   headline claim, who it is for, the proof they lead with, price posture, the
   offer, the objection they pre-empt, the word they own. Every cell is a short
   quote from their own page with a link and a date, or "not claimed", which is
   as informative as a claim.
5. **Gaps to lean into**, 2 to 4: a dimension nobody in the matrix owns, a claim
   everyone makes the same way, an audience nobody names, an objection nobody
   answers. Each needs the evidence that shows it is open. A core term with real
   impressions and no strong answer in the matrix is the best kind.
6. **Counter-moves**, 3 to 5, marketing only: a message, an offer, a channel, a
   creative angle, or a landing page change. Each gets a one-line headline the
   user could actually run, and each ties to a gap above. Never a product
   suggestion and never a roadmap.
7. Could not read footer when a source failed.

## Refresh
On demand, and whenever a competitor's fold message or the user's own
positioning changes. Keep the previous version at
`_us/matrix/<date>-matrix.md` so the drift is readable over months, and call out
which cells moved since last time.

## Shape
Succinct and scannable. Short lines, a real table, no preamble, no closing
paragraph. Readable in under two minutes. Every cell carries a link and a date,
every number carries a live-UI or export label.

## Never
Invent a claim, a price, or a traffic number. Fill a cell from memory instead of
the page. Write finished marketing copy unless the user asks. Recommend a spend
or a product change.
