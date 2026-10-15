---
name: run-the-case-study-pipeline
description: "Use when the user wants the customers ready to write, the drafts in flight, and the approvals waiting tracked somewhere their team can see, not just in chat."
---

# Run the case study pipeline

Part of the Customer Proof Desk agent preset.

Inputs: the proof bank and whatever the user says is in flight.

1. Sort every customer into four states: ready to write, drafting, waiting on approval, published.
2. One line each with the state, the date it entered that state, and the single thing that moves it forward.
3. When Linear is connected, mirror each item as an issue with the customer name in the title, the state as the status, and the blocking action in the description. Update the existing issue rather than opening a second one. Ask before you create issues the first time, and never close one on your own.
4. When Notion is connected and Linear is not, keep the same table on a page there.
5. With neither, keep the table in the tracker file and paste it into chat whenever they ask.
6. Flag anything that has not moved in 14 days, oldest first. Stories stall in approval far more often than in writing, so name who each one sits with and how long it has been there.
7. Never change a state yourself. A draft is not published until the user says it is.

Output: the four state table, the stalled list, and one line on what to do next.

Save under the proof bank folder.
