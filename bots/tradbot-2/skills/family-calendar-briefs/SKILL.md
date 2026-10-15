---
name: family-calendar-briefs
description: "Use when the user asks about the week or two ahead, adds an event, wants to know what to prepare for, or the weekend preview routine runs."
---

# Family calendar briefs

Part of the Tradbot agent preset.

---
name: Family calendar briefs
description: >-
  Use when the user asks about the week or two ahead, adds an event, wants to
  know what to prepare for, or the weekend preview routine runs.
---
Inputs: the personal calendar for the window, the watch list, and anything the inbox scan turned up with a date on it.

1. Take the window. Default is today plus the next fourteen days.
2. Read every event with a person, a place, and a time. With no Calendar connection, work from a screenshot, an export, or what they typed out.
3. Find the collisions: two things at the same hour, two kids in two places, a pickup that lands inside a work block, travel time that does not fit between back to back events. Name which one has to move and offer the obvious fix.
4. Find what needs preparing: something to bring, a form to sign first, a gift, a cake, a payment due before the date, a document to print. Two days of lead time is the default warning.
5. Find what is missing: an appointment that got discussed in mail but never landed on the calendar, an RSVP with a date and no event behind it.
6. Write it as three short lists.

Output shape:

Collisions
- Day, the two things, what to move

Prep needed
- Day, event, what to do first, by when

Not on your calendar yet
- What it is, the date from the mail, and the ask to confirm before you add it

A clear stretch gets one line saying so plus the single busiest day.

Fallbacks: a calendar you cannot read means you ask for a screenshot of the week. An all day entry with no time gets treated as the whole day.

Never add, move, or delete an event, and never invite anyone, without an explicit yes for that event.

Write anything with an open action into the ledger.
