---
name: map-an-export
description: "Use when the user hands over an ad platform export for the first time, adds a new platform, or the headers in a familiar export have changed."
---

# Map an export

Part of the Paid Media Report Desk agent preset.

Inputs: a CSV, a TSV, a spreadsheet export, a pasted table, a link to a sheet they have shared, or a screenshot of a report table.

1. Read the file and say what you found before you change anything: the platform, the header row, the row count, and the first and last date. Ask once when the platform is not obvious from the headers.
2. Map their headers onto the shared fields: date, platform, account, campaign, ad set or ad group, ad or creative, spend, impressions, clicks, conversions, conversion name, and conversion value.
3. Expect the same fields under different names. Cost, Amount spent, and Amount spent (USD) are all spend. Impr. is impressions. Meta gives you both Link clicks and Clicks (all), so ask which one they report on and record the answer. Results, Conversions, and Website purchases are all conversions, and the exact conversion name gets kept rather than flattened.
4. Normalize dates to one format and strip currency symbols and thousands separators from numbers. Keep campaign, ad set, and ad names exactly as written.
5. Anything you cannot map with confidence goes in a short list at the end of your reply, and you ask once. Never guess a currency, a timezone, an attribution window, or which conversion column counts.
6. Show the map as a table: their header, the field it becomes, and one sample value. Take one round of edits, then save it so the next export from that platform maps itself.

Output: the saved column map, the row count, the date range covered, and any rows you could not read.

Fallbacks: a spreadsheet file that will not parse gets one ask for a CSV. A screenshot gets read for whatever is legible, with the uncertain cells named. A sheet link you cannot open gets one ask for a paste. When Hex or Google Sheets is connected and the numbers already live there, read from the source instead and map its columns the same way.

Save under paid media reports.
