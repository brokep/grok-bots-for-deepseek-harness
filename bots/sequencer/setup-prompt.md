Create my scheduled routines with schedule_create. Use my time zone and ask me once for the hour if the schedule below does not name one. Do not run them now, just create them.

- Title: Sequencer daily
  Schedule: Disabled by default. Weekday mornings at 8am in the user's timezone. Advances every due sequence step, stages the next touch as a draft, writes state back to the tracker, and posts one review list. Quiet when nothing is due.
  Prompt: Load the routine-sequencer-daily skill and run it now.

- Title: Daily prospects
  Schedule: Disabled by default. Weekday mornings at 7am in the user's timezone. Queues new prospects that match the confirmed ICP onto the tracker, up to the saved daily cap. Quiet when the cap is already filled.
  Prompt: Load the routine-daily-prospects skill and run it now.

- Title: Inbox triage
  Schedule: Disabled by default. Hourly from 9am to 5pm on weekdays in the user's timezone. Flags inbound mail and messages from people already on the tracker, with a suggested next action. Quiet when nothing needs a reply.
  Prompt: Load the routine-inbox-triage skill and run it now.

- Title: CRM sequence guard
  Schedule: Disabled by default. Weekday evenings at 6pm in the user's timezone. Pauses tracker rows where the CRM shows the saved open-opportunity stage, so nobody gets a cold touch mid-deal. Quiet when nothing changed.
  Prompt: Load the routine-crm-sequence-guard skill and run it now.
