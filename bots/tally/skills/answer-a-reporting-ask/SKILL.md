---
name: answer-a-reporting-ask
description: "Use when someone asks for paid media numbers in a channel, or when the user pastes a reporting ask and wants the reply drafted."
---

# Answer a reporting ask

Part of the Paid Media Report Desk agent preset.

Inputs: the ask, the column map, the latest mapped exports, the metrics history, and the voice sample when one is saved.

1. Restate the ask in one line before you answer it: the metric, the platform, and the period you think they mean. When any of the three is unclear, ask the user who owns this bot, never the person who posted the ask.
2. Answer from the mapped exports and the metrics history only. Never recompute from memory, and never fill a gap with a figure from another period or another platform.
3. Check the data covers the period they asked about. An export that stops before the period ends gets said out loud in the reply, with the dates you actually have.
4. Write the reply short enough to read in a channel: the number, the comparison the ask implies, and one line of context. Three or four lines is usually right. A full table belongs in the report, not in a channel.
5. Match the saved voice sample when there is one, otherwise plain and direct. No greeting theater, no closing question.
6. Show the user the draft and the channel it would go to, then stop. Post only on an explicit yes, and post it as written unless they edit it.
7. When the exports on hand cannot answer the ask, say which export and which date range would answer it, and draft a two-line holding reply the user can send in the meantime.

Output: the ask restated, the draft reply, the numbers behind it and where each came from, and the gap when there is one.

Fallbacks: no Slack means the user pastes the ask here and you draft the same reply for them to copy. A screenshot of the ask works.

Log the ask, the draft, and whether it went out under paid media reports.
