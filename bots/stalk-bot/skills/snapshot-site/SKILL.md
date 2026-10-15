---
name: snapshot-site
description: "Default-on modules for website, pricing, changelog, positioning drift, and open roles. Fetches watched pages, diffs against the last snapshot, screenshots everything, stores, and writes a hiring direction read."
---

# snapshot-site

Part of the Stalk Bot agent preset.

# Snapshot site

## Inputs
Competitor, watched pages from memory (default: home, pricing, changelog or what's new, docs index, about, careers), previous snapshot path.

## Steps
1. Fetch each page. Strip nav, footer, scripts, cookie banners. Keep headings, body text, prices, plan names, CTAs, and changelog entries with dates.
2. Screenshot each page.
3. Store text and screenshot under /workspace/dossiers/<competitor>/snapshots/<date>/<page>.
4. Diff text against the previous snapshot per page. Ignore date-only changes, rotating testimonials, and whitespace.
5. Classify each real diff: pricing (plan added, removed, price changed, limit changed), positioning (hero, subhead, tagline, ICP language), feature (added or removed from a list), changelog (new entries, with their dates), jobs (roles added or removed, with department), other.
6. For changelog: parse entries into /workspace/dossiers/<competitor>/changelog.md with dates. Compute entries per month over the trailing 3 months.
7. For positioning: append the current hero and subhead to /workspace/dossiers/<competitor>/positioning-timeline.md with the date, only if changed.
8. For open roles (default-on module): read the careers page and, when they use one, the hosted job board it links to (Greenhouse, Lever, Ashby, Workable, or similar are public pages). For each role capture title, team, location, level, and the first two responsibilities. Append new roles to /workspace/dossiers/<competitor>/hiring.md with date, and mark roles that disappeared as closed with the date. Screenshot the careers page and each new posting.
9. Direction read: after each hiring diff, write 2 to 4 lines in /workspace/dossiers/<competitor>/hiring.md under the date: what the new roles say about where they are investing (for example "3 enterprise AEs and a solutions engineer in 30 days: moving upmarket", "first ML platform role: building models in-house", "support roles closed, CS roles opened: shifting from reactive to expansion"). Count open roles by function and show the change since last pulse. Only read direction from roles they actually posted; never infer from silence.

## Output
Per competitor: a list of classified changes, each with before, after, page link, screenshot path, date. "First seen" for pages with no prior snapshot. Nothing if nothing changed.

## Website pros / cons (for pulse and dossiers)
After a meaningful home or pricing snapshot (first seen, or real positioning/pricing diff), draft or refresh `/workspace/dossiers/<competitor>/site-pros-cons.md`:
- **Pros** (2 to 4): advantages a prospect would infer from their public pages alone, price points, free tier limits, named features in the hero, social proof, compare tables. Quote their words; link the page; date it.
- **Cons** (2 to 4): visible weaknesses vs our baseline or vs buyer expectations their page itself raises, pricing cliffs, AI gated behind expensive tiers, card-required trials, missing compare proof, vague ICP. Only what the page shows or conspicuously omits; never invent product bugs you did not see.
Pulse lifts from this file; do not regenerate from memory alone.


## Snapshot discipline (from memory)
Watched pages per competitor default: home, pricing, changelog or what's new, docs index, about, careers, plus any the user adds. Fetch, strip navigation and scripts, hash the main content, store the text and a screenshot per pulse under /workspace/dossiers/<competitor>/snapshots/<date>/. Diff against the previous snapshot. Ignore diffs that are only dates, cookie banners, or rotating testimonials. Report additions, removals, and rewording of headlines, prices, plan names, feature lists, and CTAs. All dossier paths in this bot are under /workspace/dossiers/.
