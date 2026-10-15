---
name: weekly-prospecting-recap
description: "Use when the user asks how prospecting is going, or when the Friday recap routine runs."
---

# Weekly prospecting recap

Part of the Outbound Prospecting agent preset.

Inputs: the target list and the outreach log.

1. Open with one line: the date range, how many first touches went out, and how many replies came back.
2. Replies. One line each with the name, the company, what they said in their own words, and the next step. Report the noes too, a no is information.
3. Went out. Counted by channel, with the names.
4. Waiting. Rows past their next touch date, oldest first, with the touch number they are on.
5. Stuck. Rows sitting at drafted for more than five days, and rows at enriched with no draft. Say plainly which of those need the user rather than you.
6. The list. How many untouched strong-fit rows are left, and how many weeks that covers at the current pace.
7. Close with one line on where the list is thin and where the next ten names should come from.

Rules: reply rate is replies divided by first touches sent inside the window, and give the raw count next to it whenever the count is under 20. Never read a silence as a no. A week with nothing sent gets two lines, what is queued and what is blocking it, and no filler.

Output: the recap in chat, and the counts written to the outreach log. Save the recap dated under the prospecting folder.
