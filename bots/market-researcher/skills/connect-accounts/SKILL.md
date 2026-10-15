---
name: connect-accounts
description: "Use this when a platform account is needed and not yet signed in, when a session has expired, or when the user adds a platform. Runs the platform widget, the sign-in handoff in the bot's own browser, the verification screenshot, the ACCOUNTS entry, and the export fallback."
---

# connect-accounts

Part of the Market Researcher agent preset.

# Connect accounts

Exports and pastes still work. They are the fallback. The primary path is that
the user signs in to their own platform accounts inside my browser, and I read
the platform's web UI from then on.

## The widget
Multi-select, allowCustom, shown once in Beat 2 of setup and again whenever the
user adds a platform:

- Google Ads
- Meta Ads
- LinkedIn Ads
- Google Analytics 4
- Google Search Console
- None of these, I will drop exports

Pre-check every platform whose tag was found on the user's own site in Beat 1
(Google tag and Ads conversion id, Meta pixel, LinkedIn insight tag, GA4
measurement id, Search Console verification tag). If they run a network that is
not on the list, they add it and it is handled the same way. Nothing here is
required. The bot's surfaces are public pages and it delivers a full weekly
brief, messaging matrix, and strategy read with no platform signed in at all.

## What each platform adds
- **Google Ads**: auction insights names the competitors actually bidding
  against the user, with impression share, overlap rate, position above rate,
  and top of page rate. No public source carries any of it. Search terms and the
  keyword planner show the demand side.
- **Meta Ads**: Ads Manager gives the user's own delivery and cost context, the
  only honest scale reference for what the public library shows.
- **LinkedIn Ads**: Campaign Manager gives the user's own delivery and the
  audience the competitor set is also buying.
- **Google Analytics 4**: traffic by channel, landing page performance, and
  conversions for the user's own site. This is what a competitor's move gets
  measured against.
- **Google Search Console**: queries, clicks, impressions, and average position
  for the user's own domain. A competitor rewriting a title matters only if the
  user's queries move, and this says whether they did.

## The sign-in handoff
One pass, all checked platforms in sequence, one message each:

> I opened <platform> in my browser. Take control and sign in, including any
> 2FA. I never see or store your password, and the session stays on my computer.

Wait for them. Do not narrate the wait. If they skip one, move to the next and
never ask again.

## Verify, then record
After each sign in:
1. Screenshot the account home with the account name visible.
2. Confirm read access by opening one real view: the campaign list in an ad
   platform, the reports home in GA4, the performance report in Search Console.
   Screenshot it.
3. Write an ACCOUNTS memory entry with only: platform, account name or id
   exactly as the UI shows it, sign-in date, access level (read or admin).
   Format: `ACCOUNT: <platform> | <account name or id> | signed in <date> |
   <read or admin>`.
4. Never put a password, a session token, a cookie value, a 2FA code, or a
   recovery code in memory, in a file, or in chat.

## Session expiry
A login wall, a consent screen, or an empty report where data existed last run
means the session lapsed. Say it in one line, reopen the platform, and ask for a
fresh sign in the same way. Never retry a credential, never reuse a code, never
guess at a login. If the user is not around, fall back to the export path for
that run and label the numbers accordingly.

## Export fallback
When a platform is not signed in and a job needs it, ask once for a sign in and
offer the export in the same message, then proceed with whatever is available.
Validate the export before using it, and name the missing column rather than
guessing:
- Google Ads: campaign, impressions, clicks, cost, conversions, date range. For
  auction insights: competitor domain, impression share, overlap rate.
- Meta Ads and LinkedIn Ads: campaign, impressions, clicks, spend, results,
  date range.
- GA4: date, channel or source, sessions, users, conversions.
- Search Console: query, clicks, impressions, average position, date range.
If a required column is missing, say which one and ask for the export again.

## Labeling, every time
Every number in every artifact says where it came from: "live UI, <platform>,
<date>" or "export, <filename>, <date range>". Never blend a live number and an
exported number into one figure without saying so. Screenshots of the UI view
used are the evidence, per capture-and-report.

## Never
- Never type a password the user pasted into chat. Tell them to type it in the
  browser instead, and tell them to rotate that password because it is now in a
  chat log.
- Never store a credential, token, cookie, or recovery code anywhere.
- Never change an account setting, a budget, a bid, a campaign, billing, users,
  or permissions. Read only, in every account, always.
- Never sign in to an account the user did not name.
- Never use a shared or service login to act as a person.
- Never sign in to anything belonging to a competitor. These are the user's own
  platforms only.
