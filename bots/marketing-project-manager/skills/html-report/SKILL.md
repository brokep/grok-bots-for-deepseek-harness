---
name: html-report
description: "Use to build the self-contained status or retro report that closes a check-in with changes, the setup test drive, and every retro. Every screenshot is embedded as a data URI so the file renders with nothing missing. Verify it in the browser before delivering."
---

# html-report

Part of the Project Manager agent preset.

# HTML report

One file, opens anywhere, nothing missing. Every screenshot is embedded inside the HTML as a
base64 data URI. No relative paths, no external URLs for assets, no CDN scripts.

## When
- Every status pass that had at least one change. Quiet passes get no report.
- The end of the setup test drive.
- Every retro.

## Build (Python, stdlib only)
1. Collect this run's assets from /workspace/pm/checkins/<date>/ and any gate screenshots from
   /workspace/pm/gates/. Order them the way the reader should see them: the plan, then workstream
   by workstream in plan order, then gates, then blockers.
2. Downscale images to max 1600px wide (Pillow if available, otherwise
   `ffmpeg -i in.png -vf scale=1600:-2 out.png`). Target under 60 MB total. If it is still over,
   keep the newest screenshot per workstream and list the rest by path at the bottom.
3. Read each file, base64-encode, and write `<img src="data:image/png;base64,...">`. Never write
   `src="./something.png"`.
4. Inline all CSS in a `<style>` block. No web fonts. No script unless it is inline and needed.
5. Structure:
   - Header: goal, launch date, days remaining, the window covered, items in flight, items
     blocked, gates open.
   - Summary: 5 lines. What moved, what is blocked, what needs a yes, and whether the date is
     still reachable.
   - Timeline: one row per workstream with deliverable, owner, due date, status, and the critical
     path marked.
   - Workstreams: one section each, what moved with its screenshot, what is blocked and since
     when, what is next.
   - Gates: one block per open gate with the artifact screenshot, the evidence, the risk, and the
     date it was opened. Then the decided gates with their timestamps and the user's words.
   - Blockers: one row each, item, blocked on, since when, who can unblock it.
   - Could not read.
   - Appendix: every remaining screenshot, captioned with the item and the date.
6. Save to /workspace/pm/reports/<date>-status.html, or <date>-retro.html for a retro, and write a
   manifest beside it listing every embedded asset and its byte size.

## Verify before delivering (mandatory)
1. Open the saved HTML in my browser.
2. Count the img elements and confirm each has a data: src and a non-zero natural width once
   loaded. Zero broken elements is the bar.
3. Screenshot the rendered header and one workstream section as proof.
4. If anything fails, fix the asset and rebuild. Never deliver a report with a broken element. If
   an asset cannot be produced, remove the element and note it under Could not read.

## Deliver
Attach the HTML with one line: goal, window covered, number of screenshots, file size. Attach the
two proof screenshots. The HTML is the deliverable, the chat lines point at it.

## Never
Embed a credential, a key, or customer data. Deliver a file you have not opened. Caption a
screenshot as something it is not.
