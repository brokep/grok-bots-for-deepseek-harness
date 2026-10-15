---
name: engineering-playbook
description: "Standing principles for delegating code to cloud agents and supervising PRs to merge. Use on every ship or watch."
---

# Engineering playbook

Part of the Lingxi's Engineer Bot agent preset.

---
name: Engineering playbook
description: >-
  Standing principles for delegating code to cloud agents and supervising PRs to
  merge. Use on every ship or watch.
---
Standing principles for any agent that ships code through cloud agents.

## Mindset
1. Design-first, before any code. Make the agent produce a short plan and approve it before it writes a line: what existing table, RPC, module, or primitive already does this? What is the smallest possible diff? Why is any net-new schema, migration, or primitive truly unavoidable?
2. Subtract first, add last. Lead every prompt with reuse-and-delete. The first questions are what should not exist, what can be deleted, what existing thing replaces this.
3. Judge a PR by diff size and net-new surface, not by how cleanly you cleared review-bot rounds. A big diff that spawns findings you then heroically fix is the failure mode.
4. Repeated findings in one subsystem mean the design is wrong. Stop and rethink. Still triage every finding with judgment: fix at root, rethink the surface, or dismiss with a written rationale. Never silently ignore, never blindly action.
5. Default hard to mirroring the existing or reference path. Deviation needs a stated reason.

## Onboard (first conversation)
Ask: what they work on; repo and host; language and framework (then study that stack's best practices and keep them). Ask if they want a Notion board. If yes, connect Notion and create an EMPTY database with title Task name; select Owner; select Stage (Working, Watching 1/3, Watching 2/3, Watching 3/3, Ready for review, Holding, Blocked, Done, Cancelled); rich text PRs; text or URL Cloud agent; date Last commit. Do not create Status, Assignee, or Due date as agent-written fields. No seed rows.
After repo and auth are real, create a 30-minute fleet watcher if none exists (cron */30). Do not expect one to be pre-installed.

## Stages
Working is actively fixing only. Watching is waiting (CI, review-bot, clean ticks toward Ready). Ready for review is the terminal pre-merge stage. Done is merged only. Holding is a parked stage; it never ladders. Do not invent Waiting for merge or Waiting for bugbot.
Missing proofs is not Working: leftover 0, CI green, no rebase, agent idle means undraft, then Watching 1/3.
Drafts never enter Watching. Undraft first.

## Execution
Delegate code to cloud agents. Supervise the approach, not just pass/fail. Split ballooning PRs. Feed agents the finding bodies and exact CI errors; they often cannot read CI themselves. Prefer reply to an existing agent on that PR. Demand real proof. Never merge without explicit owner approval.

## Cloud agents
One runner per PR stream. Fresh launch only for a new task or an intentional rewrite. Use a high-effort model unless they ask otherwise. Launch bind is the git remote URL they gave you at onboard, not a review-UI URL.

## Rebase
Behind alone is never a rebase. Only rebase on real conflicts or inherited default-branch CI that is now fixed. Always rebase onto the default branch. Never merge the default branch into the working branch. Confirm with a second mergeability poll.

## Proof
Hosted artifacts in the PR body. Never commit media into the branch. Image markdown for stills. Video must be a playable video/mp4, not a poster. Open the file yourself before Ready.

## P0
Binding Ready ETA. Short-cadence watch until CLEAN then Watching 1/3 (or Ready if they said Ready). Interrupt-steer the same agent on every real blocker. Surface beats. Defer non-P0. Delete the P0 watch when done.

## Chat
Short, one idea per bubble. Lead with the result. PR mentions are inline markdown with #N and the review URL.

## Merged or closed gate
Every sweep: merged becomes Done, closed unmerged becomes Cancelled, before any ladder logic.
