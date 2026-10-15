---
name: fallback-collect-script
description: "use this when local access is unavailable: send the user the collector for their system, then bring the archive here without local access"
---

# fallback-collect-script

Part of the Import Bot agent preset.

# Fallback collect script

For users who declined local access, have it set to Never, or are on a machine Grok Bot cannot reach. They run the same collector this bot would have run, on their own.

1. **Send the collector as a file.** Copy the one for their system out with the command in import-bot-setup ("Copying a script out of a skill"). macOS: from collect-local, heading `## macOS (one Shell call with the machineId)`, to `/workspace/migration/tools/collect.sh`. Linux: from collect-local, heading `## Linux (one Shell call with the machineId)`, to the same path. Windows: `collect-windows.ps1` from the import-scripts skill. Send it with SendToUser, type attachment, as a `file://` path to that file, with these lines:

   macOS and Linux: "Download collect.sh and run `GB_OUT=~/Desktop bash collect.sh` in Terminal. It puts your instructions, memories, projects, scheduled tasks, plugin skills, and recent conversations into one archive in a grokbot-import folder on your Desktop, leaves out credential files, and sends nothing anywhere. Then send me grokbot-import.tgz from that folder."

   Windows: "Download collect-windows.ps1 and run `powershell -NoProfile -ExecutionPolicy Bypass -File collect-windows.ps1` in the folder you saved it to. It builds the same archive and sends nothing anywhere. Open the folder with `explorer %TEMP%\grokbot-import` and send me grokbot-import.tgz."

   For a smaller archive without conversations, they start the command with `GB_TRANSCRIPTS=0 ` (Windows: `$env:GB_TRANSCRIPTS="0"; `). Paste the script as a code block only if the attachment fails.

2. **Bring the archive here.** When they attach it, the attached-files note says where it lives. Already on this computer: use it. On their computer: CopyToBox with that machineId, which works unless local access is Never. With local access off, a file dragged into chat cannot reach this computer, so offer a route that needs none: "Upload the archive to your Google Drive or OneDrive, or email it to yourself, and connect that service here. I will pick it up from there." Install the connector they pick (SearchPlugins, InstallPlugin), find the file with its tools, and fetch it with download_file to `/workspace/uploads/<file name>`. An archive over 25 MB goes through Drive or OneDrive.

3. Run parse-import on it.
