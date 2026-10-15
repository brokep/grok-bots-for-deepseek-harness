---
name: routine-kitchen-table-newspaper
description: "Scheduled routine: Every weekday morning, the printable one-page kitchen newspaper kids can read at the table."
---

# Kitchen table newspaper

Part of the Tradbot agent preset.

Schedule, as written by the template author: Every weekday morning, the printable one-page kitchen newspaper kids can read at the table.

## What to do on each run

Run every weekday at 6:30am in the timezone saved in memory, or at the hour the user picked instead. Compute the cron from that timezone and never assume Pacific or UTC. This is NOT the tactical chat digest. Build the printable kitchen-table page following the Kitchen table newspaper skill: schedule strip, cute weather, family left column, two skinny news columns, locked fonts. Look up real kid-appropriate stories. Do not invent facts. Fill one US Letter page. Attach the PDF here and send one short line that the paper is ready to print. Always send on school days. A quiet household day still gets the page (weather plus real news). Never invent an item to fill a family section, and never send, RSVP, or change the calendar from this run. Do not merge this into the weekday digest message.

Fires on:
- cron `30 6 * * 1-5`

Ask the importing user for:
- Timezone
