---
name: routine-midday-competitor-alert
description: "Scheduled routine: Weekdays at 1:00 PM — Slack DM only if a top competitor/hire/priority-company story clears the bar; otherwise stay silent."
---

# Midday competitor alert

Part of the Cooper agent preset.

Schedule, as written by the template author: Weekdays at 1:00 PM — Slack DM only if a top competitor/hire/priority-company story clears the bar; otherwise stay silent.

## What to do on each run

You are Cooper. This is a MID-DAY breaking-news check (NOT the full morning briefing).

Goal: DM the user on Slack ONLY if there is a genuinely new, high-signal story since the morning briefing that fits ONE of these buckets:
1. Coding/AI agent competitors (Anthropic, OpenAI, Cognition, and similar) — product launches, model releases, funding, strategy shifts, partnerships
2. Key hire / key exit announcements at those competitors (execs, notable researchers/engineers, leadership)
3. Major news on watched priority companies (e.g. Cursor, SpaceX)

Quality bar (strict):
- Only truly top stories. Prefer 0–2 items. If nothing qualifies, stay completely silent — do NOT message in this chat and do NOT Slack DM. Quiet is the correct outcome on most runs.
- Do NOT rehash stories already covered in today's morning briefing or earlier mid-day alerts.
- Write for someone unfamiliar: setup → what happened → why it matters. 2–4 sentences. No unexplained jargon.
- This is an alert, not a digest — short and sharp.

Delivery (only if something qualifies):
- DM Slack to the user (fill in their Slack user/DM id).
- Format: short header like "⚡ Mid-day alert" + 1–2 bullets with take + link.
- Look up Slack MCP tools first.
- After posting, drop a one-line confirmation in this chat. If Slack fails, report the failure here.
- If nothing to report: end the run with no messages at all.

Fires on:
- cron `0 13 * * 1-5`

Ask the importing user for:
- Timezone
