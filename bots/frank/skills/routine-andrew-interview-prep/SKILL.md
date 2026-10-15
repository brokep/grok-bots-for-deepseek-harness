---
name: routine-andrew-interview-prep
description: "Scheduled routine: Weekdays: check today's interviews vs a Notion prep doc."
---

# Exec interview-prep reminder

Part of the frank agent preset.

Schedule, as written by the template author: Weekdays: check today's interviews vs a Notion prep doc.

## What to do on each run

Weekday (Mon–Fri) morning task. Goal: make sure the supported exec has prep for every interview TODAY (user local timezone).

FILL-INS (set on import):
- {{EXEC_CALENDAR_ID}} — exec Google Calendar
- {{INTERVIEW_PREP_NOTION_URL}} — Notion doc with per-candidate prep by date
- {{USER_NAME}} — EA to notify

Steps:
1. Prefer Google Calendar connector. List TODAY's events; find INTERVIEW-type meetings (titles like Interview, Skip Level Interview, hiring panels). Capture time, candidate name, role from the title.
2. Read the Notion prep doc. Cross-reference each calendar interview to a prep entry (match first+last loosely; if unsure, flag).
3. Notify {{USER_NAME}} with a short chronological list (time | candidate | role) marked ✅ prep found or ⚠️ no prep. If none today, say so briefly. If all have prep, say so.
4. Never run Sat/Sun. Do not invent prep content.

Fires on:
- cron `0 8 * * 1-5`

Ask the importing user for:
- Timezone
