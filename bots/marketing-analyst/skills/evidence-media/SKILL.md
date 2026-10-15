---
name: evidence-media
description: "Use before attaching anything visual. How charts, table screenshots, and platform view screenshots are rendered, labeled, stored, and attached, so every number a user reads arrives with the picture that shows it rather than a description of one."
---

# evidence-media

Part of the Marketing Analyst agent preset.

# Evidence media

Every claim with a number in it gets the chart or the table that shows it, attached in the same
turn. A described chart is not evidence.

## Charts, always
1. Render to PNG with matplotlib. One chart, one question. Titles name the metric, the scope, and
   the date range. Axes are labeled with the unit and the currency code. Bars and points carry
   their value as a label, because a reader should not have to measure a bar.
2. The standard set:
   - Spend by campaign, current period against prior, grouped bars, sorted by current spend.
   - CPA by campaign for the period, with the account CPA drawn as a reference line.
   - Account spend trend across the periods in metrics-history, line chart.
   - Conversions against spend over time, two axes, on a monthly report.
   - Budget pacing on a monthly report: spent to date, projected, and budget as three bars.
3. Never plot a campaign under the quiet floor without marking it low volume in the label.
4. Never draw a trend line through fewer than 3 periods.
5. When matplotlib is unavailable, draw the same chart with Pillow, simplified but labeled. When
   neither is available, deliver the table and say in Could not read that charts could not be
   rendered.
6. Store under /workspace/analytics/reports/<date>/charts/<nn>-<slug>.png.

## Tables
1. Every report table is also saved as a PNG screenshot for chat, because a wide markdown table
   does not survive a phone. Render the table to PNG with matplotlib or Pillow and attach both the
   text table and the image.
2. Sort by spend unless the user asked otherwise. Show the change column in absolute terms and in
   percent. Mark "not available" where an input was missing, never a zero.
3. Store under /workspace/analytics/reports/<date>/tables/<nn>-<slug>.png.

## Source evidence
1. **Live platform reads.** Screenshot the platform view the number came from, with the date
   range control and the totals row visible, every time a live read feeds a report, an ask, or a
   crossing. That screenshot is the receipt for the source label. Store under
   /workspace/analytics/reports/<date>/sources/live-<platform>-<view>.png.
2. **Exports.** Screenshot the relevant rows of the file, cropped to the rows in question, and
   store beside the live shots.
3. Crop out account ids, billing details, user lists, and anything that identifies a person.
   Never screenshot a sign-in page, a password field, or a 2FA prompt.

## In chat
Attach the charts and table images with the message, capped at 6 images, then one line: "N more in
the report." Every image has a one line caption naming the metric and the range. Never attach an
image you did not just produce, and never reuse a chart from a prior period without relabeling it.

## Never
Attach a screenshot showing credentials, a sign-in page, a 2FA code, an account id, or a
customer's personal data. Describe a chart you did not render. Present an EXAMPLE chart without
the EXAMPLE label on the image itself.
