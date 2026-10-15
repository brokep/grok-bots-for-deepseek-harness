---
name: ingest-exports
description: "Use before every report, every reporting ask, and every spend check, and whenever new data lands. Reads every signed-in platform live first, then the export files, validates columns against the column map, dedupes, normalizes dates and currency, and stores everything under /workspace/analytics/ with its source."
---

# ingest-exports

Part of the Marketing Analyst agent preset.

# Ingest exports

Every number this bot reports comes from here. Nothing is typed from memory.

## When to use
On every report, every reporting ask, every spend check, and whenever the user says new data has
landed.

## Source order, every run
1. **Every signed-in platform, read live in my browser.** For each platform in the ACCOUNTS
   entry: open its reporting view, set the date range the job needs, set the breakdown to
   campaign and day, read the table, and screenshot the view with the date range visible. Write
   the rows to the ledger tagged source live, with the platform, the view, and the read date. A
   login wall means the session expired, so handle it per connect-accounts rather than guessing.
2. **Exports**, for every platform that is not signed in, and for history older than the platform
   view offers. Steps 1 through 10 below.
3. **Nothing for a period.** Say which platform and which date range is missing and stop. Do not
   estimate, do not carry a previous period forward, and do not fill a gap from the ledger.

Live and export rows for the same platform, date, and campaign are the same key, so the dedupe
rule below applies across sources. The live read wins, because it is the platform's own current
number, and the drop is recorded in the check file.

## Where exports come from
In this order, stopping at the first that has a file newer than the last ingest:
1. The Google Drive folder the user named in setup.
2. The Google Sheet and tab the user named in setup.
3. A file the user pasted into chat, which lands under /workspace/uploads/.
4. Nothing. Then the rule in source order 3 applies.

## Steps (export path)
1. List candidate files with their modified dates. Take the newest per platform that is not
   already recorded in /workspace/analytics/exports/index.md.
2. Copy the file unchanged to /workspace/analytics/exports/<platform>/<YYYY-MM-DD>-<name> and add
   a line to exports/index.md: file, platform, date range covered, row count, ingest date.
3. Validate the header row against /workspace/analytics/column-map.md for that platform. Required:
   a date column, a campaign column, impressions, clicks, cost. Recommended: ad set, conversions,
   conversion value, the named conversion column, device, and country when present.
4. On a mismatch, stop for that file and report it: the expected column, the header actually
   found, and the two or three closest candidates. Ask the user to confirm the mapping once, then
   update column-map.md. Never guess a mapping that changes what a number means, and never map a
   second conversion column onto the first.
5. Normalize dates to YYYY-MM-DD. Platform exports use several formats, so read the column as text
   and parse it explicitly rather than letting a tool infer it. Reject a row whose date does not
   parse and count it under rows dropped.
6. Normalize currency: read the currency from the export or the column map, keep the code with the
   number everywhere, and never convert between currencies. Strip thousands separators and
   currency symbols. Micros columns (cost in micros) are divided by 1,000,000 and the conversion
   is noted in exports/index.md.
7. Dedupe on the key date plus platform plus campaign plus ad set. When two rows share a key,
   the row from the newer export wins and the older is dropped. Count and report duplicates
   dropped. A re-export of an overlapping range is normal and must not double count spend.
8. Append to /workspace/analytics/ledger.csv, one row per date per campaign, with the raw columns
   as ingested plus the source. The source column reads `live <platform> <view> <read date>` or
   `export <file name> <ingest date>`, and it travels with the number into every report.
9. Rebuild /workspace/analytics/metrics-history.csv, one row per period per platform per campaign,
   for the periods the ledger now covers, with the derived metrics computed per the formulas
   below. Rebuild rather than patch so a late re-export corrects history.
10. Write a dated check to /workspace/analytics/checks/<date>.md: platforms read live and the
    views used, files read, rows kept, rows dropped and why, duplicates dropped, date range now
    covered per platform and per source, columns that failed validation, expired sessions, and
    any period that is still missing. Anything that needs the user goes to
    /workspace/analytics/fixes/<date>.md as a short numbered list.

## Column map shape
One row per platform header in /workspace/analytics/column-map.md:

`<platform> | <export header> | <canonical field> | <unit or format> | <notes>`

Canonical fields: date, campaign, ad_set, impressions, clicks, cost, conversions,
conversion_value, plus any extra the user reports on. Keep the platform's own conversion column
name in the notes so a report can name it.

## Metric formulas (the only ones used anywhere)
- CTR is clicks divided by impressions.
- CPC is spend divided by clicks.
- CPM is spend divided by impressions, times 1,000.
- Conversions come from the platform's own conversion column, with its name kept.
- CPA is spend divided by conversions.
- ROAS is conversion value divided by spend.
- A metric whose denominator is zero or whose input is absent is written "not available", never
  zero and never estimated.
- Never add one platform's attributed conversions to another platform's unless the user confirmed
  the attribution windows match. When they have not, report per platform and say why there is no
  total.

## Output
The counts line in chat: platforms read live, files read, rows kept, rows dropped, duplicates
dropped, date range per platform, and anything that needs the user. Then the check file path.
Nothing else.

## Never
Edit an export in place. Write a number into the ledger that came from neither a live view nor an
export. Convert currency. Carry a previous period's figure forward as new. Report a period the
data does not cover. Change anything inside a platform while reading it.
