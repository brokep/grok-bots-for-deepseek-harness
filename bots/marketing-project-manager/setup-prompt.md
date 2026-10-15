Create my scheduled routines with schedule_create. Use my time zone and ask me once for the hour if the schedule below does not name one. Do not run them now, just create them.

- Title: Weekday status check-in
  Schedule: Disabled by default. Weekdays at 9am in the user's timezone (the user can pick a different time or cadence). Runs one status pass across the workstreams, attaches a screenshot for every artifact it names, chases anything past its date once, and lists the gates waiting on the user. Quiet when nothing moved.
  Prompt: Load the routine-weekday-status-check-in skill and run it now.

- Title: Friday week ahead
  Schedule: Disabled by default. Fridays at 4pm in the user's timezone. Lists what is due in the next 7 days, what the user has to decide to keep the date, and what is already late, read from the plan and the work items. Quiet when nothing is due and nothing is late.
  Prompt: Load the routine-friday-week-ahead skill and run it now.
