---
name: set-accounts-and-thresholds
description: "Use when the user first names the accounts they run, changes a budget, wants different limits, or asks what you are watching for."
---

# Set accounts and thresholds

Part of the Ad Spend Watch agent preset.

Inputs: the platforms and accounts they spend on, the monthly or daily budget behind each one, and any limit they already carry in their head.

A threshold row is: scope, name, metric, direction, limit, window, severity.

- scope: account, campaign, or ad set
- name: the account or campaign the row watches, or all for every one of them
- metric: spend, cost per acquisition, return on ad spend, conversions, click-through rate, cost per click, cost per thousand impressions, or frequency
- direction: above or below
- limit: a flat number, a percent of the plan, or a percent of the trailing baseline
- window: today, last 3 days, last 7 days, or month to date
- severity: urgent, watch, or note

Starter set. Propose it on a first run, then edit it freely with them:
1. Account spend above 120% of the daily plan, today, urgent
2. Campaign spend above 150% of its own 7-day average, today, urgent
3. Campaign spend past the quiet floor with zero conversions, last 2 days, urgent
4. Campaign cost per acquisition above 150% of its 14-day baseline, last 3 days, urgent
5. Campaign return on ad spend below 70% of its 14-day baseline, last 3 days, watch
6. Account spend on pace to pass the monthly plan, month to date, watch
7. Campaign click-through rate below 60% of its 14-day baseline, last 7 days, note
8. Campaign frequency above 3.5 on a social account, last 7 days, note

Quiet floor: no row fires on a campaign with fewer than 100 clicks, fewer than 5 conversions, or under 50 in their currency in the window. Small numbers swing hard and a false alarm costs you their trust. Ask for their floor once and keep it.

Steps:
1. List the accounts and campaigns with the budget behind each one.
2. Show the starter set as a table, take one round of edits, then save.
3. Baseline every metric a row reads against. Mark rows with no history yet as waiting, and say when they go live.
4. Mark the accounts the user named as priority, so a check that finds ten breaches leads with theirs.

Show the table in chat and name which rows are live and which need history first.

Save under ad spend watch.
