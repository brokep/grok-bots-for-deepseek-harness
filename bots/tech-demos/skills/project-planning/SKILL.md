---
name: project-planning
description: "Use when starting a new project, scoping an idea, choosing a stack, or producing an MVP implementation plan — an opinionated Bun/shadcn planning skill."
---

# Project planning

Part of the Tech Demos agent preset.

---
name: Project planning
description: >-
  Use when starting a new project, scoping an idea, choosing a stack, or
  producing an MVP implementation plan — an opinionated Bun/shadcn planning
  skill.
---
Turn a fresh project idea into a focused, MVP-first plan that favors prebuilt solutions and opinionated frameworks over custom complexity.

## Workflow

1. Clarify the goal in one sentence and define the single-user MVP boundary: what ships in the first cut, what is explicitly out of scope.
2. Decompose the goal into a small set of manageable tasks. Group by user-visible outcome, not by layer.
3. Spawn subagents in parallel to research frameworks and libraries that could absorb whole tasks. Prefer pre-built solutions unless a clear constraint rules them out.
4. Start from an official scaffold or starter via bunx create-* (bunx create-next-app, bunx create-vite, bunx create-t3-app, bunx create-tanstack, bunx create-expo) instead of hand-rolling the project skeleton.
5. Before any dependency install in the new project, create or preserve bunfig.toml with [install] minimumReleaseAge = 259200. Prefer scaffold flags that skip the initial install, then run bun install.
6. Pick an opinionated framework (e.g. Next.js, TanStack Start) when it improves organization and removes wiring decisions. Skip framework-grade tooling for one-screen utilities. Ask the user which framework to use if unclear.
7. For UI, initialize shadcn/ui with bunx shadcn@latest init and choose a minimalist preset — prefer shadcn blocks. Pull in components on demand, not preemptively.
8. Lay out components and services in a logical, opinionated structure before any code is written.
9. Decide the minimum useful testing surface and the minimum useful git-hook surface. Both default to small.
10. Produce a short plan: goal, MVP scope, task list, stack choices with one-line rationale, deferred items.

## Planning Rules

* Build for one user first.
* Use Bun as the runtime, package manager, and script runner by default.
* Start every new project from an official scaffold or template via bunx create-*.
* Every Bun project must include a root bunfig.toml with minimumReleaseAge = 259200 under [install] before bun install or bun add.
* For UI, default to shadcn/ui with a minimalist preset. Add components with bunx shadcn@latest add <component> as needed.
* Prefer prebuilt over bespoke.
* Choose boring, well-documented defaults. Novelty is a cost, not a feature.
* Cut features before cutting clarity.
* Pick one opinionated framework per project.
* Organize by feature or domain, not by file type, once there is more than one screen.
* Write tests for critical logic and infrastructure only.
* Use git hooks for formatting and fast static checks only.
* Defer anything not on the path to a working MVP.
* Re-evaluate the plan once the first end-to-end slice runs.

## Subagent Use

* Launch independent research subagents in parallel: one per framework or library question.
* Give each a self-contained brief: problem, constraints, what a good answer looks like, length cap.
* Ask for a recommendation plus the main tradeoff, not a survey.
* Do not delegate the final decision. Synthesize yourself.

## Output Shape

A good plan is short, opinionated, and falsifiable:

- Goal in one sentence
- Single-user MVP + explicit outs
- Outcome-oriented task list (vertical slices)
- Stack with one-line rationale each
- Deferred items and why
