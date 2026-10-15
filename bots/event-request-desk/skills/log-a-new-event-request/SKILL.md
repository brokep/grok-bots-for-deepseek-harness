---
name: log-a-new-event-request
description: "Use when an event invitation, sponsorship, speaking, booth, partnership, or swag ask arrives, or when the user pastes, forwards, or points you at a batch of asks that need to land in the queue."
---

# Log a new event request

Part of the Event Request Desk agent preset.

Inputs: a Slack thread, a forwarded invitation, a sponsorship deck, a form response, a spreadsheet row, a screenshot, or a few sentences typed straight at you. Any one of them is enough to start.

Steps:
1. Read what came in and pull only the fields you can actually see. Never fill a blank with a guess.
2. Write one row per request: id, received_on, organizer or requester, their company, type, the ask in their own words, the event date, the reply-by or RSVP date, the fee or tier cost if one is named, the audience size if one is named, what they are offering in return, who it is for on the user's side, status, score, decision, notes.
3. Type is event invitation, sponsorship, speaking, booth, partnership, swag, or other. A non-event ask goes under other, and the ask field keeps their wording either way.
4. Status starts at new. A request missing something you need in order to score it goes to needs info, and you name exactly which fields are blank. The event date, the cost, and the audience are the three that block a score most often.
5. Check for a duplicate on organizer plus event. When you find one, merge the rows, keep the newer detail, and say what you merged. The same conference asking for a sponsorship and a speaker is two rows, not one.
6. When the user's calendar is connected, check the event date against it and note any clash on the row. Without it, check the blackout weeks saved in memory.
7. Score it in the same turn with the scoring skill, then show the row and the score together. Do not log it and go quiet.

Output: the new rows, the score for each, and one short list of anything that needs info before you can call it.

Fallbacks: with no connector, a paste, a CSV, a forwarded thread, or a deck works the same. A screenshot gets read, and the fields you could not make out get named rather than guessed. Never write to an organizer to collect a missing field without asking the user first.

Save the rows to the queue in the event desk folder.
