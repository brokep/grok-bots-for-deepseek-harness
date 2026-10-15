---
name: routine-andrew-room-rundown
description: "Scheduled routine: Weekday afternoon: room chart for two business days out."
---

# Exec conference-room rundown (2 business days ahead)

Part of the frank agent preset.

Schedule, as written by the template author: Weekday afternoon: room chart for two business days out.

## What to do on each run

Weekday task: post the EA a conference-room rundown for the supported exec so they stay ahead with a buffer. Review the day that is TWO business days out (Mon→Wed, Tue→Thu, Wed→Fri, Thu→next Mon, Fri→next Tue). Never run Sat/Sun.

FILL-INS:
- {{EXEC_CALENDAR_ID}}
- {{PREFERRED_ROOM_A_ID}} and label (small room, floor N)
- {{PREFERRED_ROOM_B_ID}} and label (small room, other floor)
- {{USER_NAME}}

Prefer Google Calendar connector over browser. List events on the exec calendar and both room resource calendars.

STEP 0 — WFH/travel first: if the target day shows all-day WFH/Remote/OOO/PTO/travel or working-location Home, do NOT build the chart; one-liner that no rooms are needed.

Otherwise: build a markdown table: time | meeting | booked | roomA | roomB. BOLD meetings that still need a room. booked = already-booked room or blank. ✅ free / ❌ taken / ⚠️ partial for room columns.

Booking suggestions: prefer the small preferred rooms; cluster back-to-back into one room; never change floors with no break; after a large-room call, next meeting in a small room on the SAME floor. Lead with which day the chart is for. Ask which rooms to book — do NOT book until confirmed.

Fires on:
- cron `30 14 * * 1-5`

Ask the importing user for:
- Timezone
