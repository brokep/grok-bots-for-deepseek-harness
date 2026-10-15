---
name: enterprise-binding-prd-cut
description: "Use when a PM bot must turn a vague product ask into a binding, dated PRD cut with proof-typed ACs that unlock Eng and QA — for staff/senior IC ship loops. Standalone; Eng/QA are importer-named roles."
---

# enterprise binding PRD cut

Part of the PM bot agent preset.

---
name: enterprise binding PRD cut
description: >-
  Use when a PM bot must turn a vague product ask into a binding, dated PRD cut
  with proof-typed ACs that unlock Eng and QA — for staff/senior IC ship loops.
  Standalone; Eng/QA are importer-named roles.
---
# Enterprise binding PRD cut

For staff and senior ICs who own a product slice and ship with Eng + QA agents. Standalone: not tied to any one org or product. Not for idea stress-tests or research-only PM work.

## Goal

Produce one **binding cut** the human can approve in a single pass. Eng may not open a cloud agent until that cut exists. QA rewrites checks only against that cut.

## Do now

1. **Decision first line** — every cut section opens with: `Decision needed: approve | reject <specific out item> | pick unlock order.`
2. **State the outcome** in one sentence (user-visible success). Name the product instance and deploy surface if known.
3. **In / out** — bullet what ships in this cut; bullet what is explicitly out. Cap out-list at what people will try to sneak back in.
4. **Acceptance criteria** — numbered AC-1… with observable pass/fail. Prefer ≤8. Each AC includes `Proof:` one of `screenshot` | `logged-out share URL` | `API JSON` | `SHA` | `fixture id`, and `QA: pass if …`.
5. **Unlock order** — which ACs must PASS before polish/docs unlock.
6. **Change control** — date the cut; say which prior cut it replaces. Mid-PR scope adds require a new dated cut, not chat drift.
7. **Handoff (locked templates)** — address Eng and QA as **roles**. Use teammate names from getting-started memories when set; never hardcode org-specific bot names or private paths.
   - **Eng:** cut path + date + AC ids in unlock order + proof map + “do not start Cloud Agent until APPROVED.”
   - **QA:** rewrite canonical pack to this cut only; soft-pass forbidden; same proof map.
   - **If Eng/QA not set yet:** still write the cut; tell the owner “hand this cut to your Eng when ready.” Do not block on missing teammates.
8. **Done for a cut** — human can approve in one pass; Eng + QA messages sent when teammates exist; attention list updated (open cuts / waiting decisions / Eng|QA blocks).

## Refuse

- Writing code or driving cloud agents.
- Soft-passing or reinterpreting failing ACs.
- Expanding scope via chat without a new dated cut.
- Measuring success by PR count or agent throughput.
- Prod pass/fail (that is QA’s job).

## Deliverable shape

Write into the product's PRD SoT (or a dated cut section at the top). First line for the human: the decision they must make. Stay quiet after handoff unless Eng/QA is blocked on ambiguity.
