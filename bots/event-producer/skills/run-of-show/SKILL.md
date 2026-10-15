---
name: run-of-show
description: "Use when the user needs the minute-by-minute schedule for the event day, or when a time or a speaker changes and the schedule has to move."
---

# Run of show

Part of the Event Producer agent preset.

Inputs: the event brief, the venue access times, and whatever the user knows about the agenda.

1. Anchor on three clock times first: when you get into the room, when the first guest walks in, and when you have to be out. Everything else hangs off those.
2. Build backward from doors, then forward from doors. Load-in, vendor arrivals, setup, AV check, staff briefing, doors, program, food service, close, tear-down, load-out.
3. Every row carries four things: clock time, how long it takes, what happens, and one named owner. A row with no owner is not finished.
4. Add the cue lines a person on the floor needs. Who welcomes people, who introduces the speaker, who cuts the music, who calls last drinks.
5. Build in slack. Fifteen minutes before doors and ten between program blocks. Say out loud where the plan is tight.
6. Mark the three rows where the night actually breaks if they slip. Usually AV check, food arrival, and doors.
7. Show the table in chat, take edits, then save.

Output: one table with times down the left and an owner on every row, plus three lines on the tightest points and what to cut if you run late.

Fallbacks: no venue access time means you assume three hours before doors and say plainly that you assumed it. An unconfirmed speaker keeps the slot with the name marked unconfirmed.

Save under the event folder as the run of show, and rewrite it whenever a time changes.
