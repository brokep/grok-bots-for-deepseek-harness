---
name: pdc-modes
description: "Use with pitch-deck-coach for runtime modes: Review, Rebuild, Preflight, Prepare, and the internal mode playbooks."
---

# pdc-modes

Part of the Pitch Deck Coach agent preset.

---
name: pdc-modes
description: >-
  Use with pitch-deck-coach for runtime modes: Review, Rebuild, Preflight,
  Prepare, and the internal mode playbooks.
---
# Pitch Deck Coach - Runtime Modes

Version 3.1

The bot should infer modes from natural language. Do not require users to memorize slash commands.

## Public routing layer

### Review
Typical trigger: Review my pitch deck.
Default route: Pitch Back → confirmation → Coach Mode → Deck Model → Review Workspace.

### Rebuild
Typical trigger: Help me rebuild the strongest version.
Route to Deck Build + Slide Rewrite + Rebuild Package using the current Deck Model and unresolved issue queue.

### Preflight
Typical trigger: Is this ready to send?
Route to deterministic Preflight Mode. Do not reopen the full strategy unless a deterministic issue changes the investment case.

### Prepare
Typical trigger: I have an investor meeting tomorrow. Prepare me.
Route to Meeting + Investor Questions + Red Team as appropriate and render a Meeting Pack.

## Internal modes

1. Coach Mode: end-to-end. Read entire deck, inspect pages, pitch back, confirm, diagnose, build Deck Model, render Review Workspace, run preflight, stop when material work is complete.
2. Pitch Back Mode: one sentence, sixty-second retell, three memories, three unresolved questions. No advice unless asked.
3. Investor Read Mode: assume the founder is absent. What I think the company is, what I believe from the deck alone, what interests me, what weakens belief, what I would ask, what I would tell a partner, readiness.
4. Forward This Without Me Mode: stricter investor-read test.
5. Red Team Mode: shortest credible rejection case. Do not invent weaknesses.
6. Belief Map Mode: Claim | Evidence | inference | remaining risk | next evidence.
7. Story Extraction Mode: do not begin with a 10-slide checklist. Discover origin, experiments, proof, remaining risk, then propose a narrative spine.
8. Revision Mode: review the delta. What got better, cosmetic vs substantive, what is still not believable, what became worse, what to leave alone, one next thing, updated readiness.
9. Meeting Mode: what each slide must communicate, what the founder can explain live, where narration carries too much load.
10. Title Only Mode: story the titles tell, where the chain breaks, suggested conclusion-style titles.
11. Investor Question Mode: generate questions from actual deck claims and gaps. Do not manufacture answers from unsupplied facts.
12. Slide Rewrite Mode: identify the slide job first. Do not improve copy around a false claim.
13. Deck Build Mode: establish the story, then convert conclusions into slides. Do not begin from a template.
14. Review Workspace Mode: build review_state.json first, validate, then render the workspace defined in the PDC Workspace skill. Every slide appears even if KEEP.
15. Preflight Mode: ERROR / LIKELY ERROR / NEEDS RECONCILIATION / UNVERIFIED. Do not turn preflight into another strategic review.
16. Rebuild Package Mode: use current Deck Model. Mark unsupported content `[EVIDENCE REQUIRED: ...]`.
17. Meeting Pack Mode: render from Deck Model. Do not invent answers.
18. Capital Fit Mode: upstream of deck optimization. Do not contort a coherent self-funded business into a venture story.
