Create my scheduled routines with schedule_create. Use my time zone and ask me once for the hour if the schedule below does not name one. Do not run them now, just create them.

- Title: Renewal window watch
  Schedule: Disabled by default. Weekly scan of the vendor database for contracts renewing inside the priority window (default 120 days) that have no Focus tag or thesis yet.
  Prompt: Load the routine-renewal-window-watch skill and run it now.

- Title: Monthly inventory refresh
  Schedule: Disabled by default. Monthly re-pull of Ramp cards and bills, diffed against the vendor database, with new vendors, spend changes, and dropped vendors flagged for review.
  Prompt: Load the routine-monthly-inventory-refresh skill and run it now.
