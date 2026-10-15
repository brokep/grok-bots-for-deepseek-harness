---
name: engineering-lead-digest
description: "Write the short status digest that replaces a stream of individual updates."
---

# engineering-lead-digest

Part of the Engineering Lead agent preset.

---
name: engineering-lead-digest
description: Write the short status digest that replaces a stream of individual updates.
---
Use at the end of the working day (or at the digest time the user chose), and when the user asks for status.

Format, kept to what fits on one screen:
- Needs you: items blocked on the user, each with the one action needed. Omit the section if empty.
- Ready to merge: PR links with one line each.
- Shipped: what merged or finished since the last digest.
- In flight: one line per active unit with its state (coding, CI, in review) and anything notable.

Rules:
- No per-agent play-by-play, no restating unchanged items in detail, no emoji walls.
- If nothing changed and nothing needs the user, send a one-line all-clear or skip the digest, per the user's preference.
- Link PRs and agents instead of pasting logs.
