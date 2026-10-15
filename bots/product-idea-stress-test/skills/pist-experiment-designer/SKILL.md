---
name: pist-experiment-designer
description: "Use this when Product Idea Stress Test has already named a Bottleneck Belief or equivalent primary uncertainty and has selected this skill because an experiment would help. The uncertainty is an input from methodology. Do not invent or replace it. Do not use for empty chat, unresolved clarifying questions, or to issue capital allocation or the overall verdict."
---

# pist-experiment-designer

Part of the Product Idea Stress Test agent preset.

---
name: pist-experiment-designer
description: >-
  Use this when Product Idea Stress Test has already named a Bottleneck Belief
  or equivalent primary uncertainty and has selected this skill because an
  experiment would help. The uncertainty is an input from methodology. Do not
  invent or replace it. Do not use for empty chat, unresolved clarifying
  questions, or to issue capital allocation or the overall verdict.
---
# PIST Experiment Designer

Subordinate module. Design the next test of an uncertainty methodology already named. Do not interpret the founder's thesis, rename the Bottleneck Belief, set attractiveness, set evidence confidence, issue capital allocation, or issue an overall verdict.

## Trigger

Use only when methodology has selected this skill AND:

- A Bottleneck Belief or equivalent primary uncertainty has been identified by methodology
- An experiment is useful for the current decision

## Non-trigger

Do not use when:

- The chat is empty or the opening line is required.
- The next step is a clarifying question, not a test.
- Methodology has not named the uncertainty.
- The founder already specified a test that matches the bottleneck and methodology accepted it.
- You are about to state capital allocation or the overall verdict.

## Inputs

Required, from methodology:

- Bottleneck Belief (one uncertainty)
- Mode: Quick or Deep

Optional:

- The decision the founder is considering
- Current evidence summary (grades and layers, not a dump)
- Constraints: time, money, access, technical

If the uncertainty is missing, stop. Do not invent one.

## Procedure

1. Restate the supplied uncertainty. Do not replace it with activation, competition, polish, or another concern. If it is malformed, return it to methodology with a rename request. Do not proceed under a new name.
2. Name sequential gates when the customer must do something before they feel value. Gates are diagnostic, not a new Bottleneck Belief.
3. List 2-4 candidate tests that could reduce that same uncertainty. Include at least one non-concierge option when a prototype, benchmark, paid acquisition, outbound, pricing test, or actual sale could produce stronger evidence.
4. Compare candidates on expected information gain, importance, cost, time, reversibility, and strength of evidence produced. Pick one. Concierge is allowed only when it wins. "Do not build" is not a default.
5. Write precommitted interpretation bands with observable counts, rates, payments, usage, or measurements. Not "several," "many," or "good."
6. State what the experiment cannot establish.

If the supplied bottleneck is technical feasibility (speedup, accuracy, integration), the candidate set must include a benchmark or prototype against the strongest relevant baseline. Interviews about desire are not a substitute.

If the supplied bottleneck is ongoing payment or retention after first value, and existing users exist, the candidate set must include a second-period behavior test. More installs are not a substitute.

Quick Mode: keep the design short. Methodology may use it internally. Do not add a memo that lengthens the founder-facing Quick response.

Tool fallback: this skill does not require plugins.

## Output contract

Return only:

- Primary uncertainty (the input, restated)
- Chosen method and why it won the information-gain comparison
- Candidates considered and rejected (one line each)
- Sequential gates, if any
- Upgrade band
- Ambiguous band
- Downgrade band
- What this experiment cannot establish
- Rename request, only if the input uncertainty was malformed (methodology decides)

Do not return attractiveness, capital allocation, overall verdict, or a replacement Bottleneck Belief.

## Failure modes

- Inventing or replacing the Bottleneck Belief
- Defaulting to concierge, interviews, or a landing page
- Defaulting to "do not build"
- Mixing several uncertainties into one pass/fail
- Vague bands
- Owning the company decision
- Lengthening Quick Mode with a candidate essay

## Interaction with methodology

Methodology names the uncertainty, selects this skill, consumes the design, and decides capital allocation.
