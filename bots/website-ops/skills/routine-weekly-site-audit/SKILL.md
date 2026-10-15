---
name: routine-weekly-site-audit
description: "Scheduled routine: Disabled by default. Monday at 8am in the user's timezone. Re-audits the saved page list for SEO, links, speed, accessibility, CRO, and schema, diffs against the previous audit, and delivers only what is new, fixed, or regressed with a self contained report. Report only, quiet when nothing changed."
---

# Weekly site audit

Part of the Website Ops agent preset.

Schedule, as written by the template author: Disabled by default. Monday at 8am in the user's timezone. Re-audits the saved page list for SEO, links, speed, accessibility, CRO, and schema, diffs against the previous audit, and delivers only what is new, fixed, or regressed with a self contained report. Report only, quiet when nothing changed.

## What to do on each run

# Weekly site audit

This routine ships disabled. Confirm the timezone, the Monday 8am schedule, the page list, the
destination, and that nothing gets fixed or merged automatically before enabling.

When enabled:
1. Read /workspace/site-audit/state.md for REPO, SITE, BUILD, ACCOUNTS, the page list, and the
   last audit date. If SITE or the page list is missing, do nothing and say so once.
2. Run the site-audit skill over the saved page list. Read every signed-in platform first,
   measure what can be measured this run, and label everything else an observation. If a
   platform session has expired, note it under Could not read, ask once in this delivery for a
   fresh sign in, and carry on with the rest. Never retry a credential and never stall the run
   waiting for a sign in.
3. Diff against the previous audit under /workspace/site-audit/. Classify every finding as new,
   still open, fixed, or regressed.
4. If nothing is new, fixed, or regressed, say one line and stop. No report, no attachments, no
   suggestions invented to fill the space.
5. Otherwise build the report with html-report, verify it in the browser, and deliver it to the
   saved destination with the counts by severity, the diff, and the top 3 findings one line
   each. Report only.
6. Offer the top fix as a pull request the user can ask for. Do not open it here.
7. Never edit a file, open a pull request, merge, deploy, change DNS or hosting settings, or
   touch analytics or tag manager code on a schedule. A live session in a platform dashboard
   changes none of that.

Fires on:
- cron `0 8 * * 1`

Ask the importing user for:
- Timezone
