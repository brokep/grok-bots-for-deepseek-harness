---
name: check-a-draft-against-the-bank
description: "Use when the user pastes a case study, deck, page, or post and wants every quote, number, and customer claim verified before it goes out."
---

# Check a draft against the bank

Part of the Customer Proof Desk agent preset.

Inputs: the draft, and the proof bank.

1. Pull every quote, number, customer name, and logo claim out of the draft and list them.
2. Check each one against the bank and give it one of four verdicts: matches the source word for word, differs from the source, not in the bank at all, or in the bank but not approved for this use.
3. Quote checking is character level. A changed tense, a dropped "really", a swapped "we" for "our team" all count as a difference. Show both lines and let them decide.
4. Numbers need a time period and a source in the draft itself, not only in the bank. Flag a bare number even when it is real.
5. When Hex is connected and the number is one their own data can settle, check it there and say which source you trust and why. A customer's remembered number and the measured one are both worth knowing about before publication.
6. Catch hedges that hardened into facts. "Helped us move faster" turning into "40% faster" is the failure this skill exists for.
7. Finish with the go list and the blocker list: what is safe to publish now, what needs a fix, and what needs an approval first.

Output: the item by item verdicts, then the short blocker list.

Rules: never verify your own invention. When something is not in the bank, say so and stop, do not go looking for a plausible source on the web to make it pass.
