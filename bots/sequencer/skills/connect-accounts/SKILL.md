---
name: connect-accounts
description: "Use this when a platform account is needed and not yet signed in, when a session has expired, or when the user adds a platform. Holds the sign-in handoff, the verification screenshot, the ACCOUNTS entry format, and the export fallback."
---

# connect-accounts

Part of the Sequencer agent preset.

# Connect accounts

Use this when a platform account is needed and not yet signed in, when a session has expired, or
when the user adds a platform. The user signs in inside my browser. I work the interface from then
on. I never hold a credential.

## The widget

One multi-select, folded into the Beat 1 stack question, pre-checked from evidence and never from a
guess. Evidence is a provider visible in their mail signature, a tool named on their site, or a tool
they told me about.

- A CRM with no connector on this bot
- A prospecting or enrichment console
- A sales navigator or professional network seat
- A messaging platform they use for outbound
- An analytics or reporting tool they want numbers from
- None of these, I will paste and drop exports

Say in one clause why each box is pre-checked. Never pre-check a platform because the recipe was
built on it.

## The sign-in handoff

One pass, every checked platform in sequence, one message each:

> I opened <platform> in my browser. Take control and sign in, including any 2FA. I never see or
> store your password, and the session stays on my computer.

Then stop and wait. Do not narrate, scroll, or click while they are typing. If they decline a
platform, skip it for good and never re-prompt. If they paste a password into chat, do not use it:
tell them to type it into the browser instead, and tell them to rotate it, because it is now in a
chat log.

## Verify, then record

1. Screenshot the account home with the account name visible. Crop out everything else.
2. Confirm read access by opening one list or one report. A sign-in that lands on a permissions
   error is not a connected account. Say so and ask who can grant access.
3. Note the access level from what the interface offers: read if it is view only, admin if create
   and edit are available. Do not test the level by trying to change something.
4. Write or update the ACCOUNTS section in `/workspace/sequencer/state.md`, one line per platform:

   `<platform> | <account name or id exactly as the interface shows it> | signed in <YYYY-MM-DD> | access: read or admin`

   Nothing else goes in that section. Never a password, never a session token, never a cookie
   value, never a 2FA code, never a recovery address, in memory or in any file I write.

## Session expiry

1. Detect it: a login screen, an account chooser, a 2FA prompt, or a redirect away from the page I
   asked for. Screenshot the wall, cropped so no entered address is visible.
2. Say it plainly that turn: <platform> logged me out, so I cannot read it right now.
3. Ask once for a fresh sign in with the same wording, and offer the export path in the same
   message.
4. Never retry a credential, never reuse anything from a previous session, never try another
   account to get around the wall.
5. Update the ACCOUNTS line with the new sign-in date once they are back in.

## Export fallback

Every job still works without a session, slower and with a date on it. The user exports a list or a
report and drops the file. Validate the columns the reading skill needs before using it, and say on
every number whether it came from a live interface or from an export, in the same line as the
number.

## When a job needs a platform that is not signed in

Ask once for a sign in on my computer, offer the export path in the same message, then proceed with
whatever is available and name the gap. Never stall the whole run on one missing platform.

## Never

- Type a password the user pasted in chat. Tell them to type it in the browser and rotate it.
- Store or write down a credential, a session token, a cookie value, or a 2FA code.
- Change account settings, billing, users, or permissions, on any platform, for any reason.
- Send, post, connect, or message as the account holder from a signed-in session. Sequencer drafts,
  the user sends, and that does not change because a session is open.
- Sign in to an account the user did not name, or switch accounts without asking.
- Treat being signed in as permission to act.
