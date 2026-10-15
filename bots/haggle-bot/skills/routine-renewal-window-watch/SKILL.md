---
name: routine-renewal-window-watch
description: "Scheduled routine: Disabled by default. Weekly scan of the vendor database for contracts renewing inside the priority window (default 120 days) that have no Focus tag or thesis yet."
---

# Renewal window watch

Part of the Haggle Bot agent preset.

Schedule, as written by the template author: Disabled by default. Weekly scan of the vendor database for contracts renewing inside the priority window (default 120 days) that have no Focus tag or thesis yet.

## What to do on each run

# Renewal window watch

This routine ships disabled. Confirm timezone, cadence, the vendor sheet, the renewal window, and where the summary should go before enabling.

When enabled:
1. Read the vendor database sheet. For every row with a renewal or commitment end date inside the priority window (default 120 days), check whether it has a Focus tag (Switch, Renegotiate, Waste, Sticky) and a one-line Why.
2. List the untagged or thesis-less rows first, ranked by annual spend. For each, note what evidence is missing per the opportunity bar: $ traced to live data, mechanism, why now.
3. Cross-check Ramp for any vendor with charges in the window that is missing from the sheet entirely, and add it as a new inventory row with Focus blank.
4. Deliver a short summary in this chat: count in window, count with a thesis, top 5 untagged by spend, new vendors found. Draft only. Do not post to Slack, email anyone, or change Focus tags without the operator.
5. Stay quiet if nothing entered the window and nothing changed since the last run.

Fires on:
- cron `0 9 * * 1`

Ask the importing user for:
- Timezone
