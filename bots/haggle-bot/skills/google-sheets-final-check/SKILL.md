---
name: google-sheets-final-check
description: "Mandatory live re-read QA after any Google Sheets write, before telling the operator it is done."
---

# Google Sheets final check

Part of the Haggle Bot agent preset.

# Google Sheets final check (mandatory before delivery)

After EVERY Google Sheets mutation (values, format, layout), do this BEFORE messaging the user that it is done. Write-ack alone is never done.

## Live re-read (required)
1. `get_values` the visible header, KPI block, first ~15 data rows, and a sample near the end of each list.
2. Count rows in each delivered list (COUNTA or a count of non-empty key column). Counts must match the brief exactly.
3. Reconcile rollups (owner totals, KPI cards) to those row counts.

## Completeness and readability gate (FAIL if any hit)
- Format pollution: rank, IDs, text, Yes/No showing as currency, dates, or percents.
- Blank critical columns: Account, key IDs, owner (when expected), $ metrics the brief promised.
- Mashed layout: two unrelated books side by side in one grid without clear section breaks. Prefer stacked sections (summary, then list A, then list B).
- Empty decorative columns (Tier, Sub-tier, spacer) with no data.
- Missing formatting: header row not bold, columns too narrow to read names, no freeze on header of long lists when useful.
- Wrong membership: old cut still on tab.
- Agent names or crew jargon in cells.
- Wrong sheet touched (for example edited a source of truth marked read-only).

## Fix before ship
If any gate fails: fix on the live tab, re-run this checklist, then deliver. Never hand the user a tab you have not re-read after the last write.

## Delivery line
Include: URL with gid, exact counts verified, one line on what each section is. No methodology wall.
