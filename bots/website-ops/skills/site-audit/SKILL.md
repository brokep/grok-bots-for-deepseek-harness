---
name: site-audit
description: "Use when the user asks for a site audit, when the weekly routine fires, or before proposing fixes. Audits SEO titles and metas, headings, broken links, Core Web Vitals, accessibility, CRO heuristics, and schema, reading signed-in search and analytics platforms first, and returns every finding with a page, a screenshot, a severity, and a proposed fix."
---

# site-audit

Part of the Website Ops agent preset.

# Site audit

Evidence or it did not happen. Every finding names a page, shows a screenshot, carries a
severity, and proposes a fix the user could hand to anyone.

## Inputs
REPO, SITE, BUILD, and the page list from /workspace/site-audit/state.md. The production URL
the user gave. Never invent a site URL, and never audit a URL the user did not name or that is
not linked from one they named. Artifacts go under /workspace/site-audit/<date>/.

If the site cannot be reached, stop and say so in one line rather than auditing the repo source
as a substitute. Source reading supplements a live audit, it does not replace one.

## Sources, live interface first
Read ACCOUNTS from the state file before the first lane. For every platform signed in, the live
interface is the first source and an export is the second. Order for each kind of number:
1. The platform's own interface in my browser, with the view and the date range visible in a
   screenshot per evidence-media.
2. A CSV export the user provides, columns validated per connect-accounts, labeled with the
   export date.
3. Nothing. Write "not available this run" and move on. Never model, estimate, or carry a
   number forward from an earlier run without its original date.

What each platform contributes:
- **Search platform**: the real queries and the pages that actually earn impressions, position
  and CTR per page, indexing and coverage errors, and field Core Web Vitals grouped by URL.
  This decides which pages are worth auditing and which findings matter.
- **Analytics platform**: sessions, landing pages, engagement, and conversions. This ranks
  findings by traffic at stake and grounds the CRO lane.
- **Tag platform**: what is actually firing, and what is stale. Read only, and a finding here
  is reported, never fixed.
- **Hosting dashboard**: deploy previews, build logs, and the redirect and header rules as the
  host applied them, which is the truth when the repo config and the live response disagree.
- **CMS**: where the words on a page actually live, when they are not in the repo.

If a platform is not signed in when a lane needs it: ask once for a sign in on my computer,
offer the export path in the same message, then run the lane with whatever is available and say
plainly what is missing. Never block the audit on a sign in.

## Lanes, in this order
1. **SEO, titles and metas.** Per page: title text and length, meta description text and
   length, canonical, robots directives, Open Graph and card tags, language attribute,
   duplicate titles across pages. Flag missing, duplicated, truncated, or templated defaults.
   When the search platform is signed in, read the queries and the average position for each
   audited page first and say what each page is actually found for. A title that ignores the
   query a page already ranks for is a finding with a number behind it. Read the indexing and
   coverage report too: a page excluded, crawled but not indexed, or blocked is a P0.
2. **Headings and structure.** One h1 per page, no skipped levels, headings that describe the
   section rather than styling. Flag empty headings and headings used for layout.
3. **Broken links and redirects.** Crawl every internal link on the page list plus the links
   in the sitemap. Record status codes. Flag 404s, redirect chains longer than one hop, mixed
   content, and links to pages excluded by robots. Check external links once and mark them
   external so a flaky third party is not reported as a site defect.
4. **Core Web Vitals and speed.** Measured only, and field data outranks lab data. When the
   search platform is signed in, read its Core Web Vitals report first: that is real user data
   for real URLs, grouped as good, needs improvement, or poor, with the URL group and the
   sample period. Screenshot the report. Then run a lab check for the diagnosis, Lighthouse
   locally when it is installed or installable inside the time box, otherwise the public
   PageSpeed Insights API, mobile first then desktop. Record LCP, CLS, INP or TBT, the score,
   the strategy, and the run timestamp. Label every number field or lab. If neither the field
   report nor a lab run is available, write "not measured this run" and move on. Never estimate
   a score, never carry a number forward without its date, and never present a lab score as
   what users experience.
5. **Accessibility.** Run axe or pa11y against each page. Record rule id, impact, the selector,
   and the element text. Then check by hand what tools miss: keyboard order through the primary
   navigation and any form, visible focus, alt text that describes the image, form labels, and
   contrast on the primary call to action. Screenshot the failing element.
6. **CRO heuristics.** Per page: is the primary action visible without scrolling at 1280 and at
   390, is there exactly one primary action, does the headline say what the product does, is
   proof near the ask, how many fields the form has, what the empty and error states look like,
   does the mobile layout bury the action under a fold or a sticky bar. Each observation is
   labeled an observation, never a measured result. When the analytics platform is signed in,
   put the measured numbers beside the observations: sessions, engagement, and conversions for
   that landing page, and the desktop and mobile split. A heuristic on a page with traffic
   outranks the same heuristic on a page with none, and that ordering is what the report shows.
   When the tag platform is signed in, check that the conversion events the page depends on are
   actually firing, and report a broken or stale tag as a finding rather than fixing it.
7. **Schema.org.** Extract JSON-LD, microdata, and RDFa. Validate shape and required properties
   per type. Flag invalid types, missing required properties, and structured data that claims
   something the page does not show.

## Severity
- **P0**: the page is broken, unreachable, unindexable, or unusable for someone on a keyboard or
  a screen reader. Also a schema claim that is not true on the page.
- **P1**: a real loss that is not a break. Missing or duplicate title or description, a heading
  order that breaks navigation, a redirect chain, a failing vital, a buried primary action.
- **P2**: worth fixing when nearby. Wording, minor contrast, a missing optional property.

## Finding shape (every finding, no exceptions)
- Page URL and the date read.
- What is wrong, in one sentence, with the measured value or the exact element.
- Evidence: the screenshot path, plus the raw tool output line when a tool produced it.
- Source of every number in it: live UI with the view and the date range, export with the
  export date, or a named tool with its run timestamp.
- Severity and the reason it is that severity. Traffic or impressions at stake, when a platform
  supplied them, is part of that reason.
- Proposed fix: the file and the change, concrete enough to become a pull request. Add the
  effort in one word: trivial, small, or needs a decision.

## Measured and observed stay apart
The report has two columns of truth. Measured means a tool ran or a platform interface returned
the value, with the tool or platform, the view, the date range or strategy, and the timestamp.
Observed means I looked at the page and formed a judgement. CRO heuristics are always observed,
even when a measured traffic number sits beside them. Never present an observation with a
number attached, and never present a platform number without its date range.

## Diff against the previous audit
1. Read the most recent /workspace/site-audit/<date>/findings.json.
2. Classify each current finding as new, still open, fixed, or regressed.
3. Report new, fixed, and regressed first. Still open collapses to a count with a link to the
   full report. If nothing changed at all, say that in one line.

## Output
Write /workspace/site-audit/<date>/findings.json with one record per finding, then build the
report with html-report and verify it in the browser before delivering. In chat: counts by
severity, the diff line, and the top 3 findings one line each. Then offer to ship the top fix
with ship-a-change. Pages that would not load go in a Could not read footer with the status
code.

## Never
Fix anything here. This skill reads and reports. Invent a score, a vital, a query, a session
count, or a crawl result. Audit a domain or a property the user did not name. Change a setting,
a filter, a date range default, a tag, or a redirect rule inside a platform dashboard. Report
an external site's outage as a finding on this site. Run a crawl that hits a page more than
once per second.
