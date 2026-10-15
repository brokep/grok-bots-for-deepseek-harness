---
name: take-selfie
description: "Gets a selfie sent in chat from any phone or webcam, or opens the camera app on their computer when they ask."
---

# take-selfie

Part of the Pfp Bot agent preset.

# take-selfie

Get one clear selfie. Send the tips and the ask in one message: "Face the light, look at the camera, upper body and hair in frame, plain background, no sunglasses. Snap one with your phone or webcam and send it here." When it arrives, run make-icon with it as an upload, adding --source selfie. That works everywhere and needs nothing else.

Camera app on their computer: only when they ask me to open it and ListMachines shows a connected computer (desktop messages also say "[Sent from machine <id>]"). Every command below is Shell with that machineId, and every copy is CopyToBox with it. Without a machineId, Shell runs on my own box and finds nothing.

Mac: Shell open -a "Photo Booth", then say "Photo Booth is open. Take the shot, then tell me done." and end the turn. On "done": Shell ls -t "$HOME/Pictures/Photo Booth Library/Pictures" | head -1, then CopyToBox that file with box_path /workspace/pfp-bot/selfie.jpg, and run make-icon with --photo /workspace/pfp-bot/selfie.jpg --source selfie.

Windows: Shell Start-Process microsoft.windows.camera: in PowerShell (start microsoft.windows.camera: in cmd), then the same "done" step. Newest file: Get-ChildItem "$env:USERPROFILE\Pictures\Camera Roll" | Sort-Object LastWriteTime -Descending | Select-Object -First 1. CopyToBox it the same way.

Each step on their computer shows a permission card. Say what the card is for before it appears. A declined or expired card is a no for the rest of the task, so never ask for it again unless they bring it up.

No connected computer, local tools off ("Local tools are turned off."), a declined card, or a Pictures folder the shell cannot read: "No worries. Snap one with your phone or webcam and drop it in this chat."
