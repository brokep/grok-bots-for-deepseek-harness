Create my scheduled routines with schedule_create. Use my time zone and ask me once for the hour if the schedule below does not name one. Do not run them now, just create them.

- Title: Post-merge AC fail-gate
  Schedule: When a PR merges in the watched product repo, verify Production SHA and re-run the BLOCK AC pack; stay quiet on unchanged PASS.
  Prompt: Load the routine-listed-post-merge-ac-fail-gate skill and run it now.
