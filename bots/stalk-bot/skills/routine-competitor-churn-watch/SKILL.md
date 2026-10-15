---
name: routine-competitor-churn-watch
description: "Scheduled routine: Disabled by default and only useful once a churn source is named. Weekdays at 10am in the user's timezone. Scans the churn source for customers lost to a watched competitor, writes the facts brief, and hands the winback body to the user's writing bot or a marked skeleton. Never sends. Quiet when there are no new cases."
---

# Competitor churn watch

Part of the Stalk Bot agent preset.

Schedule, as written by the template author: Disabled by default and only useful once a churn source is named. Weekdays at 10am in the user's timezone. Scans the churn source for customers lost to a watched competitor, writes the facts brief, and hands the winback body to the user's writing bot or a marked skeleton. Never sends. Quiet when there are no new cases.

## What to do on each run

# Competitor churn watch

This routine ships disabled. It does nothing until a CHURN SOURCE line exists in memory. During setup I do not ask about it; I offer it when the user mentions losing a customer or turns the module on.

When enabled:
1. Read memory for CHURN SOURCE, WINBACK WRITER, the watched competitors, and the last churn watermark. If CHURN SOURCE is missing, do nothing and say so once.
2. Run the competitor-churn skill.
3. Deliver one line per new case in the saved destination with the brief path and the winback status. If there are no new cases, say nothing.
4. Update the churn watermark.
5. Never contact a customer or a competitor. Never send. Never use the research identity here.

Fires on:
- cron `0 10 * * 1-5`

Ask the importing user for:
- Timezone
