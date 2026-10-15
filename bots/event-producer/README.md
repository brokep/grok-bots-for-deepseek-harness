# Event Producer
Turns your event details into a run of show, guest list, and day-of checklist. Tracks vendors, guests, dietary needs, and travel, and never sends a message without you.
Converted from the Grok Bot marketplace template by Jenna Nanpei (@jennananpei): https://x.ai/bot/marketplace/bots/event-producer

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/event-producer"
```

Then start a session and pick **Event Producer** in the preset selector. The bot's 8 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Event countdown check**: Every weekday morning, what is due, what is late, and what is still unconfirmed, with the days-out count, registrations against target, and the guest gaps that get expensive late.
- **Day-of brief**: On the morning of the event, the run of show with owners, vendor arrival times with phone numbers, the guest and dietary counts, and everything still open.
- **Post-event recap draft**: Two days after the event, drafts the recap from the trackers and asks for the three numbers it cannot know.

## Integrations the original bot used
- slack: Post the day-of brief and countdown checks in the channel your crew already reads.
- notion-workspace: Keep the event brief, run of show, and trackers where the team looks things up.
- linear: Give every prep task an owner and a due date in the tracker your team already uses.
- figma: Pull signage, name badges, and slide files from your real design files.
- Gmail: Vendor and invite mail waits in your drafts, unsent.
- Google Calendar: Load-in, the event, and vendor deadlines sit on a real calendar.
- Google Sheets: Keep the vendor tracker and guest list editable by the whole team.
