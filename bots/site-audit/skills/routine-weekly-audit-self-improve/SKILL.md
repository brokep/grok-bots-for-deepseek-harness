---
name: routine-weekly-audit-self-improve
description: "Scheduled routine: Weekly audit self-improve"
---

# Weekly audit self-improve

Part of the Site Audit agent preset.

Schedule, as written by the template author: Weekly audit self-improve

## What to do on each run

Weekly quiet self-improvement for Site Audit only. Stay inside this bot's job (one-site SEO, content, speed, a11y, CRO, schema audits and how they are reported). Never expand into other bots' jobs (growth posting, inboxes, prices, invoices, VM admin).

Read /workspace/site-audit/SETUP.md, /workspace/site-audit/IMPROVEMENTS.md, and any recent files under reports/ if they exist.

Do ONE concrete improvement to how you audit or report (a checklist note, evidence convention, scoring rubric line, crawl-scope reminder, or a gap you hit on a real audit). Append a short dated entry to /workspace/site-audit/IMPROVEMENTS.md. Do not invent a site or lab metrics. Do not run a full audit on this wake unless SETUP already has a site_url and you are only tightening process docs.

Stay silent after logging the improvement unless a human decision is required (for example still no site_url after setup, or a broken monthly routine). No filler "all good" ping.

Fires on:
- cron `0 9 * * 1`

Ask the importing user for:
- Timezone
