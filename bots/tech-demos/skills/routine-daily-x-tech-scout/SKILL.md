---
name: routine-daily-x-tech-scout
description: "Scheduled routine: Weekdays at 9:00 AM. Lands paused on import."
---

# Daily X tech scout

Part of the Tech Demos agent preset.

Schedule, as written by the template author: Weekdays at 9:00 AM. Lands paused on import.

## What to do on each run

Weekday X-bookmark → demo prompt pipeline. Lands paused on import — enable after the X connector is signed in and the sticky demo monorepo fill-in is set.

Goal: find ONE new technology from the owner's recent X bookmarks that is worth a small demo, draft an approval prompt, and stop. Do not build anything until they approve.

Steps each run:
1. Load tracking state from {demo_repo} tracking/seen-bookmarks.json. Never re-propose something already listed there.
2. Read the owner's X bookmarks via the X connector (reads only). Prefer folders Product Demos, Agent Examples, Design, and DevRel when those exist.
3. Skim recent bookmarks (roughly last 1–3 days of new ones, or the newest ~30 if timestamps are unclear). Filter hard for a concrete technology, library, framework, API, model, or tool that could become a single-user MVP demo.
4. Prefer candidates with bubbling sentiment on X. Use the X connector for a quick read on buzz. If X search is unavailable, note that and still pick from bookmarks.
5. Pick at most ONE candidate. If nothing qualifies, stay quiet and end the run.
6. Draft a short approval prompt that includes: the tech name, why it stood out (with the source bookmark URL), a one-line X sentiment pulse if available, a proposed demo angle / MVP scope under apps/<slug>/, and an ask to tweak or approve. Offer Approve / Tweak / Skip.
7. Append the candidate to seen-bookmarks.json under proposed (id, title, url, date).
8. Do not build on this run. After approval in chat: run the project-planning skill, write apps/<kebab-slug>/PLAN.md, then launch a Cursor cloud agent with model claude-fable-5 (Fable 5) against {demo_repo}. The agent must only add/update apps/<kebab-slug>/ (self-contained: bun install && bun run dev), open one PR, and must attach BOTH at least one screenshot AND at least one video of the running app in the PR. Never create a new GitHub repository.

Tone: warm, sharp, brief. One pick, not a list.

Fill-ins:
- {demo_repo}: the importer's sticky GitHub monorepo (https://github.com/owner/repo) with AGENTS.md, skills/project-planning/, apps/, and tracking/seen-bookmarks.json.

Schedule: weekdays 9:00 AM in the importer's local time.

Fires on:
- cron `0 9 * * 1-5`

Ask the importing user for:
- Timezone
