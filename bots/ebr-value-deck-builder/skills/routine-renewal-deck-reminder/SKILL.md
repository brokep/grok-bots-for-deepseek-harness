---
name: routine-renewal-deck-reminder
description: "Scheduled routine: On the 1st of each month, list the owner's accounts with a renewal inside 120 days that have no review deck this quarter, and offer to build each one."
---

# Renewal deck reminder

Part of the EBR & Value Deck Builder agent preset.

Schedule, as written by the template author: On the 1st of each month, list the owner's accounts with a renewal inside 120 days that have no review deck this quarter, and offer to build each one.

## What to do on each run

# Renewal deck reminder

Runs unattended on the 1st of each month at 08:00 in the owner's timezone.

1. From the CRM, list the owner's customer accounts whose contract or renewal date falls within the next 120 days.
2. For each, check memory and the file destination for a deck built in the current fiscal quarter.
3. Deliver one message: a table of accounts (Account, Renewal date, Last deck, Data available: CRM, calls, usage) and a plain-text offer to build the missing decks, one at a time, starting with the nearest renewal.
4. Build nothing until the owner names an account; then run `ebr-deck` for it.
5. If there are no renewals in the window, send one line saying so.

Unattended runs never ask clarifying questions, never send anything to a customer, and never upload files anywhere the owner did not name.

## Schedule

Create this routine paused, on cron `0 8 1 * *` read in the owner's timezone.
That is the default; if the owner named a different day or hour while setting up,
use theirs instead. Turn it on only when the owner says yes.
