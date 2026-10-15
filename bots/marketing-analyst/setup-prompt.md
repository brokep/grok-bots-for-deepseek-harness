Create my scheduled routines with schedule_create. Use my time zone and ask me once for the hour if the schedule below does not name one. Do not run them now, just create them.

- Title: Reporting ask watch
  Schedule: Disabled by default. Hourly during weekday working hours in the user's timezone. Reads the mailbox or label the user named for paid media reporting asks, drafts a reply with the real number, the date range, and the source file, and stays quiet when there is no new ask.
  Prompt: Load the routine-reporting-ask-watch skill and run it now.

- Title: Weekly paid media report
  Schedule: Disabled by default. Monday mornings in the user's timezone. Builds last week's paid media report from the exports on hand, or names exactly which export and which date range is still missing. Draft only.
  Prompt: Load the routine-weekly-paid-media-report skill and run it now.

- Title: Monthly paid media report
  Schedule: Disabled by default. The 1st of the month in the user's timezone. Builds the closed month's report with the three month trend, the campaign rollup, and budget pacing when a budget is on file. Draft only.
  Prompt: Load the routine-monthly-paid-media-report skill and run it now.
