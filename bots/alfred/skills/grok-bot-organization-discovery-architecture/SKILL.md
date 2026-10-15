---
name: grok-bot-organization-discovery-architecture
description: "Use this when starting from zero, redesigning the Grok Bot organization, the company grew or shrank, strategy/product/team changed, or the current Bot hierarchy no longer fits."
---

# Grok Bot Organization Discovery & Architecture

Part of the Alfred agent preset.

---
name: Grok Bot Organization Discovery & Architecture
description: >-
  Use this when starting from zero, redesigning the Grok Bot organization, the
  company grew or shrank, strategy/product/team changed, or the current Bot
  hierarchy no longer fits.
---
# Grok Bot Organization Discovery & Architecture

Understand enough about the company to design or redesign the correct Grok Bot organization. This is not a generic company audit. Company analysis exists only to support Bot architecture.

## Inputs (gather only what matters)

- Company product or service, customer, stage, human team
- Actual responsibilities vs formal roles
- Current important outcomes (1–3)
- Value streams and founder/leadership workload
- Important workflows, sources, approval boundaries
- Existing Bots, Skills, Routines, and handoffs when applicable

## Workflow

1. Determine whether the user starts from zero or already has Bots.
2. Identify one to three important company outcomes.
3. Identify the important value streams supporting those outcomes.
4. Map the humans currently responsible.
5. Compare formal roles with actual responsibilities.
6. Identify work concentrated around leadership.
7. Inventory existing Bots, Skills, Routines, and handoffs when applicable.
8. Detect missing ownership, duplicate ownership, overloaded roles, duplicate Bots, weak handoffs, unnecessary Bots, missing reusable Skills, and candidate recurring workflows.
9. Separate human work, process problems, deterministic automation, AI-assisted work, Bot responsibilities, Skills, and Routines.
10. Select the smallest useful Bot topology (one focused Bot; Human + Chief of Staff Bot; CoS + Manager Bots; Manager + Specialist only where independent durable responsibility is proven).
11. Create a target Bot hierarchy. Include only roles supported by evidence.
12. Define a human accountable owner for every proposed Bot.
13. Recommend no more than three immediate changes.
14. Select only the first component for implementation.
15. Route every concrete automation or Bot candidate through Workflow & Automation Decision. Do not design or create that component until that skill is complete.

Inspect authorized material first. Ask no more than three material questions in one turn. Do not perform a giant generic company audit.

Do not claim a full account scan unless the live environment actually allowed inspection of the relevant configuration.

Default new Bot recommendations to zero. A new Bot should exist only when it owns a coherent, durable, observable responsibility.

## Output

Return:

- Executive recommendation (topology + confidence)
- Relevant company context
- Current Grok Bot structure when applicable
- Target Grok Bot hierarchy as a visual text tree
- Existing Bot decisions: Keep, Improve, Merge, Reposition, Pause, Hide, Retire, or Investigate
- Proposed Bots with outcome, human owner, responsibilities, non-goals, inputs, sources, outputs, Skills, possible Routines, handoffs, approval boundaries, and success evidence
- What should not become a Bot
- Build order
- Next workflow that should move through Workflow & Automation Decision
- Assumptions and unknowns, clearly labelled

## Stop point

Stop after presenting the architecture and the first component to validate.

Do not design or create that component until Workflow & Automation Decision is complete and approved.
