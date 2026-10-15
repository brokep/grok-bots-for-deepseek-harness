---
name: team-celebrations-list
description: "Use when the user asks who has a birthday or work anniversary coming up, or the team celebrations routine runs."
---

# Team celebrations list

Part of the Office Ops Desk agent preset.

Inputs: the celebrations list, or a pasted roster with names and dates.

Steps:
1. Store month and day only. Never a birth year, never an age.
2. Anyone marked opt out stays off every reminder and every digest. Ask once whether anyone prefers to be left out, then honor it on every run after.
3. Look 14 days ahead from today and split into this week and next week.
4. Per person: name, team, occasion, the date, and days out. Include years on a work anniversary only when the start year is known.
5. Add one line of lead time when something inside five days needs a card to sign, a cake, or an order placed.
6. When an order is needed, offer to add it to the shipments ledger so it shows up in the daily status.

Output shape: two short lists, this week and next week, then the lead-time line. An empty window gets one sentence naming the next date.

Never take a date from a LinkedIn profile or a social post. Use only dates the user gave you.

Save under the office ops folder as celebrations.csv.
