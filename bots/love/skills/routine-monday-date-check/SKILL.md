---
name: routine-monday-date-check
description: "Scheduled routine: Monday date check"
---

# Monday date check

Part of the Love ❤️ agent preset.

Schedule, as written by the template author: Monday date check

## What to do on each run

Monday 08:00 date check. One message to the owner. Stay silent if a date with his partner is already booked in the next 14 days.

Read the private partner notes file first. Read the private Life notes first and act on any For Love lines (tables, bookings: draft slots with times and a link; never book, call, or email the venue).

Check only the owner's calendars (personal calendar, his own events, personal inbox if available) for a date with his partner in the next 14 days. Never open his partner's calendar, messages or accounts. Do not invent events.

If nothing is booked: send him one short WhatsApp-mate message with three options, each with dates, prices and links. One dog-friendly, one within 20 minutes of home, one worth the drive. He picks. You draft the calendar entry. He confirms. Never book. Never spend money.

If a date is booked: do not message him.

Write a short Life note for the day. Close with Worth your attention: yes + why / no. If no, five lines max. Never put the partner notes file on the bus. Never talk to other bots. Files only. No em dashes, no cheese, no guilt. If he said not now, log it in the partner notes file and go quiet until the next slot.

Fires on:
- cron `0 8 * * 1`

Ask the importing user for:
- Timezone
