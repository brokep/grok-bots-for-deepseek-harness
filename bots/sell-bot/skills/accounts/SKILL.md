---
name: accounts
description: "Use for setup.md, ledgers, account files, stages, number sources, and teammates."
---

# accounts

Part of the Sell Bot agent preset.

# accounts

Files, stages, number sources, and teammates. Read-only toward number sources.

## Files in my folder

- setup.md: "Setup: in progress, step N" or "Setup: done" on top, then these headings: Offer, Buyers, Program, Voice, Prices and terms, Calendar (30-minute calls and buffer), Lead sources, Follow-ups, Watched calls, Sources, Features and docs, Wow moment, Incentives, Credit options (a call to plan usage), Thresholds (runway 14 days, check-in change 20%, expansion at 80% of a plan limit for 2 weeks), Roster sheet, Launch channels, X, Watched accounts, Site walk, Teammates, Schedule, Routines on, Last checks (a timed line per check).
- pipeline.csv: slug,company,domain,stage,source,next_step,next_touch,touches,updated (a row per open deal, new or expansion)
- accounts/<slug>.md: stage, contacts with roles and X handles, site, account ids per source, why we reached out, a dated touch log (channel, what happened, draft or event id, thread id, link), promises, deal and contract notes, wow moment and expansion flagged dates, learnings, tried and not tried, open asks, last numbers.
- calls.csv: date,start,account,event_id,source,prep,confirm,wrap,checkin (source: pattern, account, or booked)
- requests.csv: date,account,kind,ask,status,sent_to,notified (feature or bug, open, shipped, or closed)
- drafts.csv: date,account,type,draft_id,thread_id,subject,status (open, sent, edited, or deleted)
- series.csv: account,features,next_due,step,declines,status
- prep/ and proposals/ for pages.
Match people to an account by email domain, then name, but by full address for free email domains (gmail.com and the like). Accounts found through support or a number source start as customer, others as lead. From a call: ask once. A new customer without an account id: ask once. An outside call the user won't watch: its domain, or address, goes under Watched calls as ignored.
Helpers use only python3's standard library, curl, and jq. Anything else I install can vanish in a computer update, so check for it and reinstall before each use.

## Stages

lead (nothing sent), contacted (a first touch went out), replied (a no or an unsubscribe moves them to lost with the reason), call booked, proposal (a proposal or quote went out), contract (terms or redlines in play), customer (signed or paid, or a number source shows their account), lost (a no, or the user agrees after a "propose lost"), and expansion (a customer's open deal, the account stays customer). Each change needs dated evidence in the touch log. Conflicting signals: the earlier stage, with why. Next touch: 4 business days after the last in contacted, 2 in replied and proposal, or a promise's date. After the last follow-up with no reply, clear next_touch and list them as "propose lost" in the weekly review.

## Sources

- Connector (billing, analytics, warehouse, support desk): read tools only. SQL is SELECT only, bounded by date and account.
- Sheet or CSV: the latest file or tab and its date. Over 7 days old: ask for a fresh export.
- Dashboard with no connector: the user signs in on my browser once ("take control and sign in, I never see or store your password"). I read its text or a screenshot and never click anything that changes data.
- Nothing yet: name the missing numbers and keep going.

## Metrics

Per account: usage (the measure the user named), spend, credits or balance left with expiry, plan and its limits (billing source or pricing page), features used. Daily spend is 7 days of spend divided by 7. Runway days is balance divided by daily spend, none when spend is 0. Features not tried is the feature list minus those used in 30 days. Label each number "<value>, <source>, read <date>".

## Teammates

Optional, found in my teammates list by name or description. More than one: ask the user once which, and save it under Teammates. Messages carry the facts, never a path to my files, with priority false. Save replies where they belong.
- Bug triage: each bug or feature ask with the account, their words, the date, and steps for a bug. Fix messages come back.
- Competitor intel: a walk of a booked prospect's product from its own account, news on a competitor that came up, and lost customers as win-back leads (source winback, drafts wait for the user's go).
- Marketing: replied leads. Find the thread, set stage replied, and draft a reply, or ask for the thread.
- Voice: a style guide for Voice.
None: the work goes in my report to the user.

## Never

Invent a stage, a contact, a touch, or a number, or delete a touch log line.
