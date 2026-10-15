---
name: routine-monday-signal-digest
description: "Scheduled routine: Every Monday morning, scan the week's signals across the owner's book, rank the accounts and contacts, and stage first-touch drafts for review."
---

# Monday signal digest

Part of the Signal Prospector agent preset.

Schedule, as written by the template author: Every Monday morning, scan the week's signals across the owner's book, rank the accounts and contacts, and stage first-touch drafts for review.

## What to do on each run

# Monday signal digest

Runs unattended on Mondays at 07:00 in the owner's timezone (or the day and time stored in memory).

1. Run `signal-scan` for the window since the last run, at most 14 days.
2. Run `account-tiering`, then `contact-ranking`, capped at the weekly target count from memory (default 20 contacts).
3. Run `first-touch-drafts` for Tier 1 contacts with a verified email. Save drafts; send nothing.
4. Deliver one digest to this chat or the owner's Slack DM: the Tier 1 table with hooks and draft links, Tier 2 as a shorter list, then the counts (accounts scanned, signals found, accounts excluded and why). Attach the full list as a CSV.
5. If the CRM or product source failed to load, say so at the top and deliver what the rest produced.

Unattended runs never ask clarifying questions and never send, enroll, or edit CRM ownership; the owner reviews the drafts and sends.

## Schedule

Create this routine paused, on cron `0 7 * * 1` read in the owner's timezone.
That is the default; if the owner named a different day or hour while setting up,
use theirs instead. Turn it on only when the owner says yes.
