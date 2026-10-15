---
name: evidence-media
description: "Use before taking any screenshot, on an audit, a shipped change, or a landing page. Holds the 1280 and 390 width rule, what to capture and crop, before and after composites, and how to say which build or URL each image came from."
---

# evidence-media

Part of the Website Ops agent preset.

# Evidence media

Every finding a user reads comes with the picture that proves it. Files on disk are the archive.
Attachments in chat and in the pull request body are the evidence.

## The two widths
Every page screenshot is taken twice: desktop at 1280 wide and mobile at 390 wide. Both go in
chat, both go in the pull request body. A change shown at only one width is not shown.

## Screenshots, always
1. Full page for the page itself, then a cropped shot of the specific element behind each
   finding or each change. The crop is what makes a finding readable at a glance.
2. Store under /workspace/site-audit/<date>/<page-slug>/ for audits and
   /workspace/site-audit/<date>/changes/<nn>-<slug>/ for shipped changes, named
   <width>-<state>-<step>.png so a folder listing reads as a timeline.
3. Capture the failing state as well as the fixed one: the empty state, the error state, the
   focus ring, the mobile layout under the fold. Expect 6 to 20 shots per page on an audit.
   Fewer than 4 means the pass was shallow, keep going.
4. Screenshot the measurement too when a tool produced it, the report panel or the terminal
   output, so a number in the report has a picture behind it.
5. Cap in chat at 8 images, then one line: "N more in the report."
6. Never attach a screenshot that shows a credential, a token, a staging password, an env value,
   or real customer data. Use obviously fake data in any form you fill.

## Before and after composites
1. A change needs both states of the same surface at the same width and the same viewport.
   Navigate the previous state on the default branch or the production URL, then the new state
   on the branch build or the preview.
2. Compose one side by side image per width with ImageMagick or Pillow, labeled with the state,
   the branch or URL, and the date. Put the pair in the pull request body above the description.
3. When no previous state exists, attach the after and write "first seen" rather than inventing
   a before.
4. Name composites before-after-1280.png and before-after-390.png so the pull request body
   always references the same two files.

## Platform interface screenshots
1. Every number read from a signed-in platform gets a screenshot of the view it came from, with
   the property or account name and the date range visible in the frame. A number without that
   picture is not evidence.
2. Crop to the report. Never capture the account switcher, another property in a dropdown, a
   billing panel, a user list, or a URL bar containing a token.
3. Store under /workspace/site-audit/<date>/platforms/<platform>-<view>.png.
4. Never screenshot a login page, a password field, a recovery code, or a 2FA prompt.

## Where each image came from
Say it, every time, in one clause: local run, branch build, pull request preview, hosting
dashboard, a platform report, or production. A screenshot from production is not evidence that
a branch works, and a platform report is not evidence that a page renders.

## Never
Describe a screenshot you did not attach. Reuse an old screenshot for a new claim. Crop out the
part that contradicts the finding. Attach an image of a page that failed to load without saying
it failed. Attach an image showing a credential, a token, or another property's data.
