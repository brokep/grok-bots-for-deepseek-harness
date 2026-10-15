---
name: connect-accounts
description: "Use this when a platform account is needed and not yet signed in, when a session has expired, or when the user adds a platform. Holds the platform widget, the sign-in handoff wording, the verification screenshot, the ACCOUNTS entry format, and the export fallback."
---

# connect-accounts

Part of the Performance Marketer agent preset.

# Connect accounts

Use this when a platform account is needed and not yet signed in, when a session has expired, or
when the user adds a platform. The user signs in inside my browser. I work the interface from
then on. I never hold a credential.

## The widget
One multi-select, pre-checked from evidence, never from a guess. Evidence is an ad tag found on
the user's site (the Google tag or Google Ads conversion linker, the Meta pixel, the LinkedIn
insight tag, the Microsoft UET tag, the TikTok pixel) or a platform named in the copy source or by
the user.

- Google Ads
- Meta Ads
- LinkedIn Ads
- Microsoft Ads
- TikTok Ads
- None of these, I will drop exports

Say why each box is pre-checked, naming the tag or the line that pre-checked it. Google Analytics
4 and Search Console are not on this widget, because the messaging read is click-through rate from
the ad platform itself. Offer them as an extra sign in only when the user asks for a conversion or
landing page read, and use the same handoff wording.

## The sign-in handoff
One pass, every checked platform in sequence, one message each:

> I opened <platform> in my browser. Take control and sign in, including any 2FA. I never see or
> store your password, and the session stays on my computer.

Then stop and wait. Do not narrate, do not scroll, do not click while they are typing. If the user
declines a platform, skip it for good and never re-prompt. If they paste a password into chat,
do not use it: tell them to type it into the browser instead, and tell them to rotate that
password, because it is now in a chat log.

## Verify, then record
1. Screenshot the account home with the account name visible. Crop out anything else.
2. Confirm read access by opening one campaign list or one report. A sign-in that lands on a
   permissions error is not a connected account, say so and ask who can grant access.
3. Note the access level from what the interface offers: read if the account is view only, admin
   if create and edit are available. Do not test the level by trying to change something.
4. Write or update the ACCOUNTS entry in /workspace/ads/state.md, one line per platform:

   `<platform> | <account name or id exactly as the UI shows it> | signed in <YYYY-MM-DD> | access: read or admin`

   Nothing else goes in that entry. Never a password, never a session token, never a cookie value,
   never a 2FA code, never a recovery address, in memory or in any file I write.

## Session expiry
A session dies quietly and the symptom is a login wall where a report should be.
1. Detect it: a login or account-chooser screen, a 2FA prompt, or a redirect away from the page I
   asked for. Screenshot the wall, cropped so no entered email is visible.
2. Say it plainly in that turn: "<platform> logged me out, so I cannot read it right now."
3. Ask once for a fresh sign in with the same handoff wording, and offer the export path in the
   same message.
4. Never retry a credential, never reuse anything from a previous session, never try another
   account to get around the wall. One ask, then move on with what is available.
5. Update the ACCOUNTS line with the new sign-in date once they are back in.

## Export fallback
Every job still works without a session, slower and with a date on it.
- Reading numbers: the user exports a report from the platform and pastes it or drops the file.
  Validate the columns the reading skill needs before using it, and state the export date on every
  number that came from it.
- Building: an editor or bulk import file per build-shells, which the user imports themselves.
- Always say which numbers came from a live interface and which came from an export, in the same
  line as the number.

## When a job needs a platform that is not connected
Ask once for a sign in on my computer, offer the export path in the same message, then proceed
with whatever is available and name the gap. Do not stall the whole job on one missing platform.

## Never
- Type a password the user pasted in chat. Tell them to type it in the browser and to rotate it.
- Store or write down a credential, a session token, a cookie value, or a 2FA code.
- Change account settings, billing, users, or permissions, on any platform, for any reason.
- Sign in to an account the user did not name, or switch accounts inside a platform without
  asking.
- Use a shared login to act as a person, or post, comment, or message as the account holder.
- Treat being signed in as permission to enable, spend, or publish anything.
