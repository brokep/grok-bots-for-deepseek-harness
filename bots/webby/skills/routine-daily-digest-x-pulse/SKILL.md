---
name: routine-daily-digest-x-pulse
description: "Scheduled routine: Email yesterday's digest first, then write today's social-pulse digest. Never email today's digest on the same run."
---

# Daily Digest social pulse

Part of the Webby agent preset.

Schedule, as written by the template author: Email yesterday's digest first, then write today's social-pulse digest. Never email today's digest on the same run.

## What to do on each run

Daily social-pulse Digest in the owner's timezone. All 7 days. Cost-lean. Do not ping the owner.

RUN ORDER is fixed:

1) SEND YESTERDAY FIRST. Compute yesterday's date in the owner's timezone. If the digest file exists, has signal (real body after frontmatter, not a stub), and is not already in the send log, email THAT Digest via the newsletter helper. Skip if already logged. If Create post is plan-blocked, ping the orchestrator with the Digest URL and PLAN_BLOCKED. Do not fake a send. Do not resend the intro issue. Quiet if yesterday has nothing to send. On a real send, ping the orchestrator with the newsletter post id and the live URL.

2) THEN WRITE TODAY. Find the latest daily Digest. Pull the owner's social posts, reposts, and likes since that Digest (or since yesterday if today already exists). Do not invent metrics, view counts, or quotes. If there is nothing new and on-brand to publish, stay silent on the write. Do not invent a Digest. Do not append to week-of-* files. Do not delete or rewrite old week pages. If there is signal: write or update today's digest file using today's local date as both filename and frontmatter date/slug. Match the daily Digest shape (title, date, slug, excerpt, tags, lede, headings, source links). Voice: urgent explainer. Display name only. Strip AI-isms. If today's file already exists, update it in place with no duplicate post ids. BEFORE commit: send the draft claims to the research desk. Wait for the pass. Fix anything they flag. Do not publish un-checked claims. Create-only otherwise. Push main. Then production-deploy the personal site from that main SHA so the homepage signal updates. The host is not Git-connected; a push alone does not update the home screen. Never print the token. Ping the orchestrator with SHA + live digest URL + production deploy id + that research passed.

3) NEVER email today's Digest on this run. Today's file is emailed tomorrow, as yesterday.

Do not touch Exclusive bodies, DNS, or merch.

Fires on:
- cron `40 8 * * *`

Ask the importing user for:
- Timezone
