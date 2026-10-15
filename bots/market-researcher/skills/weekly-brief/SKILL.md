---
name: weekly-brief
description: "Use this when the weekly routine fires or the user says run the brief. Per competitor ads, pages and offers, pricing and promotions, channel mix, search overlap, and content, then Against our marketing, Counter-moves, and Worth a decision."
---

# weekly-brief

Part of the Market Researcher agent preset.

# Weekly brief

## When to use
The weekly routine, or when the user says run the brief.

## Steps
1. Re-read the BASELINE entry, `_us/baseline.md`, CORE TERMS, the ACCOUNTS
   entries, and each competitor's index.md.
2. Per competitor, run the enabled surfaces: ad-and-creative-analysis,
   landing-page-and-offer-watch, search-overlap, content-and-social-cadence.
   Each reads the live platform UI first when a platform is signed in, and the
   export second.
3. When a session has lapsed, follow connect-accounts, put it in Could not read,
   and finish on public sources. Never stall the brief on a sign in.
4. Collect every change with its evidence: link, date, screenshot path, and the
   source label (live UI or export).
5. Write it in this order:
   - **Per competitor**, one block each:
     - New and retired ads: counts, the new hooks and offers in their words, the
       swipe file grid, and the fatigue numbers.
     - Landing page and offer changes: fold message, CTA, form, proof, with
       before and after.
     - Pricing and promotions: price and plan movement, promotions opened and
       closed, with dates.
     - Channel mix shifts: a network entered or left, or the creative weight
       moved between networks.
     - Search overlap changes: paid and organic positions gained and lost on the
       core terms, advertiser set changes, title and meta rewrites.
     - Content and social cadence: posts per month against the trailing average,
       themes, engagement share, any campaign call.
   - **Our numbers**, only when GA4, Search Console, or Google Ads is signed in:
     2 to 4 lines. Traffic by channel, the queries that moved, the auction
     overlap shift, each with the date range and the screenshot. Skip the
     section entirely when nothing is signed in rather than guessing.
   - **Against our marketing**: each material change read against the baseline
     in one or two sentences. Where they moved onto the user's claim, undercut
     an offer, entered a channel the user owns, or started bidding on the user's
     terms.
   - **Counter-moves**, 2 to 5, marketing only: a message change, an offer
     change, a channel move, a creative angle, or a landing page change. Each
     cites an item above and is written as a decision the user can take this
     week. Never a product suggestion, never a roadmap, never generic advice
     about improving messaging.
   - **Worth a decision**, max 3: yes or no questions, each pointing at an item
     above.
   - **Could not read**: every source that failed, one line each with the
     reason, including any lapsed session.
6. Quiet week: one line, "Quiet week, nothing moved across N competitors since
   <date>." No report, no invented items, no filler counter-moves.
7. Update each `<competitor>/index.md` with the run date and change count, and
   move the watermark.
8. Build the report per capture-and-report and attach it. Deliver in this chat, or
   to the Slack channel saved at setup, never both unless asked.

## Handoffs
When a counter-move needs copy, a page change, an ad build, or a report, produce
the brief for it first. Then, if a teammate that does that job exists, offer to
send it with SendToAgent. If none exists, the artifact is the deliverable. Never
wait on a teammate, and never let a teammate approve a publish, a spend, or a
send.

## Rules
Never repeat a change already reported unless it moved again. Never editorialize
without evidence. Every number and quote carries a source, a date, and a live-UI
or export label. Read only in every signed-in account.
