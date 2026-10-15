---
name: html-report
description: "Use to build the self-contained HTML report that closes every weekly and monthly report. Charts are rendered to PNG with matplotlib or Pillow and embedded as data URIs, and the file is opened and verified before it is delivered."
---

# html-report

Part of the Marketing Analyst agent preset.

# HTML report

One file, opens anywhere, nothing missing. Every chart and screenshot is embedded inside the HTML
as a base64 data URI. No relative paths, no external URLs for assets, no CDN scripts.

## When
- Every weekly report and every monthly report.
- Any reporting ask whose answer needs more than one table.
- The end of the setup test drive, including an EXAMPLE labeled one when no export exists.

## Build (Python, stdlib plus matplotlib or Pillow)
1. Render every chart to PNG first, per evidence-media, into
   /workspace/analytics/reports/<date>/charts/. Matplotlib is the first choice. When it is not
   available, draw the chart with Pillow: axes, bars or points, value labels, and a title. When
   neither is available, ship the tables without charts and say so in Could not read, never a
   chart described in words.
2. Confirm every PNG exists and is larger than zero bytes before the next step. A missing chart is
   a build failure, not a caption.
3. Downscale images to a maximum of 1600px wide. Target under 20 MB for the whole file.
4. Read each file, base64 encode it, and write `<img src="data:image/png base64 ...">`. Never
   write a relative src.
5. Inline all CSS in a single style block. No web fonts, no script.
6. Structure, in this order: header (period, comparison period, platforms, currency, and the
   sources with their read dates, live views and export files listed separately), TLDR, account
   table, campaign table, charts with a caption naming the metric, the range, and the source, top
   movers, commentary, trend and budget pacing on a monthly report, what to do next as questions,
   gaps, could not read, and an appendix with every remaining table, chart, and source
   screenshot.
7. Every table cell that is a derived metric shows the two inputs in a tooltip title or in a
   footnote row, so a reader can check the arithmetic. Every table carries a source column and
   every chart caption ends with its source and read date.
8. Save to /workspace/analytics/reports/<date>-<type>.html with a manifest beside it listing every
   embedded asset and its byte size.
9. An EXAMPLE report carries EXAMPLE in the file name, the title, and the header, and every number
   in it is obviously invented.

## Verify before delivering (mandatory)
1. Open the saved HTML in my browser.
2. Count the img elements and confirm each has a data src and a non-zero natural width once
   loaded. Zero broken elements is the bar.
3. Screenshot the rendered header and one chart section as proof.
4. If anything fails, fix the asset and rebuild. Never deliver a report with a broken element. If
   an asset cannot be produced, remove the element and note it under Could not read.

## Deliver
Attach the HTML with one line: period, spend, number of charts, file size. Attach the two proof
screenshots. The HTML is the deliverable and the chat lines point at it.

## Never
Embed a credential, a sign-in page, an account id, a customer's personal data, an unsourced
number, or an unlabeled example number. Deliver a file you have not opened.
