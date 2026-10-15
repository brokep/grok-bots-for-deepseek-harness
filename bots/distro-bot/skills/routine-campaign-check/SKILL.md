---
name: routine-campaign-check
description: "Scheduled routine: Disabled by default. Daily 8:25am: numbers, pacing, flags, and one loop step per campaign."
---

# Campaign check

Part of the Distro Bot agent preset.

Schedule, as written by the template author: Disabled by default. Daily 8:25am: numbers, pacing, flags, and one loop step per campaign.

## What to do on each run

# Campaign check

This routine ships disabled. Before enabling, confirm the timezone, the ad accounts to read, and the monthly cap.

When enabled:
1. distro.py status. Setup not done, or Campaign check not in routines_on: stop silently.
2. Read fresh numbers from each connected account per @ad-accounts and run a pass of @campaign-loop. An expired sign-in: one line, skip that platform.
3. Apply only lane autopilot changes, and only through a connector, each verified and listed with its undo. Everything else waits for a yes. Never change spend, launch, or start a campaign here.
4. Spend past a cap or results that stopped: lead with it and the change you would make.
5. One message: spend against the cap, results by channel, changes made, changes waiting, flags. Nothing new: quiet.

Fires on:
- cron `25 8 * * *`

Ask the importing user for:
- Timezone
