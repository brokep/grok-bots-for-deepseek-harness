---
name: score-and-qualify-leads
description: "Use when leads need a fit score and a tier, on intake or whenever the user asks which leads to work first."
---

# Score and qualify leads

Part of the Lead Pipeline Desk agent preset.

Inputs: the lead ledger and the user's fit rules from memory.

Default fit rules, used until they give you their own: a work email on a company domain, a title with budget or buying authority for what they sell, company size and industry inside the range they named, a country they sell into, and a source that has converted before.

1. Score every lead from 0 to 100 and show the parts, so a score can be argued with. Fit carries the most weight, then the intent in the source, then how recently the lead came in.
2. Put each lead in a tier. A is worth a same-day reply, B is worth a reply this week, C is nurture, and D is disqualified with a reason.
3. Write one short reason per lead in plain words. "VP Eng at a 400 person fintech, asked for a demo today" beats a number on its own.
4. Never fill a gap with a guess. A missing size or industry is missing, so score what you have and say the score is partial.
5. Disqualify on evidence only: a competitor domain the user named, a personal address on a product sold to companies, a country they do not sell into, or a repeat of a lead already closed as lost. Never disqualify on a name, a photo, or a school.
6. Sort A first and show the top rows with score, tier, reason, and source.

Output: the scored ledger plus a ranked shortlist of the A leads with the reason on each one.

When the user disagrees with a score, take the correction, update the fit rules in memory, and re-score the whole list instead of patching the one row.

Save the scored ledger under the lead desk folder.
