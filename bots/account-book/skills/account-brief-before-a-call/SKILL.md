---
name: account-brief-before-a-call
description: "Use when the user has a call or meeting with a company coming up, names an account they want to understand, or asks for a brief."
---

# Account brief before a call

Part of the Account Research Desk agent preset.

Inputs: the company name and site, who is on the call when they know, the account file when one exists, and anything they paste.

1. Read the account file first when there is one. Do not research from scratch what you already have.
2. Confirm the company and its root domain before you use anything from it. Same-name companies are common and a brief on the wrong one is worse than no brief.
3. Pull five things off the public web, each with a source URL and the date on the source: what the company does and who it sells to, size and stage signals such as headcount range, funding, and locations, what changed in the last 90 days, tech stack signals from job posts, engineering blogs, docs, status pages, and public integration pages, and who the people on the call are.
4. Fold in the user's own notes, kept labeled as theirs. Where a note and a public source disagree, show both and say which is newer.
5. Keep the brief to one screen. Longer than that and it does not get read before the call.

Output shape:
- The company in three lines: what they sell, who they sell to, and how big.
- What changed recently: three to five dated lines, each ending in a link.
- Who you are meeting: one line per person with title, tenure, and one thing worth knowing.
- Tech stack signals: what is visible and where you saw it, marked separately from what is a guess.
- Where you left off: last touch, open threads, and what they asked for.
- Three questions worth asking on this call, drawn from the lines above.

Fallbacks: a company with almost no public footprint gets a short brief that says so rather than padding. No attendee names means you brief the company and ask who is joining. No notes means the last section says first contact. Never invent a headcount, a funding number, a title, or a quote, and leave out any number you cannot source.

Save the brief into the account file and attach it here.
