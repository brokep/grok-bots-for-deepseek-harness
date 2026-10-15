---
name: routine-monday-impact-read
description: "Scheduled routine: Disabled by default. Mondays 9:20am: how accounts with calls moved against everyone else."
---

# Monday impact read

Part of the Sell Bot agent preset.

Schedule, as written by the template author: Disabled by default. Mondays 9:20am: how accounts with calls moved against everyone else.

## What to do on each run

This routine ships disabled. Before enabling, confirm the timezone, the spend or usage source, and which accounts count as the program.

When enabled:
1. Read memory and setup.md in my folder (MY FOLDER fact). No fact, no file, or Monday impact read not under Routines on: stop silently.
2. Run the Monday impact read in @follow-through.
3. One message: each group's median change and count, the gap, top movers, the caveat line, and what changed since last week. Reads only.

Fires on:
- cron `20 9 * * 1`

Ask the importing user for:
- Timezone
