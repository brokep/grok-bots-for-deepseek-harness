---
name: merge-duplicate-leads
description: "Use when a new export lands, when the same person shows up twice, or when the user asks how clean the list is."
---

# Merge duplicate leads

Part of the Lead Pipeline Desk agent preset.

Inputs: the lead ledger, plus whatever rows just arrived.

Match in this order and stop at the first hit:
1. Same email, lowercased, ignoring plus-tags and the dots in gmail addresses.
2. Same person at the same company: first and last name matched loosely against the same domain.
3. Same domain, different person. Treat that as a second contact at one account, so link the rows and leave both in the ledger.

Merging rules:
- Keep the oldest created_on so the age of the lead stays honest.
- Keep the newest title, status, owner, and last_touch.
- Keep every source and campaign, joined with a comma, so attribution survives the merge.
- Join the notes with a date on each line.
- When two rows disagree on something you cannot rank, keep both values in the notes and flag the row.

Never merge on company name text alone, and never merge two people because their titles match.

Output: the count merged, the count linked as second contacts on an account, the merges you are least sure about, and the rows you left alone. Show the uncertain ones before you write anything and take one round of corrections.

Save a dated copy of the ledger before you write the merged version back, so a bad merge can be undone.

Save under the lead desk folder.
