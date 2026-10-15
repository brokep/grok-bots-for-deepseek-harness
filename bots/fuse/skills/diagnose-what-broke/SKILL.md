---
name: diagnose-what-broke
description: "Use when a threshold fired and the cause is not obvious, or when the user asks why cost per acquisition, return on ad spend, or conversions moved."
---

# Diagnose what broke

Part of the Ad Spend Watch agent preset.

Inputs: the breached row, the numbers ledger across at least the trailing 14 days, and anything the user knows about what changed on their side.

Steps:
1. Split the metric before you explain it. A cost per acquisition jump is either a change in what traffic costs or a change in how it converts. Compare cost per click and click-through rate against conversion rate across the window, and say which side moved.
2. Walk the usual causes and say which ones these numbers support: a budget or bid change, a new campaign or creative going live, an old creative wearing out, audiences overlapping, a broken landing page or checkout, conversion tracking dropping out, a day-of-week or seasonal swing, or a competitor bidding harder.
3. Conversions falling to zero while spend holds is a tracking failure until proven otherwise. Say that first and tell them to check the pixel or the conversion import before they touch a bid.
4. Use what is connected to settle it faster. Sentry tells you whether checkout errors spiked at the hour conversions stopped. Datadog tells you whether the site or the checkout was slow or down across the same window. Figma shows the creative behind a campaign whose click-through rate is sliding, which is how you separate fatigue from a bad audience. Say which source you checked and what it showed. When none of them are connected, ask the one question that would replace them.
5. Compare against the same weekday a week back, not against yesterday. Paid performance moves on a weekly cycle.
6. Ask the one question the numbers cannot answer, usually what they changed and when.
7. Land on a ranked read: the most likely cause, what would confirm it, and the one change to make.

Say you do not know yet when the numbers cannot separate two causes, and name the data that would.

Never invent a cause, a competitor, or an outage. Never claim a platform changed something without a source.

Save the read next to the check under ad spend watch.
