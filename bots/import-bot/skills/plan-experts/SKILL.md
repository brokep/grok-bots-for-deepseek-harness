---
name: plan-experts
description: "use this to turn every project, task, skill, and recurring theme into the smallest set of expert bots that covers all of it"
---

# plan-experts

Part of the Import Bot agent preset.

# Plan experts

Turns everything imported into the smallest set of expert bots that covers all of it. Bots are scoped to expertise, never to projects. A project is work an expert owns, not a bot.

## 1. Gather work units

A work unit is one thing the person had a tool doing. List every one, with its source and evidence count:

- Cowork projects (`spaces[]`): instructions, notes, session_count, connectors.
- Cowork scheduled tasks (`scheduled_tasks[]`), each its own unit, linked to its project if `space_id` is set.
- Cowork plugin skills and any `Scheduled/**/SKILL.md`.
- ChatGPT projects and custom GPTs (`accounts.chatgpt.projects`, `gpts`).
- Claude chat projects (`accounts.claude.projects[]`, with `prompt_template`).
- OpenClaw and Hermes skills, and OpenClaw's MEMORY.md standing jobs ("Weekly: Monday territory digest").
- Codex and Claude Code: AGENTS.md, CLAUDE.md, skills, commands, repos seen in project dirs.
- Recurring themes: cluster session and conversation titles plus sample turns across every source. A theme needs 3 or more sessions. Use the transcript-toolkit search on the verbs that reveal routines: "every", "weekly", "each morning", "draft", "summarize", "follow up", "brief", "prep", "review", and on account and product names from memory.
- User-named workflows from setup. Highest priority. Each must land on exactly one expert and appear in the receipt by name.

Write them all to `/workspace/migration/pack/work-units.md` as a table: unit, source, evidence, connectors seen.

## 2. Assign each unit one expertise

Use this taxonomy. Pick by what the unit produces, not by the tool it came from.

| Expertise | Signals |
|---|---|
| Writing and Outreach | draft, email, reply, follow-up, rewrite, tone, LinkedIn message, proposal |
| Research and Briefs | research, brief, news, competitor, account, prep, summarize a call |
| Sales Pipeline | pipeline, CRM, deal, forecast, stale, close date, Salesforce, Gong |
| Inbox and Calendar | triage, inbox, schedule, reschedule, calendar, unread |
| Engineering | code, PR, test, repo, deploy, bug, AGENTS.md, CLAUDE.md, Codex, Claude Code |
| Data and Reporting | CSV, table, dashboard, SQL, metric, report, spreadsheet |
| Content and Social | post, tweet, thread, newsletter, blog, video, clip |
| Recruiting | candidate, interview, sourcing, hiring, job description |
| Support | ticket, customer question, bug report, refund, help center |
| Personal Admin | travel, family, home, health, errands, budget, hobby |
| Ops and Finance | expense, vendor, invoice, procurement, supplies, contract |
| Design and Product | mockup, Figma, spec, roadmap, user research |

A unit that fits two: the expertise of its output wins (a "draft the pipeline summary email" task is Sales Pipeline, because the number is the point).

## 2b. Existing bots first

Before deciding what to create, read `/workspace/migration/existing-bots.md`, the user's current bots from setup step 2. For each, infer its expertise from its name, description, skills, and routines using the same taxonomy. Then:

- A unit whose expertise matches an existing bot is **proposed** for that bot, never sent on its own. The proposal names what would transfer (projects, scheduled jobs, notes, connectors) and the improvements the bot could take (bot-design-standard, "Improving an existing bot"). Nothing is duplicated and nothing moves until the user says yes for that bot.
- An existing bot that is a general assistant with no clear expertise is not a candidate. Leave it alone, mention it in the receipt as untouched.
- Only expertise no existing bot covers gets a new expert, set up once the user taps Set them up under the plan table (step 5). The cap of 5 counts new experts only.
- Never rename an existing bot or change its job. Suggest, in one line each, and let the user and the bot decide.

