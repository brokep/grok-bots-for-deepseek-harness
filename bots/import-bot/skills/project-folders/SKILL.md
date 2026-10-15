---
name: project-folders
description: "use this for every project that used a folder on the user's computer: copy it here, read it on request, or connect its drive"
---

# project-folders

Part of the Import Bot agent preset.

# Project folders

Cowork projects attach folders on the user's computer, and Claude Code and Codex work inside repos. The experts here run on this computer, so every folder needs a home. Three choices, offered per folder, decided during the plan so the expert's playbook says where its files are.

## Find them

- Cowork: `spaces[].folders` in the inventory.
- Claude Code and Codex: `cwd` on sessions and `claude_code.projects[].dir` (the munged path, `-Users-name-repo` means `/Users/name/repo`).
- ChatGPT and Claude projects: files uploaded to the project, listed in `projects.md` or `projects[].docs`. Those are already in the account, and the account pull is the copy.

Check each folder exists and how big it is, one Shell call with the machineId for all of them (macOS and Linux):

```bash
for d in "<folder1>" "<folder2>"; do if [ -d "$d" ]; then echo "$d: $(du -sh "$d" 2>/dev/null | cut -f1), $(find "$d" -type f -not -path '*/.git/*' -not -path '*/node_modules/*' 2>/dev/null | wc -l | tr -d ' ') files"; else echo "$d: missing"; fi; done
```

Windows: `foreach ($d in "<folder1>","<folder2>") { if (Test-Path $d) { $f = Get-ChildItem $d -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch '\\(\.git|node_modules)\\' }; "$d: " + [math]::Round(($f | Measure-Object Length -Sum).Sum / 1MB) + " MB, " + $f.Count + " files" } else { "$d: missing" } }`

## Offer, in the plan table's folders column and again in the expert's first conversation

For each folder that exists:

1. **Copy it to my computer now.** Best for documents, spreadsheets, notes, exports. One permission card. Import Bot packs the folder (documents and text only, no `.git`, `node_modules`, `.env`, keys, or files over 25 MB, whole folder under 200 MB) and copies it to `/workspace/projects/<slug>/`. This computer is shared by every bot the user has, so the expert reads it directly. Say plainly that a copy is a snapshot and does not follow later edits.
2. **Leave it on your computer, read on request.** Best for folders that change daily or hold code. The expert asks for a permission card when it needs a file (ListMachines, then Shell with that machineId to list and CopyToBox to fetch). Nothing is duplicated.
3. **Connect the drive it syncs to.** If the folder lives in Google Drive or OneDrive, connecting that plugin lets the expert read the live files. Check with SearchPlugins first, and when none is offered, offer the copy or the on-request path instead.

For a folder that is missing (the user deleted it, or it is on another machine): say so, and ask whether to recreate it on their computer or to start it fresh on this one at `/workspace/projects/<slug>/`. Either way the expert's playbook records the decision.

A repo folder (Claude Code, Codex) always gets choice 2 or the GitHub connector. Never copy a repo.

## Copy command (choice 1, macOS and Linux)

```bash
d="<folder>"; T="${TMPDIR:-/tmp}/grokbot-import"; mkdir -p "$T"; OUT="$T/folder-<slug>.tgz"
( cd "$d" && find . -type f -not -path '*/.git/*' -not -path '*/node_modules/*' -not -name '.env*' -not -name '*.pem' -not -name '*.key' -not -name '*.p12' -size -25M \( -name '*.md' -o -name '*.txt' -o -name '*.csv' -o -name '*.tsv' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.pdf' -o -name '*.docx' -o -name '*.xlsx' -o -name '*.pptx' -o -name '*.html' -o -name '*.rtf' -o -name '*.png' -o -name '*.jpg' -o -name '*.jpeg' \) -print0 | COPYFILE_DISABLE=1 tar --null -T - -czf "$OUT" ); ls -lh "$OUT" | awk '{print "archive: '"$OUT"'\nsize: " $5}'
```

Windows: same allowlist with `Get-ChildItem -Recurse -File -Include` and `tar.exe -czf "$env:TEMP\grokbot-import\folder-<slug>.tgz" -T <list>`, placed and run like the collector.

Then CopyToBox (same machineId) to `/workspace/projects/<slug>.tgz`, extract to `/workspace/projects/<slug>/`, delete the tgz, count the files, and write the count and date into the expert's packet under Folders. Over 200 MB, stop and offer choice 2 instead. If `/workspace/projects/<slug>/` already exists, do not copy again. Say when it was copied and offer a refresh.

## Say it once

"Your <project> project used the folder <folder name>. I can copy its documents over now (you approve one read), leave it on your computer and read it when you ask, or you connect the drive it lives in. Which?" Default when the user does not answer: choice 2, recorded as such. Say the folder's name, not its full path, unless they ask.
