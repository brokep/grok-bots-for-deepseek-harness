---
name: routine-andrew-trumpet-weekly
description: "Scheduled routine: Friday: Slack outreach channel vs tracker for one exec."
---

# Weekly leadership-outreach check

Part of the frank agent preset.

Schedule, as written by the template author: Friday: Slack outreach channel vs tracker for one exec.

## What to do on each run

Friday weekly task. Check the leadership-outreach Slack channel for requests where {{EXEC_NAME}} should reach out. Cross-reference the Notion (or Sheet) tracker (newest first, Sent? column).

FILL-INS: {{OUTREACH_SLACK_CHANNEL}}, {{EXEC_NAME}}, {{TRACKER_URL}}, {{USER_NAME}}

Steps:
1. Search the channel for that exec's requests. Capture account, date, requester, stage/forecast, draft link, sent signals (✅, "sent", bot completed).
2. Read tracker; see listed vs Sent.
3. Propose NEW rows at the top (Sent unchecked). Do not mark Sent or react in Slack without confirmation.
4. Notify {{USER_NAME}}: new needing attention / still outstanding / all caught up. Link the tracker.
5. Never send the outreach itself from this routine.

Fires on:
- cron `0 11 * * 5`

Ask the importing user for:
- Timezone
