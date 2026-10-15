---
name: score-an-event-request
description: "Use when an event, sponsorship, speaking, or partnership ask needs a call: score it against the rubric and recommend yes, no, not now, or needs info."
---

# Score an event request

Part of the Event Request Desk agent preset.

Inputs: the request row and the rubric saved in memory. With no rubric yet, use the default below and say plainly that it is the default.

Default rubric, five criteria scored 0 to 3 each:
- Audience: how many of the right people this puts them in front of, in the room or on the stream.
- Fit: how close that audience is to who they actually want, and whether the topic and the brand match.
- Cost: the fee or tier price plus travel, staffing, and prep hours, scored in reverse so cheap scores high.
- Timing: whether the team has room on that date, and whether it lands in a blackout week or on top of a launch.
- Relationship: whether the ask comes from someone who matters to them, and whether the organizer delivered last time.

Steps:
1. Score each criterion 0 to 3 and write one line of evidence per score, quoting the request. A criterion you cannot judge scores nothing and gets flagged as missing.
2. Total out of 15. 11 and up recommends yes. 6 to 10 recommends not now, with the one thing that would change it. 5 and under recommends no. Two or more missing criteria recommends needs info instead of a number.
3. Apply the hard rules first when they exist. Anything above the spend cap, inside a blackout week, or past the travel limit skips the score and comes back as a no the user can override, with the rule named.
4. Name the real cost in hours and dollars: the fee, travel, booth build, swag, and the prep hours the event will eat. Say when you are estimating.
5. Add one line on what a yes would cost the team that week, and one line on what a no risks.
6. Check the reply-by date. Anything inside seven days gets called out on its own line no matter the score.
7. Set decision to your recommendation and status to scored. The user makes the actual call.

Output: the five scores with evidence, the total, the recommendation, and the one sentence someone new to this request would need to follow it.

Never score a request on details you invented. A recommendation resting on a blank field says so on the line where the blank is. When the user overrules you, log their call and the reason without arguing.

Save the scored row back to the queue.
