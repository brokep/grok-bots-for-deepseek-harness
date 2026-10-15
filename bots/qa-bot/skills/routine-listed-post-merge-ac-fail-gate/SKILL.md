---
name: routine-listed-post-merge-ac-fail-gate
description: "Scheduled routine: When a PR merges in the watched product repo, verify Production SHA and re-run the BLOCK AC pack; stay quiet on unchanged PASS."
---

# Post-merge AC fail-gate

Part of the QA bot agent preset.

Schedule, as written by the template author: When a PR merges in the watched product repo, verify Production SHA and re-run the BLOCK AC pack; stay quiet on unchanged PASS.

## What to do on each run

A PR just merged in the watched product repo (importer-configured).

1. If there is no binding PM cut: STATUS BLOCKED — ask the owner for a binding cut. Do not invent ACs.
2. Confirm the live PM cut still matches the canonical AC pack. If the cut is ambiguous, ask the PM role; do not invent ACs.
3. Verify Production (or Eng-named Preview) SHA via the deploy host. Mark SHA {slack_user} if you cannot confirm.
4. Ask the named password owner for credentials if not freshly confirmed. Never invent credentials.
5. Run the BLOCK suite from the owner's canonical pack path using their fixtures path. Exercise logged-out / public share.
6. Write run-YYYY-MM-DD-<slug>.md with report header + YAML footer. STATUS must be exactly PASS | FAIL | BLOCKED.
7. On FAIL: hand off to the Eng role + Chief role with STATUS FAIL, SHA, AC id, repro, evidence. On PASS after a prior FAIL: one line with share sample. On unchanged PASS: stay quiet — do not message the owner.

Never soft-pass BLOCK. Never heal or skip expected results. Do not write product code or open cloud agents.

Fires on:
- GitHub pr-merged

Ask the importing user for:
- GitHub repository
- Slack user
