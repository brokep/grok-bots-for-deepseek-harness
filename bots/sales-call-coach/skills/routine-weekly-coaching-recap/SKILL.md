---
name: routine-weekly-coaching-recap
description: "Scheduled routine: Once a week, reads the calls you logged and sends the counts that moved, the two weakest dimensions with quotes, and the one habit to work on next."
---

# Weekly coaching recap

Part of the Sales Call Coach agent preset.

Schedule, as written by the template author: Once a week, reads the calls you logged and sends the counts that moved, the two weakest dimensions with quotes, and the one habit to work on next.

## What to do on each run

Run once a week on the day and hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read every scorecard written to the coaching log since the last recap. Send four short parts. The counts for the week, talk share, questions asked, and longest monologue, each with its direction against the week before. The two lowest dimensions, one quote each from a real call. What got better, with the count that moved, and nothing at all when nothing did. One habit for next week and the drill that builds it. Keep it under 200 words. When the user logged no calls this week, send two lines: nothing logged, and the habit still open from last time. Never invent a call, a quote, or a number. Never say a rep improved without a count behind it. Do not post or send the recap anywhere outside this chat unless the user asks for that in this run.
