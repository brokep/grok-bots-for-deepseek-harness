---
name: routine-farzad-money-30-min-book
description: "Scheduled routine: Weekday intra-day public dashboard refresh at :35 (catch at :40). Backup only; fill ships are primary."
---

# Weekday hourly dashboard book

Part of the Webby agent preset.

Schedule, as written by the template author: Weekday intra-day public dashboard refresh at :35 (catch at :40). Backup only; fill ships are primary.

## What to do on each run

Weekday intra-day public dashboard book. Owner timezone. Cost-lean. THIS CLOCK IS BACKUP ONLY.

PRIMARY PATH (do not wait for this cron): after every desk fill or close, ship book AND trade reasoning in the SAME deploy immediately. If the desk omits the thesis, pull it from the desk and still ship.

Fires at :35 and a catch at :40, 8:35–2:40 local weekdays. 8:35 is 5 min after the 8:30 cash open. Last intra-day tick is 2:35; 2:40 is catch only. Do not ship weekends, overnight, market holidays, or after the cash close. The 3:15/3:20 close book is a separate routine.

At :40: if this hour's book already shipped (live generated_at is today after that hour's :35), stay quiet. If :35 missed or the ship failed, do the full refresh now. Do not no-op just because the :35 wake succeeded at asking the desk.

Each in-window refresh:
1) Ask the desk agent for a READ of the brokerage account only: equity, cash, unsettled, margin buying power, positions, open/pending orders, last/bid/ask for open names. No orders. Do not ask a coding agent.
2) Fetch a live index last from a public quote API. Never invent an index print. If the index cannot be fetched, do not ship and ping the orchestrator.
3) Update the public dashboard from LIVE production files. Keep a weekday-only inception chart. Bake every prior weekday desk close through yesterday; live mark is today only. Do not drop weekdays. Do not put weekend spans or extra day-dots back. generated_at is now in the owner's timezone. Do not wipe the journal. Do not treat unsettled as settled.
4) If a fill or close is in the book but missing from trades, pull thesis from the desk and ship book + reasoning together.
5) Copy publish helpers to a temp dir first if a safety review cannot bind the ship scripts. Never print the token.

Silent on a clean ship. Ping the orchestrator only if the read or deploy fails. Do not ping the owner.

Fires on:
- cron `35,40 8-14 * * 1-5`

Ask the importing user for:
- Timezone
