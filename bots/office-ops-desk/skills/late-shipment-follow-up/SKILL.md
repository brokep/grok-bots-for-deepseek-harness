---
name: late-shipment-follow-up
description: "Use when a shipment is past its ETA, a tracking number has gone quiet for days, or a vendor has not replied about an order."
---

# Late shipment follow-up

Part of the Office Ops Desk agent preset.

Inputs: the shipment row, the tracking number, and the last update you recorded.

Steps:
1. Check the ledger for last_checked and the last status you have.
2. When a tracking number exists, look it up on the carrier's public tracking page before writing anything. Record what you find, including no scans since a given date.
3. Pick the recipient. The carrier when a package stopped scanning, the vendor when an order never shipped, the person who requested it when it arrived and nobody claimed it.
4. Draft a short message, three to five sentences. Open with the order or tracking number, state the last scan and the promised date, ask the one question that unblocks it, and name the date you need an answer by.
5. When the item is tied to a start date or an event, say so in the message and give that date as the reason.
6. Update the ledger: status, last_checked, and a note that a follow-up is drafted.

Output: the draft in the chat ready to copy, plus one line on what changed in the ledger. Never send it. When Gmail is connected, save it as a draft in their account and say it is sitting there unsent.

When tracking shows nothing at all, say that plainly instead of guessing at a delivery date.

Save drafts under the office ops folder.
