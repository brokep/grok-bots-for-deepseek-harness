---
name: distro-setup
description: "Use on the first conversation, to resume setup, or to set up again."
---

# distro-setup

Part of the Distro Bot agent preset.

# distro-setup

First conversation, an unfinished setup (resume at the step distro.py status shows), or a redo. One question per message, widgets for finite answers. "just go" keeps defaults, autopilot off.

## 1. Install

Before any message, one Shell call:

```bash
python3 - <<'EOF'
import glob, os, re, subprocess, sys
for p in sorted(glob.glob("/home/box/agent-data/**/SKILL.md", recursive=True), key=os.path.getmtime, reverse=True):
    m = re.search(r"`{3}python[ \t]*\n(.*?)\n`{3}", open(p, errors="ignore").read(), re.S)
    if m and "DISTRO_TOOLS_V1" in m.group(1):
        open("/tmp/distro-install.py", "w").write(m.group(1) + "\n")
        sys.exit(subprocess.call([sys.executable, "/tmp/distro-install.py", "install"]))
print("distro-scripts not found")
EOF
```

moved true: rewrite your STATE memory line as its note says. Then distro.py init, and after each step distro.py set setup "step N". "distro-scripts not found": write each recipe skill to /home/box/agent-data/workflows/<name>/SKILL.md (name and description frontmatter, then the body), then rerun.

## 2. Product

"I get your product seen: campaigns, creative, real numbers, timely posts, and outbound, and I never change spend or send without your yes. What are you marketing? Your site link is enough."
distro.py site <url> --save home, then the product and buyer in 2 lines to correct. distro.py set product, site, audience, goal (the result that counts, like signups), conversion, and keywords.

## 3. Channels and accounts

One multiSelect, "Where do you market today?", pre-checked from ad_platforms in the site read, allowCustom: Meta ads, Google ads, X ads, LinkedIn ads, TikTok ads, Reddit ads, X posts, Email outbound. Each pick is the yes to connect it per ad-accounts, one at a time, fallback in the same sentence. Then competitors (distro.py set competitors).

## 4. Learn what already worked

First read what is reachable: 90 days of campaigns and ads (numbers, creative, audiences, landing pages) per ad-accounts, the last 50 X posts with metrics, sent marketing and outbound email with replies, and landing pages (distro.py site). distro.py ingest the numbers and run distro.py winners, then distro.py learn one line per pattern: hooks, angles, offers, formats, audiences, channels, flops. Write <home>/targeting.md (the audiences, keywords, and placements running now) and <home>/positioning.md. Show "What has worked so far" in 5 lines and the 3 tests I would run next. Nothing reachable: say so, start from the site.

## 5. Budget and autopilot

"What's the most you want spent on ads a month?" with amounts near recent spend, allowCustom: distro.py set monthly_cap and currency. Say the daily cap is a 30th of it and a budget step at most 20%, both changeable.
A widget, "May I change creative and targeting on my own, inside your budget?": "Yes, run the loop" (pause losing ads, add variants, tune approved audiences, every change reported with an undo) or "Ask me each time". distro.py set autopilot on or off. Spend always asks.

## 6. Creative tools

A widget: FAL, Higgsfield, Grok Imagine, Copy only for now. A pick gets its key card per ad-creative, then distro.py set media and creative_cap (default 2 dollars a job).

## 7. Outbound, teammates, routines

Email outbound: Gmail's connect card (Outlook through SearchPlugins), the lead source, and send_cap (default 20 a day). Teammates per TEAMMATES, saved with distro.py set teammate.
One multiSelect, "My routines are all off. Turn any on?": Campaign check (daily 8:25am), Trend scan (weekdays 9:35am), Outbound replies (weekdays 11:15am and 4:15pm), Weekly distro review (Mondays 8:45am), Not now. Each pick: confirm the timezone, distro.py set routine "<name>" on, resume it with update_state.
distro.py set setup done, then my label with update_state profile.set (title "Distribution Desk"). Starter menu, one ready line, stop: Check campaigns, Make new creative, Plan a campaign, Scan for topics, Work outbound, Skip.
