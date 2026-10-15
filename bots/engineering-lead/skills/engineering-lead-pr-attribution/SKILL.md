---
name: engineering-lead-pr-attribution
description: "Open and update PRs correctly when working as a bot identity, including co-author trailers for the requesting human."
---

# engineering-lead-pr-attribution

Part of the Engineering Lead agent preset.

---
name: engineering-lead-pr-attribution
description: >-
  Open and update PRs correctly when working as a bot identity, including
  co-author trailers for the requesting human.
---
Use whenever you, or an agent you launched, opens or pushes to a PR on the user's behalf.

- If PRs open under a bot identity, every commit the bot authors for a human's request carries a trailer on its own line at the end of the message: Co-authored-by: <Human Name> <human-commit-email>. Use the name and email saved during onboarding. If you do not have them, ask once; never invent or guess an email.
- Put the requesting human in the PR description (Requested by ...) and link the task or issue it resolves, following the repo's PR template if it has one.
- Open as a draft unless the user's norms say otherwise; mark ready only when the ready-to-merge rule is met.
- Tell launched agents these rules in their brief so their commits are attributed the same way.
- Do not add co-author trailers for people who did not ask for or contribute to the change.
