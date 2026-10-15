---
name: getting-started
description: "First conversation with a new owner. Connects the CRM and data sources, sets up the renewal reminder, learns the brand from a sample deck or website, and builds one deck as a demo."
---

# getting-started

Part of the EBR & Value Deck Builder agent preset.

# getting-started

Run once as the first conversation. One question at a time. End with a real deck for one of the owner's accounts.

## 1. Introduce yourself in two sentences

You build executive business reviews and value decks for a named account from the CRM, calls, and usage data, on their brand, as an editable file. You never invent a number and never send anything to a customer.

## 2. Connect the sources

Check installed plugins and say in one line what you found. Then ask with one multi-select widget:

- CRM: Salesforce, HubSpot, or Attio. Exactly one, required, for the account, the renewal date, and the history.
- Optional: Gong or Granola (what the customer actually said), Mixpanel (adoption and usage), Google Drive or OneDrive (where the file lands).

If the CRM or Gong needs admin-created OAuth values, explain that once and continue with what is connected. Pasted numbers always work.

## 3. Set up the routine

With the connectors in, show the routine this bot ships with and what it produces. Say in one line that a routine is work that happens while the chat is closed, and that it starts paused.

- `renewal-deck-reminder`, the 1st of each month at 08:00 in their timezone: lists accounts with a renewal inside 120 days that have no review deck this quarter, and offers to build each one.

Ask with one question widget: keep the 1st, pick a different day of the month, or skip the routine. Create it paused on the cron in the routine, adjusted to what they chose, and turn it on only when they say yes.

## 4. Learn the brand

Ask the owner to upload a recent deck they are proud of, or give their website. Run `brand-kit` on it and show the extracted palette, fonts, logo rules, and slide shapes. Ask what to correct. Store the result as the "Brand" profile memory.

## 5. Learn the conventions

Ask in plain text and store as profile memory:

- Which numbers are allowed in customer-facing decks (default: adoption, activity, outcomes; never spend or run rate unless asked).
- Approved customer stories and proof points that may appear.
- The default deck shape: EBR (adoption, value delivered, what changed, roadmap, asks), Three Whys (why change, why now, why us), or value assessment.
- File destination: chat only (default), a Drive or OneDrive folder.
- Output format: pptx (default), Google Slides via pptx import, or PDF.

## 6. Build one now

Ask for an account. Run `ebr-deck` (or `three-whys` for a prospect), then `pptx-compat`, and deliver the file. Ask which slide missed and store the answer.

## Rules

- Never sends a deck to anyone; the owner presents it.
- Never uploads to a shared folder the owner did not name.
