---
name: build-the-lead-ledger
description: "Use when the user first hands over leads, or when a new export, sheet, or pasted list needs to become the lead ledger."
---

# Build the lead ledger

Part of the Lead Pipeline Desk agent preset.

Inputs: a CRM export, a CSV, a spreadsheet link, form responses, or a pasted list. Any one of them is enough to start.

1. Read what they gave you and say which columns you found before you change anything.
2. Map their columns onto these: id, first_name, last_name, email, company, domain, title, source, campaign, country, company_size, created_on, status, owner, score, tier, last_touch, next_step, notes.
3. Take the domain from the work email when the company column is empty. Leave it blank for gmail, outlook, yahoo, and other consumer addresses, and note the row as a personal email.
4. Normalize dates, country, and the fixed value lists only. Keep their wording for company, title, source, and notes.
5. Status is one of new, working, qualified, nurture, disqualified, or converted. Anything you cannot map stays new and gets a note saying what the original value was.
6. Rows with no email and no domain, or with a date you cannot read, go in a short "needs a look" list at the end of your reply. Never guess an email address, a company, or a date.
7. Run the dedupe pass before you report a count, so the number you give them is real.

Output: the ledger written to disk, the count of rows added, merged, and set aside, the rows that need a look, and the first ten scored rows in the same reply so they see something real immediately.

When there is no file at all, ask for five example rows and build from those. When a sheet link will not open, ask them to share it or paste the rows.

Save under the lead desk folder as leads.csv.
