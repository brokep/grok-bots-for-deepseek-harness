---
name: campaign-loop
description: "Use to check campaigns, run the measure and improve loop, plan a launch, or undo a change."
---

# campaign-loop

Part of the Distro Bot agent preset.

# campaign-loop

Run, measure, and improve campaigns: one pass per Campaign check, or when asked.

## Each pass

1. distro.py status and distro.py playbook, then fresh numbers per ad-accounts.
2. distro.py report --days 7: pacing against the caps, flags (spikes, cost jumps, stopped results, stale data), winners and losers with their confidence, fatigue, channel mix, suggestions, caveats. A spend or broken-results flag leads.
3. At most one change per campaign: pause a loser, refresh a tired ad, add a variant from a winner or a playbook line (ad-creative), tune targeting inside <home>/targeting.md, or move budget toward the best cost per result. Never call a winner below the sample the report names.
4. distro.py propose it. Lane autopilot: apply it per ad-accounts, distro.py applied <id> --note "<what you verified>", and report it with its undo. Lane ask: show it with the numbers and wait. On the user's yes: distro.py approve <id> --words "<their words>", apply, distro.py applied. Blocked: name the cap it hits.
5. distro.py learn one line per result: what won, by how much, at what confidence, and what lost.

## Autopilot guardrails

Creative and targeting only, only when propose says lane autopilot: at most 3 changes per campaign a week, none within 3 days of the last unless pausing a flagged loser, 2 or more live ads per ad set, new ads only in running ad sets, audiences only from targeting.md, which the user can edit (exclusions and negative keywords are fine), the same landing pages and goal. Anything else asks.

## New campaign

A plan in <home>/plans/<date>-<slug>.md: the goal, the conversion and proof it fires (tags from distro.py site, or recent events in the account), the audience from targeting.md, a daily budget inside room_per_day in distro.py status, 3 to 5 ads from ad-creative, the landing page, and the test it runs. distro.py propose --kind launch. The yes builds it paused, and the read-back gets a second yes to start it.

## Undo

"undo <id>": put the old value back, then distro.py revert <id>.

## Report

Spend against the cap, then results and cost per result by channel with the change since last period, what changed and why, flags, and the next tests. Numbers carry source and date. A quiet day is one line.
