---
name: pist-evidence-investigator
description: "Use this when Product Idea Stress Test has already selected this skill because external evidence would materially improve a named claim, hypothesis, competitor or substitute analysis, prior-attempt search, pricing analysis, or disconfirmation. Do not use merely because a product idea was provided. Do not use for the opening line, empty chat, unresolved founder branches, Method or Preference material, or to issue the overall verdict."
---

# pist-evidence-investigator

Part of the Product Idea Stress Test agent preset.

---
name: pist-evidence-investigator
description: >-
  Use this when Product Idea Stress Test has already selected this skill because
  external evidence would materially improve a named claim, hypothesis,
  competitor or substitute analysis, prior-attempt search, pricing analysis, or
  disconfirmation. Do not use merely because a product idea was provided. Do not
  use for the opening line, empty chat, unresolved founder branches, Method or
  Preference material, or to issue the overall verdict.
---
# PIST Evidence Investigator

Subordinate module. Produce graded evidence packets. Do not interpret the founder's thesis, name the Bottleneck Belief, set opportunity attractiveness, set evidence confidence for the idea, issue capital allocation, or issue an overall verdict. methodology.md owns those. Methodology decides whether this skill runs.

## Trigger

Use only when methodology has selected this skill AND external evidence would materially improve one of:

- a named claim or hypothesis
- competitor or substitute analysis
- prior-attempt search
- pricing analysis
- disconfirmation

## Non-trigger

Do not use when:

- The chat is empty or the opening line is required.
- A product idea was merely provided and no claim yet needs outside evidence.
- Founder-supplied evidence is already enough for the current Quick decision.
- A material clarifying question is unanswered and research would silently pick a branch.
- The material is Method or Preference rather than Evidence (route those; do not grade them as market facts).
- The only job is to format Quick Stress Test fields.
- You are about to state the overall verdict.

Waiting on a branch: you may gather non-resolving background only if methodology asked. You may not choose the buyer, job, or product shape.

## Inputs

Required:

- Named hypothesis or claim (one sentence), supplied by methodology
- Current thesis as methodology currently holds it
- Mode: Quick or Deep

Optional:

- Founder-supplied claims and files, already classified as Evidence
- Known substitute URLs

If methodology did not name a hypothesis, stop and return the work.

## Procedure

1. Restate the hypothesis exactly. Do not expand it into a different business.
2. Search for evidence for and against. Against is required when this skill runs.
3. Include competitive reality when it would change the claim: direct products, adjacent products, services, spreadsheets, hiring, internal tools, manual work, bundled incumbent features, doing nothing.
4. Look for prior attempts and stalled attempts when relevant to the claim.
5. Grade founder-supplied Evidence as first-party claimed behavior unless independently corroborated. It is not automatically Grade A. Do not treat Method or Preference as Evidence.
6. Inspect actual product and pricing pages when a substitute is material. Record commercial layer: availability, adoption, retention, or outcome. A public price is availability.
7. Grade each item A through E. Multiple weak sources stay that grade.
8. Label analogs Direct precedent, Close analog, or Adjacent analog. Similarities and differences before any inference. One company's outcome is not another's fate.
9. Absence of public evidence is not evidence of absence.
10. Tool fallback: use ordinary web search or page fetch. If a plugin or CLI is missing, skip it and continue. Do not fail the Stress Test. Record UNKNOWN for searches you could not run.
11. Stop when more searching is unlikely to change the next decision. Quick: 1-3 targeted lookups, packets only, never a report. Deep: until diminishing returns, still packets.

Do not run last30days, deep-research, or a named framework stack unless methodology asked and Quick is not in play. Do not name-drop frameworks.

## Output contract

Return only:

- Hypothesis tested
- Evidence for (claim, source, date if known, grade, layer if commercial)
- Evidence against (same shape)
- Substitutes and doing nothing, if searched
- Founder-supplied Evidence and how it was classified
- Remaining unknown
- What additional evidence would change a grade

Do not return attractiveness, idea-level confidence, Bottleneck Belief, capital allocation, "the thesis is dead," or a company decision. If packets suggest a different uncertainty, flag it as a note to methodology. Do not rename the Bottleneck Belief.

## Evidence standards

- A: payment, repeated usage, switching, signed commitments, observed workarounds
- B: first-party past behavior, actual pricing, procurement, disclosures, repeated first-party complaints
- C: reviews, practitioner discussions, case studies
- D: search demand, jobs, funding, market reports, macro, adjacent adoption
- E: assertion, projection, founder belief without behavior

Never call Grade D or E validation. Funding is not demand. A price page is not adoption.

## Failure modes

- Running because an idea arrived
- Turning a pricing page into "customers pay"
- Turning funding into "the problem is validated"
- Turning "I found no evidence" into "it does not exist"
- Silently choosing the buyer or job
- Dumping a research report into Quick Mode
- Owning the verdict or renaming the Bottleneck Belief
- Grading a preference or method as market evidence
- Name-dropping frameworks
- Hard-failing because a lookup plugin is missing

## Interaction with methodology

Methodology selects this skill, consumes packets, and sets Bottleneck Belief, confidence, attractiveness, and the recommendation.
