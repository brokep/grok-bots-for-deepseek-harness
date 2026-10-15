---
name: qa-setup
description: "Use on the first conversation after import, or when the user asks to set up again: installs qa.py, asks which product to test and which email to sign up with, makes the test account, and sets the cadence."
---

# qa-setup

Part of the Startup QA Bot agent preset.

# qa-setup

First run, or when asked to set up again. One question per message, each with a default you take unless they object.

## 1. Install

Before any message, run this in one Shell call, then qa.py init.

```bash
python3 - <<'EOF'
import glob, os, re
d = os.environ.get("QA_DIR", "/workspace/startup-qa-bot")
f = "`" * 3
for p in sorted(glob.glob("/home/box/agent-data/workflows/*/SKILL.md"), key=os.path.getmtime, reverse=True):
    m = re.search(f + r"python[ \t]*\n(.*?)\n" + f, open(p, encoding="utf-8", errors="ignore").read(), re.S)
    if m and "STARTUP_QA_TOOLS_V1" in m.group(1):
        os.makedirs(d, exist_ok=True)
        open(d + "/qa.py", "w").write(m.group(1) + "\n")
        compile(m.group(1), "qa.py", "exec")
        print("installed " + d + "/qa.py")
        break
else:
    print("qa-scripts not found")
EOF
```

"qa-scripts not found": the skills did not save. Write each recipe skill to /home/box/agent-data/workflows/<name>/SKILL.md (name and description frontmatter, then the body), then rerun it.
First run and /workspace/startup-qa-bot/state.json exists: another Startup QA Bot here owns it, so rerun it as QA_DIR=/workspace/startup-qa-bot-2 python3 - ... (next free number) and rewrite your STATE memory line.

## 2. The product

Send one line: "I walk your product every day in my own test account and tell you what shipped, what got unshipped, and what broke, with repro steps. I never send or publish anything real." Then ask "Which product should I test? Staging or production both work." qa.py set product "<name>" and qa.py set product_url <url>. A desktop or mobile app: ask for a web version, else I can only check what a browser shows.

## 3. The signup email

{"prompt":"Which email should I sign up with?","helpText":"An inbox only I read lets me handle verification emails myself. AgentMail makes one in a minute.","options":[{"label":"Make me an AgentMail inbox","value":"agentmail","style":"primary","description":"I make it and read the codes"},{"label":"I'll give you an address","value":"other","description":"Used for nothing else. You paste me the codes."}],"allowCustom":true}
- AgentMail: not connected, offer its connect card once. Then create_inbox with username <product>-qa (taken: add a number) and display name "<Product> QA", and show the address.
- Another address: if it's their main inbox, ask once for a dedicated one.
qa.py set email <address> and qa.py set inbox agentmail or other, then sign up now (test-account, set up).

## 4. Changes and bugs

{"prompt":"Where do changes show up?","options":[{"label":"GitHub pull requests","value":"github"},{"label":"Linear issues","value":"linear"},{"label":"A changelog page","value":"changelog"},{"label":"Nowhere, just walk it","value":"none"}],"multiSelect":true,"allowCustom":true}
qa.py set changes <list>. GitHub or Linear: offer its connect card (read-only) or take a pasted list. Changelog: qa.py set changelog <url>.
Look in "Teammates you can message right now" for one whose profile says it triages bugs. Found: a question widget, "Your bug-triage teammate" (primary) or "Just list them for me", then qa.py set triage "<agent id> bug triage", or none. Not found: skip this.

## 5. Cadence

{"prompt":"When should I walk it?","options":[{"label":"Weekday mornings","value":"weekdays","style":"primary","description":"Ready by 9 AM"},{"label":"Every day","value":"daily"},{"label":"Once a week","value":"weekly"},{"label":"Only when I ask","value":"manual"}],"allowCustom":true}
qa.py set days <choice>. Anything but weekday mornings: match morning-product-walk with update_state, still paused.

## 6. Ready

qa.py set setup done. Echo 3 lines: product and URL, test account and inbox, cadence.
One line: "My morning routine is off until you turn it on."
Starter widget, then stop: Map and walk it now (product-walk), Check one page now, Skip for now.

## Never

Walk, turn on a routine, or connect anything unless they ask. Ask what they want an assistant for.
