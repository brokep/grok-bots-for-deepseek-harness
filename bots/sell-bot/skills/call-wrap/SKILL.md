---
name: call-wrap
description: "Use after watched calls: learnings, asks, signals, follow-ups, digest."
---

# call-wrap

Part of the Sell Bot agent preset.

# call-wrap

## Each watched call that ended in the last 3 weekdays with wrap empty

Read today's calendar first and add watched calls missing from calls.csv.
1. Notes: the notes source in setup.md, matched by time and attendees, or notes the user pastes. Not ready: leave wrap empty for the next run. On the last run in the window, one line: "No notes for <call>, paste them or say skip."
2. Learn: dated bullets in the account file: what they build, tried, and got blocked by, what landed and what didn't, what we promised, anything for the next call. Their words in quotes.
3. Asks: each feature request and bug to requests.csv, then to the bug-triage teammate per accounts with sent_to set, or into the digest.
4. Buying signals: a prospect asking for pricing, a proposal, or a contract starts proposal-desk. A customer asking for more seats or a bigger plan opens an expansion deal per proposal-desk.
5. Recap draft per draft-email: what we covered, what each side owes with dates, one thing to try next.
6. X: no saved handles, find them per watch-on-x and give the user follow links.
7. A competitor came up: ask the competitor-intel teammate, if any, what is new on it per accounts.
8. Mark wrap in calls.csv.

## Digest

After the last call: calls wrapped, drafts waiting, then up to 5 lines of patterns across today's calls (repeated asks, blockers, what landed, objections) and what went to teammates. No watched calls: quiet.
