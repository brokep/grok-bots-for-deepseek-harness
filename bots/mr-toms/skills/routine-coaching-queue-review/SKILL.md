---
name: routine-coaching-queue-review
description: "Scheduled routine: Once a week, coaches the scorecards and messages the user queued and flags ratings written without evidence."
---

# Interview coaching review

Part of the Recruiting Coordinator agent preset.

Schedule, as written by the template author: Once a week, coaches the scorecards and messages the user queued and flags ratings written without evidence.

## What to do on each run

Run once a week on the afternoon the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the coaching queue and any scorecards or candidate messages the user added since the last run. For each scorecard, check that every rating has a quote or an observed behavior behind it, and turn the ones carrying only an impression such as "seemed junior" into the question the interviewer should have asked. For each queued message, tighten it and say in one line what you changed and why. Then name the one habit worth fixing this week and the example that shows it. Keep it under 250 words. Stay quiet when the queue is empty and no scorecards came in. Never invent a candidate answer, never rate the candidate yourself, and never tell the user who to hire.
