---
name: control-matic
description: "use this when the user wants to start, pause, dock, stop, clean a room, or check status of a Matic robot vacuum"
---

# Control Matic

Part of the Home robots agent preset.

---
name: Control Matic
description: >-
  use this when the user wants to start, pause, dock, stop, clean a room, or
  check status of a Matic robot vacuum
---
Use this whenever the user wants the Matic vacuum to do something, or asks how it is doing. If Home Assistant is not connected, run Connect Matic first.

Start cleaning or clean a room: confirm floors are clear of pets, cables, and small objects. Pause, stop, or dock: do it immediately.

Control the Home Assistant vacuum entity: vacuum.start, vacuum.pause, vacuum.stop, vacuum.return_to_base, vacuum.locate, vacuum.clean_area if rooms are mapped.

Reply in one or two short sentences. If they also have a Navimow, do not send mower commands when they meant the vacuum.
