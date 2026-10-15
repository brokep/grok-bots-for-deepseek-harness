---
name: connect-accounts
description: "Use when a platform account is needed and not yet signed in, when a session has expired, or when the user adds a platform. Runs the platforms widget, hands the browser over for sign in, verifies read access with a screenshot, and records platform, account, date, and access level. Never stores a credential."
---

# connect-accounts

Part of the Website Ops agent preset.

# Connect accounts

Platform data comes from the platform's own web interface, signed in by the user inside my
browser. Exports are the fallback, not the default. No connector exists for any of these
platforms, so this is the primary path.

## When to use
First run, at the second half of Beat 2. Any time a job needs a platform that is not signed in.
Any time a session has expired. Any time the user adds or removes a platform.

## The widget (one, multi-select, allowCustom)
Pre-check from evidence, never from a guess:
- **Google Search Console**: the site has a verification tag, or the domain is live and indexed.
  Gives real queries, the pages that actually get impressions, indexing and coverage errors,
  and field Core Web Vitals.
- **Google Analytics 4**: an analytics snippet or measurement id is in the page source. Gives
  sessions, landing pages, engagement, and conversions.
- **Google Tag Manager**: a container id is in the page source. Read only, to see what is
  firing and what is stale.
- **The hosting dashboard** (Vercel, Netlify, Cloudflare Pages, or other): a host config file
  is in the repo, or the deploy checks on a pull request name the host. Gives deploy previews,
  build logs, and redirect and header rules as the host actually applied them.
- **The CMS**: a CMS client is in the package manifest, or page copy is not in the repo. Shows
  where the words the user wants changed actually live.
- **None of these, I will drop exports.**

Do not invent a platform. If the evidence is ambiguous, leave it unchecked and let the user
check it.

## The sign-in handoff (one pass, all checked platforms in sequence)
For each checked platform, in one message:

> I opened <platform> in my browser. Take control and sign in, including any 2FA. I never see
> or store your password, and the session stays on my computer.

Wait for the user to hand control back. Do not narrate the login page, do not read the form, do
not offer to type anything. If a platform is declined or skipped, say so once, use the export
path for it, and never re-prompt.

## Verify and record
1. Screenshot the account home with the account name or property name visible.
2. Prove read access by opening one real view: the performance report, the property overview,
   the container list, the deployments list, or the content list. Screenshot it.
3. Note the access level as the interface shows it, read or admin. Never change it.
4. Write or update the ACCOUNTS section in /workspace/site-audit/state.md, one line per
   platform:

   `<platform> | <account or property name as shown> | signed in <YYYY-MM-DD> | <read or admin>`

   Keep it under 480 characters. Nothing else about the account goes in the state file. Never
   a password, a session token, a cookie value, a recovery code, or a URL containing a token.

## Session expiry
A login wall, a consent screen, or a redirect to an account chooser means the session is gone.
When that happens: say which platform in one line, ask once for a fresh sign in the same way,
offer the export path in the same message, and continue with whatever else is available. Never
retry a credential, never reuse a saved form value, and never treat an expired session as a
platform outage.

## Export fallback (per platform)
Ask for a CSV in Drive or a paste, then validate the columns before using a single number.
- Search data: query or page, clicks, impressions, CTR, position, and the date range.
- Analytics data: landing page or page path, sessions or users, engagement, conversions, and
  the date range.
- Host data: deployment id, branch, state, and the preview URL.
If a required column is missing, say which one, use the file for nothing else, and ask for a
re-export rather than inferring the column from its neighbors. Every number from an export
carries the export date and the label export.

## Labeling, always
Every number I report says where it came from: live UI with the view and the date range, or
export with the export date. A number with no source does not get reported.

## Never
Type a password the user pasted in chat. If they paste one, tell them to type it in the browser
instead and to rotate that password. Store a credential, a token, or a cookie in memory, in a
file, or in a screenshot. Change account settings, billing, users, permissions, sharing, or a
property configuration. Publish a tag, a container version, or a redirect rule from a dashboard.
Deploy, promote, roll back, or change DNS from the hosting dashboard, signed in or not. Sign in
to an account the user did not name. Use a shared login to act as a person. Screenshot another
property's data that happens to be on the same screen.
