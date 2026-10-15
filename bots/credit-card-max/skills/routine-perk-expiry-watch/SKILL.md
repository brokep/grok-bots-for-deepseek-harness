---
name: routine-perk-expiry-watch
description: "Scheduled routine: Runs daily to nag only on T-5 and period-end for unmuted unused watched perks; silent otherwise."
---

# Perk expiry watch

Part of the Credit Card Max agent preset.

Schedule, as written by the template author: Runs daily to nag only on T-5 and period-end for unmuted unused watched perks; silent otherwise.

## What to do on each run

Daily perk-expiry watch. Stay silent unless there is something to nag.

1. Use the live Finance wallet and current perk watchlist / mute list from memory.
2. For each unmuted watched perk with a known period end, score redemption with confidence rules (high/medium → used; low → unknown; never mark unused solely because a manual perk has no txn).
3. Message only on **T-5** and **T-0** (period end) for unmuted perks still marked **unused**.
4. Near T-5, if a high-value unmuted perk is still **unknown**, ask once per period whether it was used (`unknown_asked_at`). Do not nag unknown as unused at T-0.
5. Combine same-window nags into one message. Every nag offers mute forever or this period.
6. Anniversary-reset watches stay quiet until anniversary month is known — infer from AF charges in Finance first; ask only if missing.
7. If nothing qualifies, send nothing.

Fires on:
- cron `CRON_TZ=America/Los_Angeles 40 9 * * *`

Ask the importing user for:
- Timezone
