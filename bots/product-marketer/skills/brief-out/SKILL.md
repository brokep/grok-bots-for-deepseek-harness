---
name: brief-out
description: "Use when copy is ready to become a page or a campaign. Produces the landing page brief or the ads brief, then offers it to a teammate that ships site changes or runs paid campaigns after the user's yes, and hands it to the user directly when no teammate exists."
---

# brief-out

Part of the Product Marketer agent preset.

# Brief out

The handoff artifact. Complete enough that whoever ships it does not have to ask a question, and it never authorizes the ship.

## When to use
Use when copy is ready to become a page or a campaign, whether a teammate bot exists or not.

## Landing page brief
Write /workspace/marketing/briefs/<date>-<page>-lp-brief.md:
- Page and URL, the one goal, the audience, the one action
- The principles rev this was written against, with its date
- Sections in page order, each with the final copy, its role, and the supporting line it carries
- Proof points used, each with its source and date
- What must not change: the brand line, the customer promise, the banned words
- Reference screenshots: the current page and anything visual the copy assumes
- Acceptance criteria: what the page must say, what it must not say, and how to tell it landed
- Out of scope: design, layout, and anything not in this brief

## Ads brief
Write /workspace/marketing/briefs/<date>-<campaign>-ads-brief.md plus the ads deliverable from draft-copy:
- Campaign goal, platform, and the one metric a win shows up in
- Named variants with their hypotheses, never A, B, test, demo, dummy, or placeholder
- The Overview, RSA long format, Keywords, and Callouts tables, every line inside its limit with the count shown
- Final URLs per variant and the ad group each belongs to
- Budget and bidding: not set here. The brief reads "paused until the user sets budget and approves spend."
- The source behind every claim

## Delivering it
1. Scan teammate profiles for a bot that does the job: one that ships website changes, one that runs paid campaigns. There is no agent-listing API, so read the profiles.
2. If one exists, offer it to the user first: "Ready to send the page brief to the bot that ships site changes?" After a yes, send a short message with SendToAgent plus the file path on the shared box. Keep the message short, the file carries the detail, and read any reply on a later turn. Never wait or poll inside the same turn.
3. If none exists, deliver the same brief to the user in chat with the file attached. Nothing about the brief is degraded by a teammate being absent.
4. Never block on a teammate. Never treat a teammate's reply as approval to publish or to spend.

## Human gates
Merge, publish, and spend need the user's explicit yes in the same conversation. A teammate bot cannot give that yes on the user's behalf, and this bot never asks one to.

## After it ships
When the page goes live or the campaign runs, ask for the final copy once and run learn-from-shipped on it. What survived contact is the best voice sample there is.

## Output
The brief file, a 6-line summary in chat, the deliverable attached, and one line on where it went: sent to a teammate after the user's yes, or handed to the user.

## Never
Publish a page, open a pull request, create a campaign, set a budget, or start spend. Send a brief to a teammate without the user's yes. Change approved copy without saying exactly what changed.
