---
name: routine-weekly-proof-roundup
description: "Scheduled routine: Every Monday morning, what new proof came in, which customers are ready for a case study, which approvals are still sitting, and which claims have nothing behind them."
---

# Weekly proof roundup

Part of the Customer Proof Desk agent preset.

Schedule, as written by the template author: Every Monday morning, what new proof came in, which customers are ready for a case study, which approvals are still sitting, and which claims have nothing behind them.

## What to do on each run

Run every Monday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the proof bank plus anything the user added since the last run. Post four short sections. New this week: the sources that came in and the quotes and numbers pulled from them. Ready to write: the customers who now have a situation, an action, and a result, so a case study can be written today. Waiting on approval: every pending item with who it sits with and how many days it has been there, oldest first. Gaps: the claims this team keeps making that the bank still cannot support. Keep it under 200 words. A quiet week gets one line saying nothing new came in, plus the oldest pending approval. Never invent a quote, a customer, or a number to fill a section. Do not send an approval request, post to a channel, create a task, or publish anything from this run. Offer a draft instead.
