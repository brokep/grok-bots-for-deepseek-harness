---
name: routine-farzad-money-close-book
description: "Scheduled routine: Official cash-close public dashboard ship at 3:15 local, with a 3:20 catch."
---

# Weekday close dashboard book

Part of the Webby agent preset.

Schedule, as written by the template author: Official cash-close public dashboard ship at 3:15 local, with a 3:20 catch.

## What to do on each run

One post-close public dashboard ship. Owner timezone. Weekdays at 3:15 PM plus a 3:20 catch. Cost-lean.

3:15 is the official close ship. 3:20 fires only if today's close is not live (generated_at not today after 15:15). If 3:15 already shipped, 3:20 stays quiet. Do not run intra-day :35 logic. No weekends or overnight.

1) Ask the desk agent for a READ of the brokerage account only: equity, cash, unsettled, buying power, positions, working orders, last/bid/ask. No orders. The desk must answer after cash close.
2) Fetch a public index last. Never invent the index. If the fetch fails, do not ship; ping the orchestrator.
3) Update the public dashboard from LIVE production. Keep weekday-only inception chart. After this close, bake today's desk close so tomorrow's live mark does not erase it. Weekends stay off. Do not wipe journal. Do not treat unsettled as settled.
4) Copy publish helpers to a temp dir if a safety review cannot bind the ship scripts. Never print the token.

Silent on a clean ship. Ping the orchestrator only if read or deploy fails. Do not ping the owner.

Fires on:
- cron `15,20 15 * * 1-5`

Ask the importing user for:
- Timezone
