---
name: routine-principles-review
description: "Scheduled routine: Disabled by default. Mondays at 9am in the user's timezone. Re-reads the positioning principles doc and the voice profile, collects new comments and open gaps, and flags copy that drifted from the current rev with the line before and after. Reports in chat, draft only, and stays quiet when nothing changed."
---

# Principles review

Part of the Product Marketer agent preset.

Schedule, as written by the template author: Disabled by default. Mondays at 9am in the user's timezone. Re-reads the positioning principles doc and the voice profile, collects new comments and open gaps, and flags copy that drifted from the current rev with the line before and after. Reports in chat, draft only, and stays quiet when nothing changed.

## What to do on each run

# Principles review

This routine ships disabled. Confirm the timezone, the Monday 9am schedule, which principles doc to watch, the destination, and that nothing is published or sent before enabling.

When enabled:
1. Read memory for the principles path and rev, the product facts, and the destination. If the principles doc does not exist, do nothing and say so once.
2. Re-read /workspace/marketing/principles.md and /workspace/marketing/voice-profile.md. Check for new comments or edits on the doc and on the drafts in Drive or Notion when either is connected, and for gaps still marked as needed.
3. Re-read the pages and placements the principles cover. Flag copy that drifted from the current rev: a hero that no longer carries the customer promise, a claim with no proof point, a banned word or a banned shape that came back, an ads line now over its limit.
4. Deliver in this chat: the rev and its date, new comments waiting, open gaps, and the drift list with the line before and after for each. Draft only. Do not update the doc, publish a page, or send anything.
5. Stay quiet when there are no new comments, no open gaps, and no drift. One line at most.

Fires on:
- cron `0 9 * * 1`

Ask the importing user for:
- Timezone
