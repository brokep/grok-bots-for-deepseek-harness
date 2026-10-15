---
name: routine-weekly-distro-review
description: "Scheduled routine: Disabled by default. Mondays 8:45am: every channel's numbers, competitor moves, and this week's tests."
---

# Weekly distro review

Part of the Distro Bot agent preset.

Schedule, as written by the template author: Disabled by default. Mondays 8:45am: every channel's numbers, competitor moves, and this week's tests.

## What to do on each run

# Weekly distro review

This routine ships disabled. Before enabling, confirm the timezone, the competitors, and the channels to cover.

When enabled:
1. distro.py status. Setup not done, or Weekly distro review not in routines_on: stop silently.
2. distro.py report --days 7 --html and distro.py lead stats: spend, results, cost per result, and trend for paid, organic X, and outbound.
3. Competitors, Trends, and Positioning in @market-scan.
4. distro.py winners --days 28, then distro.py learn the new patterns.
5. One message with the report attached: what worked, what didn't, 3 tests for this week, and any positioning change to approve. Drafts and proposals only.

Fires on:
- cron `45 8 * * 1`

Ask the importing user for:
- Timezone
