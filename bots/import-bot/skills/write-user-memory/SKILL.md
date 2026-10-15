---
name: write-user-memory
description: "use this to distill everything the old tools knew about the person into shared user memory, write it, show it, keep originals verbatim"
---

# write-user-memory

Part of the Import Bot agent preset.

# Write user memory

Puts what the old tools knew about the person into Grok Bot's shared user memory, so every bot they have or create reads it on its next new conversation. Write first, then show the list. The user strikes what they do not want.

## Sources, in priority order

1. Rules the user wrote: Cowork CLAUDE.md, ChatGPT custom instructions, OpenClaw USER.md and SOUL.md, Hermes USER.md, Codex and Claude Code AGENTS.md and CLAUDE.md. Highest confidence.
2. What the tools inferred: Cowork global memory notes, ChatGPT memories, Claude account memory (`memory_text`, `export_memory.conversations_memory`), OpenClaw MEMORY.md and dated notes, Hermes MEMORY.md, Codex memories. Newest wins a conflict.
3. Session and conversation sample turns. Voice and recurring asks only. Never facts about the person.

Project-scoped material (Cowork space notes, ChatGPT project instructions, Claude project prompts and per-project memories, custom GPT instructions) does NOT go here. It goes to the expert that owns the project.

## Budgets

Other bots show shared facts in a section of their own: profile up to 4,000 characters and log up to 2,000, counted per rendered line. Every line carries about 40 characters of prefix ("- (learned <date>) [via <this bot's name>] "), and the newest facts win, so an overflow cuts your last facts and pushes out facts the user's other bots saved. Leave room for those:

- Profile, at most 16 facts, each under 150 characters, fewer when shared profile facts already exist (keep all shared profile lines under 3,600 characters): role and team, how they want to be addressed, voice rules, hard limits (never send on my behalf, no prices unless pasted), working hours, top recurring contexts (accounts, products, people, projects by name).
- Log, at most 5 facts, each under 200 characters (all shared log lines under 1,800): the preferences, corrections, and formats most likely to matter. The rest stays in the archive file.

One sentence each, present tense, self-contained, their wording when they wrote it. Source tag in brackets: [Cowork CLAUDE.md], [ChatGPT memory], [OpenClaw SOUL.md], [Hermes USER.md], [Codex memory 2026-09-01]. Keep tag text stable so a resync does not duplicate.

Drop: anything that looks like a credential, anything about one past task with no reuse, anything a stranger should not read that the user did not write themselves (health, family) unless it is a stated working preference. When two tools disagree, keep the newer and note the older in the archive file.

## Read what is already there

Before writing, read the user's existing shared memory: the user-memory folder named in your context (one shard per assistant, each a profile.md and a log folder), or RecallMemory with scope user. Count those lines against the budgets above. A fact that is already there, in the same or close wording, is not written again and is not shown as new. The store also dedupes exact text, so a re-run is safe either way. Show returning facts under a third header, "Already known", only when the user asks.

## Write, then show

Write every fact with `update_state` (memory write, scope user, tier profile or log). Then paste the numbered list under two plain headers, "Always in mind" (profile) and "Good to know" (log), never the words tier, profile, log, or scope, and say: "Saved. Every bot you have or create will know these from its next conversation. Say strike and a number to remove one." On a strike, `update_state` memory forget with the exact text.

## Preserve everything, verbatim

1. `/workspace/migration/pack/instructions.md`: every rules file, labeled by source.
2. `/workspace/migration/pack/memories.md` (the archive file): every memory note and memory entry, labeled by source, file, and date.

Answer later questions about what the old tools knew from these two files.

Tell the user in one line that the originals are kept word for word, without naming files or skills: "I kept every original note word for word too, in case you ever want them."
