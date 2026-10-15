---
name: icon-setup
description: "First run: installs pfp.py and warms up in the background, one intro line, the photo-source widget with an X handle field, then previews as the demo."
---

# icon-setup

Part of the Pfp Bot agent preset.

# icon-setup

First run only. One intro line, one question, then straight into their first icon. The icon is the test drive.

## 1. Install, then ask

Before sending anything, make one Shell call: this install command, then on its next line the warm-up, started in the background without waiting for it.

```bash
python3 - <<'EOF'
import glob, os, re
fence = "`" * 3
code = None
for path in sorted(glob.glob("/home/box/agent-data/workflows/*/SKILL.md"), key=os.path.getmtime, reverse=True):
    match = re.search(fence + r"py(?:thon)?[ \t]*\n(.*?)\n" + fence, open(path, encoding="utf-8", errors="ignore").read(), re.S)
    if match and "PFP_TOOLS_V1" in match.group(1):
        code = match.group(1)
        break
if code is None:
    print("pfp-scripts not found")
else:
    os.makedirs("/workspace/pfp-bot", exist_ok=True)
    with open("/workspace/pfp-bot/pfp.py", "w") as f:
        f.write(code + "\n")
    try:
        compile(code, "pfp.py", "exec")
        print("installed /workspace/pfp-bot/pfp.py")
    except SyntaxError as err:
        print("installed, but line %s has a syntax error: %s. Fix that line in /workspace/pfp-bot/pfp.py" % (err.lineno, err.msg))
EOF
```

nohup python3 /workspace/pfp-bot/pfp.py warm --name "<my current name>" > /workspace/pfp-bot/warm.log 2>&1 &

If the install prints "pfp-scripts not found", Read pfp-scripts and write its script to /workspace/pfp-bot/pfp.py exactly as shown. If it names a line with a syntax error, fix that line in the installed file.

Send one line: "I turn a photo of you (or your pet) into a tiny Grokbot-style icon: your hair and colors, capsule eyes, no mouth, never a realistic likeness. I only make icons of you or people who said yes."

Then send this widget and end the turn:
{"prompt":"Which photo should I turn into your icon?","helpText":"Using your X photo? Just type your handle, like @yourname.","options":[{"label":"My X profile photo","value":"x","style":"primary","description":"Type your handle, or click and I'll ask"},{"label":"Upload photos","value":"upload","description":"1 to 3 photos of just you, face and hair visible"},{"label":"Take a selfie","value":"selfie","description":"Snap one with your phone or webcam"}],"allowCustom":true}

Reading the answer:
- A typed handle (@name, x.com/name, or a single word): run make-icon with that handle.
- "x" with no handle: if the X connector is connected, call get_users_me right away, say "Got @<handle>.", and run make-icon with its profile_image_url. Ask "What's your X handle?" only when that call fails or the connector is missing, then wait.
- "upload": "Send 1 to 3 photos of just you (or your pet), face and hair visible, upper body in frame, good light, a plain background if you have one."
- "selfie": run take-selfie.
- Dismissed: "No problem. Send a photo or an X handle whenever you want an icon."

If the handle lookup fails and the X connector is not installed, offer it with a question widget first. Never install without a yes.

## 2. First icon

Run make-icon. Their first previews are the demo.

## Anti-patterns

No settings interview. One question per message. Never generate before they pick a source. Never ask for the handle twice. Never ask about connectors before the first icon. Never generate an icon they did not ask for.
