---
name: review-sheet
description: "Use before anything is built, and whenever copy or a variant changes. Writes the campaign, variants, targeting, exclusions, copy fields with counted characters against the limit that platform shows, budget, and bid strategy into a sheet the user approves first."
---

# review-sheet

Part of the Performance Marketer agent preset.

# Review sheet

The sheet is the deliverable that comes before the build. The user reads it, edits it, and
approves it. Nothing is created in an ad account until they do.

## When to use
Before any build, when copy changes, when a variant is added, and whenever the user asks what
would be built.

## Inputs
The accepted test plan, the platform and its ACCOUNTS line, the copy source (a paste, a document
in Drive, or a teammate handoff), the landing page, the final URL, and the daily budget and
maximum CPC cap when the user has named them. Google Sheets when connected. When it is not, the
same sheet is written as Markdown in chat and saved to
/workspace/ads/<platform>/<campaign-slug>/review-sheet.md. The sheet is the same either way, only
the surface changes.

## Tabs and columns
One sheet per platform. Write all five tabs. Empty is fine, missing is not.

1. Overview: Variant | Platform | Hypothesis | Ad group or ad set | Final URL | Status
2. Ad copy, one row per field: Variant | Platform | Ad group or ad set | Field | Copy | Chars |
   Limit | OK | Source | Status
3. Targeting: Ad group or ad set | Keyword or audience | Match type | Why | Status
4. Exclusions: Term or audience | Match type | Why
5. Settings: Campaign name | Platform | Objective | Networks or placements | Locations |
   Languages | Daily budget | Budget level | Bid strategy | Maximum CPC cap | Schedule | Start
   state

Status in every tab is Keep, Edit, or Cut. Only Keep rows get built. An Edit row carries what has
to change in the same row. A Cut row stays in the sheet as a record and is never built.

## Character limits, counted not guessed
Count every field yourself, put the number in the Chars column beside its Limit, and mark OK yes
or no. Count characters, including spaces and punctuation, not words.

Google Ads and Microsoft Ads responsive search ads, which are stable enough to state here:
- Headline: 30 characters maximum. At least 3 per ad, at most 15.
- Description: 90 characters maximum. At least 2 per ad, at most 4.
- Display path: two optional fields, 15 characters each.

Every other platform and every other ad format: read the limit the composer shows for that field
in the signed-in interface, screenshot it, and put that number in the Limit column. Never carry a
limit over from another platform and never state one from memory. If I cannot see the limit,
write "limit unread" in the column rather than a number.

Anything over the limit is rewritten to fit and marked Edit, with the original in the Source
column, never silently trimmed. Anything under the minimum count for an ad is a blocking gap
listed under Missing, never filled with invented copy.

## Settings the sheet always states
- Platform, and the account name from the ACCOUNTS line, so the user can see where this lands.
- Objective: the lowest-intervention click objective the platform offers, named exactly as the
  platform names it.
- Bid strategy: the cheapest-click option with a maximum CPC cap on the search platforms. On the
  others, the closest cost control the platform offers, named exactly, with the cap.
- Daily budget and the level it sits at, campaign or ad set. State the implied figure over 30 days
  beside it so the user sees what the daily number means over a month.
- Placements or networks: the narrowest sensible set unless the user asks otherwise. Say plainly
  that adding partner or audience networks changes what the test measures.
- Start state: Paused or off, at every level, campaign, ad group or ad set, and ad.
- Locations, languages, and schedule: whatever the user names, stated explicitly rather than left
  to a default nobody looked at.

## Rules
- One ad group, ad set, or campaign per named variant. Same targeting, same exclusions, same
  budget, and the same final URL across every variant, so the copy is the only thing that differs.
  Any deviation the platform forces is called out in the Overview row with the reason.
- Variants carry their real positioning names. Never A, B, Test 1, or placeholder.
- Every line of copy carries its Source: the paste, the document, the teammate handoff, or
  "written here from <the page section>". Copy written here is marked as such so the user can see
  what is theirs and what is mine.
- Never invent a product claim, a spec, a price, a guarantee, or a statistic. If an ad needs a
  number the source does not have, leave the field blank and list it under Missing.
- Check every final URL before delivering the sheet. A URL that does not load is a Cut row with
  the reason.

## Output
The sheet, plus 5 lines in chat: platform and campaign name, variant count, targeting count, daily
budget and cap, and what is still blank. Then one line asking for approval of the whole sheet.
Attach the landing page screenshot, the composer screenshot for any limit read from the interface,
and the sheet screenshot when Sheets is connected.

## Never
Build from this sheet before the user approves it. Read a comment on one tab as approval of the
sheet. Change an approved sheet without saying what changed and asking again. Put a live campaign
identifier, an account credential, or any billing detail in the sheet.
