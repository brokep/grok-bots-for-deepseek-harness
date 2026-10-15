---
name: build-the-target-list
description: "Use when the user first describes who they sell to, hands over companies or an export, or asks to add, drop, or widen names on the list."
---

# Build the target list

Part of the Outbound Prospecting agent preset.

Inputs: their ideal customer from memory, plus whatever they have. A pasted list of companies, a CRM or sales-tool export, a link to a sheet, a conference or portfolio page, or nothing but the ideal customer.

The list is one row per person: prospect_id, company, company_url, person, title, location, icp_fit, channel, contact, hook, hook_source_url, hook_date, enriched_on, status, last_touch_on, next_step, notes.

Fixed values. icp_fit is strong, maybe, or weak. channel is email, linkedin, x, or other. status runs new, enriched, drafted, approved, sent, replied, meeting, no, or on hold.

1. Start from companies. With only an ideal customer, find 10 to 20 companies that match it on the public web and say where each one came from. With a paste or an export, read the columns back before you change anything.
2. Score each company strong, maybe, or weak against the ideal customer, with one line of reason. Leave the weak ones out unless the user wants them.
3. Find one or two people per company who hold the job the ideal customer names. Confirm the title on the company's own site, the person's own profile, or a press page. An unconfirmed title stays blank and the row stays at new.
4. Never guess a contact. Do not build an email address from a pattern and do not assume a profile URL from a name. A contact goes in a row only when you found it published and can link to it.
5. Deduplicate on person plus company, then on company URL. Drop anyone on the do-not-contact list and anyone the user already has as an inbound lead, an open deal, or a customer, and say who you dropped.
6. Show the first ten rows in chat with the fit reason, take one round of edits, then save the whole list.

Fallbacks: an export that will not parse means you ask them to paste the rows. A company with no public team page gets a note asking them to name the person.

Stop the first build at 25 rows so they can check your aim before you go wide, and go further the moment they ask. The target list is the record, so edit it in the same turn they add or drop a name. Save under the prospecting folder.
