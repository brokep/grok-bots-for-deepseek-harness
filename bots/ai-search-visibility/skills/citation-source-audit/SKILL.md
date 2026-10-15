---
name: citation-source-audit
description: "Use when the user asks why they are not showing up, or which sites and pages the answers are pulling from."
---

# Citation source audit

Part of the AI Search Visibility agent preset.

Inputs: the source links from the most recent capture.

1. Pull every source link the answers cited across the run and count how often each domain appears.
2. Sort the domains into four buckets: the user's own site, a rival's own site, a third-party list or review site, and everything else such as forums, news, docs, and video.
3. For the third-party sources, say plainly which ones the user is on, which ones list a rival and not them, and which ones take a public submission or listing request. That last group is the actionable one.
4. For their own site, name the exact pages that got cited and the ones that never did. A page a buyer would expect to be cited that never is usually means something is missing on the page, and you can often say what.
5. Write the fix list. Three to six items, each a named action on a named URL, ordered by how cheap it is against how often that source appears. Getting added to a list that shows up in nine answers beats rewriting a page that shows up in one.
6. Flag a paid placement, a private community, or a site with no public submission path as out of reach. Do not put it on the fix list.
7. Offer to draft the top item through Draft the fix.

Output: the domain count table, the four buckets, the fix list, and the flagged items.

Fallbacks: a run with no source links at all means the surfaces you reached do not publish sources, so say that and audit the plain search results instead. Never infer a citation you did not see.

Save the audit dated under the visibility folder.
