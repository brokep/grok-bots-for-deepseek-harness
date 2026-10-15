---
name: import-scripts
description: "use this only as the source the copy command reads: import-tools.py, the Windows collector, and the Windows ChatGPT pull. Never read it into the conversation"
---

# import-scripts

Part of the Import Bot agent preset.

# Import scripts

The scripts other skills copy out with the command in import-bot-setup ("Copying a script out of a skill"). Copy the one you need by its heading. Never read this skill into the conversation.

## import-tools.py

```python
#!/usr/bin/env python3
"""Import Bot's tools on its own computer, in one script.

    python3 import-tools.py parse <archive-or-dir> [out-dir]
    python3 import-tools.py normalize <migration-dir>
    python3 import-tools.py search <migration-dir> "<pattern>" [--from <harness>] [-n 20]
    python3 import-tools.py view <migration-dir> <id-prefix> [--max 80]
    python3 import-tools.py seed <migration-dir> <slug> <id,id,...> [--max-sessions 12] [--max-messages 40]

parse, in order: extract into <out>/raw and drop AppleDouble sidecars, reduce
credential-bearing configs to names and delete them, delete anything on the
never-copy list, split account bundles, redact secret-looking strings value-only,
write <out>/inventory.json and <out>/sources.md, then normalize.

normalize writes one text-only document per session to <out>/pack/sessions/ plus
index.json: {"id","harness","title","timestamp","last_activity","cwd","model","source",
"messages":[{"role","text","timestamp"}],"tools":{name:count},"connectors":[...]}.
Tool calls are counted, never carried.

Sources: Claude Cowork, Claude Code, Codex, OpenClaw, Hermes, and the account pulls
placed under raw/accounts/{chatgpt,claude}/ (official exports and live conversation
JSON). Unknown keys are kept under "raw" so nothing is lost.
"""
import json
import os
import re
import shutil
import sqlite3
import sys
import tarfile
import time
import zipfile
from collections import Counter
from pathlib import Path


# ---------------------------------------------------------------- redaction
SECRET_PATTERNS = [
    r"sk-[A-Za-z0-9_-]{16,}",
    r"xox[abprs]-[A-Za-z0-9-]{10,}",
    r"gh[pousr]_[A-Za-z0-9]{20,}",
    r"AKIA[0-9A-Z]{16}",
    r"AIza[0-9A-Za-z_-]{30,}",
    r"ya29\.[A-Za-z0-9_-]{20,}",
    r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----",
]
RX = [re.compile(p) for p in SECRET_PATTERNS]
RX_KV = re.compile(
    r"(?i)((?:api[_-]?key|secret|token|password|passwd|authorization|bearer|cookie|session_key)[\"']?\s*[:=]\s*[\"']?)([^\s'\",;}]{8,})"
)
TEXT_EXT = {".md", ".json", ".jsonl", ".toml", ".yaml", ".yml", ".txt"}

# High-entropy tokens: long, no spaces, mixed letters and digits, not a UUID, path, or URL.
# Catches secrets in formats the pattern list does not know. Shannon entropy over 4.0 bits
# per character on 32+ characters is rare in prose and common in keys.
RX_TOKEN = re.compile(r"(?<![A-Za-z0-9/:._\-])([A-Za-z0-9_\-+/=]{32,})(?![A-Za-z0-9/:._\-])")
RX_UUID = re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}")


def looks_like_secret(tok: str) -> bool:
    if RX_UUID.search(tok) or "/" in tok:
        return False
    if not (any(c.isalpha() for c in tok) and any(c.isdigit() for c in tok)):
        return False
    import math
    counts = {}
    for c in tok:
        counts[c] = counts.get(c, 0) + 1
    ent = -sum(n / len(tok) * math.log2(n / len(tok)) for n in counts.values())
    return ent > 4.0


def redact_text(text: str):
    n = 0
    for r in RX:
        text, k = r.subn("[redacted]", text)
        n += k
    text, k = RX_KV.subn(r"\1[redacted]", text)
    n += k
    def _tok(m):
        nonlocal n
        if looks_like_secret(m.group(1)):
            n += 1
            return "[redacted]"
        return m.group(0)
    text = RX_TOKEN.sub(_tok, text)
    return text, n


NEVER_COPY_DIRS = {"uploads", "outputs", "ccd-session-secrets", "vm_bundles", "claude-code-vm", "skills-plugin", "rpm", "node_modules", ".git", "credentials", "debug", "backups"}
NEVER_COPY_NAMES = {"claude_desktop_config.json", ".claude.json", "config.toml", "settings.json", "openclaw.json", "auth.json", "gateway.json"}
NEVER_COPY_PREFIXES = ("host-creds-",)
NEVER_COPY_SUFFIXES = (".audit-key", ".pem", ".key")
UUIDISH = re.compile(r"^[0-9a-fA-F-]{20,}$")


def extract(src: Path, raw: Path):
    raw.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, raw, dirs_exist_ok=True)
    elif zipfile.is_zipfile(src):
        with zipfile.ZipFile(src) as z:
            z.extractall(raw)
    else:
        with tarfile.open(src) as t:
            t.extractall(raw)
    for p in list(raw.rglob("._*")):
        if p.is_file():
            p.unlink()
    for junk in list(raw.rglob(".DS_Store")):
        junk.unlink()


def enforce_allowlist(raw: Path) -> int:
    removed = 0
    for p in list(raw.rglob("*")):
        if not p.exists():
            continue
        parts = set(p.relative_to(raw).parts)
        if p.is_dir() and p.name in NEVER_COPY_DIRS:
            removed += sum(1 for f in p.rglob("*") if f.is_file())
            shutil.rmtree(p, ignore_errors=True)
            continue
        if p.is_file() and (parts & NEVER_COPY_DIRS or p.name in NEVER_COPY_NAMES
                            or p.name.startswith(NEVER_COPY_PREFIXES) or p.name.endswith(NEVER_COPY_SUFFIXES)):
            p.unlink()
            removed += 1
    return removed


def redact_tree(root: Path) -> int:
    n = 0
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in TEXT_EXT:
            continue
        try:
            data = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        new, k = redact_text(data)
        n += k
        if new != data:
            p.write_text(new, encoding="utf-8")
    return n


SCAFFOLD_PREFIXES = ("<environment_context>", "<user_instructions>", "<system-reminder>", "<command-name>", "<local-command", "<bash-input>", "<bash-stdout", "<uploaded_files>")


# ---------------------------------------------------------------- helpers
def read_text(p: Path, limit=200_000) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")[:limit]
    except Exception:
        return ""


def load_json(p: Path):
    try:
        return json.loads(read_text(p, 50_000_000))
    except Exception:
        return None


def first(d, *keys, default=None):
    for k in keys:
        if isinstance(d, dict) and k in d and d[k] not in (None, ""):
            return d[k]
    return default


def iso(ts):
    if ts is None:
        return None
    try:
        ts = float(ts)
        if ts > 1e12:
            ts /= 1000
        return time.strftime("%Y-%m-%d", time.gmtime(ts))
    except Exception:
        return str(ts)[:10]


def md_notes(folder: Path):
    notes = []
    if folder.is_dir():
        for p in sorted(folder.rglob("*.md")):
            notes.append({"file": p.name, "modified": iso(p.stat().st_mtime), "text": read_text(p, 20_000)})
    return notes


def skill_files(folder: Path, raw: Path):
    return [str(p.relative_to(raw)) for p in folder.rglob("SKILL.md")] if folder.is_dir() else []


def user_turns(jsonl: Path, cap=8):
    """First user messages from a Claude Code or Codex style JSONL transcript."""
    turns = []
    try:
        with open(jsonl, encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    o = json.loads(line)
                except Exception:
                    continue
                msg = o.get("message") if isinstance(o.get("message"), dict) else o
                role = msg.get("role") or o.get("type")
                if role != "user" or o.get("isMeta"):
                    continue
                c = msg.get("content")
                if isinstance(c, list):
                    c = " ".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
                if isinstance(c, str) and c.strip() and not c.lstrip().startswith("<"):
                    turns.append(c.strip()[:400])
                if len(turns) >= cap:
                    break
    except Exception:
        pass
    return turns


def audit_tools(audit: Path) -> Counter:
    tools = Counter()
    for line in read_text(audit, 5_000_000).splitlines():
        try:
            o = json.loads(line)
        except Exception:
            continue
        # Agent SDK stream: assistant messages carry tool_use blocks
        msg = o.get("message") if isinstance(o.get("message"), dict) else None
        if msg and isinstance(msg.get("content"), list):
            for b in msg["content"]:
                if isinstance(b, dict) and b.get("type") == "tool_use" and isinstance(b.get("name"), str):
                    tools[b["name"]] += 1
        name = first(o, "tool", "toolName", "tool_name")
        if isinstance(name, str):
            tools[name] += 1
    return tools


def connectors_from_tools(tools) -> list:
    names = set()
    for n in (tools.keys() if isinstance(tools, Counter) else [t for t, _ in tools]):
        if isinstance(n, str) and n.startswith("mcp__") and len(n.split("__")) > 1:
            names.add(n.split("__")[1])
    return sorted(names)


def mcp_names_from_json(p: Path, per_project=False):
    cfg = load_json(p) or {}
    out = sorted((cfg.get("mcpServers") or {}).keys())
    if per_project:
        for proj, pc in (cfg.get("projects") or {}).items():
            out += [f"{n} (project {proj})" for n in (pc.get("mcpServers") or {}).keys()]
    return out


def mcp_names_from_toml(p: Path):
    names = []
    for line in read_text(p).splitlines():
        m = re.match(r"\s*\[mcp_servers\.([^\].]+)", line)
        if m:
            names.append(m.group(1))
    return sorted(set(names))


def iter_jsonl(p: Path):
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except Exception:
                    continue
    except Exception:
        return


def iso_ts(ts):
    if ts is None or ts == "":
        return None
    if isinstance(ts, str):
        return ts[:19]
    try:
        ts = float(ts)
        if ts > 1e12:
            ts /= 1000
        return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(ts))
    except Exception:
        return str(ts)[:19]


def blocks_text(content, tools: Counter):
    """Anthropic-style content: string, or list of blocks. Returns text, counting tool_use names."""
    if isinstance(content, str):
        return content
    out = []
    if isinstance(content, list):
        for b in content:
            if not isinstance(b, dict):
                continue
            t = b.get("type")
            if t in ("text", "input_text", "output_text") and isinstance(b.get("text"), str):
                out.append(b["text"])
            elif t in ("tool_use", "function_call") and isinstance(b.get("name"), str):
                tools[b["name"]] += 1
    return "\n".join(out)


def is_scaffold(text: str) -> bool:
    s = text.lstrip()
    return any(s.startswith(p) for p in SCAFFOLD_PREFIXES)


def connectors_from(tools: Counter, extra=()):
    names = set()
    for n in list(tools.keys()) + list(extra):
        if isinstance(n, str) and n.startswith("mcp__") and len(n.split("__")) > 1:
            names.add(n.split("__")[1])
    return sorted(names)


def doc(harness, sid, title, timestamp, messages, cwd=None, model=None, source=None, tools=None, connectors=None, last=None):
    tools = tools or Counter()
    for m in messages:
        m["text"], _ = redact_text(m["text"])
    return {
        "id": f"{harness}-{sid}",
        "harness": harness,
        "title": (title or (messages[0]["text"][:60] if messages else sid)).strip() if isinstance(title or "", str) else sid,
        "timestamp": timestamp,
        "last_activity": last or (messages[-1]["timestamp"] if messages and messages[-1].get("timestamp") else timestamp),
        "cwd": cwd,
        "model": model,
        "source": str(source) if source else None,
        "messages": messages,
        "tools": dict(tools.most_common(40)),
        "connectors": connectors if connectors is not None else connectors_from(tools),
    }


# ---------------------------------------------------------------- configs
def reduce_configs(raw: Path) -> dict:
    """Names out of files that can carry credentials, then delete those files.
    Runs before redaction (files still parse) and before parsing (nothing
    downstream sees them)."""
    out = {"desktop_mcp": [], "claude_code_mcp": [], "claude_code_settings": {}, "codex_mcp": [], "openclaw_channels": [], "hermes_config": []}
    for names in raw.rglob("connector-names.txt"):      # bot path, written on the Mac
        section = None
        for line in read_text(names).splitlines():
            line = line.strip().lstrip("\ufeff")
            if line.startswith("## "):
                section = line[3:]
                continue
            if not line or section is None:
                continue
            if section.endswith("claude_desktop_config.json"):
                out["desktop_mcp"].append(line)
            elif section.endswith(".claude.json"):
                out["claude_code_mcp"].append(line)
            elif section.endswith("config.toml"):
                out["codex_mcp"].append(line)
            elif section.endswith("settings.json"):
                m = re.match(r'"([a-zA-Z]*[cC]leanupPeriodDays)"\s*:\s*(\d+)', line)
                if m:
                    out["claude_code_settings"][m.group(1)] = int(m.group(2))
            elif section.endswith("openclaw.json"):
                out["openclaw_channels"].append(line)
            elif section.endswith("config.yaml"):
                out["hermes_config"].append(line)
    for cfg in list(raw.rglob("claude_desktop_config.json")):
        out["desktop_mcp"] += mcp_names_from_json(cfg)
        cfg.unlink()
    for cfg in list(raw.rglob(".claude.json")):
        out["claude_code_mcp"] += mcp_names_from_json(cfg, per_project=True)
        cfg.unlink()
    for cfg in list(raw.rglob("settings.json")):
        if cfg.parent.name not in (".claude", "claude-code"):
            continue
        settings = load_json(cfg) or {}
        for k in ("cleanupPeriodDays", "desktopSessionCleanupPeriodDays"):
            if k in settings:
                out["claude_code_settings"][k] = settings[k]
        cfg.unlink()
    for cfg in list(raw.rglob("config.toml")):
        if cfg.parent.name in (".codex", "codex"):
            out["codex_mcp"] += mcp_names_from_toml(cfg)
            cfg.unlink()
    for cfg in list(raw.rglob("openclaw.json")):
        data = load_json(cfg) or {}
        for key in ("channels", "connectors", "plugins", "mcpServers", "tools"):
            v = data.get(key)
            if isinstance(v, dict):
                out["openclaw_channels"] += list(v.keys())
            elif isinstance(v, list):
                out["openclaw_channels"] += [x.get("name", x.get("id", "")) if isinstance(x, dict) else str(x) for x in v]
        cfg.unlink()
    for cfg in list(raw.rglob("config.yaml")):
        if cfg.parent.name in (".hermes", "hermes"):
            keep = [l.rstrip() for l in read_text(cfg).splitlines() if l.strip() and not re.search(r"(?i)key|token|secret|password", l)]
            out["hermes_config"] += keep[:60]
            cfg.unlink()
    for k in ("desktop_mcp", "claude_code_mcp", "codex_mcp", "openclaw_channels"):
        out[k] = sorted({x for x in out[k] if x})
    return out


def find_dir(raw: Path, *names):
    for name in names:
        for d in raw.rglob(name):
            if d.is_dir():
                yield d


# ---------------------------------------------------------------- Cowork
def parse_cowork(raw: Path, configs: dict):
    result = {"found": False, "accounts": [], "plugins": [], "mcp_servers": configs["desktop_mcp"], "scheduled_skill_files": []}
    roots = list(find_dir(raw, "local-agent-mode-sessions")) + list(find_dir(raw, "claude-code-sessions"))
    for root in roots:
        for acct in sorted(d for d in root.glob("*/*") if d.is_dir()):
            # An account tree is <org-uuid>/<account-uuid>. skills-plugin and app state sit beside it.
            if not (UUIDISH.match(acct.parent.name) and UUIDISH.match(acct.name)):
                continue
            a = {"path": str(acct.relative_to(raw)), "layout": root.name}
            settings = load_json(acct / "cowork_account_settings.json") or {}
            a["display_name"] = first(settings, "displayName", "display_name")
            a["memory_enabled"] = first(settings, "memoryEnabled", "memory_enabled")
            a["global_instructions"] = read_text(acct / "memory" / "CLAUDE.md")
            a["global_memory_notes"] = md_notes(acct / "memory" / "memory")

            # Projects (spaces). Schema inferred, kept tolerant.
            spaces_raw = load_json(acct / "spaces.json")
            items = []
            if isinstance(spaces_raw, dict):
                items = spaces_raw.get("spaces") if isinstance(spaces_raw.get("spaces"), list) else \
                    [dict(v, id=k) if isinstance(v, dict) else {"id": k} for k, v in spaces_raw.items() if isinstance(v, dict)]
            elif isinstance(spaces_raw, list):
                items = spaces_raw
            spaces = []
            for s in items:
                sid = first(s, "id", "uuid", "spaceId")
                spaces.append({
                    "id": sid,
                    "name": first(s, "name", "title"),
                    "instructions": first(s, "instructions", "prompt", "systemPrompt"),
                    "folders": first(s, "folders", "paths", default=[]),
                    "created": iso(first(s, "createdAt", "created_at")),
                    "memory_notes": md_notes(acct / "spaces" / str(sid) / "memory") if sid else [],
                    "raw": {k: v for k, v in s.items() if k not in {"instructions", "folders"}},
                })
            a["spaces"] = spaces

            # Scheduled tasks. Top-level key "scheduledTasks" verified 2026-09-12.
            st = load_json(acct / "scheduled-tasks.json") or {}
            tasks = st.get("scheduledTasks") if isinstance(st, dict) else st
            a["scheduled_tasks"] = []
            for t in tasks or []:
                if isinstance(t, dict):
                    a["scheduled_tasks"].append({
                        "name": first(t, "name", "title"),
                        "schedule": first(t, "schedule", "cron", "rrule"),
                        "timezone": first(t, "timezone", "tz"),
                        "prompt": first(t, "prompt", "instructions", "description"),
                        "space_id": first(t, "spaceId", "space_id", "projectId"),
                        "enabled": first(t, "enabled", "isEnabled", default=None),
                        "skill_path": first(t, "skillPath", "skill_path"),
                        "raw": t,
                    })

            # Sessions. Record local_<uuid>.json + storage dir local_<uuid>/ (same stem),
            # agent-type sessions under agent/. Per txcript docs/formats/cowork.md.
            sessions = []
            cards = sorted(acct.glob("local_*.json")) + sorted((acct / "agent").glob("local_*.json")) if (acct / "agent").is_dir() else sorted(acct.glob("local_*.json"))
            for card in cards:
                c = load_json(card) or {}
                sid = first(c, "sessionId", "id", default=card.stem)
                sdir = None
                for cand in (card.parent / card.stem, card.parent / str(sid), acct / card.stem, acct / str(sid)):
                    if cand.is_dir():
                        sdir = cand
                        break
                transcripts, turns, session_tools = [], [], Counter()
                if sdir:
                    transcripts = [t for t in sdir.rglob("*.jsonl") if t.name != "audit.jsonl" and "subagents" not in t.parts]
                    for t in transcripts[:2]:
                        turns += user_turns(t, cap=4)
                    for audit in sdir.rglob("audit.jsonl"):
                        session_tools.update(audit_tools(audit))
                enabled_mcp = first(c, "enabledMcpTools", default=[]) or []
                connectors = set(connectors_from_tools(session_tools))
                for tool in enabled_mcp if isinstance(enabled_mcp, list) else []:
                    if isinstance(tool, str) and tool.startswith("mcp__") and len(tool.split("__")) > 1:
                        connectors.add(tool.split("__")[1])
                sessions.append({
                    "id": sid,
                    "record": card.name,
                    "title": first(c, "title", "name", "summary"),
                    "created": iso(first(c, "createdAt", "created_at", "startedAt")),
                    "last_activity": iso(first(c, "lastActivityAt", "updatedAt")),
                    "cwd": first(c, "cwd"),
                    "model": first(c, "model"),
                    "cli_session_id": first(c, "cliSessionId"),
                    "space_id": first(c, "spaceId", "space_id", "projectId"),
                    "archived": first(c, "isArchived", "archived", default=False),
                    "agent_type": card.parent.name == "agent",
                    "has_transcript": bool(transcripts),
                    "sample_user_turns": turns,
                    "tool_usage": session_tools.most_common(30),
                    "connectors_seen": sorted(connectors),
                    "raw": {k: v for k, v in c.items() if k not in {"systemPrompt", "enabledMcpTools", "egressAllowedDomains", "initialMessage"}},
                })
            sessions.sort(key=lambda s: s["created"] or "")
            a["sessions"] = sessions
            a["session_count"] = len(sessions)
            a["sessions_with_transcript"] = sum(1 for s in sessions if s["has_transcript"])
            a["oldest_session"] = sessions[0]["created"] if sessions else None
            a["newest_session"] = sessions[-1]["created"] if sessions else None
            with_t = [s["created"] for s in sessions if s["has_transcript"] and s["created"]]
            a["oldest_transcript"] = min(with_t) if with_t else None

            merged_all = Counter()
            for s in sessions:
                merged_all.update(dict(s["tool_usage"]))
            a["tool_usage"] = merged_all.most_common(60)
            a["connectors_seen"] = sorted({c for s in sessions for c in s["connectors_seen"]})
            for sp in a["spaces"]:
                own = [s for s in sessions if s["space_id"] and sp["id"] and str(s["space_id"]) == str(sp["id"])]
                merged = Counter()
                for s in own:
                    merged.update(dict(s["tool_usage"]))
                sp["session_count"] = len(own)
                sp["tool_usage"] = merged.most_common(30)
                sp["connectors_seen"] = sorted({c for s in own for c in s["connectors_seen"]})
            unassigned = [s for s in sessions if not s["space_id"]]
            a["connectors_seen_outside_projects"] = sorted({c for s in unassigned for c in s["connectors_seen"]})
            a["sessions_outside_projects"] = len(unassigned)
            result["accounts"].append(a)
            result["found"] = True

    for pdir in find_dir(raw, "cowork_plugins"):
        for plug in sorted(d for d in pdir.iterdir() if d.is_dir()):
            manifest = load_json(plug / "plugin.json") or load_json(plug / ".claude-plugin" / "plugin.json") or {}
            result["plugins"].append({
                "name": first(manifest, "name", default=plug.name),
                "version": first(manifest, "version"),
                "skills": [p.parent.name for p in plug.rglob("SKILL.md")],
                "skill_files": [str(p.relative_to(raw)) for p in plug.rglob("SKILL.md")],
            })
    result["scheduled_skill_files"] = [str(p.relative_to(raw)) for p in raw.rglob("Scheduled/**/SKILL.md")]
    return result


# ---------------------------------------------------------------- Claude Code
def parse_claude_code(raw: Path, configs: dict):
    r = {"found": False}
    homes = [d for d in find_dir(raw, ".claude", "claude-code") if any((d / x).exists() for x in ("CLAUDE.md", "projects", "skills", "rules"))]
    if not homes:
        return r
    h = homes[0]
    r["found"] = True
    r["instructions"] = read_text(h / "CLAUDE.md")
    r["settings"] = configs["claude_code_settings"]
    r["skills"] = skill_files(h / "skills", raw)
    r["rules"] = [str(p.relative_to(raw)) for p in (h / "rules").rglob("*.md")] if (h / "rules").is_dir() else []
    r["commands"] = [p.stem for p in (h / "commands").rglob("*.md")] if (h / "commands").is_dir() else []
    r["agents"] = [p.stem for p in (h / "agents").rglob("*.md")] if (h / "agents").is_dir() else []
    r["projects"] = []
    if (h / "projects").is_dir():
        for proj in sorted(d for d in (h / "projects").iterdir() if d.is_dir()):
            transcripts = list(proj.glob("*.jsonl"))
            turns = []
            for t in sorted(transcripts, key=lambda x: x.stat().st_mtime, reverse=True)[:3]:
                turns += user_turns(t, cap=3)
            r["projects"].append({"dir": proj.name, "transcripts": len(transcripts), "memory_notes": md_notes(proj / "memory"), "sample_user_turns": turns})
    r["mcp_servers"] = configs["claude_code_mcp"]
    return r


# ---------------------------------------------------------------- Codex
def parse_codex(raw: Path, configs: dict):
    r = {"found": False}
    homes = [d for d in find_dir(raw, ".codex", "codex") if any((d / x).exists() for x in ("AGENTS.md", "memories", "sessions", "skills"))]
    if not homes:
        return r
    h = homes[0]
    r["found"] = True
    r["instructions"] = read_text(h / "AGENTS.md")
    r["instructions_override"] = read_text(h / "AGENTS.override.md")
    r["memories"] = md_notes(h / "memories")
    r["memories_enabled"] = bool(r["memories"])
    r["skills"] = skill_files(h / "skills", raw)
    r["shared_skills"] = [str(p.relative_to(raw)) for p in raw.rglob(".agents/skills/**/SKILL.md")] + [str(p.relative_to(raw)) for p in raw.rglob("agents-skills/**/SKILL.md")]
    r["mcp_servers"] = configs["codex_mcp"]
    sessions = list((h / "sessions").rglob("*.jsonl")) if (h / "sessions").is_dir() else []
    r["session_count"] = len(sessions)
    turns = []
    for t in sorted(sessions, key=lambda x: x.stat().st_mtime, reverse=True)[:10]:
        turns += user_turns(t, cap=2)
    r["sample_user_turns"] = turns
    return r


# ---------------------------------------------------------------- OpenClaw
def parse_openclaw(raw: Path, configs: dict):
    r = {"found": False}
    homes = [d for d in find_dir(raw, ".openclaw", "openclaw") if any((d / x).exists() for x in ("workspace", "agents", "skills"))]
    if not homes:
        return r
    h = homes[0]
    r["found"] = True
    ws = h / "workspace"
    r["bootstrap"] = {name: read_text(ws / f"{name}.md") for name in ("AGENTS", "SOUL", "IDENTITY", "USER", "MEMORY") if (ws / f"{name}.md").exists()}
    r["memory_notes"] = md_notes(ws / "memory")
    r["skills"] = skill_files(h / "skills", raw) + skill_files(ws / "skills", raw)
    r["channels"] = configs["openclaw_channels"]
    r["agents"] = []
    if (h / "agents").is_dir():
        for ag in sorted(d for d in (h / "agents").iterdir() if d.is_dir()):
            info = {"id": ag.name, "session_count": 0, "sample_user_turns": []}
            for db in ag.rglob("*.sqlite"):
                info.update(sqlite_summary(db))
            legacy = list((ag / "sessions").rglob("*.jsonl")) if (ag / "sessions").is_dir() else []
            info["session_count"] += len(legacy)
            for t in legacy[:3]:
                info["sample_user_turns"] += user_turns(t, cap=2)
            r["agents"].append(info)
    return r


def sqlite_summary(db: Path) -> dict:
    """Read-only look at an agent session database: table names, row counts,
    and a few user-authored texts. Never writes."""
    out = {"db": db.name, "tables": {}, "session_count": 0, "sample_user_turns": []}
    try:
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        cur = con.cursor()
        tables = [r[0] for r in cur.execute("select name from sqlite_master where type='table'")]
        for t in tables:
            try:
                out["tables"][t] = cur.execute(f'select count(*) from "{t}"').fetchone()[0]
            except Exception:
                pass
        for t in tables:
            if "session" in t.lower():
                out["session_count"] = max(out["session_count"], out["tables"].get(t, 0))
        for t in tables:
            cols = [c[1] for c in cur.execute(f'pragma table_info("{t}")')]
            if "role" in cols and "content" in cols:
                rows = cur.execute(f'select content from "{t}" where role=\'user\' order by rowid desc limit 12').fetchall()
                for (c,) in rows:
                    if isinstance(c, str) and c.strip():
                        out["sample_user_turns"].append(c.strip()[:300])
                break
        con.close()
    except Exception as e:
        out["error"] = str(e)[:200]
    return out


# ---------------------------------------------------------------- Hermes
def parse_hermes(raw: Path, configs: dict):
    r = {"found": False}
    homes = [d for d in find_dir(raw, ".hermes", "hermes") if any((d / x).exists() for x in ("state.db", "memories", "skills"))]
    if not homes:
        return r
    h = homes[0]
    r["found"] = True
    r["memory"] = read_text(h / "memories" / "MEMORY.md")
    r["user_profile"] = read_text(h / "memories" / "USER.md")
    r["skills"] = skill_files(h / "skills", raw)
    r["config_lines"] = configs["hermes_config"]
    r["sessions"] = []
    db = h / "state.db"
    if db.exists():
        summary = sqlite_summary(db)
        r["db"] = summary
        try:
            con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
            rows = con.execute("select id, title, started_at, model, cwd from sessions where coalesce(archived,0)=0 order by started_at desc limit 200").fetchall()
            for sid, title, started, model, cwd in rows:
                r["sessions"].append({"id": sid, "title": title, "started": iso(started), "model": model, "cwd": cwd})
            con.close()
        except Exception as e:
            r["sessions_error"] = str(e)[:200]
    r["session_count"] = len(r["sessions"])
    return r


# ---------------------------------------------------------------- account bundles
def ingest_bundles(raw: Path) -> dict:
    """Split the one-file bundles the page scripts download (claude-pull-*.json,
    chatgpt-pull-*.json) into the per-conversation layout the account parsers read.
    Idempotent: existing files are not rewritten."""
    stats = {"claude": 0, "chatgpt": 0}
    for f in list(raw.rglob("claude-pull-*.json")) + list(raw.rglob("chatgpt-pull-*.json")):
        b = load_json(f) or {}
        service = b.get("service") or ("claude" if f.name.startswith("claude") else "chatgpt")
        base = raw / "accounts" / service
        (base / "conversations").mkdir(parents=True, exist_ok=True)
        for conv in b.get("conversations") or []:
            cid = conv.get("uuid") or conv.get("conversation_id") or conv.get("id")
            if not cid:
                continue
            out = base / "conversations" / f"{cid}.json"
            if not out.exists():
                out.write_text(json.dumps(conv))
                stats[service] += 1
        if service == "claude" and b.get("projects"):
            (base / "projects-live.json").write_text(json.dumps(b["projects"], indent=1))
        if service == "chatgpt" and b.get("custom_instructions") and not (base / "custom-instructions.md").exists():
            ci = b["custom_instructions"]
            if isinstance(ci, dict):
                text = "\n\n".join(str(ci.get(k) or "") for k in ("about_user_message", "about_model_message") if ci.get(k))
                if text.strip():
                    (base / "custom-instructions.md").write_text(text + "\n")
    return stats


def parse_chatgpt_account(raw: Path):
    r = {"found": False, "conversations": [], "memories": "", "custom_instructions": "", "projects": "", "gpts": ""}
    base = None
    for d in find_dir(raw, "chatgpt"):
        if "accounts" in d.parts:
            base = d
            break
    if base is None:
        return r
    r["found"] = True
    for name in ("memories", "custom-instructions", "projects", "gpts"):
        p = base / f"{name}.md"
        if p.exists():
            r[name.replace("-", "_")] = read_text(p, 60_000)
    convs = []
    exp = base / "export" / "conversations.json"
    if exp.exists():
        data = load_json(exp) or []
        for conv in data if isinstance(data, list) else []:
            turns = chatgpt_turns(conv)
            convs.append({"id": first(conv, "conversation_id", "id"), "title": conv.get("title"), "created": iso(conv.get("create_time")),
                          "updated": iso(conv.get("update_time")), "turns": len(turns), "sample_user_turns": [t["text"][:300] for t in turns if t["role"] == "user"][:4], "source": "export"})
    live = base / "conversations"
    if live.is_dir():
        for p in sorted(live.glob("*.json")):
            conv = load_json(p) or {}
            if not conv.get("mapping"):
                continue
            turns = chatgpt_turns(conv)
            convs.append({"id": first(conv, "conversation_id", "id", default=p.stem), "title": conv.get("title"), "created": iso(conv.get("create_time")),
                          "updated": iso(conv.get("update_time")), "turns": len(turns), "sample_user_turns": [t["text"][:300] for t in turns if t["role"] == "user"][:4], "source": "live", "file": str(p.relative_to(raw))})
    convs.sort(key=lambda c: c["updated"] or c["created"] or "")
    r["conversations"] = convs
    r["conversation_count"] = len(convs)
    r["export_present"] = exp.exists()
    return r


def parse_claude_account(raw: Path):
    r = {"found": False, "conversations": [], "memory_text": "", "projects": [], "projects_text": ""}
    base = None
    for d in find_dir(raw, "claude"):
        if "accounts" in d.parts:
            base = d
            break
    if base is None:
        return r
    r["found"] = True
    if (base / "memory.md").exists():
        r["memory_text"] = read_text(base / "memory.md", 60_000)
    if (base / "projects.md").exists():
        r["projects_text"] = read_text(base / "projects.md", 60_000)
    exp = base / "export"
    mem = load_json(exp / "memories.json") if (exp / "memories.json").exists() else None
    if isinstance(mem, list) and mem:
        m0 = mem[0] if isinstance(mem[0], dict) else {}
        r["export_memory"] = {"conversations_memory": m0.get("conversations_memory", ""), "project_memories": m0.get("project_memories", {})}
    projs = load_json(exp / "projects.json") if (exp / "projects.json").exists() else None
    live = load_json(base / "projects-live.json") if (base / "projects-live.json").exists() else None
    seen = set()
    for p in (projs if isinstance(projs, list) else []) + (live if isinstance(live, list) else []):
        if p.get("uuid") in seen:
            continue
        seen.add(p.get("uuid"))
        r["projects"].append({"uuid": p.get("uuid"), "name": p.get("name"), "description": p.get("description"), "prompt_template": p.get("prompt_template"),
                              "docs": [d.get("filename") or d.get("file_name") for d in (p.get("docs") or []) if isinstance(d, dict)]})
    convs = []
    data = load_json(exp / "conversations.json") if (exp / "conversations.json").exists() else None
    for conv in data if isinstance(data, list) else []:
        msgs = conv.get("chat_messages") or []
        humans = [m.get("text", "") for m in msgs if m.get("sender") == "human" and m.get("text")]
        convs.append({"id": conv.get("uuid"), "title": conv.get("name"), "created": (conv.get("created_at") or "")[:10], "turns": len(msgs),
                      "sample_user_turns": [h[:300] for h in humans[:4]], "source": "export"})
    live = base / "conversations"
    if live.is_dir():
        for p in sorted(live.glob("*.json")):
            conv = load_json(p) or {}
            msgs = conv.get("chat_messages") or []
            if not msgs:
                continue
            humans = [m.get("text", "") for m in msgs if m.get("sender") == "human" and m.get("text")]
            convs.append({"id": conv.get("uuid", p.stem), "title": conv.get("name"), "created": (conv.get("created_at") or "")[:10], "turns": len(msgs),
                          "sample_user_turns": [h[:300] for h in humans[:4]], "source": "live", "file": str(p.relative_to(raw))})
    r["conversations"] = convs
    r["conversation_count"] = len(convs)
    r["export_present"] = (exp / "conversations.json").exists()
    return r


# ---------------------------------------------------------------- report
def sources_md(inv: dict) -> str:
    L = ["# Sources", "", "| Source | Found | What |", "|---|---|---|"]
    cw = inv["cowork"]
    if cw["found"]:
        for a in cw["accounts"]:
            L.append(f"| Claude Cowork ({a['layout']}) | yes | {len(a['global_memory_notes'])} memory notes, {len(a['spaces'])} projects, "
                     f"{len(a['scheduled_tasks'])} scheduled tasks, {a['session_count']} sessions ({a['sessions_with_transcript']} with transcript, "
                     f"{a['oldest_session']} to {a['newest_session']}), memory {'on' if a['memory_enabled'] else 'off or unknown'}, connectors {', '.join(a['connectors_seen']) or 'none'} |")
        if cw["plugins"]:
            L.append(f"| Cowork plugins | yes | {', '.join(p['name'] for p in cw['plugins'])} |")
        if cw["mcp_servers"]:
            L.append(f"| Claude Desktop MCP servers | yes | {', '.join(cw['mcp_servers'])} |")
    else:
        L.append("| Claude Cowork | no | not installed or never used on this Mac |")
    cc = inv["claude_code"]
    L.append(f"| Claude Code | {'yes' if cc['found'] else 'no'} | " + (f"{len(cc['skills'])} skills, {len(cc['rules'])} rules, {len(cc['projects'])} project dirs, MCP {', '.join(cc['mcp_servers']) or 'none'}, retention {cc['settings'] or 'defaults'} |" if cc["found"] else " |"))
    cx = inv["codex"]
    L.append(f"| Codex | {'yes' if cx['found'] else 'no'} | " + (f"memories {'on' if cx['memories_enabled'] else 'off'} ({len(cx['memories'])} files), {len(cx['skills']) + len(cx['shared_skills'])} skills, {cx['session_count']} sessions, MCP {', '.join(cx['mcp_servers']) or 'none'} |" if cx["found"] else " |"))
    oc = inv["openclaw"]
    L.append(f"| OpenClaw | {'yes' if oc['found'] else 'no'} | " + (f"bootstrap files {', '.join(oc['bootstrap'].keys()) or 'none'}, {len(oc['memory_notes'])} memory notes, {len(oc['skills'])} skills, {len(oc['agents'])} agents, channels {', '.join(oc['channels']) or 'none'} |" if oc["found"] else " |"))
    hm = inv["hermes"]
    L.append(f"| Hermes | {'yes' if hm['found'] else 'no'} | " + (f"MEMORY.md {'yes' if hm['memory'] else 'no'}, USER.md {'yes' if hm['user_profile'] else 'no'}, {len(hm['skills'])} skills, {hm['session_count']} sessions |" if hm["found"] else " |"))
    gpt = inv["accounts"]["chatgpt"]
    L.append(f"| ChatGPT (account) | {'yes' if gpt['found'] else 'no'} | " + (f"{gpt['conversation_count']} conversations ({'export' if gpt['export_present'] else 'live pull'}), memories {'yes' if gpt['memories'] else 'no'}, custom instructions {'yes' if gpt['custom_instructions'] else 'no'}, projects {'yes' if gpt['projects'] else 'no'}, GPTs {'yes' if gpt['gpts'] else 'no'} |" if gpt["found"] else " |"))
    cl = inv["accounts"]["claude"]
    L.append(f"| Claude.ai (account) | {'yes' if cl['found'] else 'no'} | " + (f"{cl['conversation_count']} conversations ({'export' if cl['export_present'] else 'live pull'}), {len(cl['projects'])} chat projects, memory {'yes' if (cl['memory_text'] or cl.get('export_memory')) else 'no'} |" if cl["found"] else " |"))
    L += ["", f"(internal) redactions: {inv['redactions']}, removed by never-copy list: {inv['removed_by_allowlist']}. Do not paste this line to the user."]
    return "\n".join(L) + "\n"


def cmd_parse(src_arg: str, out_arg: str) -> Path:
    src = Path(src_arg).expanduser().resolve()
    out = Path(out_arg).expanduser().resolve()
    raw = out / "raw"
    extract(src, raw)
    configs = reduce_configs(raw)
    removed = enforce_allowlist(raw)
    bundles = ingest_bundles(raw)
    redactions = redact_tree(raw)
    inv = {
        "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source": str(src),
        "redactions": redactions,
        "removed_by_allowlist": removed,
        "bundles_ingested": bundles,
        "cowork": parse_cowork(raw, configs),
        "claude_code": parse_claude_code(raw, configs),
        "codex": parse_codex(raw, configs),
        "openclaw": parse_openclaw(raw, configs),
        "hermes": parse_hermes(raw, configs),
        "accounts": {"chatgpt": parse_chatgpt_account(raw), "claude": parse_claude_account(raw)},
    }
    (out / "inventory.json").write_text(json.dumps(inv, indent=2, default=str))
    (out / "sources.md").write_text(sources_md(inv))
    print(f"inventory: {out / 'inventory.json'}")
    print(f"sources:   {out / 'sources.md'}")
    print(f"redactions: {redactions}, removed: {removed}")
    return out


# ---------------------------------------------------------------- Claude Code JSONL (also Cowork transcripts)
def read_claude_code_jsonl(p: Path):
    msgs, tools = [], Counter()
    meta = {"sessionId": None, "cwd": None, "model": None, "first_ts": None, "title": None, "custom_title": None, "summary": None}
    for o in iter_jsonl(p):
        t = o.get("type")
        if t == "summary" and meta["summary"] is None:
            meta["summary"] = o.get("summary")
        elif t in ("custom-title", "agent-name") and not meta["custom_title"]:
            meta["custom_title"] = o.get("title") or o.get("customTitle") or o.get("agentName") or o.get("name")
        if t not in ("user", "assistant"):
            continue
        if o.get("isMeta"):
            continue
        m = o.get("message") if isinstance(o.get("message"), dict) else {}
        role = m.get("role") or t
        text = blocks_text(m.get("content"), tools)
        if role == "assistant" and m.get("model") and not meta["model"]:
            meta["model"] = m["model"]
        for k in ("sessionId", "cwd"):
            if o.get(k) and not meta[k]:
                meta[k] = o[k]
        if o.get("timestamp") and not meta["first_ts"]:
            meta["first_ts"] = iso_ts(o["timestamp"])
        text = text.strip()
        if not text or is_scaffold(text) or role not in ("user", "assistant"):
            continue
        msgs.append({"role": role, "text": text, "timestamp": iso_ts(o.get("timestamp"))})
    return msgs, tools, meta


def harvest_claude_code(raw: Path, docs: list):
    # Cowork keeps a private .claude/projects per session. Those belong to the cowork harvester.
    for home in {d for d in raw.rglob("*") if d.is_dir() and d.name in (".claude", "claude-code") and (d / "projects").is_dir()
                 and not ({"local-agent-mode-sessions", "claude-code-sessions"} & set(d.parts))}:
        for proj in sorted(d for d in (home / "projects").iterdir() if d.is_dir()):
            for f in sorted(proj.glob("*.jsonl")):
                msgs, tools, meta = read_claude_code_jsonl(f)
                if not msgs:
                    continue
                sid = meta["sessionId"] or f.stem
                docs.append(doc("claude_code", sid, meta["custom_title"] or meta["summary"], meta["first_ts"], msgs, cwd=meta["cwd"], model=meta["model"], source=f.relative_to(raw), tools=tools))


# ---------------------------------------------------------------- Cowork
def harvest_cowork(raw: Path, docs: list):
    for root in [d for d in raw.rglob("*") if d.is_dir() and d.name in ("local-agent-mode-sessions", "claude-code-sessions")]:
        for acct in sorted(d for d in root.glob("*/*") if d.is_dir()):
            if not (UUIDISH.match(acct.parent.name) and UUIDISH.match(acct.name)):
                continue
            cards = sorted(acct.glob("local_*.json"))
            if (acct / "agent").is_dir():
                cards += sorted((acct / "agent").glob("local_*.json"))
            for card in cards:
                c = load_json(card) or {}
                sid = c.get("sessionId") or card.stem
                sdir = None
                for cand in (card.parent / card.stem, card.parent / str(sid), acct / card.stem):
                    if cand.is_dir():
                        sdir = cand
                        break
                msgs, tools = [], Counter()
                if sdir:
                    for f in sorted(t for t in sdir.rglob("*.jsonl") if t.name != "audit.jsonl" and "subagents" not in t.parts):
                        m, tl, _ = read_claude_code_jsonl(f)
                        msgs += m
                        tools.update(tl)
                    for audit in sdir.rglob("audit.jsonl"):
                        for o in iter_jsonl(audit):
                            m = o.get("message") if isinstance(o.get("message"), dict) else None
                            if m and isinstance(m.get("content"), list):
                                blocks_text(m["content"], tools)
                enabled = c.get("enabledMcpTools") if isinstance(c.get("enabledMcpTools"), list) else []
                if not msgs and not enabled:
                    # a record whose transcript the 30-day cleanup already removed
                    docs.append(doc("cowork", sid, c.get("title"), iso_ts(c.get("createdAt")), [], cwd=c.get("cwd"), model=c.get("model"), source=card.relative_to(raw), tools=tools, connectors=[], last=iso_ts(c.get("lastActivityAt"))))
                    continue
                docs.append(doc("cowork", sid, c.get("title"), iso_ts(c.get("createdAt")), msgs, cwd=c.get("cwd"), model=c.get("model"), source=card.relative_to(raw), tools=tools, connectors=connectors_from(tools, enabled), last=iso_ts(c.get("lastActivityAt"))))


# ---------------------------------------------------------------- Codex rollouts
def harvest_codex(raw: Path, docs: list):
    for home in {d for d in raw.rglob("*") if d.is_dir() and d.name in (".codex", "codex") and (d / "sessions").is_dir()}:
        for f in sorted((home / "sessions").rglob("*.jsonl")):
            msgs, tools = [], Counter()
            meta = {"id": None, "timestamp": None, "cwd": None, "model": None}
            for o in iter_jsonl(f):
                t = o.get("type")
                payload = o.get("payload") if isinstance(o.get("payload"), dict) else o
                ts = iso_ts(o.get("timestamp"))
                if t == "session_meta":
                    meta["id"] = payload.get("id") or meta["id"]
                    meta["timestamp"] = iso_ts(payload.get("timestamp")) or ts
                    meta["cwd"] = payload.get("cwd") or meta["cwd"]
                    continue
                if t == "turn_context":
                    meta["model"] = payload.get("model") or meta["model"]
                    continue
                kind = payload.get("type") if isinstance(payload, dict) else None
                if t == "response_item" and kind == "message" or (t == "message" and payload is o):
                    role = payload.get("role")
                    if role not in ("user", "assistant"):
                        continue
                    text = blocks_text(payload.get("content"), tools).strip()
                    if text and not is_scaffold(text):
                        msgs.append({"role": role, "text": text, "timestamp": ts})
                elif t == "response_item" and kind in ("function_call", "custom_tool_call", "web_search_call"):
                    tools[payload.get("name") or kind] += 1
            if not msgs:
                continue
            sid = meta["id"] or f.stem.replace("rollout-", "")[-36:]
            docs.append(doc("codex", sid, None, meta["timestamp"], msgs, cwd=meta["cwd"], model=meta["model"], source=f.relative_to(raw), tools=tools))


# ---------------------------------------------------------------- Hermes state.db
def harvest_hermes(raw: Path, docs: list):
    for db in raw.rglob("state.db"):
        if db.parent.name not in (".hermes", "hermes"):
            continue
        try:
            con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
            cols = {r[1] for r in con.execute("pragma table_info(messages)")}
            has_active = "active" in cols
            for sid, model, started, cwd, title in con.execute("select id, model, started_at, cwd, title from sessions where coalesce(archived,0)=0 order by started_at"):
                q = f"select role, content, tool_calls from messages where session_id=? {'and active=1' if has_active else ''} order by id" if "tool_calls" in cols else f"select role, content, null from messages where session_id=? {'and active=1' if has_active else ''} order by id"
                msgs, tools = [], Counter()
                for role, content, tool_calls in con.execute(q, (sid,)):
                    if role not in ("user", "assistant"):
                        continue
                    text = content or ""
                    if isinstance(text, str) and text.startswith("\0json:"):
                        try:
                            parts = json.loads(text[6:])
                            text = " ".join(p.get("text", "") for p in parts if isinstance(p, dict) and p.get("type") == "text")
                        except Exception:
                            pass
                    if tool_calls:
                        try:
                            for tc in json.loads(tool_calls):
                                name = (tc.get("function") or {}).get("name") or tc.get("name")
                                if name:
                                    tools[name] += 1
                        except Exception:
                            pass
                    text = (text or "").strip()
                    if text:
                        msgs.append({"role": role, "text": text, "timestamp": None})
                if msgs:
                    docs.append(doc("hermes", str(sid), title, iso_ts(started), msgs, cwd=cwd, model=model, source=db.relative_to(raw), tools=tools))
            con.close()
        except Exception as e:
            docs.append(doc("hermes", "unreadable", f"state.db unreadable: {str(e)[:80]}", None, [], source=db.relative_to(raw)))


# ---------------------------------------------------------------- OpenClaw (sqlite generic + jsonl)
def harvest_openclaw(raw: Path, docs: list):
    for home in {d for d in raw.rglob("*") if d.is_dir() and d.name in (".openclaw", "openclaw") and (d / "agents").is_dir()}:
        for ag in sorted(d for d in (home / "agents").iterdir() if d.is_dir()):
            for db in ag.rglob("*.sqlite"):
                try:
                    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
                    tables = [r[0] for r in con.execute("select name from sqlite_master where type='table'")]
                    msg_table = next((t for t in tables if {"role", "content"} <= {c[1] for c in con.execute(f'pragma table_info("{t}")')}), None)
                    if not msg_table:
                        con.close()
                        continue
                    cols = {c[1] for c in con.execute(f'pragma table_info("{msg_table}")')}
                    key = next((k for k in ("session_id", "sessionId", "conversation_id", "thread_id") if k in cols), None)
                    groups = {}
                    order = "rowid"
                    rows = con.execute(f'select {key + "," if key else "NULL,"} role, content from "{msg_table}" order by {order}').fetchall()
                    for gid, role, content in rows:
                        groups.setdefault(gid or "all", []).append((role, content))
                    for gid, items in groups.items():
                        msgs = [{"role": r, "text": str(c).strip(), "timestamp": None} for r, c in items if r in ("user", "assistant") and c and str(c).strip()]
                        if msgs:
                            docs.append(doc("openclaw", f"{ag.name}-{gid}", None, None, msgs, source=db.relative_to(raw)))
                    con.close()
                except Exception:
                    continue
            for f in sorted((ag / "sessions").rglob("*.jsonl")) if (ag / "sessions").is_dir() else []:
                msgs, tools = [], Counter()
                for o in iter_jsonl(f):
                    m = o.get("message") if isinstance(o.get("message"), dict) else o
                    role = m.get("role") or o.get("type")
                    text = blocks_text(m.get("content"), tools).strip()
                    if role in ("user", "assistant") and text:
                        msgs.append({"role": role, "text": text, "timestamp": iso_ts(o.get("timestamp"))})
                if msgs:
                    docs.append(doc("openclaw", f"{ag.name}-{f.stem}", None, msgs[0]["timestamp"], msgs, source=f.relative_to(raw), tools=tools))


# ---------------------------------------------------------------- ChatGPT (export array or live detail)
def chatgpt_turns(conv: dict):
    mapping = conv.get("mapping") or {}
    node, chain, seen = conv.get("current_node"), [], set()
    while node and node in mapping and node not in seen:
        seen.add(node)
        chain.append(mapping[node])
        node = mapping[node].get("parent")
    chain = list(reversed(chain)) if chain else sorted(mapping.values(), key=lambda n: ((n.get("message") or {}).get("create_time") or 0))
    turns = []
    for n in chain:
        m = n.get("message") or {}
        role = (m.get("author") or {}).get("role")
        c = m.get("content") or {}
        parts = c.get("parts") if isinstance(c.get("parts"), list) else ([c.get("text")] if c.get("text") else [])
        text = " ".join(p for p in parts if isinstance(p, str)).strip()
        if role in ("user", "assistant") and text and not (m.get("metadata") or {}).get("is_visually_hidden_from_conversation"):
            turns.append({"role": role, "text": text, "timestamp": iso_ts(m.get("create_time"))})
    return turns


def harvest_chatgpt(raw: Path, docs: list):
    for base in [d for d in raw.rglob("chatgpt") if d.is_dir() and "accounts" in d.parts]:
        exp = base / "export" / "conversations.json"
        if exp.exists():
            for conv in load_json(exp) or []:
                if isinstance(conv, dict) and conv.get("mapping"):
                    turns = chatgpt_turns(conv)
                    if turns:
                        docs.append(doc("chatgpt", conv.get("conversation_id") or conv.get("id") or str(len(docs)), conv.get("title"), iso_ts(conv.get("create_time")), turns, source=exp.relative_to(raw), last=iso_ts(conv.get("update_time"))))
        for f in sorted((base / "conversations").glob("*.json")) if (base / "conversations").is_dir() else []:
            conv = load_json(f) or {}
            if conv.get("mapping"):
                turns = chatgpt_turns(conv)
                if turns:
                    docs.append(doc("chatgpt", conv.get("conversation_id") or conv.get("id") or f.stem, conv.get("title"), iso_ts(conv.get("create_time")), turns, source=f.relative_to(raw), last=iso_ts(conv.get("update_time"))))


# ---------------------------------------------------------------- Claude.ai (export or live detail)
def claude_turns(conv: dict):
    msgs = conv.get("chat_messages") or []
    by_id = {m.get("uuid"): m for m in msgs if isinstance(m, dict)}
    leaf = conv.get("current_leaf_message_uuid")
    ordered = []
    if leaf and leaf in by_id:
        seen = set()
        node = leaf
        while node and node in by_id and node not in seen:
            seen.add(node)
            ordered.append(by_id[node])
            node = by_id[node].get("parent_message_uuid")
        ordered.reverse()
    else:
        ordered = msgs
    tools, turns = Counter(), []
    for m in ordered:
        sender = m.get("sender")
        role = "user" if sender in ("human", "user") else "assistant" if sender == "assistant" else None
        if not role:
            continue
        text = ""
        if isinstance(m.get("content"), list):
            text = blocks_text(m["content"], tools)
        if not text:
            text = m.get("text") or ""
        text = text.strip()
        if text:
            turns.append({"role": role, "text": text, "timestamp": (m.get("created_at") or "")[:19] or None})
    return turns, tools


def harvest_claude_chat(raw: Path, docs: list):
    for base in [d for d in raw.rglob("claude") if d.is_dir() and "accounts" in d.parts]:
        exp = base / "export" / "conversations.json"
        if exp.exists():
            for conv in load_json(exp) or []:
                if isinstance(conv, dict) and conv.get("chat_messages"):
                    turns, tools = claude_turns(conv)
                    if turns:
                        docs.append(doc("claude_chat", conv.get("uuid") or str(len(docs)), conv.get("name"), (conv.get("created_at") or "")[:19] or None, turns, source=exp.relative_to(raw), tools=tools, model=conv.get("model")))
        for f in sorted((base / "conversations").glob("*.json")) if (base / "conversations").is_dir() else []:
            conv = load_json(f) or {}
            if conv.get("chat_messages"):
                turns, tools = claude_turns(conv)
                if turns:
                    docs.append(doc("claude_chat", conv.get("uuid") or f.stem, conv.get("name"), (conv.get("created_at") or "")[:19] or None, turns, source=f.relative_to(raw), tools=tools, model=conv.get("model")))


# ---------------------------------------------------------------- commands
def cmd_normalize(mig: Path):
    raw, out = mig / "raw", mig / "pack" / "sessions"
    out.mkdir(parents=True, exist_ok=True)
    docs = []
    for h in (harvest_cowork, harvest_claude_code, harvest_codex, harvest_hermes, harvest_openclaw, harvest_chatgpt, harvest_claude_chat):
        try:
            h(raw, docs)
        except Exception as e:
            print(f"warning: {h.__name__} failed: {str(e)[:120]}", file=sys.stderr)
    seen = set()
    index = []
    for d in docs:
        if d["id"] in seen:
            d["id"] = d["id"] + "-" + str(sum(1 for s in seen if s.startswith(d["id"])))
        seen.add(d["id"])
        safe = re.sub(r"[^A-Za-z0-9_.-]", "_", d["id"])[:120]
        (out / f"{safe}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1))
        index.append({"id": d["id"], "file": f"{safe}.json", "harness": d["harness"], "title": d["title"], "timestamp": d["timestamp"], "last_activity": d["last_activity"],
                      "messages": len(d["messages"]), "user_turns": sum(1 for m in d["messages"] if m["role"] == "user"), "connectors": d["connectors"], "tools": list(d["tools"].keys())[:8], "cwd": d["cwd"]})
    index.sort(key=lambda x: x["last_activity"] or x["timestamp"] or "", reverse=True)
    (out / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1))
    by = Counter(i["harness"] for i in index)
    print(f"{len(index)} sessions normalized: " + ", ".join(f"{k} {v}" for k, v in sorted(by.items())))
    print(f"index: {out / 'index.json'}")


def load_index(mig: Path):
    idx = load_json(mig / "pack" / "sessions" / "index.json")
    if idx is None:
        sys.exit("run normalize first")
    return idx


def load_doc(mig: Path, entry):
    return load_json(mig / "pack" / "sessions" / entry["file"]) or {}


def cmd_search(mig: Path, pattern: str, harness=None, limit=20):
    pat = pattern.lower()
    hits = []
    for e in load_index(mig):
        if harness and e["harness"] != harness:
            continue
        d = load_doc(mig, e)
        lines = []
        if pat in (d.get("title") or "").lower():
            lines.append(("title", d["title"]))
        for m in d["messages"]:
            for line in m["text"].splitlines():
                if pat in line.lower():
                    lines.append((m["role"], line.strip()[:200]))
        if lines:
            hits.append((len(lines), e, lines[:3]))
    hits.sort(key=lambda h: (-h[0], h[1]["last_activity"] or ""), reverse=False)
    for n, e, lines in hits[:limit]:
        print(f"{e['id']}  [{e['harness']}] {e['title'][:60]}  {e['last_activity'] or e['timestamp'] or ''}  hits={n}")
        for role, line in lines:
            print(f"    {role}: {line}")
    if not hits:
        print("no hits")


def cmd_view(mig: Path, prefix: str, max_messages=80):
    matches = [e for e in load_index(mig) if e["id"].startswith(prefix) or e["id"].endswith(prefix)]
    if len(matches) != 1:
        sys.exit(f"{len(matches)} sessions match {prefix!r}, be more specific")
    d = load_doc(mig, matches[0])
    print(f"# {d['title']}  [{d['harness']}]  {d['timestamp'] or ''}  cwd={d.get('cwd') or '-'}  connectors={', '.join(d['connectors']) or '-'}")
    for i, m in enumerate(d["messages"][:max_messages], 1):
        print(f"\n── #{i} {m['role']} ──\n{m['text'][:2000]}")


def cmd_seed(mig: Path, slug: str, ids: list, max_sessions=12, max_messages=40):
    idx = {e["id"]: e for e in load_index(mig)}
    chosen = [idx[i] for i in ids if i in idx]
    chosen.sort(key=lambda e: e["last_activity"] or e["timestamp"] or "", reverse=True)
    chosen = chosen[:max_sessions]
    pack = mig / "pack"
    pack.mkdir(exist_ok=True)
    md, jsonl = [f"# History for {slug}\n"], []
    label = {"cowork": "Claude Cowork", "claude_code": "Claude Code", "codex": "Codex", "hermes": "Hermes", "openclaw": "OpenClaw", "chatgpt": "ChatGPT", "claude_chat": "Claude.ai"}
    total = 0
    for e in chosen:
        d = load_doc(mig, e)
        intro = f"From {label.get(d['harness'], d['harness'])}, \"{d['title']}\", {(d['timestamp'] or '')[:10]}:"
        md.append(f"\n## {intro}\n")
        jsonl.append({"role": "user", "message": {"content": [{"type": "text", "text": intro}]}})
        for m in d["messages"][-max_messages:]:
            text = m["text"][:1500]
            md.append(f"**{m['role']}:** {text}\n")
            jsonl.append({"role": m["role"], "message": {"content": [{"type": "text", "text": text}]}})
            total += len(text)
            if total > 400_000:
                break
        if total > 400_000:
            md.append("\n(history trimmed at 400 KB)\n")
            break
    (pack / f"{slug}-history.md").write_text("\n".join(md))
    (pack / f"{slug}-history.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in jsonl) + "\n")
    print(f"{len(chosen)} sessions, {len(jsonl)} messages, {total // 1024} KB -> {pack / (slug + '-history.md')} and .jsonl")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "parse":
        cmd_normalize(cmd_parse(args[0], args[1] if len(args) > 1 else "/workspace/migration"))
        return
    mig, rest = Path(args[0]).expanduser().resolve(), args[1:]
    if cmd == "normalize":
        cmd_normalize(mig)
    elif cmd == "search":
        harness = rest[rest.index("--from") + 1] if "--from" in rest else None
        limit = int(rest[rest.index("-n") + 1]) if "-n" in rest else 20
        pattern = next(a for a in rest if not a.startswith("-") and a not in (harness, str(limit)))
        cmd_search(mig, pattern, harness, limit)
    elif cmd == "view":
        mx = int(rest[rest.index("--max") + 1]) if "--max" in rest else 80
        cmd_view(mig, rest[0], mx)
    elif cmd == "seed":
        ms = int(rest[rest.index("--max-sessions") + 1]) if "--max-sessions" in rest else 12
        mm = int(rest[rest.index("--max-messages") + 1]) if "--max-messages" in rest else 40
        cmd_seed(mig, rest[0], rest[1].split(","), ms, mm)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## collect-windows.ps1

```powershell
# The collector Import Bot runs on a Windows computer. PowerShell 5.1 or newer and
# the tar.exe that ships with Windows 10 1803 and later. Allowlist only. Writes
# %TEMP%\grokbot-import\grokbot-import.tgz plus connector-names.txt.
#
# Credential-bearing configs are NOT packed. Their connector names and retention
# keys are reduced into connector-names.txt with ConvertFrom-Json.
#
# Set $env:GB_TRANSCRIPTS = "0" to skip session transcripts and databases.
#
# How the bot runs it: write this file on the box, CopyFromBox it to
# $env:TEMP\collect-windows.ps1, then Shell with the user's machineId:
#   powershell -NoProfile -ExecutionPolicy Bypass -File "$env:TEMP\collect-windows.ps1"
#
# All file writes go through .NET so they are UTF-8 without a BOM. PowerShell 5.1's
# Set-Content and Add-Content with -Encoding UTF8 add a BOM, which corrupts the
# first path in tar's file list.
$ErrorActionPreference = "Continue"
$T = Join-Path $env:TEMP "grokbot-import"; New-Item -ItemType Directory -Force -Path $T | Out-Null
$OUT = Join-Path $T "grokbot-import.tgz"; $N = Join-Path $T "connector-names.txt"; $E = Join-Path $T "collect-errors.txt"; $L = Join-Path $T "filelist.txt"
[System.IO.File]::WriteAllText($N, ""); [System.IO.File]::WriteAllText($E, "")
function Out-Line([string]$path, [string]$text) { [System.IO.File]::AppendAllText($path, $text + "`n") }
$A = Join-Path $env:APPDATA "Claude"; $H = $env:USERPROFILE
$includeTranscripts = ($env:GB_TRANSCRIPTS -ne "0")
$maxDb = 100MB

