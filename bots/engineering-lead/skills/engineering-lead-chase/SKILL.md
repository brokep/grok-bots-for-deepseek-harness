---
name: engineering-lead-chase
description: "One pass over every tracked agent and PR: unstick what you can, escalate only what needs a human, and stay silent when everything is healthy."
---

# engineering-lead-chase

Part of the Engineering Lead agent preset.

---
name: engineering-lead-chase
description: >-
  One pass over every tracked agent and PR: unstick what you can, escalate only
  what needs a human, and stay silent when everything is healthy.
---
Run on each chase routine firing, and whenever the user asks for status.

For every item on your task list:

1. Agent state. If the agent is still working and making progress, leave it alone. If it stopped, errored, or has not produced new output for a long stretch, read its latest transcript and either send a concrete follow-up (what to fix, what to try next) or restart it with a tighter brief.
2. CI. If checks failed, open the failing check, find the root cause, and send the owning agent a follow-up with the failure and a suggested fix. Re-run a check only when the failure is clearly flaky, and say so.
3. Reviews. If review comments are unaddressed, send the agent a follow-up to address them. If the PR is waiting on reviewers with no activity, request review from the default reviewers once; after that, surface it in the digest instead of re-pinging.
4. Merge readiness. If the PR meets the ready-to-merge rule from memory, mark it ready (undraft) and notify the user that it is ready to merge. Only merge yourself if the user explicitly allowed it for that PR or repo.
5. Update the task list with the new state and what you are waiting on.

Then decide whether to speak:
- Something is blocked on the user (a decision, access, a secret, an approval): ping once, with the item, the blocker, and the exact action needed.
- A PR is ready to merge: ping with the PR link and one line on what it does.
- A unit or the whole task is finished: ping with a short summary and links.
- Otherwise: say nothing. Healthy progress goes in the digest, not in a message.

Never re-send the same ping on consecutive passes. Track what you already told the user.
