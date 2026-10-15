---
name: ebr-deck
description: "Builds an executive business review deck for a customer account from the CRM, calls, and usage data: adoption, value delivered, what changed, roadmap, asks. Every number sourced; on brand; delivered as a file."
---

# ebr-deck

Part of the EBR & Value Deck Builder agent preset.

# ebr-deck

## When to use

"Build an EBR for Acme", "QBR deck for Northwind", "executive review for our call Thursday". Input: an account name, optionally the meeting date and audience.

## Gather, in parallel

1. CRM: account, contract terms and dates (for internal notes only), contacts and roles, open opportunities, support or success history if recorded, the goals captured at kickoff.
2. Calls (Gong, if connected): what the customer said they wanted to achieve, in their words, from the kickoff and the last two reviews; open asks and commitments.
3. Usage (Mixpanel or CRM product fields, if connected): adoption over the review period, active users and teams, feature adoption, trend versus the prior period. Note the source and date range of every series.
4. Public: anything the customer announced that connects to the goals (a launch, a reorg, a stated priority).

If a source is missing, leave its slide out and say so in the delivery note. Never fill a gap with an estimate.

## Deck (10 to 14 slides)

1. Title: account, date, presenters.
2. Where we started: the goals from kickoff, quoted from the customer.
3. Adoption: users, teams, activity, with the trend. Charts built from the actual data.
4. Value delivered: outcomes against each goal, with the evidence (a metric, a quote, a shipped result). Business framing first.
5. What changed since last review: three to five bullets.
6. Voice of the customer: two verbatim quotes from calls, attributed by role.
7. What is not working: honest gaps and what we are doing about them.
8. Roadmap: what is coming that maps to their goals.
9. Recommendations: two or three plays for the next period (expand to a team, enable a feature, a training).
10. Asks and next steps: what we need from them, dates, owners.
11. Appendix: sources, with links.

Customer-facing numbers are adoption and outcomes. Spend, ARR, run rate, and per-user dollars stay out unless the owner asks for them by name.

## Build

Apply the brand profile from `brand-kit`, generate the pptx, run `pptx-compat`, and deliver the file (plus a PDF on request). Upload to the folder in memory only if the owner set one. Show a one-paragraph summary and the list of slides that lack data.

## Rules

- Never invent a number, a quote, or a logo. Speaker notes carry the source of each figure.
- Never sends to the customer. The owner presents and shares.
- No em dashes on slides. Sentence case. One idea per slide.
