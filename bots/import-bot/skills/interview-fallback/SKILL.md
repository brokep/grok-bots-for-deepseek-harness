---
name: interview-fallback
description: "use this when there is little to import or a gap remains: six questions, then memory and experts from the answers"
---

# interview-fallback

Part of the Import Bot agent preset.

# Interview fallback

For a user with little or nothing to import, or to fill what the import missed. Short. One question at a time. Stop as soon as there is enough to write memory and plan one expert.

## Questions, only the ones the import did not answer

1. "What do you do, in one line, and who for?"
2. "What did you use <tool> for most? Name the three things that came up every week."
3. "For each, what goes in and what comes out?" A CSV, an inbox, a call recording. A brief, a draft, a table.
4. "Any rules you gave it that stuck? Tone, format, things it must never do."
5. "Which tools did it touch? Email, calendar, Slack, CRM, docs."
6. "How do you like to be talked to?" Quote the answer back as the voice line.

Six at most. Skip anything already known. Nothing about family or health unless they bring it up.

## Then

- Shared memory per write-user-memory, tagged [interview, date].
- Each weekly task is a work unit with the user's words as evidence. Plan per plan-experts, spawn per spawn-experts.
- Connectors from question 5 per connectors-encourage.
- Receipt as usual, with "Source: interview" in the sources line.

If they name a tool this bot does not import (Gemini, Perplexity, a custom agent), say: "Paste what it knew about you and I treat it like a memory note." Gemini keeps saved info under Settings, Saved info. Most tools print their memories if asked to "write out everything you remember about me, verbatim".