## 3. Merge to the optimal set

- An expertise with fewer than 2 units and fewer than 5 sessions merges into its neighbor: Content into Writing, Research into Sales Pipeline for a sales user or into Writing otherwise, Data into Engineering for a technical user or into Sales Pipeline otherwise, Ops into Personal Admin, Inbox into Writing, Recruiting into Research, Support into Writing, Design into Research.
- Cap at 5 experts. Over 5, merge the two smallest until 5.
- Floor at 1. A user with only chat memories and no workflows gets one expert for their dominant theme, named for it.
- A user-named workflow always earns coverage even with zero evidence elsewhere. It goes to the expertise it fits, or forces one if nothing else fits.

## 4. Name and scope each expert

Per the bot-design-standard skill: one job, a title of four words or fewer that says the job, a two-line card with the payoff in the first 90 characters, and two or three anti-jobs that each name a specific unit another expert owns ("pipeline numbers belong to <the other expert>"), so no two experts can be mistaken for each other.

Prescribe how the expert manages its units:

- Each owned project becomes a playbook skill `project-<slug>` on that expert: the project's instructions verbatim, its memory notes verbatim, a "how I run this" section you write from the sessions (inputs, steps, output shape), and three sample asks the user actually made.
- Each owned scheduled task becomes a routine on that expert, paused, per bot-design-standard.
- Each custom GPT becomes a skill `gpt-<slug>` holding its instructions and a line on when the user reached for it.
- OpenClaw SOUL.md and IDENTITY.md shape the voice lines of the expert closest to that agent's job. USER.md already went to shared memory.
- The expert's memory gets one fact per owned unit: "I own <unit>: <status or key fact, under 150 chars>." plus "Hand off to <other expert> for <their units>."
- Connectors: the union of `connectors_seen` across the expert's units, marked "used" with counts. Account-wide connectors seen only outside projects are "likely". Connectors the user has anywhere that Grok Bot offers and no expert claimed go to the receipt as "connect these too". A connector with no plugin gets the MCP path from connectors-encourage.
- Folders: every local folder its projects used, with the choice from project-folders (copied here, on request, or a connected drive).
- History seed: the 12 most recent sessions or conversations tied to the expert's units, for the transcript-toolkit seed command.

## 5. Write the plan

`/workspace/migration/pack/expert-plan.md`: one section per owner, existing or new, with title, card, anti-jobs, owned units, skills, routines, connectors, history seed count, and for existing bots the improvement suggestions. Then a coverage check: every work unit appears under exactly one owner, and every user-named workflow is present by name. Fix the plan until both are true.

Show the user a compact table (bot, existing or new, what it takes care of, scheduled jobs, connect for it, folders) with one line above it: "Here is the setup. New: <names>. For your existing <names> I have a proposal below, nothing goes to them until you say so." Under the table, one line: "Rename, move a project, or merge two of these any time by telling me."

Then one question widget for the new experts: "Set up these <n> new experts now? I create each one and hand it its notes." Options: "Set them up" and "Change something first". This is the yes Grok Bot wants before you message several bots at once, so nothing is created or messaged before it. "Change something first": take the change, show the table again, and ask again. A dismissed widget means not yet: say in one line that they can say go any time, and wait.

Then, for each existing bot, one short block and a question:

"**<Existing bot>** already covers your <kind of work>. I can send it your <project>, the <scheduled job> (paused), and <n> notes about <topic>. It could also use a first conversation and a quiet rule on its <routine>. Send these to <Existing bot>?" Options: yes, yes but skip the improvements, no, make a new expert for this instead.

Do not make the new experts wait on these answers. Set up the new ones as soon as the user taps Set them up, then handle each existing-bot answer as it comes. No answer means parked: the units are listed in the receipt under "waiting for your call" and adjust-experts can send them later.
