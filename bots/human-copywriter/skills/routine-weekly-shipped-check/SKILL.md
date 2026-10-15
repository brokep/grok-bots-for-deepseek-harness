---
name: routine-weekly-shipped-check
description: "Scheduled routine: Every Friday afternoon, asks what copy actually went out this week and folds the edits the user made into their voice profile."
---

# Weekly shipped check

Part of the Copy Humanizer agent preset.

Schedule, as written by the template author: Every Friday afternoon, asks what copy actually went out this week and folds the edits the user made into their voice profile.

## What to do on each run

Run every Friday afternoon at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the drafts and edits you produced this week and the shipped log. If nothing was drafted or edited this week, send nothing at all. Otherwise send one short message naming the pieces still marked unshipped, at most three, and ask one question: what went out, and what did they change. Take a pasted final, a link, or a one-line answer. When they hand you a final, run Learn from what shipped, update the voice profile, and reply with two lines on what you changed in it. When they skip or do not reply, mark those pieces closed and never ask about them again. Never nag, never send a second reminder for the same piece, and never guess what shipped from a live page. Never publish, send, or post anything from this run.
