---
name: html-report
description: "Use to close an audit or a test drive with a self contained HTML report. Every screenshot is embedded as a data URI, measured results stay separate from observations, and the file is opened and verified in the browser before it is delivered."
---

# html-report

Part of the Website Ops agent preset.

# HTML report

One file, opens anywhere, nothing missing. Every screenshot is embedded inside the HTML as a
base64 data URI. No relative paths, no external URLs for assets, no CDN scripts.

## When
- After every site audit that produced at least one finding.
- At the end of the setup test drive.
- On request for a landing page or a shipped change, when the user wants something to forward.

## Build (Python, stdlib only)
1. Collect this run's assets from /workspace/site-audit/<date>/ in reading order: the home page
   at both widths, then each audited page, then the cropped evidence per finding, then any tool
   output screenshot.
2. Downscale images to a maximum of 1600px wide with Pillow when it is available, otherwise with
   ffmpeg. Target under 60 MB total. If it is still over, keep the evidence crops for P0 and P1
   findings and list the rest by path in a "more on disk" section at the bottom.
3. Read each file, base64 encode it, and write an img tag whose src is the data URI. Never write
   a relative src.
4. Inline all styling in one style block. No web fonts. No script unless it is inline and needed.
5. Structure, in this order:
   - Header: site, pages audited, the date, the tools that ran with their versions, the
     signed-in platforms read with their account names and date ranges, and the build or URL
     each screenshot came from.
   - Summary: 5 lines. Counts by severity, the diff against the previous audit, and the single
     finding worth doing first.
   - Measured results: one table. Source (tool, live platform view, or export), page, metric,
     value, date range or strategy, timestamp. Every row names its source. Nothing in this
     table is an opinion.
   - Findings: one section per finding, ordered P0 then P1 then P2, each with the cropped
     evidence image, the page URL, what is wrong, the severity reason, and the proposed fix with
     its file and effort.
   - Observations: CRO heuristics and anything judged rather than measured, labeled as such.
   - Diff: new, fixed, regressed, still open.
   - Could not read: every page, tool, or platform that failed, with the status code, the
     error, or the words "session expired, sign in again".
   - Appendix: the remaining screenshots, captioned with page, width, and date.
6. Save to /workspace/site-audit/<date>/report.html with a manifest beside it listing every
   embedded asset and its byte size.

## Verify before delivering (mandatory)
1. Open the saved file in my browser.
2. Count the img elements and confirm each has a data URI src and a non zero natural width once
   loaded. Zero broken elements is the bar.
3. Screenshot the rendered header and one findings section as proof.
4. If anything fails, fix the asset and rebuild. Never deliver a report with a broken element.
   If an asset cannot be produced, remove the element and note it under Could not read.

## Deliver
Attach the HTML with one line: site, pages, findings by severity, screenshot count, file size.
Attach the two proof screenshots of the rendered page. The HTML is the deliverable and the chat
body points at it.

## Never
Embed a credential, a token, a session cookie, an env value, or another person's data. Deliver
a file you have not opened. Put an unlabeled placeholder number, or a number with no source, in
the measured table.
