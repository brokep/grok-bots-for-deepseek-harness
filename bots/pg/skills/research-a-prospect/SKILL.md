---
name: research-a-prospect
description: "Use when a row needs research before anyone writes to it, on demand or from the weekday batch, or when the user asks what you know about a company or person."
---

# Research a prospect

Part of the Outbound Prospecting agent preset.

Inputs: one row or a batch of rows from the target list, plus what the user sells.

Work only from the public web. Never go behind a login, never pay for anything, and never read anything the person did not publish themselves.

Per row, fill what you can find:
- What the company does, in one sentence in their own words from their own site.
- The size or stage signal that is visible: a headcount range, a funding round, a customer logo wall.
- Why this person, in one line: what their title owns and how that meets the offer.
- One hook, dated, with a link. A hook is a specific recent thing this person or company did. A post they wrote, a talk or podcast they were on, a launch or changelog entry, a job post that points at a project, a funding round, a conference session.
- The tooling signal when it is public: a jobs page requirement, a docs page, an engineering blog post.

Rules:
1. Every field carries the URL it came from and the date on the source. No source, no field. Leave it blank.
2. Prefer the last 90 days for a hook. Anything older than a year is not a hook, so leave hook blank instead.
3. Never take a birthday, a home town, a family detail, or anything from a private or gated profile.
4. A person you cannot verify holds that role goes to on hold with a note. Nobody writes to an unverified row.
5. Set enriched_on and move status from new to enriched only when the row has a confirmed title and either a hook or a clear company reason.

Output: the enriched rows, each hook with its link and date, and a short list of rows you could not research with the reason for each.

Fallback: a company with nothing public in 90 days gets a company-level reason instead of a personal hook, and the row gets marked thin so the draft stays short and honest.

Write the rows back to the target list. Save under the prospecting folder.
