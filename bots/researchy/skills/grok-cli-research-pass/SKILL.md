---
name: grok-cli-research-pass
description: "Use when running a live Grok CLI research or fact-check. Launch grok-4.6 xhigh, wait until the process exits, then deliver sourced dated claims immediately."
---

# Grok CLI research pass

Part of the Researchy agent preset.

---
name: Grok CLI research pass
description: >-
  Use when running a live Grok CLI research or fact-check. Launch grok-4.6
  xhigh, wait until the process exits, then deliver sourced dated claims
  immediately.
---
Use this for every live research or fact-check.

## Launch
- Binary: `grok` on this computer (`~/.grok/bin/grok`).
- Always: `--no-auto-update --reasoning-effort xhigh -m grok-4.6 --always-approve`.
- Live search on. Never a training-only pass.

## Wait
- After launch, wait on that same process until it exits.
- Do not end the work and hope a later ping arrives.
- If the user messages mid-run: acknowledge them, then check the run and keep waiting until it finishes.

## Deliver
- The moment the process exits, send the sourced, dated result.
- Do not wait for the user to ask whether it is done.
- If the run failed, say that immediately and the next step.
