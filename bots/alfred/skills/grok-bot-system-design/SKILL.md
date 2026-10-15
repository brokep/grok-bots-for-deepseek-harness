---
name: grok-bot-system-design
description: "Use this only after the user approves an Automation Decision Brief, when an approved workflow decision requires a Bot, Skill, Routine, or small multi-Bot handoff design."
---

# Grok Bot System Design

Part of the Alfred agent preset.

---
name: Grok Bot System Design
description: >-
  Use this only after the user approves an Automation Decision Brief, when an
  approved workflow decision requires a Bot, Skill, Routine, or small multi-Bot
  handoff design.
---
# Grok Bot System Design

Design an approved Bot, Skill, Routine, or small multi-Bot handoff. Use only after the user approves the Automation Decision Brief from Workflow & Automation Decision.

## Workflow

1. Reopen the approved Decision Brief.
2. Verify relevant platform capabilities. Label anything the platform cannot do as a manual setup item.
3. Define exactly one durable outcome for each Bot.
4. Define human owner, scope, non-goals, inputs, outputs, sources, dependencies, handoffs, completion evidence, exceptions, and approval boundaries.
5. Separate durable Bot profile, reusable Skills, Routine timing, changing live state, and Registry metadata.
6. Design the smallest number of Skills.
7. Design a Routine only for a manually proven workflow. Keep the Routine as a proposal until specifically approved.
8. Define least-privilege access.
9. Define failure behavior.
10. Create normal, edge, failure, approval, and adversarial tests.
11. Define success metrics.
12. Define pilot limits.
13. Define disable or rollback method.
14. Present a concise architecture summary.
15. Stop for approval before creation.

A Manager Bot owns one durable company outcome or value stream and must have: one durable outcome, one human accountable owner, clear responsibilities, explicit non-goals, authoritative sources, defined inputs and outputs, clear handoffs, success evidence, approval boundaries, and failure behavior.

Create a Specialist Bot only when the responsibility is recurring, durable, has a clear independent outcome, needs materially different context/sources/tools/working style, would make the parent Manager Bot materially less clear, has a clear requester and recipient, and can be tested independently. Otherwise use a Skill.

A Chief of Staff Bot may coordinate priorities, consolidate updates, track decisions, detect missing owners, surface blockers, prepare leadership reviews, route work, and escalate exceptions. It may not become the CEO, change strategy, hire/fire, change pricing, make major financial or legal commitments, make sensitive HR decisions, or contact external parties without required authority. Do not recommend a CoS Bot for one narrow workflow.

## Output

Return a versioned Build Pack:

- Executive recommendation
- Architecture diagram (text tree)
- Bot profile
- Core instructions
- Skill specifications
- Proposed Routine specifications
- Sources and permission matrix
- Handoff contract
- Approval matrix
- Failure policy
- Test matrix
- Pilot plan
- Success metrics
- Disable or rollback method
- Registry entry
- Change log
- Unsupported or manual setup items

## Stop point

Stop for approval of the exact Build Pack.

Do not claim that a drafted Build Pack has been installed. Do not create, edit, or activate anything until the exact version is approved. After approval, route to Pilot, Test & Activate.
