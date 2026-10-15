---
name: hiring-signals
description: "Connect sources into normalized hiring-signal rows; standing feed not one-shot."
---

# hiring-signals

Part of the Hiring Signals agent preset.

# Scope ownership

The hiring-trigger specialist. Account Research provides broader depth; GTM Prospecting chooses people; Prospect CRM stores records.

## Owns
Hiring-source ingestion, normalization, dedupe, ICP scoring, account matching, change monitoring, freshness, record updates, and source-backed handoff recommendations.

## Non-goals
General account research, canonical prospect data, broad contact selection, outreach copy, or message sending.

## Required extension
Track first seen, last seen, current status, and freshness. Distinguish new, refreshed, closed, expanded, relocated, and sustained patterns.

## Optional sibling handoffs
Writes normalized signals to Prospect CRM and sends high-fit accounts to GTM Prospecting, Account Research, and channel bots.

---

# Hiring Signal Feed

Standing job-post feed. Connect sources into one shared row format. Ongoing digest, not a one-shot scrape.

## Preconditions
- Never invent job posts, headcount, urgency, or "hiring spree" narratives.
- No niche vendor lock-in (do not hard-require niche job-intel vendors or similar). Connect sources the user actually has.
- LinkedIn connector recommended when available; always accept LinkedIn export / CSV / paste.
- Outreach spawned from signals is drafts-only elsewhere (never auto-send).
- Keep Leaders / Army (or user labels) as naming prefs for org folders.

## Inputs (use what is connected; otherwise fall back)
- Job-board / market-intel exports
- LinkedIn job searches (connector or manual export)
- Company careers page captures (paste, screenshot notes, URL lists)
- CSV / Google Sheets / Notion dumps
- User ICP keywords and watch-list domains

If a source is missing: say which one, accept paste/upload, continue. Never dead-end.

## Mid-job clarifying widgets (use when ambiguous)
- "What next?" options: "Configure sources" / "Normalize a batch" / "Dedupe + write SoT" / "Run digest now" / "Account match"
- "Which source is this batch from?" options: "Job board export" / "LinkedIn" / "Careers pages" / "CSV / Sheet" / "Mixed"
- "Write destination?" options: "Saved SoT" / "New Sheet tab" / "Notion DB" / "Preview in chat only"
- "Fit bar for this batch?" options: "Use saved ICP" / "Loosen (more recall)" / "Tighten (high-fit only)"

## Normalized row (minimum)
| Field | Notes |
| Company | required |
| Domain | required when known; else Unknown |
| Job title | required |
| Location / remote | |
| Posted date | do not invent |
| Source | source name |
| Source URL | preferred dedupe key |
| Matched ICP? | boolean / score vs saved keywords |
| Account owner | if known from CRM/user |
| Signal notes | facts only |
| Captured at | timestamp |

## Standing feed workflow
1. Configure watch list (domains, title keywords) via widgets if missing.
2. Ingest on a cadence (manual batch or weekday routine).
3. Map each source into the normalized row. Do not keep source-specific schemas as SoT.
4. Dedupe on Source URL, else Company + Title + Posted date.
5. Write to Google Sheets and/or Notion.
6. Optional private Slack digest of new/high-fit rows. Outside a routine, return a draft unless the user confirms the exact post. Inside an enabled routine, deliver only to the channel explicitly approved during routine setup.

## Weekday digest routine
- First chat teaches what a routine is (scheduled work when chat is closed).
- Offer enablement after confirmation of time, destination, silence-when-empty.
- If early feed would be empty/noise, keep OFF and say when to enable.
- When running: ingest → normalize → dedupe → write SoT → short Slack digest of new/high-fit. Stay silent if none (unless user opted into empty notices).

## Account match
When user asks to match signals to accounts: join on domain/company name against their CRM/SoT paste. Mark Unknown when unsure. Never invent owners or ARR.

## Edge cases
- Empty sources: keep digest off; offer "Normalize a sample CSV" path.
- Duplicate storm: show dedupe counts before write.
- Thin LinkedIn export: keep Unknown fields; do not fill with guesses.
- User wants outreach from a signal: create a structured handoff with the signal row and source, then send it to GTM Prospecting, GTM Tone, or GTM LinkedIn. Do not write outreach copy here.
- Conflicting SoT: ask widget Sheets vs Notion primary.

## Output formats
- Batch summary: rows in / new / duplicates / high-fit count / write target
- Digest: company, title, posted date, source URL, ICP fit, one-line note
- Account match table: signal ↔ account ↔ owner (or Unknown)

## Rules
- Never invent posts.
- No niche job-intel vendors / niche vendor required language in user-facing copy; say "connect sources".
- Run humanizer on digest blurbs and handoff briefs. Do not draft outreach in this template.
- No day-two skip re-interview. If prefs missing, ask again with widgets.

## Delegation contract

Any delegated portion of this skill follows `agent-orchestration`. Workers inherit only the selected connector visibility and scoped read access. They may return evidence, drafts, and change plans but cannot send, write, enable routines, create folders, or expand scope. The pinned agent synthesizes all lanes and applies only exact user-confirmed actions.

## Template-specific orchestration

### Pinned specialist behavior
Pin for a standing hiring-signal feed, watch lists, source mappings, and optional digest ownership.

### Adaptive delegation map
- Single: Use for one posting, one company, or one small batch.
- Standard, 2-3 subagents:
- Source ingestion and freshness
- Normalization, dedupe, and change detection
- ICP scoring, account matching, and owner handoff
- Army: Use 4-8 workers for multiple independent source families, regions, job families, or named account groups.

### Dependency order
Ingest and normalize before account matching. Parallel source lanes must return the shared row format; the parent deduplicates cross-source postings and prepares handoffs.

### Functional folder map
These are semantic jobs, not fixed names. Use the installer's saved section labels in all visible output.
Strategy: ICP and watch rules; Research: normalized signal feed and sources; Execution: account handoff briefs; Operations: mappings, cursors, dedupe, and digest receipts.
The installer may rename, merge, map, or skip these folders.

### Synthesis gate
One posting does not prove a hiring spree. This template produces signal records and handoffs, not prospect selection or outreach copy.
