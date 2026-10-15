---
name: market-scan
description: "Use for topics to jump on, competitor moves, trends, and positioning."
---

# market-scan

Part of the Distro Bot agent preset.

# market-scan

Topics to jump on, competitors, trends, and positioning. Read only, drafts only.

## Topics (Trend scan, or when asked)

Keywords and competitors from distro.py status. X: news, trends, and posts with the X connector (post search can fail with an access error, then skip it), logging keepers with distro.py topic add. Then distro.py scan hn and scan news per keyword, and WebSearch with site:reddit.com and the communities the user named. Worth jumping on: under 48 hours old, close to the problem the product solves, and gaining. Up to 3 a day, each with a draft post or reply, the link, and why now, then distro.py topic mark <id> drafted. A product QA teammate's note on what shipped becomes a launch post draft, only for what is live. On the user's yes for that exact text, post it in my browser (signed in per ad-accounts), send the link, and mark it posted.

## Competitors (Weekly distro review, or when asked)

A competitor-intel teammate's news first. Per competitor: distro.py site <url> --save <name> for landing page, offer, and price changes, new ads in the public Meta Ad Library, Google Ads Transparency Center, and LinkedIn Ad Library in my browser, with screenshots, and their recent X posts. Report what changed and what it means for the user's message.

## Trends

distro.py topics --days 30 for what keeps coming back, and what the winners in distro.py winners share. Questions people search go to the SEO and AEO teammate if one is saved.

## Positioning

From scans, the playbook, and what wins in ads: one claim, for whom, the proof, and how it differs from each competitor's message. Suggest edits to <home>/positioning.md with the evidence, saved only on the user's yes.
