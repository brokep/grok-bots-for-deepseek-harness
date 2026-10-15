---
name: build-the-hiring-tracker
description: "Use when the user first hands over roles, candidates, or scheduled loops, or when their source list changed and the tracker needs rebuilding."
---

# Build the hiring tracker

Part of the Recruiting Coordinator agent preset.

Inputs: a pasted list, an applicant tracking export from Greenhouse, Lever, Ashby, or Workday, a spreadsheet, a CSV, a shared sheet link, or forwarded candidate mail. Any one of them is enough to start.

Steps:
1. Read what they gave you and say which columns you found before changing anything.
2. Map their columns onto three lists:
   - Roles: role, level, hiring manager, target start, panel, stage the role is at, notes
   - Candidates: name, role, stage, source, owner, last contact, next step, waiting on, days in stage, notes
   - Loops: candidate, role, date, start and end in the user's timezone, interviewers, what each slot covers, status, scorecards in or out
3. Keep their wording for role titles, stage names, and notes. Normalize only dates and times.
4. Take contact details exactly as given. Never guess an email address, a phone number, or an employer, and never go looking for one.
5. Keep protected attributes out entirely. No age, no graduation year used as an age proxy, no gender, race, nationality, religion, health, disability, pregnancy, marital or family status. Drop any column like that out of an export and say in one line that you dropped it.
6. Rows you cannot parse go in a short "needs a look" list at the end of your reply. Never guess a stage or an owner.
7. Deduplicate candidates on name plus role, loops on candidate plus date. When two rows disagree, keep the newer one and say what changed.

Output: the tracker written to disk, a count of rows added and updated, the rows that need a look, then today's picture in the same reply so they see something real immediately: interviews today, who needs scheduling, and what is waiting on someone.

With no source at all, ask for five example rows and build from those.

Save under the hiring folder as roles.csv, candidates.csv, and loops.csv.
