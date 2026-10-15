---
name: routine-daily-hiring-brief
description: "Scheduled routine: Every weekday morning, today's interviews, who still needs scheduling, and what is waiting on someone."
---

# Daily hiring brief

Part of the Recruiting Coordinator agent preset.

Schedule, as written by the template author: Every weekday morning, today's interviews, who still needs scheduling, and what is waiting on someone.

## What to do on each run

Run every weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the tracker, plus the calendar and candidate mail when those are connected. Post the brief in three parts. Today: every interview with the time in the user's timezone, the candidate, the role, the interviewer per slot, and any slot with no scorecard owner. Needs scheduling: candidates waiting on a loop, oldest first, with days waiting. Waiting on someone: who is holding each item up and the one action that unblocks it. Keep it under 200 words and open on the first interview, no preamble. Write the check date back to the tracker. When the day is clear and nothing is stuck, say that in one line. Never invent a meeting, an interviewer, a candidate, or a piece of feedback. Do not mail a candidate or an interviewer from this run, offer a draft instead.
