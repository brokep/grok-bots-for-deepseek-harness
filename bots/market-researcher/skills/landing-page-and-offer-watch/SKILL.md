---
name: landing-page-and-offer-watch
description: "Use this when you need a competitor's page and offer broken down or compared with the user's own: fold message, offer, CTA, form fields, proof, objections, plus price movement and the dated promotion calendar."
---

# landing-page-and-offer-watch

Part of the Market Researcher agent preset.

# Landing page and offer watch

## When to use
Every weekly brief. On demand when the user asks what a competitor is promising
or charging, or wants their own page compared against one.

## Pages to watch, per competitor
Home, pricing, the main product page, any compare page, and every landing page
an ad points to (ad-and-creative-analysis finds those). Store snapshots under
`<competitor>/snapshots/<date>/<page>` in the working root.

## Landing page breakdown
For each page, capture and record in `<competitor>/pages/<date>-<page>.md`:
1. **Above the fold**: the headline, the subhead, the visual, and what a visitor
   knows in five seconds. Screenshot the fold at 1440 wide, not the full page.
2. **Offer**: what they are actually giving (trial length, card required or not,
   demo, freemium tier, discount, guarantee, free tool or report), in their
   words.
3. **CTA**: primary wording, secondary wording, how many times it repeats, and
   where each one goes.
4. **Form**: how many fields, which are required, whether work email is
   enforced, whether there is a phone or company-size qualifier. Field count is
   the single best proxy for how much friction they accept.
5. **Proof**: logos, named customers, numbers, quotes, third-party badges,
   security or compliance marks. Count them and note which are specific.
6. **Objections handled**: FAQ, comparison table, pricing calculator, migration
   promise, security page link.
7. **Page speed impression** and whether the fold works on a phone width.

## Side by side with our page
When the user asks, or whenever a competitor's page changes materially, put
their page beside the user's equivalent page in a two-column table on exactly
these rows: fold message, offer, CTA wording, form fields, proof count and type,
objections handled, price shown or hidden. Attach the two folds as one composed
image per capture-and-report. End with what the user's page is missing that theirs
has, and what theirs is missing that the user's has. Both directions, always.

## Pricing and promotion calendar
1. Snapshot the pricing page every run. Diff plan names, prices, limits, seat
   minimums, trial terms, and what sits behind which tier.
2. Every discount, seasonal offer, bundle, expiring banner, annual-prepay
   incentive, or free-tier change goes to `<competitor>/promotions.md` as one
   dated row: start seen, end seen, offer, the page or ad that carried it, the
   screenshot path.
3. That file is the calendar. After two or three cycles, say plainly whether a
   pattern exists: end of quarter, back to school, the week of a conference,
   always-on. Do not call two events a pattern.
4. A promotion that appears in the ads before the site is a test. A promotion on
   the pricing page with no ads behind it is positioning. Say which.

## Diff rules
Ignore date-only changes, rotating testimonials, and whitespace. Classify every
real diff: fold message, offer, CTA, form, proof, price, plan structure,
promotion, or other. Quote both versions for anything you call a message change,
and compose a before and after image per capture-and-report.

## Output
Per competitor: classified page changes with before and after, offer and price
movement, new and expired promotions with dates, and the side-by-side table when
one was asked for or earned. "First seen" for pages with no prior snapshot.
Nothing if nothing changed.

## Never
Fill in a form or start a trial to see what is behind it. Report a price change
without dated screenshots on both sides. Call two data points a seasonal
pattern.
