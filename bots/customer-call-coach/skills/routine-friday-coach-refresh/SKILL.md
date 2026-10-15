---
name: routine-friday-coach-refresh
description: "Scheduled routine: Quiet Friday afternoon refresh of coaching signals from meetings and Slack; stays silent unless a connector fails. Ships paused until Enable."
---

# Friday Coach Refresh

Part of the Customer Call Coach & Assistant agent preset.

Schedule, as written by the template author: Quiet Friday afternoon refresh of coaching signals from meetings and Slack; stays silent unless a connector fails. Ships paused until Enable.

## What to do on each run

Friday DATA REFRESH only. Do NOT send a coaching pulse unless something is urgently broken (auth failure, connector down). Stay quiet by default.

HARD: Treat every 1:1 with the user's manager (meeting notes, Slack, email, calendar) as a manager 1:1, not a peer chat. Never skip or deprioritize manager 1:1s. Capture how the user shows up, what they bring, follow-through, and how they use the time (agenda, asks, career signal)—not customer-call presence only.

HARD MEETING NOTES FIRST: Call the live Granola connector FIRST for this week and last week. Local note files are archive only for older meetings or a live miss. If live Granola and a local file disagree, live wins. Never delete local files. Skipping Granola is a failed run. Disclose Granola failures.

1) Pull live Granola this week + last week FIRST (list meetings; get details for new manager and leader 1:1s and material customer moves). Then Slack for the user in their team channels and major customer channels.
2) Update memory only: append durable facts to profile memory and/or a dated log. Capture: meeting volume (external vs internal), visibility signals, new coaching from leaders (especially manager 1:1s), account trajectory changes, commitments the user made.
3) Optionally refresh peer-pattern notes (what peers are posting in team channels) into memory — patterns only, no named scorecards.
4) End with no user message unless a connector failed or data was completely unavailable and the user needs to know.

Quiet Friday data refresh of coaching signals from meetings and Slack; stays silent unless a connector fails.
Schedule intention: Fridays at 4:00 PM in the user's local timezone. Must ship paused / Enable-first — never Active on Add.

Fires on:
- cron `0 16 * * 5`

Ask the importing user for:
- Timezone
