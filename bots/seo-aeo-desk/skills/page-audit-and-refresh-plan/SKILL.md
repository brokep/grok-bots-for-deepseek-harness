---
name: page-audit-and-refresh-plan
description: "Use when a page is slipping, a new page is about to go live, or the user asks why a URL is not ranking."
---

# Page audit and refresh plan

Part of the SEO & AEO Desk agent preset.

Inputs: the URL or a list of them, the query the page is supposed to win, and Search Console data for that page when it exists.

1. Fetch the page. Note the title, meta description, H1, heading structure, length, publish and update dates, schema, canonical, and whether the main answer sits above the fold.
2. Check intent match first. Read the top results for the target query and say plainly whether this page is even the right shape. A tutorial does not win a comparison query.
3. Check the mechanics: indexable, canonical pointing at itself, one H1, headings in order, images with alt text, internal links coming in from relevant pages, and load time from a real fetch.
4. Check the answer quality. Does the page answer the main question in one liftable paragraph, are the claims sourced, is anything out of date.
5. Write the fixes in priority order, each with the reason and the effort, split into rewrite, add, and delete.
6. With Search Console data, add what the page actually ranks for today against what it was aimed at. That gap is usually the real problem.

Output: the findings and the ordered fix list in chat, saved dated. Offer a refresh brief when the fix is a rewrite rather than a tweak.

Fallbacks: a page you cannot fetch gets named, not guessed at. A page behind a login is out of scope. Never change a live page, a CMS entry, or a robots file yourself. Hand over the fixes and let them apply them.

Save audits under the search content folder.
