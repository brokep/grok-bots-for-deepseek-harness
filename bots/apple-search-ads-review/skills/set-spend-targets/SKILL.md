---
name: set-spend-targets
description: "Use when the user first gives you a cost per install target, changes one, or asks what numbers you are holding them to."
---

# Set spend targets

Part of the Apple Search Ads Review agent preset.

Inputs: their target cost per install, the currency, and any split they care about.

1. Get one number first. A single blended target is enough to run a review, so do not stall on tiers.
2. Ask whether the target differs by anything that matters to them: storefront or region, or campaign type. On Apple Search Ads the useful split is brand terms, competitor terms, generic or category terms, discovery, and the Today tab or product page placements if they run them. Take what they give and leave the rest blended.
3. Write one row per group: group name, what it covers, target cost per install, currency, and a tolerance band. Default is 20 percent over target before you call something a problem, and say that out loud so they can change it.
4. Brand terms should carry their own much lower ceiling. If they have not set one, say so plainly rather than judging brand against the blended number, which makes brand look like a hero every week.
5. Ask whether a second number decides things for them: cost per trial, cost per paying subscriber, or return on ad spend. Record it with the export column that carries it. Without one, say plainly that you are judging on installs alone, which says nothing about what those installs do next.
6. Note whether their installs figure counts redownloads. Apple reports new downloads and redownloads separately, and a target set against total installs is a looser target than they think.
7. Show the table in chat, take one round of edits, then save it.

Rules: never invent a target. A group with no target of its own inherits the blended one and gets marked as inherited. Keep the currency on every row and never convert between currencies unless they give you the rate.

Save under the Apple Search Ads folder as the targets sheet.
