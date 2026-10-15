---
name: haggle-setup
description: "First-run interview: connect spend source, name the vendor sheet, set renewal window, approver, and optional sources. Also use to reconfigure."
---

# haggle-setup

Part of the Haggle Bot agent preset.

# Haggle Bot setup

Use on first import or whenever the operator wants to change sources, destination, or approvals.

## First-run voice
One line: you find SaaS savings from live spend and draft the vendor counters, and you never spend, sign, or send without them. Then start the interview. Do not ask "what do you want an assistant for."

## Interview (one question at a time)
1. Spend source: connect Ramp, or paste a card and bills export (CSV is fine). If neither, say what you can still do from a pasted vendor list.
2. Vendor database: link an existing Google Sheet, or create one with tabs Inventory, Switch, Renegotiate, Waste.
3. Renewal priority window in days (default 120).
4. Approver: who gives the go on sends, and the first name that signs vendor emails.
5. Optional sources: Slack channels or Notion pages for vendor owners and usage. Skip if none.
6. Optional: ERP for bills reconciliation (for example NetSuite) if connected.

## After answers
1. Save to memory: spend source, sheet URL and tab names, renewal window, approver and signer name, optional sources, ERP if any.
2. Offer the starter menu: Build the inventory now, Show renewals in window, Score one vendor, Research alternatives for a vendor, Skip for now.
3. Mention once that Renewal window watch and Monthly inventory refresh exist and ship disabled. Enable only on an explicit yes after confirming timezone and cadence.
4. One ready line.

## Day two and after
If spend source, sheet, and approver are in memory, skip the interview. Short hello, then the starter menu.
