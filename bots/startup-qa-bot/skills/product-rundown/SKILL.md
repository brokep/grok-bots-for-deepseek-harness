---
name: product-rundown
description: "Use after a product walk: sort shipped, unshipped, broke, and decisions, send the rundown, hand bugs to the bug-triage teammate, and record the user's calls."
---

# product-rundown

Part of the Startup QA Bot agent preset.

# product-rundown

Sort the walk and deliver the daily rundown. Runs after product-walk.

## Sort

- Shipped: a new surface, or a change signal you saw live. Claimed but not visible goes under Unshipped as "claimed, not live".
- Unshipped: something that was live and is gone. qa.py check missing records it. Never assume it was removed on purpose.
- Broke: what a user would hit that fails: an error, a dead button, a blank page, wrong data. Repro steps: 1) where, 2) what you did, 3) what happened instead of what you expected, plus a shot.
- Decision: works as built but needs a product call: a feature removed with no note, two flows that disagree, copy that contradicts the docs, a half rolled-out change.
Record each with qa.py find <shipped|unshipped|broke|decision> "<title>" --surface <id>, plus --repro, --expected, --actual, and --shot for bugs. qa.py keeps anything already reported or settled out of the rundown.

## Deliver

qa.py rundown writes report.md in the run folder and prints the message. Send it unchanged as one SendToUser text, then report.md as an attachment unless the day was quiet.

## Hand-offs

Bugs: with settings.triage set, send each bug in handoff to that teammate with SendToAgent, priority true: title, repro steps, expected and actual, where, when, and what the shot shows, since my files don't travel. Then qa.py sent <id>. No teammate: the bug lines are copy-ready for the user.
Calls: only the user decides. When they make one, qa.py decide <id> "<their call>", and say it won't come up again.
Shipped: if they have a sales or marketing teammate, offer once to send it what shipped, by role, so it only sells what's live.

## Never

Call a bug fixed without rechecking it, present a guess as a decision, or post the rundown anywhere but this chat.
