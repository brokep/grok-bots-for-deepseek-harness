---
name: routine-weekly-library-check
description: "Scheduled routine: Every Monday morning, checks the component library and token set for new duplicates, detached instances, and hardcoded values, and reports only what drifted since last week."
---

# Weekly library check

Part of the figma bro agent preset.

Schedule, as written by the template author: Every Monday morning, checks the component library and token set for new duplicates, detached instances, and hardcoded values, and reports only what drifted since last week.

## What to do on each run

Run every Monday at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the newest saved audit first, then read the library and the variables in the file they named. Report only what changed since that audit: new components, new duplicates or near-duplicate tokens, newly detached or drifted instances, new hardcoded values, and components that gained or lost variants. One line each, with the component or token name and the file it lives in. Close with a single counts line so the trend is visible: components, tokens, open issues, and the change against last week. Save the new audit so next week compares against it. A week with no drift gets one line saying the library held. When the file cannot be read, say which one in one line and stop, and do not repeat that more than once a week. Never rename, merge, delete, or publish anything, and never open an issue without an explicit yes.
