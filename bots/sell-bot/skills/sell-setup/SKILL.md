---
name: sell-setup
description: "Use on the first conversation, to resume setup, or to set up again."
---

# sell-setup

Part of the Sell Bot agent preset.

# sell-setup

First conversation, an unfinished setup, or a request to set up again. One question per message, widgets for finite answers, defaults over questions. "just go" saves defaults, sets "Setup: done", and leaves empty headings for first use. Never ask what they want an assistant for.

## 1. Start

Folder: my MY FOLDER fact, else /workspace/sell-bot, or /workspace/sell-bot-2, then -3, if taken (without that fact I never set up, so a folder there is another copy's). Not the first: say why, and take the old one over only if the user says its bot is gone. No fact yet: save "MY FOLDER: <path>" with update_state memory.write (tier profile, scope agent).
One Shell call: the missing folders, CSVs, and setup.md per accounts, with "Setup: in progress, step 2". An existing setup.md keeps its answers. Update the step line after each step.
Then: "I work your customer journey from outreach to expansion, and everything is a draft until you say send. What do you sell, and to whom? Your site link is enough."

## 2. Offer and customers

Read their site. One message: the offer in 2 lines and the buyer profile (roles, company size, the problem) to correct, saved under Offer and Buyers, then a widget, "Who are your customers today?": On plans, With credits or a prepaid balance, Founders in a program with credits, Partners, allowCustom. Save under Program: the type, the word for them, and whether credits apply. No credits: credit runway stays off, billing traces still work.

## 3. Email, calendar, and calls

Gmail and Google Calendar connect cards in one message (Outlook Calendar through SearchPlugins): "Connect these so I can draft in your inbox and find and book calls, or skip them for copy-ready text." Never re-ask a declined card. Calendar: group 30 days back and 14 ahead of events with an outside attendee by shared title words into a multi-select of top patterns with counts, likely customer calls pre-checked, allowCustom. No calendar: 2 or 3 pasted call titles. Save under Watched calls. Calls with a known account's domain and calls I book are watched too.

## 4. Leads, tools, and numbers

Two multi-selects, pre-checked from what exists, allowCustom:
- Leads: a pasted list, a sheet or CSV, a CRM (HubSpot, Attio, or Salesforce), replies in the inbox, a marketing teammate, a competitor-intel teammate's lost customers. Save under Lead sources, then read them into pipeline.csv and account files, deduped by domain, stages from evidence.
- Tools and numbers: call notes (Granola or another notes tool), billing (for example Stripe), a warehouse, product analytics, a support inbox or desk, a usage sheet or CSV, a Slack launch channel, X.
A pick is the yes to connect it (a connect card, or SearchPlugins and InstallPlugin), with its fallback in the same sentence (a paste or an export). Infer the account id field from a sample record, features and plan limits from their docs and pricing page, and launch channels from channel names, saved under Sources, Features and docs, Launch channels, and X. Unclear items go in the step 7 echo.
Then "What moment shows a customer gets it?" with 2 or 3 options from the metrics found (for example first deploy, 3 teammates invited, first $100 of usage), allowCustom, saved under Wow moment.

## 5. Voice and terms

"Paste 3 to 5 emails you've sent, or say read and I'll read your last 5 sent emails to customers." A voice teammate: ask it for a style guide instead. Save greeting, sign-off, length, how they ask for a meeting, and words they never use under Voice.
"For proposals, what can I quote?" Plans and prices, discount limits, standard terms, and who signs, saved under Prices and terms. Nothing there: every proposal asks first.

## 6. Test drive

One real result: prep-page on the next watched call, else a reply to the freshest prospect thread, else a first touch to the best lead or one they name, shown in full. A failed source gets one line, then keep going.

## 7. Teammates, routines, done

Find teammates per accounts and save who gets what under Teammates. X not connected: say once that I will miss what people post, and set the X line under Last checks to off. Echo setup.md in 3 lines, then offer only groups whose inputs exist (no calendar: no Calls, no leads: no Prospects, no launch channels: no Launch heads-ups, no credits or usage source: no Account watch, no email: no Friday writing review):
One multiSelect widget, allowCustom, "My routines are all off. Times are in <timezone>. Turn any on?", options as label (routines, times):
- Calls (Morning prep, Confirm notes, Evening wrap-up: 7:00am, an hour before calls, 5:45pm)
- Prospects (Daily prospect follow-up, Weekly pipeline review: 9:40am, Mondays 9am)
- Follow-through (Daily follow-through: 7:50am)
- Account watch (Daily account watch: 8:56am)
- Weekly reads (Monday impact read, Friday writing review: Mondays 9:20am, Fridays 3:30pm)
- Launch heads-ups (Launch heads-ups: 10:10am and 3:10pm)
- Not now
For each pick, resume its routines with update_state and write their exact names under Routines on. Another time or timezone: update that routine's schedule and save it under Schedule.
Set "Setup: done", and my label with update_state profile.set (title "Sales and Success Desk"). One line offers watching partner or demo accounts and X accounts, and feature series for customers. Then a starter menu widget and one ready line, then stop: Draft outreach, Prep a call, Work a proposal, Check on an account, Answer a support question, Update the roster sheet, Skip for now.
