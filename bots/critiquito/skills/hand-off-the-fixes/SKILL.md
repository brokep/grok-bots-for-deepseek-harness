---
name: hand-off-the-fixes
description: "Use when the user wants findings turned into tickets, posted to their team, or kept somewhere they can read later, in Linear, Notion, Slack, or as text they can paste anywhere."
---

# Hand off the fixes

Part of the Critiquito: Design Critique agent preset.

Inputs: a critique you already ran, and where they want it to land. Never invent findings here. Everything you hand off comes from a critique in front of you.

1. Ask which findings go, or offer the default: every blocker, plus anything they call out. Minors stay in the critique unless they ask.
2. Draft before you send. Show the exact titles and bodies in the chat and wait for a yes. One yes covers the batch they just read, not future ones.
3. Ticket shape, one per finding, never a single ticket holding six problems:
   - Title: the screen and the problem in plain words, for example "Invite screen, primary button does not say it sends".
   - Body: what a user hits, where on the screen, what it costs them, the specific fix, and the severity. Attach or link the shot you reviewed.
   - Leave the team, project, and assignee to them. Ask once, do not guess.
4. Page shape for an archive: one page per screen, newest critique at the top, the open fix list underneath with severity and the date each finding opened. Update the same page on the next critique instead of making a second one.
5. Channel shape: the verdict line, the blockers, and a link to the full critique. Never paste a full critique into a channel.
6. No connector is needed. Offer the same output as markdown they can paste, and say so before they go connect anything.
7. Write the ticket or page links onto that screen's open fix list so the weekly check can point at them.

Save the handoff record under design critiques with the screen name.
