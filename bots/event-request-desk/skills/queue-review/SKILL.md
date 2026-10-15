---
name: queue-review
description: "Use when the user asks what is in the event queue, what needs a decision, or what has gone stale, or when the weekly queue review routine runs."
---

# Queue review

Part of the Event Request Desk agent preset.

Inputs: the queue, plus anything logged since the last review.

Steps:
1. Re-read the queue and fold in the new rows first so the view is current.
2. Compute days waiting from received_on, days to the reply-by date, and days to the event date.
3. Group into five buckets and sort each by tightest reply-by date first:
   - Needs your call: scored and waiting on a human
   - Needs info: blocked on the organizer
   - Decided, not replied: the draft is written or still missing
   - Committed: a yes with an event date coming up, and what is still owed on it
   - Closed since the last review
4. Flag anything waiting more than five days with no movement, anything whose reply-by date lands inside seven days, and any two committed events inside the same week.
5. Finish with two numbers: how many came in and how many closed since the last review, plus the current yes rate.

Output: one line per request with organizer, type, the ask in six words, score, days waiting, and the reply-by date. Start with the first bucket, no preamble. Keep it under 200 words unless more than 15 requests are open. An empty queue gets one line saying it is clear and naming the next committed event.

When the queue is missing or empty, say which in one line and offer to build it from a paste.

Save the review with today's date in the event desk folder and write the recomputed queue back.
