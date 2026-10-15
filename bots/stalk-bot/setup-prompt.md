Create my scheduled routines with schedule_create. Use my time zone and ask me once for the hour if the schedule below does not name one. Do not run them now, just create them.

- Title: Competitor pulse
  Schedule: Disabled by default. Monday, Wednesday, Friday at 9am in the user's timezone (user can pick daily, weekly, or a custom cron). Runs every enabled module for every competitor and delivers the live brief with media, Against-us, For-our-site, Worth a decision, and Proactive suggestions. Quiet when nothing changed.
  Prompt: Load the routine-competitor-pulse skill and run it now.

- Title: Weekly deep dive
  Schedule: Disabled by default. Friday 10am, one competitor in rotation. Re-walks the product on video, re-runs the feature test pass, diffs against the previous teardown, and delivers a self-contained HTML report. Report only.
  Prompt: Load the routine-weekly-deep-dive skill and run it now.

- Title: Competitor churn watch
  Schedule: Disabled by default and only useful once a churn source is named. Weekdays at 10am in the user's timezone. Scans the churn source for customers lost to a watched competitor, writes the facts brief, and hands the winback body to the user's writing bot or a marked skeleton. Never sends. Quiet when there are no new cases.
  Prompt: Load the routine-competitor-churn-watch skill and run it now.
