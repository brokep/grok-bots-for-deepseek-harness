---
name: pull-numbers-from-a-connected-source
description: "Use when a sheet, a warehouse, or report email is connected and you need fresher numbers than the last paste, including before every routine run."
---

# Pull numbers from a connected source

Part of the Ad Spend Watch agent preset.

Inputs: whichever of these the user connected. A Google Sheet they keep, a Hex project holding their spend query, or the daily report the ad platform emails them.

Steps:
1. Check which sources are connected and which one is freshest. Say the one you used.
2. Google Sheets: read the tab the user named, treat the header row as the column map, and read it live on every run rather than trusting what you read yesterday. When the tab moved or the headers changed, say so instead of guessing.
3. Hex: run or read the saved query the user pointed you at. Ask once for the project and query name, save both, and reuse them. Never write to their warehouse.
4. Report email: find the newest report from each platform, take the attachment when there is one and the table in the body when there is not, and ignore anything older than the freshest date already in the ledger.
5. Hand every row to the export skill for column mapping and de-duplication, so one path owns the ledger.
6. Say the source, the date range, and how many rows are new.

Fallback: nothing connected, or the source is empty or stale. Say it in one line, ask for a paste, and stop there. Do not stall a check waiting on a connection, and do not fill a gap with an estimate.

Save under ad spend watch.
