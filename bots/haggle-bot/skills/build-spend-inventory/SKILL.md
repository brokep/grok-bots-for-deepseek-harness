---
name: build-spend-inventory
description: "Pull live spend from Ramp or an export, dedupe vendors, tag purpose, owner, cadence, commitment, and Focus, and write the vendor database sheet."
---

# build-spend-inventory

Part of the Haggle Bot agent preset.

# Build spend inventory

## Sources, in priority order
1. Ramp cards and bills (live). Bills and agreements are the source of truth for commitments and cadence.
2. ERP bills if connected.
3. Pasted or uploaded export if neither is connected.
4. Slack and Notion only for owners, users, and sentiment, and only where they do not contradict expense data.

Never use an internal project channel as a source for vendor rows, owners, or sentiment.

## Steps
1. Pull the trailing 12 months of card transactions and bills. Group by normalized vendor name. Merge obvious duplicates (Vendor Inc, vendor.com, VENDOR*).
2. For each vendor compute: trailing 12 month spend, current cadence (monthly, annual, usage), last charge date, entity or card owner, and commitment evidence (agreement, order form, or bill memo).
3. Fill Purpose in five words or fewer from bill memos, agreement titles, or Notion. Mark Unknown rather than guess.
4. Fill Owner from Slack or Notion when available. Mark Unknown otherwise.
5. Leave Focus blank unless a thesis already meets the opportunity bar. Most rows stay blank on purpose. Any Focus tag needs a one-line Why with mechanism and live $.
6. Write the Inventory tab. Columns: Vendor, Purpose, Owner, Cadence, Trailing 12mo Spend, Last Charge, Commitment or EA, Renewal Date, Focus, Why, Vendor Sentiment. All dollar cells in currency format. No Source notes column.
7. Run the Google Sheets final check before reporting.

## Output
Sheet link with gid, row count, total trailing spend, count of vendors with Unknown purpose or owner, and the list of renewals inside the priority window. Ask for billing-admin or bills access if cards clearly miss vendors.
