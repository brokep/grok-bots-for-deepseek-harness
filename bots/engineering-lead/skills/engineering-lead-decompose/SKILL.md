---
name: engineering-lead-decompose
description: "Turn a request into a small set of independently shippable Cloud Agent tasks or a Project, then launch and track them."
---

# engineering-lead-decompose

Part of the Engineering Lead agent preset.

---
name: engineering-lead-decompose
description: >-
  Turn a request into a small set of independently shippable Cloud Agent tasks
  or a Project, then launch and track them.
---
Use when the user hands you a feature, bug, migration, or any request bigger than a single small edit.

1. Restate the goal in one sentence and name what done looks like (merged PRs, a doc, a decision).
2. Split it into the fewest independently reviewable units. Each unit should produce one PR that can merge on its own. Separate backend, frontend, and infrastructure changes into different units when they touch different areas. Order units by dependency.
3. For multi-unit or multi-day work, create a Project so the units share context and status. For a single unit, one Cloud Agent is enough.
4. For each unit, write a self-contained brief: goal, repo and base branch, files or areas likely involved, acceptance criteria, how to test, and the review and draft-PR norms from memory. Tell the agent to open a draft PR when it has something reviewable.
5. Launch the agents. Record each one on your task list with: unit name, agent or Project link, PR link once it exists, current state, and what you are waiting on.
6. Tell the user the plan in a few lines (units, order, what you need from them, if anything). Do not ask for approval on routine decomposition unless the request was ambiguous or risky.

Rules:
- Steer before you spawn. If an existing agent already has the right context, send it a follow-up instead of starting a new one.
- Never mark a unit done because its agent finished; done means the PR merged or the user closed it.
