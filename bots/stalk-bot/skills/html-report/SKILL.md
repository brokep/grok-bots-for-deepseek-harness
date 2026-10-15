---
name: html-report
description: "Build the self-contained HTML report that closes every teardown, every pulse with changes, and the onboarding test drive. Every image and video is embedded as a data URI so the file renders with zero missing assets anywhere. Verify by opening it in the browser before delivering."
---

# html-report

Part of the Stalk Bot agent preset.

# HTML report

One file, opens anywhere, nothing missing. Every screenshot and video is embedded inside the HTML as a base64 data URI. No relative paths, no external URLs for assets, no CDN scripts.

## When
- After every product walkthrough (teardown report).
- After every pulse that had at least one change (pulse report). Quiet pulses get no report.
- At the end of the onboarding test drive (first-seen report for the first competitor).

## Build (Python, stdlib only)
1. Collect the assets for this report from the dossier: PNGs and MP4s produced this run. Order them the way the reader should see them: onboarding steps in sequence, then feature clips, then site snapshots, then X posts, then careers.
2. Downscale images to max 1600px wide (Pillow if available, otherwise `ffmpeg -i in.png -vf scale=1600:-2 out.png`). Re-encode any video over 25 MB to 720p H.264 with `ffmpeg -i in.mp4 -vf scale=1280:-2 -c:v libx264 -crf 28 -preset veryfast -movflags +faststart -an out.mp4`. Target under 60 MB total per report. If still over, drop feature clips beyond the first 6 and link them by dossier path in a "more in the dossier" list at the bottom.
3. Read each file, base64-encode, and write `<img src="data:image/png;base64,...">` or `<video controls preload="metadata" src="data:video/mp4;base64,..."></video>`. Never write `src="./something.png"`.
4. Inline all CSS in a `<style>` block. No `<script>` unless it is inline and needed. No web fonts.
5. Structure:
   - Header: competitor, report type, date, the research identity used (alias only), sources read.
   - Summary: 5 lines. What changed or what was found. Against us in one line.
   - Onboarding: the walkthrough video first, then the step table (step, what it asks, required, skippable, seconds) with the step screenshot beside each row.
   - Features tested: one section per feature with the clip, 2 to 4 screenshots, what it does in their words, what worked, what broke, plan gate if any, and "vs us" in one line from the baseline.
   - Website pros and cons with the cited page screenshot under each bullet.
   - Shipped timeline (X and changelog) with post screenshots.
   - Hiring direction with the careers screenshot.
   - Against us. For our site. Worth a decision.
   - Could not read.
   - Appendix: every remaining screenshot, captioned with page or step and date.
6. Save to /workspace/dossiers/<competitor>/reports/<date>-<type>.html. Also save a manifest next to it listing every embedded asset and its byte size.

## Verify before delivering (mandatory)
1. Open the saved HTML in my browser.
2. Run a check that counts `<img>` and `<video>` elements and confirms each has a `data:` src and a non-zero natural width or duration once loaded. Zero broken elements is the bar.
3. Screenshot the rendered report top and one mid-section as proof it renders.
4. If anything fails: fix the asset (re-encode or re-screenshot) and rebuild. Never deliver a report with a broken element. If an asset truly cannot be produced, remove the element and note it in Could not read.

## Deliver
Attach the HTML file in chat with one line: report type, competitor, number of screenshots, number of videos, file size. Attach the two proof screenshots of the rendered page. The HTML is the deliverable; the chat summary points to it.
