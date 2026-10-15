---
name: routine-friday-recap-roundup
description: "Scheduled routine: Every Friday, the recaps that went out this week, the drafts still sitting unsent, and the next steps that are past their date."
---

# Friday recap roundup

Part of the Meeting Recap Deck agent preset.

Schedule, as written by the template author: Every Friday, the recaps that went out this week, the drafts still sitting unsent, and the next steps that are past their date.

## What to do on each run

Run Friday afternoons at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the recaps folder and write three short lists. Went out this week: the meeting, the date, and who it went to. Still sitting: recaps you drafted that were never sent, oldest first, with how many days each has been waiting. Past their date: next steps from any recap whose date has gone by with nothing marked done, with the owner on each line, and the ticket link when one exists. Keep it under 150 words. A quiet week gets one line saying nothing is waiting. Never chase anyone, never mail or message a customer from this run, and never mark a next step done on your own. Ask before you touch anything on the list.
