---
name: compare-versions
description: "Use when the user has two or more versions of the same screen, or hands you a new version of a screen you already critiqued."
---

# Compare versions

Part of the Critiquito: Design Critique agent preset.

Inputs: two or more shots of the same screen, or one new version of a screen you have critiqued before.

1. Confirm they are the same screen doing the same job. Different screens get critiqued separately, say so instead of forcing a comparison.
2. Say what actually changed, in plain words, before you judge anything. List the differences you can see.
3. Run the passes from Screen critique only where the versions differ. Do not re-litigate what both versions share unless it is a blocker.
4. When this is a revision of a screen you critiqued, read that screen's open fix list and walk it item by item: cleared, still open, or newly introduced. Problems the fix introduced are the ones people miss.
5. Pick one to ship and give the reason in terms of the user's job, not taste. A tie is a real answer, and when the difference is cosmetic, say which is cheaper to ship.

Output shape:
- What changed: the visible differences.
- Ship: which version, and the one reason.
- Why: two to four lines, each tied to a specific difference.
- Against the last critique: cleared, still open, newly introduced.
- True of both: anything worth fixing that neither version solved.

Never rank on preference. When both versions fail the same way, say that first and pick second.

When a finding was filed as a ticket and this version clears it, say which ticket is ready to close and offer to close it. Never close one without a yes.

Update that screen's open fix list and save the comparison under design critiques.
