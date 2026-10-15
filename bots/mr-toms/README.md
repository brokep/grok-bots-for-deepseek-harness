# Recruiting Coordinator
Schedules interview loops, preps your interviewers, and chases what's stalled. Works from your calendar or a pasted list, and never emails a candidate without you.
Converted from the Grok Bot marketplace template by Tommy Hansen (@TommyHansenTA): https://x.ai/bot/marketplace/bots/mr-toms

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/mr-toms"
```

Then start a session and pick **Recruiting Coordinator** in the preset selector. The bot's 8 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Daily hiring brief**: Every weekday morning, today's interviews, who still needs scheduling, and what is waiting on someone.
- **Evening interview prep**: The evening before, a prep packet for each of tomorrow's interviews with the competency, questions, and open items per slot.
- **Afternoon loop check**: Every weekday afternoon, what went stale since the morning brief, each item with a drafted nudge.
- **Urgent thread check**: Through the workday, flags a candidate or interviewer message that threatens a booked loop and drafts the reply.
- **Candidate reply drafts**: Through the workday, leaves an unsent draft reply for each new candidate email so the user only edits and sends.
- **Interview coaching review**: Once a week, coaches the scorecards and messages the user queued and flags ratings written without evidence.
- **Weekly pipeline review**: Every Friday afternoon, what moved per role, who is stuck and with whom, next week's interview load, and the calls that need the user.

## Integrations the original bot used
- slack: Post a hiring brief or an interviewer nudge you approved to a channel you choose.
- notion-workspace: Keep the hiring tracker, prep packets, and debrief summaries where the hiring team already looks.
- linear: Open a task for an approved req, a take-home review, or a new hire's first week.
- figma: Open a design candidate's portfolio or take-home file so the panel reviews the real work.
- Gmail: Search, read, draft, and manage email.
- Google Calendar: Search events and schedule meetings.
- Granola: Pull interview notes and action items straight from your meetings.
- Google Sheets: Read and write Google Sheets.
- Ashby: Search candidates, prep interviews, and manage pipeline tasks.
