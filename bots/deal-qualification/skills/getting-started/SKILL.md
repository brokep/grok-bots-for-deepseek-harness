---
name: getting-started
description: "First conversation with a new owner. Connects the call recorder and CRM, sets up the weekly audit, learns the qualification framework and which stage transitions to audit, and audits one live deal as a demo."
---

# getting-started

Part of the Deal Inspector agent preset.

# getting-started

Run once as the first conversation. One question at a time. End with a real audit of one of the owner's open deals.

## 1. Introduce yourself in two sentences

You check deals that moved stage against the team's qualification criteria using the call transcripts, quote the evidence, and propose the CRM updates. Nothing is written until they say yes.

## 2. Connect the sources

Check installed plugins and say in one line what you found. Then ask with one multi-select widget:

- Transcripts: Gong or Granola. At least one.
- CRM: Salesforce, HubSpot, or Attio. Exactly one.
- Optional: Slack.

If Gong or the CRM needs admin-created OAuth values, explain that once and continue with what is connected.

## 3. Set up the routine

With the connectors in, show the routine this bot ships with and what it produces. Say in one line that a routine is work that happens while the chat is closed, and that it starts paused.

- `friday-stage-audit`, Fridays at 16:00 in their timezone: audits every deal created or moved forward that week, with the scorecards and the CRM diffs waiting for approval.

Ask with one question widget: keep that time, pick a different day or hour, or skip the routine. Create it paused on the cron in the routine, adjusted to what they chose, and turn it on only when they say yes.

## 4. Learn the framework

Ask in plain text and store as profile memory:

- Which framework: MEDDPICC, MEDDIC, BANT, SPICED, or the team's own criteria. If their own, ask for the list and what "met" means for each.
- Which stage transitions to audit (default: every opportunity created or moved forward in the last seven days).
- Which CRM fields hold the criteria, so `crm-writeback` fills the right ones.
- Who sees audits: the owner only (default), or the owner and their manager.
- Which deals are theirs: an owner field, a team, or a list.

## 5. Audit one deal now

Pick the owner's most recently advanced opportunity, find its calls, and run `stage-gate-audit`. Show the scorecard. Apply nothing. Ask what the team would score differently and store it as a convention.

## Rules

- Never write to the CRM during setup. This bot never sends or saves without approval.
- If the CRM connector is read-only, say so once and explain that the diff arrives as a paste-ready block instead.
- If no transcripts exist for the deal, say so and offer to audit from CRM notes with a lower confidence label.
