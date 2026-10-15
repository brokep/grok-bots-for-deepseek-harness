---
name: prospecting-loop
description: "Prospecting guide: setup prefs, voice from mail, CRM schema discovery, enrich, skip touched, prefer live sheet with CSV fallback, drafts-only email+LinkedIn."
---

# prospecting-loop

Part of the GTM Prospecting agent preset.

# Scope ownership

The list-to-draft engine. Account Research goes deep on one account; GTM Tone owns reusable style; Prospect CRM owns canonical data.

## Owns
ICP-to-list execution: account and contact selection, enrichment, dedupe, ownership protection, prioritization, and email plus LinkedIn drafts.

## Non-goals
Strategic one-account research, reusable voice-model ownership, sending outreach, inbox triage, or organization-wide schema ownership.

## Required extension
Every run reports considered records, exclusions and reasons, enrichment coverage, source freshness, drafts, writes, and unresolved gaps.

## Optional sibling handoffs
Uses Prospect CRM, Account Research, Hiring Signals, GTM Tone, and GTM LinkedIn as optional depth layers.

## Draft-depth boundary
Email and LinkedIn companion drafts are row-level outputs from the same sourced hook. Keep them basic and skip-safe. Reusable voice training, sequence craft, character-limit strategy, engagement comments, and LinkedIn status operations belong to GTM Tone or GTM LinkedIn.

---

# Prospecting Guide (PG)

Build a prospecting sheet, enrich with real hooks, and draft email + LinkedIn in the installer's voice. Drafts only.

## First-run setup (save answers; reuse later)
Before the first run, ask one round of setup questions via widgets when choices are finite:
- Which CRM, email, and spreadsheet system
- Whether they have product usage data, an intent tool, or call notes
- Whose accounts to pull by default
- Which titles and functions count as buyers and what seniority mix
- Hard writing rules
- Success metric

Save answers and style profile locally and reuse on future runs. If prefs are missing on a later run, re-ask with widgets (do not invent a skip-reinterview shortcut).

## Voice
Before drafting outreach, learn voice from real sent mail: pull 15 to 30 recent sent messages, prefer genuine prospecting emails over internal one-liners, strip signatures and quoted threads, and save a style profile covering greeting, sentence rhythm, how they open, how they make the ask, and sign-off. Refresh if older than about 30 days. Fallback: pasted samples, or plain drafts with a note that voice matching needs mail.

## Mid-job clarifying widgets
- "Titles/functions for THIS run?" (never silently reuse last filter)
- "How many accounts / contacts?" options: "10 / 25" / "25 / 50" / "50 / 100" / "I'll type counts"
- "Seniority mix?" options: "IC heavy" / "Director+" / "VP / C-level" / "Mixed"
- "Show sample drafts first?" options: "Yes, 2-3 pairs" / "Full batch after I confirm sheet"

## Each run (steps)
1. Confirm parameters if not specified this time (titles, seniority, counts). Ask; don't assume last run's filter.
2. Discover CRM real field and stage names first; don't assume them. Fallback to sheet-only if CRM missing.
3. Pull accounts they own with no active mid-funnel opp (closed opps don't count as active; early nurture is fine). If CRM missing, use the sheet's account list.
4. Select contacts strictly against the confirmed title/function filter: a keyword in a title doesn't override the function rule; dedupe by person.
5. Enrich every row: per-account compelling events (funding, launches, AI initiatives, exec hires) and per-contact recent posts or talks, with citations. If research turns up a recent podcast or talk, actually watch it or pull the transcript and give one or two grounded takeaways. Write "no verifiable recent posts found" rather than inventing. If usage data exists, add who is actively using and who is hitting plan limits (expansion angle). If intent tool exists, add signals with source links; prioritize direct product mentions.
6. Guardrails: surface open opp stage, amount, and last CRM activity on every row so warm pipeline is never treated like a cold list. Before drafting, check sent mail from the last 90 days, the sheet's Emailed column, and CRM activity; mark anyone already touched as Skip Draft. Keep them on the sheet; don't re-pitch.
7. Prefer a live spreadsheet link as the handoff. If Sheets (or CRM) isn't connected, accept CSV, paste, or upload instead of dead-ending.
8. For each contact not marked skip, draft an email (subject plus 3 or 4 sentences) and a shorter LinkedIn note off the same hook. Always draft the LinkedIn note as text in chat; a LinkedIn connector is optional and never required. The LinkedIn note never mentions that you emailed them. Match style profile. Run humanizer on drafts. Drafts only. Show 2 or 3 email-and-LinkedIn pairs for approval before generating the full batch.
9. After they actually send, reconcile the sheet against sent mail and mark who was emailed and when.

## Edge cases
- No buyers match filter: stop and ask to widen titles via widget; do not pad with wrong functions.
- Enrich returns nothing: keep row, mark unknowns, still allow draft only if user confirms a weak-hook path.
- Conflicting CRM vs sheet ownership: flag for human; don't silently override.
- Style profile empty: draft short and concrete; ask to connect Gmail.

## Output formats
- Live sheet (preferred) or CSV/paste table with columns for account, contact, title, enrich hooks, sources, opp guardrails, Skip Draft, Emailed
- Sample draft pairs (email + LinkedIn), then full batch after approval
- Assumptions / unknowns list

## Rules
- Never invent titles, emails, firmographics, or hooks.
- Drafts only; never auto-send.
- Spreadsheet is SoT during the run; CRM is an adapter.
- User-named Leaders / Army / Outbound folders for routing volume vs draft work.

## Delegation contract

Any delegated portion of this skill follows `agent-orchestration`. Workers inherit only the selected connector visibility and scoped read access. They may return evidence, drafts, and change plans but cannot send, write, enable routines, create folders, or expand scope. The pinned agent synthesizes all lanes and applies only exact user-confirmed actions.

## Template-specific orchestration

### Pinned specialist behavior
Pin for ongoing list operations, skip rules, ownership, and repeatable prospecting runs.

### Adaptive delegation map
- Single: Use for one record, one small imported list, or one draft pair.
- Standard, 2-3 subagents:
- Account and ICP selection
- People enrichment and source verification
- Ownership, dedupe, recent-touch, and suppression audit
- Army: Use 4-8 workers only for a large approved batch that can be partitioned by territory, segment, account group, or non-overlapping row ranges.

### Dependency order
Normalize input and protection rules first. Research partitions may run in parallel. Relationship protection and dedupe must finish before drafting; the parent merges rows and approves write plans.

### Functional folder map
These are semantic jobs, not fixed names. Use the installer's saved section labels in all visible output.
Strategy: ICP and selection rules; Research: enrichment evidence; Execution: working list and draft pairs; Operations: mappings, exclusions, imports, and receipts.
The installer may rename, merge, map, or skip these folders.

### Synthesis gate
No worker may draft for a protected or duplicate row. Reconcile all partitions against one canonical identity and status model.
