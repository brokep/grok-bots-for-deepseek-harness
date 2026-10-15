---
name: evidence-media
description: "Use before taking a single screenshot, on any build, read, or demo. Holds the screenshot-per-step rule, the before and after of campaign status, what must never appear in a frame, and the rule that a screenshot belongs to the run that produced it."
---

# evidence-media

Part of the Performance Marketer agent preset.

# Evidence media

Every claim a user reads should come with the picture that proves it. Screenshots in chat are the
evidence, not a description of evidence.

## Screenshots, always
1. Every step in a platform interface gets a screenshot taken on that run: the account
   verification after sign in, the account name before the first create, every settings screen,
   the campaign form, the ad group or ad set creation, the targeting, the exclusions, each ad as
   it saves, any composer limit I read off the screen, and every error or rejection. Store under
   /workspace/ads/<platform>/<campaign-slug>/build/<date>/step-<nn>-<slug>.png. Expect 10 to 30
   for a build. Fewer than 8 means steps went unrecorded, go back.
2. Status, before and after. Any change to a campaign, ad group, ad set, or ad gets a screenshot
   of the status column immediately before and immediately after, composed side by side when both
   exist. This is what proves a build is paused, and what proves an enable happened.
3. The landing page and final URL: screenshot on the first read and again before any launch gate.
4. The review sheet: when Sheets is connected, screenshot the Overview and Ad copy tabs. When it
   is not, the Markdown in chat is the artifact.
5. Traffic reads: screenshot the campaign row with the spend column and the variant table with its
   metrics, every read. Store under /workspace/ads/<platform>/<campaign-slug>/reads/<date>/.
6. Cap at 8 images per message, then one line, "N more in the build log."
7. Never attach or save a screenshot showing a password field, a 2FA code, a session or cookie
   value, a payment method, billing details, an invoice, another advertiser's data, or a full
   account identifier. Crop the frame rather than skipping the evidence. A login wall is fine as
   proof of being logged out once any entered email is cropped out.

## Composing before and after
Compose one side by side image with ImageMagick or Pillow, labeled with the time and what changed.
When there is no before, attach the after and write "first build" rather than implying a
comparison that does not exist.

## Honesty rules, not optional
1. A screenshot belongs to the run that produced it. Never reuse a screenshot from an earlier run,
   an earlier campaign, an earlier platform, or a demo to stand in for work done now.
2. Never describe a screen I did not open, and never call a step done when its screenshot does not
   exist.
3. If a platform is unreachable, slow, erroring, or logged out, say so plainly in that turn, put it
   in a Could not read line with what failed, and stop. Do not narrate a build that is not
   happening, in a demo or anywhere else.
4. Every number carries whether it came from a live interface or an export, and every filename
   carries its date so a folder listing reads as a timeline.

## Demo and example artifacts
When the user wants a demo, a sample, or a picture of what the output looks like, build it as
clearly labeled example work: the word EXAMPLE in the title, in the sheet header, and in the
filename, with invented copy and invented numbers that are labeled as invented. Never mix example
rows into a real sheet, never store example artifacts under a real campaign path, and never
present an earlier real campaign's screenshots as a live build.

## Naming
Filenames carry platform, campaign slug, date, and step or metric, so a folder listing reads as a
timeline without opening anything.
