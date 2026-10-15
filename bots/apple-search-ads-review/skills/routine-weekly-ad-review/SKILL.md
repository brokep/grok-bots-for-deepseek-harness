---
name: routine-weekly-ad-review
description: "Scheduled routine: Every week on the user's chosen morning, a read on last week's Apple Search Ads spend against target, with the changes worth making first."
---

# Weekly ad review

Part of the Apple Search Ads Review agent preset.

Schedule, as written by the template author: Every week on the user's chosen morning, a read on last week's Apple Search Ads spend against target, with the changes worth making first.

## What to do on each run

Run once a week on the morning and hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the targets sheet, every export saved since the last review, and the previous weekly review. When no new export has landed, send one short line naming the last date you have and what to drop in, then stop. With data, write the review in the shape from the Weekly ad review skill: the range and blended cost per install against target, the trend per campaign with cost per tap and conversion rate split out, the groups costing the most money above target with the money figure, where there is room to spend more, harvest and negative candidates, the bid changes worth making, what happened to last week's recommendations, and the three to five changes to make first. Every line carries a number from the export. Save the dated review and attach it, then deliver it to the destination they picked, and treat anything that posts or emails as a draft for them first. Never invent spend, taps, or installs, and never edit the ad account.
