---
name: weekly-facilities-digest
description: "Use when the user asks for a facilities update or the weekly facilities digest routine runs."
---

# Weekly facilities digest

Part of the Office Ops Desk agent preset.

Inputs: the facilities log, plus anything the user pasted or forwarded since the last digest.

Steps:
1. Re-read the log and fold in the new items first so the digest is current.
2. Compute days open for every issue from opened_on.
3. Group into four buckets and sort each oldest first: urgent, waiting on a vendor, routine, no owner yet.
4. Flag anything open past seven days with no update.
5. When the user tracks more than one site, group inside each bucket by site.
6. Finish with one line on what moved to closed since the last digest.

Output shape:

Urgent
- Location, issue, owner, days open, last update

Waiting on a vendor
- Location, issue, vendor, days open, what you are waiting for

Routine
- Location, issue, owner, days open

No owner yet
- Location, issue, days open

Closed since last digest
- One line with the count and the notable ones

Start with the first bucket, no preamble. Keep it under 200 words unless more than 15 issues are open. An empty list gets one line saying it is clear.

When the log is missing or empty, name what you need, ask once, and offer to build it from a paste.

When the user has a ticket destination saved, offer at the end to file the urgent and no-owner items through the sync skill. Offer only, never file on your own.

Save the digest under the office ops folder with today's date in the filename, and write the recomputed log back.
