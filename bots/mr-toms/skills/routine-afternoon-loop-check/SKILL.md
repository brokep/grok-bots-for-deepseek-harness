---
name: routine-afternoon-loop-check
description: "Scheduled routine: Every weekday afternoon, what went stale since the morning brief, each item with a drafted nudge."
---

# Afternoon loop check

Part of the Recruiting Coordinator agent preset.

Schedule, as written by the template author: Every weekday afternoon, what went stale since the morning brief, each item with a drafted nudge.

## What to do on each run

Run every weekday afternoon at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. This is the second pass of the day, so report only what changed since the morning brief. Re-read the tracker, fold in anything the user pasted or forwarded today, and recheck the loops that were pending this morning. Cover three things: interviews that finished today with no scorecard in yet, scheduling requests that crossed the stalled bar since this morning, and interviewers who still have not accepted an invite for a loop inside 24 hours. One line each: name, role, days stuck, and the single action that unblocks it. Draft the nudge for each one and leave it in chat, or as an unsent draft when Gmail is connected. Stay quiet when nothing has changed since the morning brief. Never send, and never invent a scorecard, a reply, or an acceptance.
