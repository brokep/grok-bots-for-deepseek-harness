---
name: routine-daily-exclusive-long-form-publish
description: "Scheduled routine: Daily scan for new public long-form videos, write an Exclusive, fact-check, ship the site, and email the same day."
---

# Daily Exclusive long-form check

Part of the Webby agent preset.

Schedule, as written by the template author: Daily scan for new public long-form videos, write an Exclusive, fact-check, ship the site, and email the same day.

## What to do on each run

Daily Exclusive scan in the owner's timezone. All 7 days. Cost-lean. Quiet if nothing new.

MEMBERS-ONLY RULE: Never publish a public Exclusive, newsletter email, homepage hero, listing, sitemap, RSS, or llms.txt entry for a members-only YouTube video. Detect via player playability: status {slack_user} and reason containing "members". Skip those videos in the scan. Do not write a public exclusive post for them. If a draft already exists, set frontmatter members: true and keep the file (create-only, never delete). When that same video later becomes public, then research desk → push → production-deploy → same-day newsletter. Early access is YouTube Members only. Do not leak the writeup. Do not add a paid newsletter tier unless the owner asks. Do not resend or unsend an email that already went.

1) List new long-form uploads on the owner's YouTube channel. Prefer the named long-form playlist, also any other new long-form. Skip Shorts (under ~3 minutes). Skip members-only. Prefer on-disk transcripts or captions over the YouTube Data API; a downloader often rate-limits.

2) For each candidate, check if the exclusive content folder already has a matching Exclusive in the site repo. Skip matches. Create-only. Never delete posts, videos, or files. Do not rewrite existing Exclusive bodies.

3) If a new PUBLIC long-form has no Exclusive: pull the transcript, write a real Exclusive matching existing frontmatter (title, date, slug, excerpt, tags). Voice: urgent explainer, concrete stakes, display name only. Strip AI-isms hard (no Key Takeaways, no pivotal/testament/underscore/delve, no em-dash spam). YAML: never use \" escapes.

4) BEFORE commit: send the draft claims (named facts, numbers, quotes, titles) to the research desk. The research desk owns Exclusive/Digest sourcing fact-check with live search. Wait for the pass. Fix anything they flag. Do not publish un-checked claims.

5) Then commit and push to main. Production-deploy the personal site from that main SHA so the homepage hero updates. The host is not Git-connected; a push alone does not update the home screen. Never print the token. This bot still ships the site.

6) Same-day newsletter email. After the research desk passed and the Exclusive is live, email it that same day. Do not wait until tomorrow. Use the newsletter helper. Skip if that exclusive slug is already in the send log. Do not send a first intro issue. Display name only. Strip AI-isms on wrapper copy. If Create post is plan-blocked, ping the orchestrator with the Exclusive URL/SHA/deploy and PLAN_BLOCKED. Do not fake a send. Then ping the orchestrator with titles, slugs, SHA, production deploy id, that research passed, and the newsletter post id. If nothing new, stay silent. Do not ping the owner. No production DNS. No catastrophic deletes. Do not touch Digest bodies, merch, or homepage H1.

This also applies when the orchestrator asks you to ship an Exclusive mid-day: email it the same day after the site is live, then ping the orchestrator with the post id.

Fires on:
- cron `15 9 * * *`

Ask the importing user for:
- Timezone
- Slack user
