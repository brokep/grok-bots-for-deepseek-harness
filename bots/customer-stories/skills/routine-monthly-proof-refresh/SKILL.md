---
name: routine-monthly-proof-refresh
description: "Scheduled routine: Once a month, the quotes and numbers that have aged out, the customers worth a fresh call, and the claims with the thinnest proof behind them."
---

# Monthly proof refresh

Part of the Customer Proof Desk agent preset.

Schedule, as written by the template author: Once a month, the quotes and numbers that have aged out, the customers worth a fresh call, and the claims with the thinnest proof behind them.

## What to do on each run

Run on the first Monday of each month at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the proof bank and check three things. Age: every quote and number older than 12 months, and say where it is currently published so they know what is out in the world running on old data. Staleness: any customer whose most recent source is older than 9 months, worth a check before their story gets used again. Coverage: the audiences and claims in memory with the fewest approved items behind them. Give each item one recommended action in a few words, such as refresh the number, ask for re-approval, retire it, or book a new call. Keep it under 150 words and lead with anything published on data older than 12 months. A clean month gets one line. Never retire, edit, or unpublish anything on your own, and never invent a replacement number for one that aged out.
