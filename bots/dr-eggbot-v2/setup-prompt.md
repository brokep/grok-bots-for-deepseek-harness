Create my scheduled routines with schedule_create. Use my time zone and ask me once for the hour if the schedule below does not name one. Do not run them now, just create them.

- Title: transcript-healthcheck
  Schedule: Cron 44 8 * * 1-5 (weekdays 8:44 local). Scans recent bot transcripts for user friction; proposes skills/bots/routines; stays quiet when nothing is worth proposing.
  Prompt: Load the routine-transcript-healthcheck skill and run it now.

- Title: routine-healthcheck
  Schedule: Cron 49 8 * * 1 (Mondays 8:49 local). Audits fleet routines for token waste; reports fixes; stays quiet when nothing is worth proposing.
  Prompt: Load the routine-routine-healthcheck skill and run it now.
