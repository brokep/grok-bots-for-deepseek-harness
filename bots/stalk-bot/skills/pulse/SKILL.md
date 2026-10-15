---
name: pulse
description: "Use for the scheduled pulse or when the user says \"run a pulse\". Runs every enabled module for every competitor, reads the dossiers, writes the delta report with Shipped, Hiring direction, Against-us, Website pros/cons, and For-our-site, with screenshots attached."
---

# pulse

Part of the Stalk Bot agent preset.

# Pulse

## Steps
1. Re-read the BASELINE memory entry and every competitor's dossier index. Also re-read the user's own latest site snapshot under `/workspace/dossiers/_us/` when present.
2. For each competitor, run the enabled modules: snapshot-site (website, pricing, changelog, positioning, open roles), read-the-mail (newsletter, sequence), watch-x (shipped timeline, positioning, complaints). X and open roles are on by default. Product walkthrough is not re-run in a pulse; the deep-dive routine handles that.
3. Collect every change with its evidence (link or screenshot path, date).
4. From each competitor's **current** public site (home + pricing + any compare/FAQ pages), extract a short **Website pros / cons** list, only what their own pages claim or show, with quotes and links. Pros = concrete advantages a buyer would see on their site (price, free path, feature named in hero, proof). Cons = gaps, cliffs, missing free AI, card walls, weak proof, confusing CTAs, still grounded in what the page shows or omits vs our baseline, never invented.
5. Write the report as a live brief, in this order:
   - Per competitor: product changes first (site, pricing, changelog, X shipped timeline, mail), then hiring changes, each vs the prior watermark. One line each, evidence attached.
   - **Media in the same turn**: attach the latest HTML report for each competitor with changes, the most recent onboarding video, up to 3 feature clips, and the key screenshots (home, pricing, every cited gate or post). Never describe media you did not attach.
   - **Shipped** (per competitor, from watch-x cross-referenced with the changelog): what they shipped or announced since last pulse, dated, in their words, with the post or changelog link and screenshot. Note X-only announcements and quiet ships. Ships per month beside changelog entries per month.
   - **Hiring direction** (per competitor, when roles changed): new and closed roles by function, then the 2 to 4 line direction read from hiring.md. Skip when no roles changed.
   - **Website pros / cons** (per competitor, or once on first-seen / when positioning or pricing pages changed): 2 to 4 pros, 2 to 4 cons. Each bullet = fact from their site + link/screenshot + date. No vibes.
   - **Against us**: each change (and each material pro/con) read against the baseline in one or two sentences. Where they moved toward our positioning, undercut a price, or shipped something we list as a strength.
   - **For our site** (actionable next steps for the user's own website): max 3 items. Each is a concrete web change or experiment tied to evidence from this pulse (e.g. "Add a mid-tier on /pricing between our entry and mid plans; Acme's comparable plan sits above it and their compare table calls out the gap"). Phrase as a decision the user can take on their marketing site, not generic strategy. Skip this section on a quiet pulse.
   - **Worth a decision**: max 3 yes/no questions (can overlap with For our site; prefer site-specific when the evidence is on-page).
   - **Proactive suggestions** (always on a substantive pulse, 2 to 5 bullets): counterpositioning the user can act on. Pattern: "<competitor> is hiring for X, look out for <what that implies>" or "<competitor> shipped Y, we can counterposition by <move>". Sources: hiring direction, shipped timeline, complaint themes, positioning drift. Each bullet cites an item above. When /workspace/dossiers/_us/in-flight.md exists, tag each suggestion with the in-flight item it supports or conflicts with. Suggestions, not marketing copy.
   - **Competitor churn close** (only when the churn module is on and a case exists): one line per case from competitor-churn, with the brief path and the winback status. Skip the header otherwise.
   - **Could not read**: any source that failed this pulse, one line each.
6. If no competitor had any change and no churn case: one line, "Quiet pulse, nothing changed across N competitors since <date>." Nothing else. Do not invent pros/cons, For-our-site items, or proactive suggestions on a quiet pulse.
7. Update `/workspace/dossiers/<competitor>/index.md` with the pulse date and change count. Optionally refresh `/workspace/dossiers/<competitor>/site-pros-cons.md` when the pros/cons list changed.
8. Attach evidence per the evidence-media skill: before/after screenshots for each change, the cited page for each pro or con, the post for each shipped item, the careers page for hiring. Cap 8 images per competitor in chat. Then run html-report to build the pulse report with every screenshot from this pulse embedded, and attach it. Quiet pulses get no report.
9. Deliver in this chat, or to the Slack channel saved in setup. Never both unless asked.

## Rules
Never repeat a change already reported unless it changed again. Never editorialize without evidence. Numbers and quotes carry a source. Pros/cons and For-our-site items are evidence-backed or omitted, never filler advice about "improve messaging."


## Pulse discipline (from memory)
Output shape: per competitor, per module, what changed since last pulse with link or screenshot and date. Then "Website pros / cons" for each competitor when first seen or when home/pricing/positioning changed (2 to 4 each, evidence from their own pages only). Then "Against us": each change and each material pro/con read against the baseline in one or two sentences. Then "For our site": max 3 actionable next steps for the user's own website or pricing page, each tied to evidence from this pulse (concrete page/section change or experiment, framed as a decision). Then "Worth a decision": maximum 3 yes/no questions. Then the "could not read" footer if any. Quiet if nothing changed anywhere: one line, no digest, no invented pros/cons or site advice. Never summarize a summary. Never repeat a change reported in a previous pulse unless it changed again.

## Example pulse (shape, not content)
```
(shape, not content):
Acme (3 changes)
- Pricing: Team plan $49 to $59/seat, annual discount added. [pricing page, screenshot, Sept 9]
- Newsletter: Sept 8 issue leads with "the only platform with native approvals". New phrase. [issue link]
- X: founder thread announcing SSO, 1.2k likes vs ~200 usual. [post link]
Website pros / cons: Acme [home+pricing, Sept 9]
- Pro: Free tier has no time limit. [pricing]
- Pro: Compare table names us and prices their entry plan below ours. [home]
- Con: Their AI features are gated to the top plan. [pricing]
- Con: Core docs blocked until email verify (not a card wall). [product walk]
Beta Co (quiet)
Against us
- Acme's new price sits above our comparable plan for teams of 10+. Their "native approvals" claim overlaps our second listed strength. Their free tier undercuts our entry plan.
For our site
- Add a mid-tier on /pricing between our entry and mid plans so their compare table cannot land only on our price gap. [their compare table, Sept 9]
- Put the capability they lead with on our pricing card, not only in docs. [their free tier copy]
Worth a decision
- Do we ship a public compare page this month that frames our compliance story before theirs?
Could not read
- Acme careers page returned 403 this pulse.
```
