---
name: contact-ranking
description: "Picks and ranks the people to contact at each tiered account, Director-plus and power users first, deduped against CRM ownership and open deals, with verified emails where a tool can verify them."
---

# contact-ranking

Part of the Signal Prospector agent preset.

# contact-ranking

## When to use

After `account-tiering`, or when the owner asks who to reach at an account.

## Steps

1. Candidates: contacts already in the CRM for the account, people attached to the signals (a signup, a form fill, a job post's hiring manager), and, if Clay or the public web supports it, the functional leader and executive who own the KPI in the POV.
2. Rank: the champion or power user at Director level or above first, then the functional leader (VP or Director), then the executive whose strategy the signals point to, then individual users. Individual signups are evidence for the senior message, not the target, unless the owner sells to individuals.
3. Dedupe against ownership: skip contacts owned by another rep or attached to another rep's open opportunity, and say so.
4. Emails: use the CRM address if present. Otherwise ask Hunter to find and verify; if verification fails, mark the contact "no verified email" rather than guessing.
5. Attach the two best hooks per contact from the account's signal history.

## Output

Per account, up to three contacts: Name, Title, Seniority tier, Why them (one line), Hooks (two, sourced), Email status (CRM, verified, not found), LinkedIn or company bio link. Keep the whole list to the weekly target count stored in memory, top accounts first.

Offer a CSV of the full list. Offer to create CRM contacts for the verified new ones; create them only after the owner says yes.

## Rules

- Never message anyone. Never create CRM records without approval.
- Respect do-not-contact and unsubscribe flags in the CRM.
- No personal data beyond name, title, company, business email, and public statements.
