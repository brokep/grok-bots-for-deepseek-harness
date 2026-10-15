---
name: read-an-ad-platform-export
description: "Use when the user pastes numbers, uploads a CSV, shares a sheet, or forwards the report an ad platform emailed them."
---

# Read an ad platform export

Part of the Ad Spend Watch agent preset.

Inputs: a CSV or spreadsheet export, a pasted table, a screenshot of the platform's table, a shared sheet, or the platform's emailed report. Any one of them is enough to start.

Steps:
1. Say which columns you found before you change anything.
2. Map their columns onto these: date, account, campaign, ad set, spend, impressions, clicks, conversions, conversion value, currency. Every platform names these differently, so map cost to spend, purchases or leads or results to conversions, and revenue or purchase value to conversion value. Ask when a column could go two ways.
3. Derive the rest instead of asking for it. Cost per acquisition is spend over conversions. Return on ad spend is conversion value over spend. Click-through rate is clicks over impressions.
4. Note the date range and the currency. When the export covers dates you already hold, replace those rows instead of adding them, and say how many you replaced.
5. Rows you cannot parse go in a short needs a look list at the end of your reply. Never guess a number, a date, or a campaign name.
6. Append to the numbers ledger keyed on date plus campaign, then say how many rows landed and which range is now covered.

A screenshot gets read for the columns you can see, with one line naming what is missing. An export in two currencies stays in two currencies and you say so rather than converting.

The moment the rows land, run the check in the same reply. Do not load numbers and stop.

Save under ad spend watch.
