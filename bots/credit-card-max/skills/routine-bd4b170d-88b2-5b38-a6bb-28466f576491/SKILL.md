---
name: routine-bd4b170d-88b2-5b38-a6bb-28466f576491
description: "Scheduled routine: Fires on the 1st of each month to deliver a perk-maximization rollup (not a budget review)."
---

# Monthly card rollup

Part of the Credit Card Max agent preset.

Schedule, as written by the template author: Fires on the 1st of each month to deliver a perk-maximization rollup (not a budget review).

## What to do on each run

Monthly credit-card benefits and points rollup. This is perk maximization, not budgeting.

Do this each run:
1. Refresh Finance connections + credit accounts (live wallet). If the wallet is incomplete, say what's missing instead of inventing cards.
2. Refresh watched-perk status with redemption-confidence rules (+ user overrides).
3. Per card: spend themes, utilization, unused unmuted credits, and credits about to expire.
4. Wrong-card recurring flags vs priorities + playbook.
5. Short scorecard: what's working, what's left on the table, and the 2–3 highest-value moves. Recommend a card for typical spend categories they actually use, with the runner-up and a one-line why.
6. Never invent balances, points, or cards.
7. Stay quiet on generic personal-finance advice.

Deliver the rollup in chat in your normal voice.

Fires on:
- cron `CRON_TZ=America/Los_Angeles 37 8 1 * *`

Ask the importing user for:
- Timezone
