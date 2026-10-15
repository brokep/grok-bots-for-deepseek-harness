---
name: routine-listed-weekday-attention-list
description: "Scheduled routine: Weekday morning quiet digest of open cuts, Eng/QA blockers, and decisions waiting on the owner; stays silent when nothing changed."
---

# Weekday attention list

Part of the PM bot agent preset.

Schedule, as written by the template author: Weekday morning quiet digest of open cuts, Eng/QA blockers, and decisions waiting on the owner; stays silent when nothing changed.

## What to do on each run

Weekday quiet attention list for this product only. Read the living PRD SoT the owner named (PM review section wins) and recent Eng / QA context if those teammates exist. Build a short attention list: open cuts still binding, Eng blocked waiting on a cut or ambiguity, QA blocked on missing AC/proof expectations, decisions waiting on the owner. If nothing material changed since the last run, stay completely silent. If something needs a decision or unblock, surface only that: cut name/date, who is blocked, and the one decision or next step under ~2 minutes. Address Eng and QA as roles (use the names from getting-started memories). If Eng/QA are not set yet, still list open cuts and say hand this cut to your Eng when ready. Do not rewrite the PRD. Do not open cloud agents, pass/fail QA, or write code.

Fires on:
- cron `CRON_TZ=America/Los_Angeles 34 9 * * 1-5`

Ask the importing user for:
- Timezone
