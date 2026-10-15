---
name: guest-travel-and-hotels
description: "Use when guests are travelling in: hotel options and room blocks, room lists, flights and arrival times, ground transport, and per-guest itineraries."
---

# Guest travel and hotels

Part of the Event Producer agent preset.

Inputs: the guest list, the event date, the venue address, and any hotel or travel budget the user already has.

1. Split the list into local, travelling in, and unknown. Ask about the unknowns only.
2. Hotel: find two or three options within a short walk or a short ride of the venue and capture nightly rate, distance, cancellation terms, and whether a room block is worth it. A block usually starts to make sense around ten rooms, and it comes with a cutoff date and often an attrition clause, so name both before they sign anything.
3. Room list: one row per guest with check-in date, check-out date, room type, who pays, confirmation number, and booked or not. Never write booked, or a confirmation number, that you have not been given.
4. Travel: arrival time and airport or station, departure time, whether they need a ride, and any access need that changes the journey.
5. Build the arrival day sheet: who lands when, who needs a car, who arrives during load-in when nobody is free to meet them, and who arrives after doors.
6. Per-guest itinerary: one short block each with their hotel, the venue address, the start time in local time, who is meeting them, and a phone number that will be answered. Draft it, do not send it.
7. Put the two dates that bite on the deadline list in the brief: the hotel block cutoff, and any flight the user is paying for.

Output: hotel options with terms, the room list, the arrival day sheet, and per-guest itineraries as drafts.

Fallbacks: no travel budget means you show options with prices and let them choose. Never book a room, a flight, or a car, and never handle a card number. When you cannot confirm a rate, say it is a listed price and not a quote.

Save under the event folder as the guest travel sheet.
