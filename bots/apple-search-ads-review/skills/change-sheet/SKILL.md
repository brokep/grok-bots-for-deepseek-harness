---
name: change-sheet
description: "Use when the user approves recommendations and wants them in a form they can apply in their ad account."
---

# Change sheet

Part of the Apple Search Ads Review agent preset.

You never touch the ad account. This turns approved recommendations into something they can paste, upload, or hand to whoever holds access.

Inputs: the review or recommendation list, and which items they said yes to.

1. Read the approved list back in one short block before you build anything. Only what they said yes to goes in.
2. One row per change: campaign, ad group, the object (keyword, negative keyword, bid, daily cap, budget, status), the match type where it applies, the current value, the new value, and a one line reason with the number behind it.
3. Write it two ways. A table in chat they can read, and a CSV they can open. Use the Apple Search Ads bulk sheet column names where you know them, so the file drops straight into a bulk edit.
4. Order the rows the way they have to be applied. Keyword adds before the negatives that protect them, budget increases before the bid raises that spend them.
5. Add the manual steps for anything with no bulk path, in the order they would click them. Storefront and account level settings usually fall here.
6. Set the check date. Say when to look again and which number would tell them it worked. Most changes need several days before they are readable.
7. Log every change with the date and the state you left it in. Nothing counts as applied until they tell you it is.

Rules: never say a change is live. Never apply, upload, or authorize anything. When they tell you what they applied, mark it in the log so the next review measures the change instead of recommending it again.

Save under the Apple Search Ads folder as the change list.
