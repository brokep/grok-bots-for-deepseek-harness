---
name: capture-a-pasted-answer
description: "Use when the user pastes what an assistant told them, or when a prompt needs an assistant they are signed into and you are not."
---

# Capture a pasted answer

Part of the AI Search Visibility agent preset.

Inputs: the pasted answer, which assistant it came from, and the prompt they typed.

1. Ask for the prompt exactly as they typed it if they did not say. A paste without its prompt cannot be compared next week.
2. Save it as today's capture for that prompt and that assistant, dated and marked as pasted by them. It counts the same as one you fetched, and the brief treats it the same way.
3. Score the user and every company named, on the ladder: recommended, cited, mentioned, absent.
4. Pull the quoted sentence that names each company, and the source links when the assistant listed any. An assistant that shows no sources gets scored for position only, and you say that in one line.
5. Say what changed against the last capture for that prompt, in one or two lines. Nothing to compare against yet gets one line saying this is the baseline.
6. Offer to take the rest of the top prompts the same way while they are already in that assistant, and write those prompts out so they can copy them.

Fallbacks: a screenshot works, read the text off it and say back what you read. A partial paste gets scored for what it shows and flagged as partial. A paste from a chat that already had context in it is worth noting, since a fresh chat and a long one answer differently.

Save under the visibility folder.
