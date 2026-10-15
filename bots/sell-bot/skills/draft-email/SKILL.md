---
name: draft-email
description: "Use for every email, sending after a yes, the sent check, and the Friday review."
---

# draft-email

Part of the Sell Bot agent preset.

# draft-email

## Write

Voice in setup.md, then a voice teammate's guide, else plain, short, and warm, saying the voice is not learned yet. Their first name, the sign-off under Voice, one ask, a sentence-case subject under 45 characters that says the thing and never repeats to the same person. Confirm notes 2 or 3 lines, others under 150 words. Numbers carry a date, claims a source.
- First touch: why this account, what the product does for someone like them, one ask. 4 sentences at most.
- Follow-up: something new since the last touch (their post, a launch, a number), then one question. Nothing new: skip it. Never "just checking in." At most 3, or per Follow-ups in setup.md.
- Reply: answer in their words, then one next step. A meeting ask gets 3 slots per schedule.
- Win-back: their reason for leaving if known, what changed with a link and date, a small ask. No discount unless Prices and terms allows it.

## Save

Email connected: a draft in their thread (cc only people the user named), and a drafts.csv row with draft and thread ids, status open. Not connected: copy-ready text in chat with address and subject, draft_id chat, sent when the user says so. One line per batch: "3 drafts waiting: <names>".

## Send

Only on the user's explicit yes for that message in this conversation. Read the draft back: edited in the inbox or carrying an attachment, ask them to send it there. Else read the recipients back in one line, send the approved text in its thread, delete the draft, and run the sent check. A yes covers one email, and a routine never sends.

## Sent check

Daily runs look up open drafts. Gone and sent in its thread: status sent, or edited if the text changed, the send date in the touch log, its stage move (a first touch to contacted, a proposal to proposal), and the next touch. Gone, not sent: status deleted.

## Friday writing review

The last 7 days of rows, except draft_id chat: a draft still open after 3 days counts as skipped, and gone drafts get the sent check (find the sent message by thread, or by recipient and subject). From the edits, up to 3 rules (what they cut, add, or reword) merge under Voice, 10 at most, newest wins. A type skipped 3 times in a row: one line asking whether to stop drafting it. A skipped series email counts as a decline in series.csv. Report counts, new rules, and anything paused.

## Never

Add a recipient not in the account file, attach a file they have not seen, forward or schedule email, or promise a date, price, discount, credit, or feature the sources do not support.
