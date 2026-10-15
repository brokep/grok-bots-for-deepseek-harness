---
name: schedule
description: "Use to book, move, or cancel a call."
---

# schedule

Part of the Sell Bot agent preset.

# schedule

Booking calls.

## Propose

Calendar connected: the next 10 business days, around existing events, in the hours and buffer under Calendar. Not connected: ask for windows. Offer 3 slots in the user's timezone with theirs beside each when known, never before 9am or after 5pm for either side.

## Invite

Title "<their company> and <user's company>, <topic>". Body: why the call, the agenda in one line, what to bring. Attendees exactly as the user named them. Show it in full.

## Create

Only after the user's yes for that slot and those attendees, read back in one line, then create it so they get the invite. Log the event id in the account file, set stage call booked, and add the call to calls.csv (source booked), prepping it now if it is later today, and asking for a walk per accounts. No calendar: hand over the invite text, and do the same once the user says it went out.

## Responses

The daily prospect run reads attendee responses on booked events. Declined: draft a reschedule note. Moved or declined: update calls.csv.

## Never

Invite anyone the user did not name, book over a hold, or move, shorten, or cancel an event on my own.
