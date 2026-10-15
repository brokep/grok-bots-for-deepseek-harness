---
name: weekly-competitor-brief
description: "Use when the user asks for a competitor brief, or when the weekly brief routine runs."
---

# Weekly competitor brief

Part of the Competitor Watch agent preset.

Inputs: the findings from a diff run, the watch list, and what the user's company sells.

1. Open with one line: the date range and how many material changes you found.
2. What changed. One block per competitor, every line ending in the source URL and the date. No block for a competitor with nothing material.
3. So what. Two to four lines written for this user's job. A pricing move gets a pricing read, a launch gets a roadmap or positioning read, hiring gets a direction read. Say it is unclear when it is unclear.
4. Quiet this week. One line naming the competitors with nothing material.
5. Sources. Every URL you fetched, including the ones that failed.

Rules: no change without a link. Never pad the brief to look busy. A week with nothing material is one line saying the week was quiet, not a brief. Fold in anything the daily launch check already logged instead of reporting it twice.

When Linear is connected, offer to turn any change that needs a product decision into an issue, one issue per change, with the source URL and the date in the body. Only on a yes, and only for the ones they pick.

Save the brief dated under competitors and attach it here, then deliver it to the destination the user picked. Anything that posts or emails goes to them as a draft first.
