---
name: routine-daily-shipments-status
description: "Scheduled routine: Every weekday morning, a short status on what was delivered, what is late, and what has stopped moving."
---

# Daily shipment status

Part of the Office Ops Desk agent preset.

Schedule, as written by the template author: Every weekday morning, a short status on what was delivered, what is late, and what has stopped moving.

## What to do on each run

Run every weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the shipments ledger plus any carrier mail or pasted update since the last run, and refresh tracking on anything still open. Post a status in three parts: delivered since the last run, late (past eta with no delivery, with days late and owner), and stalled (no tracking movement in three days). One line per shipment with item, vendor, carrier, tracking, and the date it is now expected. Call out separately anything tied to a start date or an event that will not arrive in time. Write the updated rows back to the ledger, including last_checked. Stay quiet when nothing changed and nothing is late. Say it when something is late, even if nothing else moved. Never invent a scan, a date, or a tracking number. Do not mail a carrier, vendor, or teammate from this run, offer a draft instead. When the ledger or the source is missing, say which one in one line and stop.
