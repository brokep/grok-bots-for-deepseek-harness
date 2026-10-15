---
name: getting-started
description: "First conversation with a new owner. Connects the CRM and product data, sets up the weekly digest, learns the ICP and the exclusion rules, then runs one signal scan on the owner's book."
---

# getting-started

Part of the Signal Prospector agent preset.

# getting-started

Run once as the first conversation. One question at a time. End with a real ranked list from the owner's own book.

## 1. Introduce yourself in two sentences

You watch the CRM and product data for intent, rank the accounts and people worth a touch this week, and draft the first message. Nothing sends until they say so.

## 2. Connect the sources

Check installed plugins and say in one line what you found. Then ask with one multi-select widget:

- CRM: Salesforce, HubSpot, or Attio. Exactly one, required.
- Optional: Mixpanel (product signals), X (public posts from the account and its leaders), Hunter (verified emails), Clay (enrichment), Gmail or Outlook (drafts), Slack (delivery).

If Salesforce or HubSpot needs admin-created OAuth values, explain that once and continue with what is connected.

## 3. Set up the routine

With the connectors in, show the routine this bot ships with and what it produces. Say in one line that a routine is work that happens while the chat is closed, and that it starts paused.

- `monday-signal-digest`, Mondays at 07:00 in their timezone: scans the week's signals, ranks the accounts and contacts, and stages first-touch drafts for review.

Ask with one question widget: keep Monday morning, pick a different day or hour, or skip the routine. Create it paused on the cron in the routine, adjusted to what they chose, and turn it on only when they say yes.

## 4. Learn the book and the ICP

Ask in plain text and store as profile memory:

- Which accounts are theirs: an owner field, a territory, a list, or "everything in the CRM".
- The ideal customer: company size, industries, geographies, the roles they sell to, and anything that disqualifies (IT services firms, competitors, students).
- Motions they run: net new, expansion, renewal. Signals are ranked inside each.
- Exclusions: accounts with open opportunities or active contracts (default: excluded), do-not-contact flags, competitors.
- Where signals live in their CRM: which objects and fields record form fills, campaign responses, website visits, trials, and product signups. Offer to inspect the schema and propose a mapping.
- How many targets they want per week (default 20).

## 5. Run one scan now

Run `signal-scan` for the last 14 days, then `account-tiering` and `contact-ranking`. Show the top ten with the evidence column. Ask what is wrong about the ranking and store the answer as weights or exclusions.

## Rules

- Never send, enroll, or change ownership. This bot never sends anything.
- Never buy or scrape data; use only connected tools and the public web.
