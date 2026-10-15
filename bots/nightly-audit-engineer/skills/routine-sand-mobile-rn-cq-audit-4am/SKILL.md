---
name: routine-sand-mobile-rn-cq-audit-4am
description: "Scheduled routine: Research the whole tree, then one cleanup per area. Defaults to 4am; ask when to run."
---

# Nightly code-quality audit (4am)

Part of the Nightly Audit Engineer agent preset.

Schedule, as written by the template author: Research the whole tree, then one cleanup per area. Defaults to 4am; ask when to run.

## What to do on each run

Nightly code-quality audit of the owner's whole codebase.

Ask the importer when to run. Default is 4am if they do not pick a time.

Goal: research the entire tree for cleanup opportunities, aggregate findings, then start ONE cleanup per distinct area. Stay quiet if nothing actionable.

Audit lenses (all required each run):
1. Platform best practices for the stack in this repo — read and apply the repo's own skills as a checklist.
2. Dead / killable — unused exports, dead branches, orphaned files/components, unreachable UI, leftover flags/code after merges that can be deleted entirely.
3. Needless complexity — overbuilt state/machinery that made no user-visible difference, or something that could be done simpler (no ms-level micro-opts, no defensive race-guard piles).
4. Unnecessary comments — trim noise; fewer comments, ONLY necessary ones. Prefer deleting stale/narrating comments over rewriting them.

Hard constraints (always):
- Ask what to audit if the owner has not named a tree. Do not assume a product or repo name.
- Research the whole assigned tree first. Do not start cleanup until research is aggregated.
- One cleanup per distinct area. Do not fold unrelated gaps into one change.
- Prefer the simplest real improvements; skip nitpicks, ms-level micro-opts, and intentional platform-impossible surfaces.
- If an area already has an open cleanup covering the same gap, leave it alone — do not duplicate.
- New pull requests open on the owner's existing source-control path; do not invent a host.
- Never clone the repo locally — use remote APIs and cloud agents only.
- agent done is not task done: stay in progress until the change is merged.

Steps each run (strict order — do not start cleanup until research is aggregated):
1. RESEARCH (read-only): launch a few research-only cloud agents that together cover the whole assigned directory, every file. Split by area/subtree so coverage is complete. Each research agent MUST: (a) not open a PR or edit code, (b) walk every file in its assigned slice, (c) report findings under the four lenses above with file paths + short why + suggested kill/simplify/trim. Wait for all research agents to finish.
2. AGGREGATE: merge the research reports into one deduped list. Group related findings into coherent areas (one area = one cleanup). Drop noise, already-covered items, out-of-scope work, and anything too tiny to justify a PR.
3. {slack_channel_id}: for each remaining area, start one cleanup cloud agent with the aggregated findings, a clear outcome, and proof rules for that stack. Do not start a second area until the first is boarded as its own change.
4. If zero actionable new areas after aggregation, stay quiet.
5. If you started anything, send the owner a short lowercase update listing the new cleanup areas (and PR numbers if already open). Keep it a couple short bubbles, not a wall.

Fires on:
- cron `0 4 * * *`

Ask the importing user for:
- Timezone
- Slack channel id
