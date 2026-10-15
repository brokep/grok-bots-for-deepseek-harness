---
name: pilot-test-activate
description: "Use this after approval of a versioned Build Pack or material patch, to safely test before activation. Never use activation as the first test."
---

# Pilot, Test & Activate

Part of the Alfred agent preset.

---
name: 'Pilot, Test & Activate'
description: >-
  Use this after approval of a versioned Build Pack or material patch, to safely
  test before activation. Never use activation as the first test.
---
# Pilot, Test & Activate

Safely test an approved design before activation. Use after approval of a versioned Build Pack or material patch. Never use activation as the first test. Never invent test results.

## Workflow

1. Confirm the approved version and scope.
2. Use read-only, draft-only, mock, synthetic, or reversible inputs.
3. Run one representative normal example.
4. Compare expected and actual behavior.
5. Obtain human correction.
6. Run a second materially different normal example.
7. Run at least one exception case.
8. Test missing input, stale source, conflicting source, ambiguous request, permission failure, connector failure, duplicate trigger, partial completion, consequential action without approval, and out-of-scope request.
9. Diagnose failures before changing instructions.
10. Change one uncertain variable at a time.
11. Show the configuration diff.
12. Re-run affected and regression tests.
13. Return Go, Conditional go, Repair, or No-go.
14. Require the human reviewer to make the go-live decision.
15. Require separate explicit approval before activation.
16. Update the Registry and change log when approved.

If the workflow cannot be tested safely, keep it read-only, draft-only, or manual.

## Output

Return:

- Test matrix
- Expected versus actual behavior
- Evidence
- Failures and root causes
- Configuration diff
- Remaining limitations
- Success baseline
- Go, conditional go, repair, or no-go
- Exact activation action awaiting approval

## Stop point

Never activate without separate explicit approval.

Never invent test results. Never claim a component was installed or verified unless the live environment actually confirms it.
