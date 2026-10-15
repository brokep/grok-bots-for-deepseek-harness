---
name: vip-ae-nomination-sheet
description: "Use when building or updating a VIP event sales-nomination Google Sheet for a tentpole (tracking only — sales owns inviting)."
---

# VIP AE nomination sheet

Part of the WTD agent preset.

---
name: VIP AE nomination sheet
description: >-
  Use when building or updating a VIP event sales-nomination Google Sheet for a
  tentpole (tracking only — sales owns inviting).
---
# VIP AE nomination sheet

Use this shape for every VIP tentpole sales-nomination spreadsheet. This skill is **tracking and sheet structure only** — sales owns guest inviting and outreach.

## Tabs
- **Instructions** — how to nominate, who can be approved, what sales vs the bot fills, and the event timeline.
- One tab per segment or vertical the event uses. Do not mix verticals on one tab.

## Instructions timeline (follow this cadence; shift dates to the event)
1. Sales can nominate
2. Nominations due + schedule leadership review/approve
3. Sales invites from approvals (sales owns this step — the bot does not send guest invites)
4. Event day

## Each segment tab
- **A1 (required, live):** `{Segment} receives N total customer/prospect seats · Registered: X / N` as a formula, never a static X. Count Registered TRUE with a named company, excluding internals and blank names. Restore the formula if A1 is blank or broken.
- **Row 2:** grouped labels — sales columns vs bot enrichment columns.
- **Row 3 headers (left to right):**
  - Approved by leadership? (checkbox)
  - Registered (checkbox; registration tool or owner-designated agent ticks from name+company match)
  - Declined? (checkbox; tick when the guest cannot attend / sales says no)
  - FOR LEADERS Rounds / Wave (Wave 1 / 2 / 3 or R1 / R2 / R3)
  - AE / seller Name
  - Regional leader (immediately right of AE; do not overwrite)
  - Company Name
  - Individual Name
  - Title (VP+ unless the owner sets a different bar for that event)
  - Potential Future Deals ARR
  - Reason why
  - Current ARR (if customer)
  - Open Opportunity ACV
  - Close Date of Open Opptys
  - LinkedIn
  - CRM Account Link
  - CRM Oppty Link
  - CRM Contact Link
- Data rows start on row 4 with checkboxes on Approved, Registered, and Declined.

## Who fills what
- **Sales:** Company Name, Individual Name, Title, Potential Future Deals ARR, Reason why, AE Name.
- **Bot:** when sales adds an Individual Name (or Company Name), fill Current ARR, Open Oppty ACV, Close Date of open opptys, LinkedIn, and the three CRM links from live CRM data. Never invent numbers. Do not overwrite sales columns.

## Do not
- Do not invent a different column set.
- Do not post guest lists to Slack unless the owner says.
- Do not run guest-invite or wave-invite-promote playbooks — sales owns inviting.
