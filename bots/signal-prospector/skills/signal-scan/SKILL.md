---
name: signal-scan
description: "Pulls every intent signal across the owner's accounts from the CRM, product analytics, and the public web for a time window, and builds a per-account signal history with sources."
---

# signal-scan

Part of the Signal Prospector agent preset.

# signal-scan

## When to use

The `monday-signal-digest` routine, or on demand ("what lit up in my book this week", "pull my signals since the 1st"). Input: a time window (default: since the last run, at most 30 days) and optionally a subset of accounts.

## Sources, run in parallel

Use only what is connected and say which sources ran.

1. CRM engagement: new leads and contacts on owned accounts, campaign responses and event attendance, form fills, email opens or replies where the CRM tracks them, website or pricing-page visits where recorded, tasks logged by marketing. Read the field mapping stored in memory.
2. Product data (Mixpanel or CRM product fields): new signups grouped by company domain, activation events, weekly active users per company, usage spikes versus the prior four weeks, users hitting plan limits, and new admins or workspaces.
3. Public web: job postings mentioning our category or adjacent tools, new leaders in the buying center (VP or above), funding or M&A, public initiatives that match the POV, tech-stack changes on the company's engineering blog or job posts.
4. Public posts (X, if connected): what the company account and the leaders in the buying center have posted in the window. A post that names a problem we solve, announces an initiative, complains about a tool in our category, or marks a leadership change is a signal; a product launch retweet is not. Record the post's own date and its link, and quote it rather than paraphrasing, because this is the one source a first-touch email can cite word for word.
5. Our history: last touch per account, open opportunities, active contracts, prior lost deals with reason.

## Normalize

One row per signal: account, contact (if any), signal type, detail, date, source, strength (1 to 3). Fold repeated signals of the same type into one row with a count. Attach each row to its account's running signal history in memory (keep the last 90 days).

## Classify the motion

Per account: net new (no active contract, no open opportunity), expansion (active customer with growth signals), renewal (contract ending within 180 days). The motion decides which list the account goes on; never rank across motions.

## Output

A table sorted by account, then date: Account, Motion, Signal, Detail, Date, Source, Strength. Then three counts: accounts with new signals, contacts with new signals, accounts excluded and why. Hand the table to `account-tiering`.

## Rules

- Personal-plan or free-tier individual usage is a weak signal by itself; corporate-domain or team-level usage is strong. Say which one a row is.
- A public post is only a signal when the account posted it. Never treat a mention of the company by someone else, or a post older than the window, as one.
- Never infer a signal from silence.
- Read-only. Never edits the CRM, never posts, never replies, and never follows anyone.
