---
name: handle-a-reply
description: "Use when a prospect answers, when the user pastes a reply and asks what to say back, or when a row moves to replied."
---

# Handle a reply

Part of the Outbound Prospecting agent preset.

Inputs: the reply in full, the row it belongs to, and what the user sells.

1. Read the reply and put it in one bucket: interested, wants a specific answer, a referral to someone else, a not now with a date, or a no.
2. Update the row before you draft anything. Status goes to replied, meeting, or no. Write the date and one line of what they said in their own words, not your read of it.
3. Interested. Draft the shortest message that closes the loop. Confirm the ask, offer two concrete times in the prospect's timezone, and stop. No re-pitch, no attachments, no new claims.
4. Wants a specific answer. Pull it from what the user told you and nothing else. Anything you do not have, ask the user for it in one line rather than guessing. Pricing, security review, legal terms, and anything about a roadmap always go back to the user before a word is drafted.
5. Referral. Thank them, ask for the introduction rather than the email address, and open a new row for the named person at status new so research runs before anyone writes to them.
6. Not now with a date. Two lines, no pitch. Set next_step to that date and stop the sequence until then.
7. No. Reply once, short, no pitch, no last try. Take the row to no where it stays, and never write to that person again.
8. Never claim a call happened, a trial is running, or a discount exists unless the user said so.

Output: the updated row, the draft reply with any sources, and one line naming anything you need from the user before it can go. Never send. Log the reply and its bucket in the outreach log so the pattern read has something to work with. Save under the prospecting folder.
