---
name: write-the-fix-list
description: "Use when the user says yes to a change you recommended, or asks exactly what to do about a breach."
---

# Write the fix list

Part of the Ad Spend Watch agent preset.

Inputs: the breaches they approved and the platform each one sits on.

Steps:
1. One block per change, ordered by the money at stake.
2. Each block: the campaign, where to click in that platform's own words (Google Ads goes campaign then settings then budget, Meta goes ad set then budget and schedule), the current value, the new value, and what you expect to happen.
3. Add the one thing to watch after the change and when to look, usually 48 hours for anything touching bids or budgets and one week for anything touching creative.
4. Fixes that belong to engineering rather than the ad account get their own list: a broken conversion import, a pixel that stopped firing, a landing page returning errors, a checkout that fails on mobile. Offer to file each one in Linear with the numbers attached.
5. Offer to post the list to Slack when they picked a channel.
6. Say plainly that you have not made any of these changes and will not.

When they come back and say a change is done, note the date against that campaign so the next check reads the before and after instead of flagging it again.

Save the fix list dated under ad spend watch.
