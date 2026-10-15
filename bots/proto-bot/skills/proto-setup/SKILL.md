---
name: proto-setup
description: "Use on the first conversation after import, or when the user asks to set up again: installs proto.py, asks which tools they use, connects GitHub, picks the repo and app, sets the spend check, and maps the code."
---

# proto-setup

Part of the Proto Bot agent preset.

# proto-setup

First run, or when the user asks to set up again. One question per message, each with a default. Setup builds, spends, posts, and turns on nothing.

## 1. Install

Before sending anything, make one Shell call with this command.

```bash
python3 - <<'EOF'
import glob, os, re, subprocess, sys
for path in sorted(glob.glob("/home/box/agent-data/**/SKILL.md", recursive=True), key=os.path.getmtime, reverse=True):
    m = re.search(r"`{3}python[ \t]*\n(.*?)\n`{3}", open(path, encoding="utf-8", errors="ignore").read(), re.S)
    if m and "PROTO_TOOLS_V1" in m.group(1):
        tmp = "/tmp/proto-%d.py" % os.getpid()
        open(tmp, "w").write(m.group(1) + "\n")
        sys.exit(subprocess.call([sys.executable, tmp, "install"]))
print("proto-scripts not found")
EOF
```

Bots share /workspace, so it picks /workspace/proto-bot or the first free /workspace/proto-bot-N. moved true: rewrite your STATE memory line as its note says. Then run proto.py init. "proto-scripts not found": Read proto-scripts, write its script to /tmp/proto.py exactly, and run python3 /tmp/proto.py install.

## 2. Intro and tools

One line: "I turn your ideas into live prototypes people can click and share: features in your real app as draft PRs, plus Figma mocks, images, and memes. Nothing merges, posts, or ships without your yes."
Then this widget and end the turn:
{"prompt": "Which of these do you use?", "helpText": "I need GitHub, and Cursor for builds. For images and video, pick FAL (also voice), Higgsfield, or Grok Imagine.", "options": [{"label": "GitHub", "style": "primary"}, {"label": "Cursor"}, {"label": "FAL"}, {"label": "Higgsfield"}, {"label": "Grok Imagine"}, {"label": "Figma", "description": "Your Figma plugin"}, {"label": "Slack"}, {"label": "X"}], "multiSelect": true, "allowCustom": true}
Save with proto.py set tools <comma list>, then connect GitHub per proto-connect, skipping connectors the import installed.

## 3. Repo and app

A widget of up to 6 repos from CloudAgent repositories, else search_repositories, allowCustom: "Which repo should prototypes live in?" Then: "Where can I see the app? A staging or preview URL works best." Save with proto.py set repo, set ref <default branch>, and set app_url. No GitHub: offer Figma, images, and research until there is a repo.

## 4. Connect the rest

The build check, then each other pick, one at a time, per proto-connect.

## 5. Spend

Widget "Check with you before spending over?": $2 (value 2, primary), $10 (10), Every paid job (0). Save with proto.py set spend_cap.

## 6. Map, then ready

Run proto-codebase, then send 3 lines: stack, component library, screens.
QA or writing teammates in the teammate list: widget "Tag in your QA and writing bots?": Yes (auto, primary), Ask each time (ask), No (off). Save with proto.py set teammates.
One line: "Two routines are off: a weekday rundown of finished builds and queued ideas, and a Monday craft scan. Want either on? I'll need your timezone."
Starter widget, then stop: Drop an idea (proto.py idea add <one line>), Prototype a feature (proto-build), Mock it in Figma (proto-figma), Make an image or meme (proto-media), Loop a still into an avatar (proto-media), Skip for now.

## Never

Ask what they want an assistant for.
