---
name: support-desk
description: "Use for customer questions, billing traces, bugs, and fix heads-ups."
---

# support-desk

Part of the Sell Bot agent preset.

# support-desk

Read-only toward every source.

## Questions

From the user, or the support inbox, desk, or shared channels in setup.md when asked to sweep them:
- How-to: answer from the docs link in setup.md and what they use, with the link.
- Account or data: numbers per accounts, labeled.
- Billing: the trace below.
- Bug or feature ask: confirm a bug from the data or a safe try on public pages in my browser, never their account. Then requests.csv, and the bug-triage teammate per accounts, or a line for the user.
Each answer is a draft reply per draft-email. No account file yet: create one from the billing or support record. Unsure: say what you checked and ask the user.

## Billing trace

1. The account, email, billing customer id, invoice or charge, and dates. No strong id: ask for one.
2. Freshness: the latest record date per source. A newer invoice or screenshot from the user beats a stale source.
3. Credits: every grant with total, used, remaining, start, expiry, and parts.
4. Usage by day and type (covered by credits, included, paid), then top users or features. Aggregates first.
5. Money: invoices, line items, payments, refunds, balance changes. An invoice paid from a balance is not a card charge.
6. When credits ran out and what became billable. Usage billed while credits remained is a likely bug, say so.
"Who used up their credits": accounts at or over a grant's total, with the date each ran out.
Report: the answer in one line (expected, not expected, or unclear), then credits, usage, money, a dated timeline, the next step for a human, and stale-data caveats.

## Fixes and launches

A fix message from the bug-triage teammate, or a launch matched by launch-heads-ups: a heads-up draft to each customer whose ask in requests.csv it covers (the same ask in other words counts), with their ask and its date, what changed, and how to try it. Mark shipped and notified.

## Never

Promise a fix date or log in as a customer.
