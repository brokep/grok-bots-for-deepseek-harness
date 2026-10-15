---
name: build-the-office-ops-ledger
description: "Use when the user first hands over shipments, facilities issues, or team celebrations, or when their source list changed and the ledger needs rebuilding."
---

# Build the office ops ledger

Part of the Office Ops Desk agent preset.

Inputs: a pasted list, a CSV or spreadsheet export, a spreadsheet link, or forwarded carrier mail. Any one of them is enough to start.

Steps:
1. Read what they gave you and say which columns you found before changing anything.
2. Map their columns onto these:
   - Shipments: id, item, vendor, carrier, tracking, ordered_on, eta, status, owner, for_whom, site, notes, last_checked
   - Facilities: id, opened_on, site, location, issue, severity, owner, vendor, status, ticket_ref, last_update, notes
   - Celebrations: name, team, occasion, month, day, opt_out, notes
3. Keep their wording for item, vendor, and issue text. Normalize only dates and the fixed value lists. Shipment status is ordered, in transit, out for delivery, delivered, delayed, lost, or returned. Facilities severity is urgent, needs a vendor, or routine.
4. Celebrations get month and day only, never a birth year or an age.
5. Rows you cannot parse go in a short "needs a look" list at the end of your reply. Never guess a date, a carrier, or an owner.
6. Deduplicate shipments on tracking number, facilities on site plus location plus issue, celebrations on name plus occasion. When two rows disagree, keep the newer one and say what changed.
7. Leave site blank rather than guessing when they run one office.

Output: the ledger written to disk, a count of rows added and updated, the rows that need a look, then the first status in the same reply so they see something real immediately. Late means past eta with no delivery.

When there is no source at all, ask for five example rows and build from those.

Save under the office ops folder as shipments.csv, facilities.csv, and celebrations.csv.
