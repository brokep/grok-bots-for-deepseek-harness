---
name: routine-weekday-hiring-signal-digest
description: "Scheduled routine: Disabled by default. Ingest selected sources, write normalized rows to the confirmed system of record, and deliver new or materially changed high-fit signals to the confirmed private destination."
---

# Weekday hiring signal digest

Part of the Hiring Signals agent preset.

Schedule, as written by the template author: Disabled by default. Ingest selected sources, write normalized rows to the confirmed system of record, and deliver new or materially changed high-fit signals to the confirmed private destination.

## What to do on each run

# Weekday hiring signal digest

This routine ships disabled.

## Enable gate
Confirm timezone, cadence, source scopes, normalized field map, exact Sheets/Notion destination, exact private digest destination, empty-result behavior, and approval boundary. Show the complete setup and require explicit confirmation before enabling.

## Authorized run
1. Pull only the configured sources and watched accounts or job families.
2. Normalize and deduplicate records using the saved schema and keys.
3. Write only the confirmed normalized fields to the confirmed Sheets/Notion destination.
4. Deliver only new or materially changed high-fit signals to the confirmed private digest destination.
5. Preserve source evidence, label partial coverage, and honor the saved empty-result behavior.
6. Save the last successful run and source cursors when supported.

Enablement is durable approval only for this exact scope. Any field, destination, source scope, or permission change pauses affected writes until the user confirms again. Never send customer-facing messages, write outside confirmed destinations, expand scope, or allow a subagent to write.
