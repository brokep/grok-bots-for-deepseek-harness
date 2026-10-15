---
name: routine-monthly-inventory-refresh
description: "Scheduled routine: Disabled by default. Monthly re-pull of Ramp cards and bills, diffed against the vendor database, with new vendors, spend changes, and dropped vendors flagged for review."
---

# Monthly inventory refresh

Part of the Haggle Bot agent preset.

Schedule, as written by the template author: Disabled by default. Monthly re-pull of Ramp cards and bills, diffed against the vendor database, with new vendors, spend changes, and dropped vendors flagged for review.

## What to do on each run

# Monthly inventory refresh

This routine ships disabled. Confirm timezone, run day, the vendor sheet, and whether the operator wants the diff applied to the sheet automatically or as a draft tab.

When enabled:
1. Pull the last 30 days of Ramp card transactions and bills. Group by vendor. Normalize vendor names against the existing sheet.
2. Diff against the vendor database: new vendors not on the sheet, vendors whose trailing spend moved more than 20 percent, vendors with no charges in 90 days (possible zombie SaaS), and vendors whose cadence changed (monthly to annual or the reverse).
3. Never overwrite Purpose, Owner, Focus, or Why. Only update spend, cadence, and last-charge fields, and only if the operator chose auto-apply. Otherwise write the diff to a dated review tab.
4. Run the Google Sheets final check before reporting.
5. Report in this chat: rows added, rows changed, possible zombies, and the sheet link with gid. Draft only. No Slack, no email.

Fires on:
- cron `0 9 1 * *`

Ask the importing user for:
- Timezone
