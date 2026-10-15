---
name: control-navimow
description: "use this when the user wants to start, pause, resume, dock, stop, or check status of a Segway Navimow robot lawn mower"
---

# Control Navimow

Part of the Home robots agent preset.

---
name: Control Navimow
description: >-
  use this when the user wants to start, pause, resume, dock, stop, or check
  status of a Segway Navimow robot lawn mower
---
Use this whenever the user wants the mower to do something, or asks how it is doing. If credentials are missing or the token fails, run Connect Navimow first.

Safety: this moves a real machine with spinning blades. Start or resume: confirm the lawn is clear of people and pets. Pause, stop, or dock: do it immediately.

Talk to the mower with the official SDK (pip install -U navimow-sdk). Use MowerAPI against https://navimow-fra.ninebot.com. Commands: START, PAUSE, RESUME, DOCK, STOP.

After a command, re-read status and report the new state in plain language plus battery percent. On 401, re-run Connect Navimow.
