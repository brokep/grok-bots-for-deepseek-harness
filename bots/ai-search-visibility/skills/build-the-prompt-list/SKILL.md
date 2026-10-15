---
name: build-the-prompt-list
description: "Use when the user first describes what they sell, adds or drops a prompt, or asks which questions you are testing."
---

# Build the prompt list

Part of the AI Search Visibility agent preset.

Inputs: what they sell, their site URL, who they sell to, buyer region and language, and their rival names when they have them.

1. Read their site or their pitch and write two lines back: what you think they sell and who for. Take a correction before you build anything.
2. Write 12 to 20 prompts a real buyer would type or say out loud. Cover four kinds and label each one.
   - Category: "best X for Y", "X tools for a small team"
   - Problem: the pain in the buyer's own words, with no product name in it
   - Comparison: "X vs Y", "alternatives to X"
   - Brand: their own name, and "is X any good"
3. Use the buyer's words. A prompt built from a phrase only their team says is a prompt no buyer will ever ask. Write them in the language their buyers search in, and add the region when it changes the answer.
4. Mark the five they care most about as top prompts. Those are the only ones the spot check uses.
5. Show the list in chat as a short table: prompt, kind, top prompt yes or no. Take one round of edits, then save.

Fallbacks: no site and no pitch means you ask for one sentence on what they sell and build from that. A keyword list pasted out of an SEO tool is a fine starting point, translate each keyword into a question a person would actually ask. A category with no product yet still works, run the category and problem prompts alone.

Cap the list at 20 unless they ask for more. The prompt list is the source of truth for what gets tested, so edit it in the same turn the user adds or drops a prompt. Save under the visibility folder.
