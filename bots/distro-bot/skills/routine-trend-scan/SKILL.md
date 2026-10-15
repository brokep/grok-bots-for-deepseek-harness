---
name: routine-trend-scan
description: "Scheduled routine: Disabled by default. Weekdays 9:35am: topics worth jumping on, each with a draft post."
---

# Trend scan

Part of the Distro Bot agent preset.

Schedule, as written by the template author: Disabled by default. Weekdays 9:35am: topics worth jumping on, each with a draft post.

## What to do on each run

# Trend scan

This routine ships disabled. Before enabling, confirm the timezone, the keywords, and whether X is connected.

When enabled:
1. distro.py status. Setup not done, or Trend scan not in routines_on: stop silently.
2. Run Topics in @market-scan over the last day.
3. Up to 3 topics worth jumping on, each with a draft post or reply, the link, and why now. Searchable questions go to the SEO and AEO teammate if one is saved.
4. Never post, reply, like, or follow. Nothing worth jumping on: quiet.

Fires on:
- cron `35 9 * * 1-5`

Ask the importing user for:
- Timezone
