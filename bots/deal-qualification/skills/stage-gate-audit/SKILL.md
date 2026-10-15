---
name: stage-gate-audit
description: "Audits one opportunity against the qualification framework from its call transcripts: a quote and timestamp per criterion, what is missing, and a Promote, Close, or Insufficient Data verdict."
---

# stage-gate-audit

Part of the Deal Inspector agent preset.

# stage-gate-audit

## When to use

The `friday-stage-audit` routine, or on demand ("audit the Acme deal", "is Acme really Stage 2", "run MEDDPICC on Northwind"). Input: an opportunity or account name.

## Steps

1. Resolve the opportunity in the CRM: stage, stage history with dates, amount, close date, owner, contacts and roles, current values of the qualification fields, last activities.
2. Find the calls: every recorded call linked to the account in the last 120 days from whichever recorder is connected (Gong, Granola, or both), plus any call whose participants match the opportunity's contacts. Read the summaries, then the transcripts of the calls since the last stage change in full.
3. Score every criterion of the framework from `qualification-frameworks`:
   - Met: quote the exact customer words that establish it, with the call date and timestamp, and the speaker's name and title.
   - Partial: quote what was said and state what is still missing.
   - Missing: say so. Do not infer a champion from enthusiasm or a budget from company size.
4. Check the follow-through: did we do what we promised on the last call (from the CRM activities and, if available, email)? A deal whose next steps are overdue is flagged.
5. Compare the transcript evidence with the CRM fields. Note every field that claims more than the calls support.

## Verdict

One of three, with a one-paragraph rationale:

- Promote: the criteria for the next stage are met on the transcript evidence. Name the champion, the economic buyer, the pain in the customer's words, and the size estimate with its basis.
- Close: the evidence contradicts the stage (no problem stated, no buyer, explicit no, dead for 45 days with no reply). Say which fact drives it.
- Insufficient Data: no recorded calls since the stage change, or the transcript is silent on the gating criteria. List the two or three questions the next call must answer.

## Output

A scorecard table (Criterion, Status, Evidence with quote and timestamp, Gap), the verdict paragraph, the follow-through check, the CRM discrepancies, and the proposed field updates handed to `crm-writeback`. Deliver to the owner; include the manager only if memory says so.

## Rules

- Quotes verbatim, never paraphrased inside quotation marks.
- Never move a stage or change a field from this skill; `crm-writeback` does that after approval.
- Never grade the rep. Grade the deal.
