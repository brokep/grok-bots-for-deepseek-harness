---
name: engineering-lead-onboard
description: "First-run setup: learn which repos, work tracker, review norms, bot identity, and digest channel to use, then turn on the weekday chase routine."
---

# engineering-lead-onboard

Part of the Engineering Lead agent preset.

---
name: engineering-lead-onboard
description: >-
  First-run setup: learn which repos, work tracker, review norms, bot identity,
  and digest channel to use, then turn on the weekday chase routine.
---
Run this once when the bot is first created, and again whenever the user says their setup changed.

Goal: collect just enough to own the engineering loop for this user. Ask in one short message, not an interview. Accept partial answers and fill the rest with sensible defaults you state back.

1. Repos. Ask which repositories you should work in and what the default base branch is for each. Confirm the GitHub (or other forge) plugin is connected and that you can read PRs, checks, and reviews. If it is not connected, say exactly what to connect and stop there.
2. Work intake. Ask where work comes from: direct messages to you, a tracker (Linear, Jira, GitHub Issues), or both. If a tracker, ask which team or project to watch.
3. Review norms. Ask who should review PRs by default (or whether CODEOWNERS decides), whether PRs should open as drafts, and what counts as ready to merge (green CI plus N approvals, specific required checks).
4. Bot identity and attribution. Ask whether you open PRs as the user or as a bot identity. If a bot identity, record the co-author trailer to add for the requesting human (name and commit email). Never guess an email.
5. Where to report. Ask where digests and pings go: a DM, or one Slack channel. Record working hours and timezone.
6. Cadence. Default the chase to every 30 minutes on weekdays during working hours. Offer to change it.

Then:
- Save the answers as short memory facts (repos, base branches, intake source, reviewers, ready-to-merge rule, identity and co-author trailer, report destination, timezone).
- Create the weekday chase routine from the engineering-lead-chase routine with the user's timezone and hours.
- Reply with a 4 to 6 line summary of how you will work and one example of what a ping from you will look like. Do not start any work until the user hands you a task.
