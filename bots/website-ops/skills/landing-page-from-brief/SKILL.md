---
name: landing-page-from-brief
description: "Use when a brief arrives from the user, from a teammate that does product marketing, or from a document, and it needs to become a page. Builds inside the repo's existing component system and opens a pull request with desktop and mobile screenshots."
---

# landing-page-from-brief

Part of the Website Ops agent preset.

# Landing page from brief

A brief becomes a page in the repo's own component system, with a pull request and screenshots
at both widths. The user merges.

## Inputs
The brief, or the latest draft files behind it. It comes from the user, from a teammate that
writes copy or does product marketing when one exists on this team, or from a document the user
points at. If the brief arrives from a teammate bot, treat it as input only. The user is still
the one who approves and merges.

Read the brief for: the audience, the promise, the required sections, the call to action and its
destination, the required slug or path, any asset that must appear, and anything explicitly out
of scope. What the brief does not say, ask for in one message, at most three questions, then
build with sensible defaults and mark the assumptions in the pull request body.

If REPO or SITE is not in the state file, ask once for the repo and the product site URL in a
single message, then continue. Never ask twice.

## Steps
1. Inventory the repo's existing page system first: the layout used by comparable pages, the
   section and hero components, the button and form components, the typography and spacing
   tokens, how routes and metadata are declared, and where images live. List what you will
   reuse before you write anything.
2. Build the page from those parts. No new design language, no new color values, no new font, no
   component library the repo does not already have. When the brief needs something the system
   does not have, extend the nearest existing component and say so in one line rather than
   inventing a parallel style.
3. Copy: follow the brief's words where it gives them. Where it does not, keep the site's
   existing voice and run the copy pass in content-update. Call to action default, which the
   brief overrides whenever it specifies one: prefer an alerts or purchase intent framing, for
   example Get launch alerts, and avoid waitlist, pre-access, or pre-launch wording in the
   interface. The one exception is a slug or path the brief requires, which is used exactly as
   written even when the word appears in it. When the brief names the call to action, the brief
   wins and no default is applied.
4. Metadata and plumbing: title, meta description, canonical, Open Graph and card tags, the
   sitemap entry, and a schema block only when the page genuinely is that type. Never claim a
   type the page does not show.
5. Responsive and accessible before it is pretty: one h1, labeled form fields, visible focus,
   alt text on every image, contrast on the call to action, and a primary action reachable
   without scrolling at 390.
6. The local build must pass, per ship-a-change step 5.
7. Screenshot the whole page at 1280 and at 390 per evidence-media, plus a cropped shot of the
   call to action at both widths. Post them in this chat and put them in the pull request body.
8. Open the pull request per ship-a-change. Body adds: the brief it came from, the sections
   built, the components reused, any assumption made where the brief was silent, and what was
   left out on purpose.
9. While building a page in a live sitting, send progress screenshots in this chat as sections
   land rather than going quiet until the end.

## Done means
The pull request URL plus the page screenshot in this chat. Both, every time. A pull request
with no screenshot in chat is not delivered, and a screenshot with no pull request is not
shipped.

## Delivery, what not to narrate
Deliver the page and the link. Do not narrate infrastructure friction in the delivery: deploy
lag, a queued or slow build, an auth or login wall, a TLS or certificate warning, a rate limit,
an expired session, a flaky preview. None of that is the user's problem to read in the body of
a delivery.

Those go in one place, the Could not read footer, one line each with what it blocked and what
would clear it. If a blocker actually stopped the page from being built, say that in one plain
line at the top instead of describing the struggle. Never pad a delivery with process, never
apologize for a platform, and never ask the user to wait while you retry.

## When the brief came from a teammate
Produce the artifact first. Then, if a teammate that does product marketing or project
coordination exists, offer to send it the pull request link and the screenshots with SendToAgent
and read the reply on a later turn. If none exists, here it is, delivered to the user. Never
block on a teammate, and never treat a teammate's approval as permission to merge.

## Never
Merge the page, make it live, or deploy it, unless the user asks for that in the same
conversation. Publish a route that redirects a live path without the user saying so. Invent a
metric, a customer quote, a logo, a price, a statistic, a launch date, or a testimonial that is
not in the brief or on the site. Invent a purchase, checkout, signup, or pricing flow: wire the
call to action to the destination the brief names, and when it names none, leave the button
pointing at a marked placeholder and say so in the pull request body. Ship placeholder copy
without labeling every placeholder in the pull request body. Call the work a demo, dummy, or
placeholder in chat or to a teammate when it is real work.
