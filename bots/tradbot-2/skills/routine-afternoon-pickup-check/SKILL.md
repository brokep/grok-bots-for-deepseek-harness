---
name: routine-afternoon-pickup-check
description: "Scheduled routine: Every weekday afternoon, a one line check that today's pickup is covered, and the fix when it is not."
---

# Afternoon pickup check

Part of the Tradbot agent preset.

Schedule, as written by the template author: Every weekday afternoon, a one line check that today's pickup is covered, and the fix when it is not.

## What to do on each run

Run every weekday at 2:30pm in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. The hour is the point, a pickup problem found at 2:30pm still has time to be fixed. Read the pickup facts on the watch list, today's calendar, and mail since the morning. Check that every kid has a named adult, a place, and a time for today. Flag anything that moved: an early dismissal, a cancelled practice, a meeting sitting on top of the pickup hour, weather calling off an outdoor activity, a sick kid, a coach changing the field. Name the gap in one line, say which adult is closest to free, and offer the swap rather than making it. When a message would solve it, draft the note to the teacher, the coach, or the other parent and leave it in chat. A day that matches the plan gets one line, pickup is covered, with the time and the person. If you do not know the default pickup person, ask. Never message anyone yourself, never move a calendar event, and never guess a dismissal time you did not read. Stay quiet on the no school days the user told you about.

Fires on:
- cron `30 14 * * 1-5`

Ask the importing user for:
- Timezone
