---
name: video-tools
description: "Use before an edit to get raw footage onto my computer and to check or install Whisper, Remotion, and SyncNet, with fallbacks."
---

# video-tools

Part of the Video Editor agent preset.

# Video tools

## When to use
Before the first edit and each new one, to get footage in and check the tools. Everything lives in /workspace/video-editor: projects/<video> for working copies, assets for the video assets folder when it is kept on my computer, and tools for installs.

## Footage in
- Their computer: ListMachines, then CopyToBox each raw file, one file per call. If local access is off or a file is too big to copy, say what it was for and ask for a Google Drive link instead.
- Google Drive: download_file from the link, or the Google Drive connector.
- Chat upload: fine for short clips.
Work on copies, never the originals.

## Tools
ffmpeg and ffprobe come with my computer. The rest install on first use and can vanish after a computer update, so check each one quietly before an edit and reinstall what is missing.
- Whisper, for transcripts with word timestamps: a Python venv at tools/venv with faster-whisper (the lightest install) or openai-whisper. Fallback: ask for a caption file (SRT) or transcript from their phone, CapCut, or Descript, and say the captions will follow it.
- Remotion, for graphics and rendering: needs Node 18 or newer. If node is missing, install Node from nodejs.org into tools/node, then install remotion and @remotion/cli in the project folder. With the Remotion plugin connected, follow its skills for compositions, captions, and rendering. Fallback: simpler text pop-ins and overlays in ffmpeg, said in the plan.
- SyncNet, for the lip-sync offset: optional and a large install. Fallback: at 3 points, line up a hard consonant or clap in the waveform with the frame where the lips close, and apply the offset.

## Never
Install anything outside /workspace/video-editor or with sudo.
