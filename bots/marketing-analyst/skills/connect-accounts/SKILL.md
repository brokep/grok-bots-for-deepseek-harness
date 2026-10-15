---
name: connect-accounts
description: "Use when a platform account is needed and not yet signed in, when a session has expired, or when the user adds a platform. Holds the platform widget, the sign-in handoff wording, the verification screenshot, the ACCOUNTS entry format, and the export fallback. The user signs in, the bot never holds a credential."
---

# connect-accounts

Part of the Marketing Analyst agent preset.

# Connect accounts

The platforms have no connector here, so the user signs in to each one inside my browser and I
read the reporting views the same way a person would. Their password never touches me.

## When to use
At setup Beat 2, when a job needs a platform that is not signed in, when a session has expired,
and when the user adds a platform.

## The platform widget
Multi-select, allowCustom, pre-checked from evidence rather than from a blank question. Evidence
is the advertising and analytics tags found on the user's own site, plus any platform they named.

Options: Google Ads, Meta Ads, LinkedIn Ads, Microsoft Ads, TikTok Ads, Google Analytics 4,
Google Search Console, and "None of these, I will drop exports".

Tag to platform: a Google Ads conversion tag or a Google tag with an AW identifier means Google
Ads. A G identifier means Google Analytics 4. A Meta pixel means Meta Ads. A LinkedIn insight tag
means LinkedIn Ads. A Microsoft UET tag means Microsoft Ads. A TikTok pixel means TikTok Ads. A
Search Console verification meta tag means Search Console. Say which tag pre-checked which box in
one line each, so the user can see why.

## The sign-in pass (one pass, all platforms in sequence)
For each checked platform, in one message:

> I opened <platform> in my browser. Take control and sign in, including any 2FA. I never see or
> store your password, and the session stays on my computer.

Wait for them. Do not narrate the page while they are typing. If they decline a platform, say so
once, note it as export only, and never re-prompt.

## Verify, then record
1. Screenshot the account home with the account name visible.
2. Confirm read access by opening one real view: the campaign list for an ad platform, a standard
   report for an analytics platform. Screenshot that too.
3. Note whether the access is read or admin as the UI shows it. Admin access does not change what
   I do, it only tells the user what I could touch and will not.
4. Write the ACCOUNTS memory entry, one line per platform:

   `<platform> | <account name or id as shown in the UI> | signed in <YYYY-MM-DD> | <read or
   admin>`

   Keep the same lines in /workspace/analytics/accounts.md with the screenshot paths. Nothing
   else about the account goes in memory, and no credential, session token, or cookie value goes
   anywhere at all.
5. Report the pass in one line per platform: platform, account name, what view confirmed it.

## Session expiry
A login wall, a consent screen, or a redirect to a sign-in page where a report should be is an
expired session, not a failure of the job. Stop reading that platform, say which one and what I
saw, ask once for a fresh sign in, and offer the export path in the same message. Never retry a
credential, never attempt a password reset, never click through a 2FA prompt on the user's
behalf. Mark the platform stale in accounts.md with the date and carry on with what is available.

## Export fallback
Any platform that is not signed in falls back to an export: a CSV or a sheet in the location the
user named, or a paste. Run ingest-exports for those. A report may be half live and half export,
and every number says which it is, with its date.

## Never
Type a password the user pasted into chat. Tell them to type it in the browser instead, and tell
them once to rotate any password they have already pasted anywhere. Store a password, a session
token, a cookie value, a recovery code, or a 2FA seed. Change an account setting, a budget, a
bid, a campaign, billing, a user, or a permission. Sign in to an account the user did not name.
Use a shared login to act as a person, or post, comment, or message from inside a platform.
Screenshot a page showing a password field with characters in it, an account id the user asked
to keep private, or another person's personal data.
