---
name: routine-craft-scan
description: "Scheduled routine: Disabled by default. Mondays at 10: new models, techniques, and guides for the crafts you name, with links."
---

# Craft scan

Part of the Proto Bot agent preset.

Schedule, as written by the template author: Disabled by default. Mondays at 10: new models, techniques, and guides for the crafts you name, with links.

## What to do on each run

# Craft scan

This routine ships disabled. Before enabling, confirm the timezone and the crafts to watch, saved with proto.py set craft_topics (for example avatar loops, meme remakes, product shots).

When enabled:
1. Read memory, then proto.py status. No craft_topics and no files in <home>/craft/: stop without a word.
2. proto.py fal find for each craft's task, noting models tagged new.
3. Look for techniques and guides since last_scan on the web and X, per @proto-research.
4. Send up to 5 items: what it is, why it matters for their work, link, date. Offer to update a playbook or try one on their asset.
5. proto.py set last_scan today. Read only, never post, quiet when nothing is new.

Fires on:
- cron `0 10 * * 1`

Ask the importing user for:
- Timezone
