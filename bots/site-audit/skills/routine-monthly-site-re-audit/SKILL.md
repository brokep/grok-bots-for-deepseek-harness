---
name: routine-monthly-site-re-audit
description: "Scheduled routine: Monthly re-audit of the one primary site"
---

# Monthly site re-audit

Part of the Site Audit agent preset.

Schedule, as written by the template author: Monthly re-audit of the one primary site

## What to do on each run

Monthly re-audit of the one primary site. User local time is already on this schedule (10:00 on the 1st).

Setup gate first: read /workspace/site-audit/SETUP.md (also accept /workspace/full-site-audit/SETUP.md). If setup_complete is not true or site_url is empty, do not invent a site and do not fake Lighthouse/PSI/lab numbers. Stay quiet if still waiting on a URL.

If site_url is set: re-run the same crawl_scope (homepage, nav-linked top pages, one example of each public template; cap about 30 pages unless SETUP says otherwise). Gentle crawl. Public pages only. Cover all six dimensions: SEO technical, content, speed, accessibility, CRO, schema/structured data. If you cannot measure something, mark it unmeasured and say why.

Compare to baseline/ and the last reports/. Write reports/YYYY-MM-DD.md, reports/YYYY-MM-DD-diff.md, and copy the full report to reports/latest.md. Diff sections: fixed / still open / new / regressions. Do not claim a fix without evidence. Update baseline/ snapshots (titles, small HTML hashes or saved copies of critical pages — keep them small). Put screenshots and tool links under evidence/YYYY-MM-DD/.

Chat the diff even if there is no material change (monthly always reports). Attach the report if you can. Never invent metrics, traffic, rankings, or conversion rates. Do not change the live site. Do not expand into other bots' jobs.

Fires on:
- cron `0 10 1 * *`

Ask the importing user for:
- Timezone
