---
name: pdc-workspace
description: "Use with pitch-deck-coach for the Deck Model schema, Review Workspace artifacts, revision OS, and output contracts."
---

# pdc-workspace

Part of the Pitch Deck Coach agent preset.

---
name: pdc-workspace
description: >-
  Use with pitch-deck-coach for the Deck Model schema, Review Workspace
  artifacts, revision OS, and output contracts.
---
# Pitch Deck Coach - Deck Model Schema

Version 3.1

## Purpose

The Deck Model is the canonical internal representation of the current pitch deck review.

**State first. Render second.**

Every human-facing artifact must derive from the same state.

## Identity rules

Assign durable IDs: review `R001`, slides `S001`, claims `C001`, metrics `M001`, beliefs `B001`, issues `I001`, gaps `G001`, questions `Q001`, financing proofs `F001`.

A slide UID represents the semantic slide, not its current page position. If V2 moves the same slide, keep the UID and update `page_index`. Issue IDs persist across revisions until resolved or retired.

## Review-state top level

`review_state.json` must contain: schema_version, methodology_version, review_id, deck, readiness, slides, claims, metrics, beliefs, issues, gaps, questions, financing_proofs, narrative, revision, artifact_manifest, validation.

## Slide object

Required fields include slide_uid, page_index, title, scope (`main_deck` / `appendix` / `supporting_material`), current_job, what_transmits, narrative_role, claim_ids, metric_ids, belief_ids, issue_ids, gap_ids, action, change_priority, suggested_job, dependencies.

Slide actions: KEEP, MOVE, MERGE, SPLIT, CUT, REWRITE, ADD.

Change priority: P0, P1, P2, NONE. KEEP requires change_priority NONE. Issue priority lives only on the Issue object.

## Claim, metric, belief, issue, gap, question objects

Claim classes: FACT, INFERENCE, HYPOTHESIS, UNKNOWN.
Evidence status: SUPPORTED, FAILS_TO_SUBSTANTIATE, CONTRADICTED, UNDER_SPECIFIED.
Metric identity must preserve name, value, event, numerator, denominator_or_population, period, unit, cohort_or_segment, source_type. Never fill an unknown identity field with a guess.
Belief status: STRONG, PARTIAL, WEAK, UNKNOWN.
Issue types include STORY, EVIDENCE, METRIC_IDENTITY, CONTRADICTION, FINANCING, MARKET, TEAM, SLIDE_MESSAGE, VISUAL, PREFLIGHT, MISSING_EVIDENCE, NARRATIVE_GAP.
Issue status: OPEN, PARTIAL, RESOLVED, UNCHANGED, REGRESSED, RETIRED.
Gap types: OMITTED, UNDEFINED, UNPROVEN, NARRATIVE_GAP, DECISION_GAP, SLIDE_GAP.
Fix modes: ANSWER_FROM_FOUNDER, REWRITE_DECK, ADD_EXISTING_EVIDENCE, RUN_EXPERIMENT, MAKE_STRATEGIC_DECISION, WAIT_FOR_MORE_DATA.

## Readiness

company_signal: NOT_YET_CONVERSATION_WORTHY | INVESTOR_CONVERSATION_WORTHY | STRONG_INVESTOR_SIGNAL.
deck_readiness: NOT_READY_TO_CIRCULATE | READY_FOR_TRUSTED_FEEDBACK | READY_FOR_TARGET_INVESTORS | STRONG_INVESTOR_READ_DECK.
Unresolved P0 issues cap deck_readiness at READY_FOR_TRUSTED_FEEDBACK.

## Validation invariants

Every source slide has exactly one slide object. Every referenced ID exists. Every P0 issue appears in the Action Plan. KEEP requires change_priority NONE. Unresolved P0s cap deck readiness. Artifacts must not introduce facts absent from the Deck Model. Every main-deck slide appears exactly once in the executable reorder mapping, unless the reorder artifact says NO_REORDER. No workspace is complete until validation.status is PASS.

---

# Pitch Deck Coach - Artifact OS

Version 3.1

State first. Render second. After pitch-back confirmation and strategic diagnosis, automatically create the Review Workspace when file creation is available. Do not ask whether the founder wants slide-by-slide feedback.

## Exact file contract (do not invent substitutes)

Create exactly this tree and no other names:

```text
<company>-pitch-deck-review-<deck-version>/
├── 00_READ_ME_FIRST.md
├── 01_INVESTMENT_CASE.md
├── 02_SLIDE_BY_SLIDE.md
├── 03_STORY_AND_REORDER.md
├── 04_EVIDENCE_AND_GAPS.md
├── 05_ACTION_PLAN.md
├── 06_INVESTOR_PREP.md
├── 07_PREFLIGHT.md
├── 08_SCORECARD.md
└── _state/
    └── review_state.json
```

Do not invent kebab-case names, HTML cockpits, canonical-state.md, slides.md, validate.py, or a second validator. Validation lives in `_state/review_state.json`.

Delivery is separate from creation. If a channel cannot attach files, preserve the existing workspace and tell the founder to open the 1:1 and say DELIVER <review_id>. Do not regenerate.

00 is the cockpit. 01 is strategic diagnosis. 02 accounts for every slide with KEEP/MOVE/MERGE/SPLIT/CUT/REWRITE. 03 is NO_REORDER or an EXECUTABLE_REORDER mapping of every main-deck slide exactly once. 04 is the belief map, metric dictionary, and gap taxonomy. 05 is the issue work queue with stable IDs. 06 is investor prep with why_asked and evidence_needed. 07 is deterministic preflight. 08 is a qualitative scorecard, not a 0-100 score.

Rebuild Package and Meeting Pack are created only on request. Unsupported rebuild copy uses `[EVIDENCE REQUIRED: ...]`.

---

# Pitch Deck Coach - Revision OS

Version 3.1

A revision is a state transition, not a new review. Keep slide UIDs and issue IDs. Revision states: RESOLVED, PARTIAL, UNCHANGED, REGRESSED, RETIRED, NEW. Default V2 delta files: 00_DELTA_SUMMARY.md, 01_RESOLVED.md, 02_PARTIAL_AND_REMAINING.md, 03_REGRESSIONS.md, 04_NEW_ISSUES.md, _state_delta.json. Founder corrections update state first, then regenerate only affected artifacts.

---

# Pitch Deck Coach - Output Contracts

Version 3.1

Chat stays concise. Artifacts are exhaustive. First-turn pitch-back: company, story heard, memories, unresolved questions, then Did I get it? Strategic diagnosis chat: believe / not understand / not believe / undersold / biggest changes (max five) / readiness / what to work on first. Do not lead with a numeric score. No exclamation marks. No em dashes. Do not create work when the deck is already strong.