function Add-Names([string]$file, [scriptblock]$extract) {
  if (Test-Path $file) {
    Out-Line $N ("## " + $file)
    try { $names = & $extract (Get-Content -Raw -Path $file | ConvertFrom-Json); if ($names) { Out-Line $N ($names -join "`n") } }
    catch { Out-Line $E ("names failed for " + $file + ": " + $_.Exception.Message) }
  }
}
Add-Names (Join-Path $A "claude_desktop_config.json") { param($o) if ($o.mcpServers) { $o.mcpServers.PSObject.Properties.Name } }
Add-Names (Join-Path $H ".claude.json") { param($o) $k = @(); if ($o.mcpServers) { $k += $o.mcpServers.PSObject.Properties.Name }; if ($o.projects) { foreach ($p in $o.projects.PSObject.Properties) { if ($p.Value.mcpServers) { $k += ($p.Value.mcpServers.PSObject.Properties.Name | ForEach-Object { "$_ (project $($p.Name))" }) } } }; $k }
Add-Names (Join-Path $H ".openclaw\openclaw.json") { param($o) $k = @(); foreach ($s in "channels","connectors","plugins","mcpServers","tools") { $v = $o.$s; if ($v -is [System.Array]) { $k += ($v | ForEach-Object { if ($_.name) { $_.name } elseif ($_.id) { $_.id } else { "$_" } }) } elseif ($v) { $k += $v.PSObject.Properties.Name } }; $k }
$toml = Join-Path $H ".codex\config.toml"; if (Test-Path $toml) { Out-Line $N ("## " + $toml); Select-String -Path $toml -Pattern '^\s*\[mcp_servers\.([^\].]+)' | ForEach-Object { Out-Line $N $_.Matches[0].Groups[1].Value } }
$settings = Join-Path $H ".claude\settings.json"; if (Test-Path $settings) { Out-Line $N ("## " + $settings); Select-String -Path $settings -Pattern '"[a-zA-Z]*[cC]leanupPeriodDays"[^,}]*' -AllMatches | ForEach-Object { $_.Matches | ForEach-Object { Out-Line $N $_.Value } } }
$hcfg = Join-Path $H ".hermes\config.yaml"; if (Test-Path $hcfg) { Out-Line $N ("## " + $hcfg); Get-Content $hcfg | Where-Object { $_ -notmatch 'key|token|secret|password' } | Where-Object { $_ -match '^[a-zA-Z_]+:|^\s+-\s' } | Select-Object -First 60 | ForEach-Object { Out-Line $N $_ } }
foreach ($d in (Join-Path $H ".cursor"), (Join-Path $H ".gemini")) { if (Test-Path $d) { Out-Line $N ("## also-present " + $d) } }

