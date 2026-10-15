---
name: ad-accounts
description: "Use to connect, read, or change an ad or marketing account, by connector, browser, or export."
---

# ad-accounts

Part of the Distro Bot agent preset.

# ad-accounts

Connect, read, and change ad and marketing accounts. Read-only until campaign-loop clears a change.

## Connect, in this order

1. Connector: SearchPlugins for the platform (X ads has its own X Ads plugin). A third-party service that covers several ad platforms: say it is a separate company with its own terms and pricing, and install only on the user's yes. Then AuthenticateMcpServer.
2. My browser: say in chat what to sign into and why, then request_box_help "Please sign in to <platform> in my browser, then hand it back." Screenshot after. Sessions stay in this computer's browser, which the user's other bots share, so never sign out or switch accounts.
3. Export: name the report to download (by day: campaign, ad set, ad, spend, impressions, clicks, results, value), dropped in chat.
distro.py set platform <name> <connector|browser|export> "<account>". Never re-ask a declined card.

## Read

Numbers by day and ad: save them as a file and distro.py ingest <file> --platform <name> --source "<how> <date>". Connector output in another shape: write a CSV with those columns first. In the browser: the reporting table's text or a screenshot, never a click that changes anything. Creative: each ad's text, headline, image or video, audience, and landing page, into <home>/accounts/<platform>.md. A failed or stale read: one line, then skip that platform.

## Change, only when campaign-loop clears it

Connector: make the change, then read it back. Browser, in a live conversation only: a screenshot before, the edit, then a screenshot showing the new value. New campaigns and ad sets are built paused, read back, and started on a second yes.

## Never

Billing, payment methods, users and access, account or pixel settings, or terms. Delete anything.
