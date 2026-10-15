---
name: pist-method-codifier
description: "Use this when Product Idea Stress Test has classified substantial user-provided material as Method (a framework, rubric, investment memo, operating principle, or way of evaluating ideas) and needs an optional reasoning lens. Do not use for Evidence, Preference, or Context alone. Do not edit methodology.md. Do not use for empty chat or to issue the overall verdict."
---

# pist-method-codifier

Part of the Product Idea Stress Test agent preset.

---
name: pist-method-codifier
description: >-
  Use this when Product Idea Stress Test has classified substantial
  user-provided material as Method (a framework, rubric, investment memo,
  operating principle, or way of evaluating ideas) and needs an optional
  reasoning lens. Do not use for Evidence, Preference, or Context alone. Do not
  edit methodology.md. Do not use for empty chat or to issue the overall
  verdict.
---
# PIST Method Codifier

Subordinate module. Turn user-provided Method into a structured optional lens. Do not silently rewrite the canonical operating system. Do not issue a product-idea verdict.

Canonical evidence discipline wins unless the user explicitly asks to compare methodologies.

## Trigger

Use only when methodology has selected this skill AND the user provided substantial Method material: a framework, rubric, investment or product methodology, examples of prior evaluation decisions used as a procedure, or an explicit request to use their way of judging ideas.

## Non-trigger

Do not use when:

- The material is Evidence (interviews, analytics, URLs, transcripts of customers). Send it to evidence investigation.
- The material is Preference only (outcome bar, risk tolerance, "we only do X"). Methodology holds it as a decision criterion.
- The material is Context only (who the founder is, resources, stage).
- The user uploaded a book or framework intending a canonical methodology change. That is a Method Contribution Review, not this skill's edit path.
- The chat is empty.
- You would be editing methodology.md.

A mixed document can still trigger this skill for the Method slice only, after methodology has classified the slices.

## Inputs

- The Method source text or file
- Source provenance (filename, URL, or "pasted")
- Requested lens scope if the user stated one; otherwise default to this Stress Test only
- Canonical conflict surface: evidence grades, commercial layers, analog rules, no-false-universals

## Procedure

1. Extract distinctive principles. What the source actually prioritizes, not a vague summary.
2. Turn them into concrete decision rules.
3. Write trigger and non-trigger conditions for the lens.
4. Separate leftover Evidence and Preference. Do not fold them into the lens as if they were methods.
5. List canonical conflicts. Example: a lens that treats competitor funding as demand proof conflicts with Grade D / not-validation. Record the conflict. Do not accept the funding claim as factual evidence.
6. Assign lens scope: this Stress Test only (default), this project or company, or future Stress Tests for this user. Do not assume permanence. Do not write methodology.md.
7. If the source proposes a change to the canonical OS, note that a Method Contribution Review is required for that change. You may still emit a user lens for this session.
8. Produce 1-2 abstract eval examples showing correct vs incorrect use of this lens.

Do not ingest startup books into the canonical OS during this procedure.

## Output contract

- Source provenance
- Distinctive principles
- Concrete decision rules
- Trigger conditions
- Non-trigger conditions
- Evidence relationship (what was Method vs Preference vs Evidence in the source)
- Canonical conflicts (where the lens disagrees with PIST evidence or calibration rules)
- Lens scope
- Eval cases (short)
- Canonical-edit flag: yes/no (if yes, Method Contribution Review is required; this skill did not edit methodology.md)

Do not return attractiveness, Bottleneck Belief, capital allocation, or an overall verdict. Do not write files into memory/methodology.md.

## Failure modes

- Silently editing methodology.md
- Treating Preference as Evidence ("only $1B outcomes" as proof of a large market)
- Treating the lens as mandatory on every future idea
- Accepting a conflicting rule (funding proves demand) as factual evidence
- Running on interview transcripts as if they were a methodology
- Name-dropping the source framework in founder-facing Quick Mode unless naming helps

## Interaction with methodology

Methodology classifies user material, selects this skill for the Method slice, may apply the lens when its triggers hit, and still owns thesis, Bottleneck Belief, attractiveness, confidence, verdict, and capital allocation. Evidence conflicts are resolved by canonical evidence discipline unless the user asked for an explicit methodology comparison.
