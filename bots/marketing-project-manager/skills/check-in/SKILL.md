---
name: check-in
description: "Use for the scheduled status pass or whenever the user asks where things stand. One line per workstream with what moved, what is blocked, and what is waiting on them, every artifact line carrying its screenshot, plus the chase rules and the quiet-pass rule."
---

# check-in

Part of the Project Manager agent preset.

# Check-in

A status pass is one line per workstream, and every line about an artifact carries the picture
that proves it.

## When to use
The scheduled status routine, and any time the user asks where things stand.

## Steps
1. Re-read /workspace/pm/plan.md and /workspace/pm/items.md. Never report from memory alone.
2. Refresh what is readable: the tracker, the shared drive folder, the channel the user named, the
   preview links and pull requests recorded on items, the ad copy review document, the analytics
   export, and anything the user pasted since the last pass. Anything not connected or not
   readable goes in Could not read.
3. For every item that changed, capture the evidence now: screenshot the board, the pull request,
   the preview page, the review document, the report. Store under
   /workspace/pm/checkins/<date>/<item-id>-<slug>.png.
4. Update each item's status and artifact. An item that moved with no artifact is still in
   progress, not done.
5. Chase. Any item past its due date gets one chase, to the teammate that owns it or to the user
   otherwise, naming the item, the date it was due, and what is needed. One chase per item per
   pass. A second miss makes the item blocked, and it goes to the user as a line, not a second
   chase.
6. Recompute the critical path and the days remaining. If a slip moved the launch date, that is
   the first line, with the number of days.

## Output shape
- Header: goal, date, days remaining, items in flight, items blocked, gates waiting on you.
- One line per workstream: what moved, what is blocked, what is waiting on you. Attach the
  screenshot for every artifact named, or write the marker no artifact yet. Never describe a
  screenshot you did not attach.
- Blocked: one line each, what it is blocked on, since when, who can unblock it.
- Waiting on you: every open gate, one line each, with the date it was opened. Do not re-argue a
  gate here, open it per the gates skill.
- Could not read: one line per source that failed, with the reason.
- Then the status report per html-report when anything changed, with the screenshots embedded.

Cap 8 images in chat, then the line "N more in the report."

## Quiet pass
Nothing moved, nothing newly blocked, no gate waiting: one line, "Nothing moved since <date>, <N>
days to <goal>." No report, no attachments, no invented urgency.

## Never
Report an item as done without an artifact. Repeat an item that has not changed since the last
pass. Chase the same item twice in one pass. Turn a status line into advice the user did not ask
for. Soften a blocked item into in progress.
