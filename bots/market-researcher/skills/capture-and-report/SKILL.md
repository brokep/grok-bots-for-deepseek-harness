---
name: capture-and-report
description: "Use this when capturing anything visual or building the report that closes a brief, a matrix, or a strategy read. Screenshot and filing rules, the swipe grid and before-and-after composites, and the self-contained report builder with its verify step."
---

# capture-and-report

Part of the Market Researcher agent preset.

# Evidence media

Every finding a user reads should come with the picture that proves it. Files on
disk are the archive. Attachments in chat and the report are the evidence.

The working root for everything this bot saves is `/workspace/marketing-research/`,
with one folder per competitor and `_us/` for the user's own material. Every
relative path in any skill hangs off that root.

## Screenshots, always
1. **Ad creatives**: the creative itself in the library, not the results page,
   plus the results page once for the count. Filed into
   `<competitor>/swipe/<theme>/<first-seen-date>-<network>-<nn>.png` so the
   swipe file builds itself as a side effect of the weekly run.
2. **Landing pages**: the fold at 1440 wide as its own image, plus the full page
   under `<competitor>/snapshots/<date>/<page>.png`. The fold is what gets
   compared, the full page is the record.
3. **Search results**: the whole above-the-fold block for each core term, ads
   included, under `_us/search/<date>/<term-slug>.png`. Note the date, because
   results move.
4. **Signed-in platform views**: the auction insights table, the Search Console
   performance report, the GA4 acquisition view, with the date range visible in
   the shot, under `_us/platforms/<date>/<platform>-<view>.png`. A platform
   number with no view screenshot does not go in the brief.
5. **Posts**: the post itself, never the feed, under
   `<competitor>/social/<date>/`.
6. Never attach a screenshot showing a password field, a session cookie, billing
   or payment details, or another customer's data. Crop the account switcher out
   when it names accounts the user did not name.

## Composites, the artifacts people actually use
1. **Before and after**: for every fold message, offer, or price change, one
   side-by-side image from the previous and current snapshots, labeled with both
   dates. Crop to the changed region on a long page and keep the full pair in
   the appendix.
2. **Swipe grid**: for a competitor's live ads, one grid per theme, each tile
   captioned with the hook, the network, and the first-seen date, ordered oldest
   to newest so fatigue reads left to right. This is what gets attached in chat
   rather than 30 loose images.
3. **Page against page**: the competitor's fold beside the user's fold, labeled,
   whenever the side-by-side table is delivered.
4. No previous snapshot means attach the current one and say "first seen". Never
   fabricate a before.
5. Build composites with ImageMagick or Pillow.

## Video, rare
Only on request, and only when a competitor replaces a page outright: a 20 to 30
second before and after clip stitched from the two snapshots with
`ffmpeg -framerate 0.5 -pattern_type glob -i 'ba-*.png' -vf
"scale=1280:-2,format=yuv420p" clip.mp4`. Say which method produced it. Never
claim a recording that did not happen.

## Caps and naming
8 images per competitor in chat, then "N more in the report". Filenames carry
competitor or platform, date, and page, view, theme, or creative number so a
folder listing reads as a timeline.

## The report
One file, opens anywhere, nothing missing. Every image and clip is embedded as a
base64 data URI. No relative paths, no external asset URLs, no CDN scripts.

**When**: every weekly brief that had at least one change (quiet weeks get no
report), every messaging matrix with more than a handful of images, every
monthly strategy read, and the end of the setup first proof.

**Build** (Python, standard library only):
1. Collect this run's assets in reading order: the user's homepage shot, swipe
   grids, before and after composites, landing page folds, search result shots,
   platform views, posts.
2. Downscale images to 1600px wide (Pillow if available, otherwise
   `ffmpeg -i in.png -vf scale=1600:-2 out.png`). Re-encode any clip over 25 MB
   to 720p H.264. Target under 60 MB total.
3. Base64-encode each file and write
   `<img src="data:image/png;base64,...">` or
   `<video controls preload="metadata" src="data:video/mp4;base64,..."></video>`.
   Never write `src="./something.png"`.
4. Inline all CSS in a `<style>` block. No web fonts.
5. Structure: header (competitors covered, report type, window, date, and which
   sources were live UI versus export), a 5-line summary, then per competitor
   the ads and swipe grid, the page and offer changes with composites, pricing
   and promotions, channel mix, search overlap, content and social. Then Our
   numbers with the platform views, Against our marketing, Counter-moves, Worth
   a decision, Could not read, and an appendix of every remaining screenshot
   captioned with its source and date.
6. Save to `reports/<date>-<type>.html` under the working root with a manifest
   beside it listing every embedded asset and its size.

**Verify before delivering (mandatory)**:
1. Open the saved file in the browser.
2. Count `<img>` and `<video>` elements and confirm each has a `data:` src and a
   non-zero natural width or duration. Zero broken elements is the bar.
3. Screenshot the rendered report top and one section as proof.
4. Fix and rebuild anything broken. If an asset cannot be produced, remove the
   element and note it in Could not read.

**Deliver**: attach the file in chat with one line, report type, competitors,
image count, file size, plus the two proof screenshots. The report is the
deliverable and the chat body points at it.