$never = '\\(uploads|outputs|skills-plugin|rpm|debug|backups|ccd-session-secrets|subagents|credentials|node_modules|\.git)\\|\.audit-key$|\\host-creds-|\\\.claude\.json$'
$files = New-Object System.Collections.Generic.List[string]
$files.Add($N)
function Add-Tree([string]$root, [string[]]$patterns, [switch]$recent, [long]$cap = 5MB) {
  if (-not (Test-Path $root)) { return }
  $cut = (Get-Date).AddDays(-90)
  Get-ChildItem -Path $root -Recurse -File -Include $patterns -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch $never -and $_.Length -lt $cap -and (-not $recent -or $_.LastWriteTime -gt $cut) } | ForEach-Object { $files.Add($_.FullName) }
}
foreach ($r in (Join-Path $A "local-agent-mode-sessions"), (Join-Path $A "claude-code-sessions")) {
  Add-Tree $r @("*.md", "*.json", "audit.jsonl")
  if ($includeTranscripts) { Add-Tree $r @("*.jsonl") -recent }
}
Add-Tree (Join-Path $A "cowork_plugins") @("*.md", "*.json", "*.yaml")
foreach ($f in (Join-Path $H ".claude\CLAUDE.md"), (Join-Path $H ".codex\AGENTS.md"), (Join-Path $H ".codex\AGENTS.override.md"), (Join-Path $H ".hermes\memories\MEMORY.md"), (Join-Path $H ".hermes\memories\USER.md")) { if (Test-Path $f) { $files.Add($f) } }
foreach ($d in ".claude\skills", ".claude\rules", ".claude\commands", ".claude\agents", ".codex\memories", ".codex\skills", ".agents\skills", ".hermes\skills", ".openclaw\skills", ".openclaw\workspace", "Claude\Scheduled", "Documents\Claude\Scheduled") { Add-Tree (Join-Path $H $d) @("*.md", "*.json", "*.yaml") }
Add-Tree (Join-Path $H ".claude\projects") @("*.md")
if ($includeTranscripts) {
  foreach ($d in ".claude\projects", ".codex\sessions", ".openclaw\agents") { Add-Tree (Join-Path $H $d) @("*.jsonl") -recent }
  $db = Join-Path $H ".hermes\state.db"; if ((Test-Path $db) -and ((Get-Item $db).Length -lt $maxDb)) { $files.Add($db) }
  Add-Tree (Join-Path $H ".openclaw\agents") @("*.sqlite") -cap $maxDb
}
$files.Add($E)
[System.IO.File]::WriteAllLines($L, [string[]]($files | Select-Object -Unique))
& tar.exe -czf $OUT -T $L 2>> $E
"archive: $OUT"
"size: " + [math]::Round((Get-Item $OUT).Length / 1KB) + "K"
"files: " + ($files | Select-Object -Unique).Count
"errors: " + ((Get-Content $E | Where-Object { $_ -and $_ -notmatch 'Removing leading' }).Count)
```

## pull-chatgpt-codex.ps1

```powershell
# ChatGPT conversations through the Codex sign-in already on the user's Windows
# computer. PowerShell 5.1 or newer, tar.exe (Windows 10 1803 and later). The token
# is read from %USERPROFILE%\.codex\auth.json, used only in request headers to
# chatgpt.com, and never written anywhere. Output: one JSON per conversation, tarred.
#
# Requires Codex signed in with a ChatGPT account (auth_mode "chatgpt"). Stops at 300
# conversations or when the list ends. All file writes are UTF-8 without a BOM.
$A = Join-Path $env:USERPROFILE ".codex\auth.json"
$T = Join-Path $env:TEMP "grokbot-import\chatgpt"; New-Item -ItemType Directory -Force -Path (Join-Path $T "conversations") | Out-Null
$OUT = Join-Path $env:TEMP "grokbot-import\chatgpt-conversations.tgz"
if (-not (Test-Path $A)) { "status: no codex login"; return }
$o = Get-Content -Raw $A | ConvertFrom-Json
if ($o.auth_mode -ne "chatgpt") { "status: codex login is not a chatgpt account"; return }
$tok = $o.tokens.access_token; $acc = $o.tokens.account_id
if (-not $tok) { "status: no chatgpt token"; return }
$h = @{ Authorization = "Bearer $tok"; "ChatGPT-Account-ID" = "$acc"; "User-Agent" = "Mozilla/5.0" }
$n = 0; $off = 0; $status = "ok"
while ($off -lt 300) {
  try { $page = Invoke-RestMethod -Headers $h -Uri "https://chatgpt.com/backend-api/conversations?offset=$off&limit=100&order=updated" -TimeoutSec 30 }
  catch { $status = "list request failed: " + $_.Exception.Message; break }
  if (-not $page.items -or $page.items.Count -eq 0) { break }
  foreach ($c in $page.items) {
    try {
      $detail = Invoke-RestMethod -Headers $h -Uri "https://chatgpt.com/backend-api/conversation/$($c.id)" -TimeoutSec 30
      [System.IO.File]::WriteAllText((Join-Path $T ("conversations\" + $c.id + ".json")), ($detail | ConvertTo-Json -Depth 60 -Compress))
      $n++
    } catch {}
    Start-Sleep -Milliseconds 300
  }
  $off += 100
}
& tar.exe -czf $OUT -C $T conversations
"status: $status"; "conversations: $n"; "archive: $OUT"
```
