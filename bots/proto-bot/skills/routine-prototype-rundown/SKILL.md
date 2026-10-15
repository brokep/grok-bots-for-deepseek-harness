---
name: routine-prototype-rundown
description: "Scheduled routine: Disabled by default. Weekday mornings at 9: packets for builds that finished, results of media jobs, and briefs for queued ideas, waiting for your yes."
---

# Prototype rundown

Part of the Proto Bot agent preset.

Schedule, as written by the template author: Disabled by default. Weekday mornings at 9: packets for builds that finished, results of media jobs, and briefs for queued ideas, waiting for your yes.

## What to do on each run

# Prototype rundown

This routine ships disabled. Before enabling, confirm the timezone and that the rundown comes to this chat.

When enabled:
1. Read memory, then proto.py status. Nothing in open_builds, pending_jobs, or ideas_queued: stop without a word.
2. Each open build: CloudAgent get. Finished: follow "When it lands" in @proto-build and send the packet per @proto-share. Failed: one line with the reason and a retry offer, never relaunching on your own.
3. Each pending media job: run its resume command from proto.py status, then send the files.
4. Queued ideas: shape each and write its brief per @proto-build, mark it with proto.py idea set <n> briefed, then send one widget: build them as draft PRs with the cost, pick some, or later. Never launch without a yes in chat.
5. Draft only. Never merge, mark ready, post, or share outside this chat. Quiet when nothing changed.

Fires on:
- cron `0 9 * * 1-5`

Ask the importing user for:
- Timezone
