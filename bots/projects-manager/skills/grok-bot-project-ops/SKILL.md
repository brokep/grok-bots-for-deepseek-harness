---
name: grok-bot-project-ops
description: "Use this when creating or running a Grok Bot project: Notion Projects and Tasks, staffing, sidebar Projects placement, bots claiming work, and pinging the user when blocked. Every Project and Task row must have a page icon. Task Blocked is a Status value. Use Note for the question or context."
---

# Grok Bot project ops

Part of the Projects Manager agent preset.

---
name: Grok Bot project ops
description: >-
  Use this when creating or running a Grok Bot project: Notion Projects and
  Tasks, staffing, sidebar Projects placement, bots claiming work, and pinging
  the user when blocked. Every Project and Task row must have a page icon. Task
  Blocked is a Status value. Use Note for the question or context.
---
Operating loop for the user's project rooms. Notion is the source of truth. A Grok Bot channel is the shop floor. The user decides. Agents execute.

## Boards

Two Notion databases under the user's workbench:

- Projects: one row per project. Fields: Project name, Status (Backlog / Planning / In progress / Paused / Done / Cancelled), Channel (Grok Bot channel id), Bots (comma-separated agent names), Tasks (relation).
- Tasks: one row per task, always related to a Project. Fields: Task name, Status (Not started = todo, In progress, Blocked, Done, Archived), Project (relation), Bot (the Grok Bot name that claimed it), Note (text: blocked question, context, or leftover), Assignee (Notion person, usually leave empty), Due (optional).

Treat Not started as Todo. There is no Review status. There is no Blocked checkbox. Blocked is a Status value. Use Note for the question or any other short context.

Look up the live database URLs from Projects Manager's profile or from the user's workbench page. Do not hardcode stale IDs in other skills.

## Icons

Every Project row and every Task row must have a page icon (emoji). This is the Notion page icon, not a property column.

- Never create a row without icon set.
- Pick one emoji that matches the work. Distinct enough to scan the board.
- If you find a row with no icon, set one before doing anything else on it.

## Staffing

Projects Manager owns who sits in the room.

1. Start from the existing specialist roster. Prefer reuse over a new bot.
2. Propose a roster of at most 5 specialists besides Projects Manager (channel cap 6).
3. Create a new bot only when no existing specialist can do the work, and only after the user says yes. Do not spawn for a one-task gap a generalist can cover.
4. Name a project-only bot after the project (or ProjectName Role if several). Give it a tight brief: what this project is, what it owns, what it must not do, and that it follows this skill.
5. After creating: add the name to Projects.Bots and seat it in the channel.
6. Agents cannot be deleted by bots. When the project is Done or Cancelled, tell the user which project-only bots to delete from the sidebar (right-click the agent row, Delete).

Do not create bots speculatively. Do not duplicate an existing specialist under a new name.

## Starting a project

Only Projects Manager does this, after the user names the project.

1. Staff the room (see Staffing). If the user already named the bots, use that roster. Otherwise propose one from existing specialists.
2. Create a Projects row in the Projects database under the user's workbench (never a private or workspace-level page). Status Planning or In progress. Bots = the roster (existing names, plus any newly created ones the user approved). Set a page icon.
3. Create a Grok Bot project with the same name so it lives in the Projects section of the sidebar, then create a Grok Bot channel named after the project.
4. Seat Projects Manager plus the specialist bots. Channel cap is 6 members. If the roster would exceed that, ask the user which 5 specialists besides the PM.
5. Write the channel id into Projects.Channel.
6. Confirm to the user with the Notion project link and that the room is open.

Do not create a channel without a Projects row. Do not create a sample project unless the user asked. Do not leave a new project as a private Notion page or a loose chat outside the Projects sidebar section.

## Creating a task

From the project channel (the user or a bot):

1. Create a Tasks row.
2. Set Task name, Project = this project, Status = Not started, Bot empty. Note optional. Set a page icon that matches the task.
3. Confirm in the channel with the Notion link.

## Claiming and doing work

Specialist bots in the project channel:

1. Query Tasks for this project where Status is Not started and Bot is empty.
2. Pick one you can actually do. One bot per task.
3. Set Bot to your exact agent name, Status to In progress.
4. Do the work. Put useful leftovers in Note. Update the task page if useful.
5. When finished: Status Done, leave Bot set.

Do not grab a task another bot already claimed. If nothing fits, say so in the channel and leave it.

## Blocked

If you cannot continue without the user:

1. Set Status to Blocked.
2. Put the exact question or missing input in Note.
3. Ping the user in the project channel (and Projects Manager if you are not already talking to them). Wait. Do not guess.

When the user unblocks you: set Status back to In progress, update Note if needed, keep going, then mark Done.

## Projects Manager

Watches across projects. Does not do specialist work.

- Staffing: propose the roster, reuse first, create a new specialist only with the user's yes, then seat.
- Unowned Not started tasks: nudge the right specialist in that project's channel, or tell the user no bot fits (and propose creating one if that is the real gap).
- Status Blocked tasks: make sure the user has been pinged. Do not silently sit on them.
- New project / new task / roster change: the user asks the PM (in its own chat or in a project channel).
- Missing icons: set one. Do not leave a blank row on the board.

## Reporting to the user

Only surface what needs them: blocked work, no owner, a roster question, a request to create or delete a bot. Do not spam progress. They can read the Notion board.
