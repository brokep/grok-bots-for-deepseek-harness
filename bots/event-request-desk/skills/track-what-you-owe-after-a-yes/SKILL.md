---
name: track-what-you-owe-after-a-yes
description: "Use when the user says yes to an event and the team now owes the organizer something, or when they ask what is due, who has it, and what is late."
---

# Track what you owe after a yes

Part of the Event Request Desk agent preset.

Inputs: the decided row, the yes reply, and whatever the organizer asked for.

Steps:
1. List every deliverable the yes created. The usual ones: a signed contract, payment or an invoice, a logo pack, booth artwork, a speaker bio and headshot, a talk title and abstract, slides, a shipping address and the swag itself, a passes or attendee list, and a staffing plan for the day.
2. Give each one a due date worked backward from the event date. Use the organizer's date when they named one. Otherwise default to the contract inside seven days of the yes, artwork and bios three weeks out, shipping two weeks out, and slides one week out. Say which dates are yours rather than theirs.
3. Ask who owns each one, a few at a time, and default to the user when they don't say. Status is owed, sent, or confirmed.
4. With Linear connected, offer one issue per deliverable in a project or team they name, with the due date and owner on it. Create them only after a yes. With Figma connected, look for the logo pack, booth artwork, or slide deck they pointed you at and say which of them exist and which are missing.
5. Flag anything overdue and anything due inside seven days at the top, every time you show the list.
6. When the user says something went out, mark it sent, and mark it confirmed only when the organizer acknowledges it.

Output: one line per deliverable with the event, what is owed, the owner, the due date, and the status, overdue first.

Fallbacks: with no connector, keep the list yourself and surface it in the Thursday check. Never message an organizer, never mark anything delivered on the user's behalf, and never commit the team to something the user did not agree to.

Save the commitments list in the event desk folder.
