---
name: crm-adapter
description: "Use this before reading or writing any CRM, whether it has a connector, runs through a browser sign-in, arrives as a CSV, or does not exist. Discovers real field and stage names and keeps writes behind an explicit yes."
---

# crm-adapter

Part of the Sequencer agent preset.

# CRM adapter

A CRM is optional and it is the user's choice of vendor. This skill covers all four cases without
assuming any of them.

## The four cases

1. **A CRM with a connector on this bot.** Connect it, discover the real object, field, and stage
   names, and read through the connector.
2. **A CRM with no connector.** The user signs in inside my browser through connect-accounts, and I
   read the views and record pages they point me at. Every number says which view it came from and
   when.
3. **A CSV export.** They export accounts, contacts, and open opportunities. Validate the columns
   before using them and put the export date on every number that comes from it.
4. **No CRM.** The tracker is the only source of truth. Ownership and pause rules become manual
   rules the user states once, and I say plainly which guards cannot run.

Ask which case applies during setup. Never present one vendor as the default, and never assume the
CRM this recipe was built on.

## Discover, do not assume

- Read the actual stage picklist, the actual opportunity object, the actual owner field. Stage
  labels differ in every instance and a hard-coded label is a silent bug.
- Save the discovered names in `/workspace/sequencer/state.md` as a short mapping: pause stage,
  owner field, activity field.
- Re-check the mapping when a read fails, before blaming the data.

## What I read

- Open opportunities on accounts that are on the tracker, for the pause guard.
- Owner, for the ownership filter.
- Recent activity, so nobody gets a cold opener while a colleague is mid-deal.
- Closed-won and meeting history, for title winners during discovery.

## Writing

Reading is the default and it covers the whole job. A write happens only when the user says yes to
that specific write in that conversation, for example logging a staged touch as an activity. Never
create, update, or delete a record from a routine. Never change a stage, an owner, or a field
definition. A routine that thinks a write is needed says so in the review list and waits.

## When the CRM is unavailable

Say so in one line, fall back to tracker-only pause rules, and name the guard that is off. Do not
stall the daily loop over it.

## Never

- Write without an explicit yes in that conversation.
- Assume a stage label, an owner field, or a pipeline shape.
- Export or copy bulk CRM records into memory or the state file. Save mappings and ids, not
  contents.
- Treat a connected CRM as permission to change anything in it.
