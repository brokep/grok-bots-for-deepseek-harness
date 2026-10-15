---
name: routine-morning-product-walk
description: "Scheduled routine: Disabled by default. Weekday mornings, ready by 9: walks your product in its test account and sends what shipped, what got unshipped, what broke, and the calls to make."
---

# Morning product walk

Part of the Startup QA Bot agent preset.

Schedule, as written by the template author: Disabled by default. Weekday mornings, ready by 9: walks your product in its test account and sends what shipped, what got unshipped, what broke, and the calls to make.

## What to do on each run

# Morning product walk

This routine ships disabled. Before enabling, confirm the time zone, the schedule, the product URL, and that the test account is signed in.

When enabled:
1. Read memory, then qa.py status. Stop without a word if routine is not true. Setup not done or no account saved: say so once and stop.
2. The check in @test-account, in my own browser (start it if it isn't running): signed out, sign back in with the saved email. Any other account: say so once and stop.
3. Run @product-walk: change signals first, then every surface, then recheck open bugs. Non-destructive only.
4. Run @product-rundown: the rundown goes here, and new bugs go to the bug-triage teammate if one is saved.
5. Never submit, send, pay, invite, delete, publish, or use any account but the test one.
6. A quiet day is one line.

Fires on:
- cron `0 8 * * 1-5`

Ask the importing user for:
- Timezone
