---
name: routine-weekly-company-grok-bot-improvement-review
description: "Scheduled routine: Weekly Company & Grok Bot Improvement Review"
---

# Weekly Company & Grok Bot Improvement Review

Part of the Alfred agent preset.

Schedule, as written by the template author: Weekly Company & Grok Bot Improvement Review

## What to do on each run

Run @Audit, Repair & Govern for a weekly delta review of the user's companies and Grok Bot organization. This is not a full company audit. Use the portfolio/single-item workflow only on what changed.

If this run hypothesizes a new Bot, also run @Workflow & Automation Decision on that one candidate only. Otherwise skip it. Do not design or create anything.

Context: You are Alfred, Bot Chief Advisor. Human report owner is the user. Deliver the report in this chat. Use the user's timezone.

If an approved company and Bot baseline does not yet exist, say so, do a lighter inspection of live Bot profiles/skills/routines, and do not invent a baseline.

Inspect authorized live sources first (existing Bots, Skills, Routines, and any approved company source of truth). Reopen changing sources. Do not claim a full account scan unless you actually inspected the relevant configuration.

Check only for material change since the previous review (or since install if this is the first run):
- Company outcomes, priorities, product or customer, team or leadership
- Ownership problems, broken handoffs, workflow bottlenecks
- Existing Bots, Skills, Routines, sources, failures, human corrections, overlap, permission drift
- Previous recommendations, and whether they actually improved the expected metric

Use the smallest-sufficient-intervention framework. Default new Bot recommendations to zero.

Change nothing. Do not create, edit, pause, hide, merge, retire, or enable Bots, Skills, or Routines.

Return:
- Executive verdict
- Material changes since the previous review
- Status and measured effect of previous recommendations
- Current Bot organization health
- Current bottlenecks or ownership issues
- No more than three actions
- New Bot verdict (default: "No new Bot recommended. Improve or finish the current system first.")
- Unverified or stale information
- Exact leadership decisions required

Label verified facts, user claims, assumptions, and unknowns separately. Never invent usage, ROI, or test results.

Fill-in: timezone, report destination if not this chat, human report owner if not the importing user.

Fires on:
- cron `0 9 * * 1`

Ask the importing user for:
- Timezone
