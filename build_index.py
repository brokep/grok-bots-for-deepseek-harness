#!/usr/bin/env python3
"""Rewrite docs/index.json so every version points at the current HEAD commit. Run after committing bots/, then commit docs/."""
import json, subprocess, sys, os
here = os.path.dirname(os.path.abspath(__file__))
sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=here).decode().strip()
ts = int(subprocess.check_output(["git", "log", "-1", "--format=%ct", "HEAD"], cwd=here).decode().strip())
p = os.path.join(here, "docs", "index.json"); d = json.load(open(p))
for pl in d["plugins"]:
    for v in pl["versions"]:
        v["source"]["commit"] = sha; v["publishTimestamp"] = ts
json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)
print("index.json ->", sha, len(d["plugins"]), "plugins")
