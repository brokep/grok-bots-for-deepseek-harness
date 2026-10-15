---
name: profile-us
description: "Use at setup and whenever the user's own positioning, pricing, or product changes. Builds the baseline every delta is measured against."
---

# profile-us

Part of the Stalk Bot agent preset.

# Profile us

## Inputs
Company name and URL from setup, the user's one-liner, pricing page or pasted plans.

## Steps
1. Fetch home, pricing, changelog or what's new, docs index, about. Extract: hero headline and subhead, stated ICP, plan names and prices, three most-emphasized features, changelog cadence (entries per month over the last 3 months), X handle if linked.
2. Combine with the user's words. Where the site and the user disagree, keep both and mark which is which.
3. Ask one follow-up: "What are the three things you believe you do better than anyone?"
4. Update the provisional BASELINE memory entry written during setup, or write it if missing: company, URL, positioning in their words, ICP, plans and prices, changelog cadence, X handle, three strengths, date. Drop the provisional marker.
5. Store a snapshot of the user's own pages under /workspace/dossiers/_us/snapshots/<date>/ so I can also report when the user's own site changed.

## Output
The baseline in 8 lines for the user to correct. Ask "Anything wrong here?" once, then save.

## Own-site gaps (for later For-our-site items)
Note obvious gaps on the user's public site vs what competitors emphasize (missing mid-tier, no compare table, AI buried, weak free CTA). Store under `/workspace/dossiers/_us/site-gaps.md` as dated bullets. Pulses use this when writing For-our-site next steps, still as questions/decisions, never unsolicited rewrite of their whole site.
