---
name: distro-scripts
description: "The distro.py helper, copied out by the install command in distro-setup. Never read or retype it."
---

# distro-scripts

Part of the Distro Bot agent preset.

# distro-scripts

The distro.py helper. The install command in distro-setup copies it out by its marker, so never read or retype it. Commands: install, init, status, set, ingest, report, winners, propose, approve, applied, revert, reject, changes, learn, playbook, site, scan, topic, topics, lead, leads, suppress, fal, higgs, grok, sizes. Each prints one JSON line.

```python
#!/usr/bin/env python3
# DISTRO_TOOLS_V1: Distro Bot helper: settings, performance ingest and analysis, the change ledger and budget caps,
# the playbook, site snapshots, topic scans, the outbound ledger, and ad creative on FAL, Higgsfield, or Grok Imagine.
# Every command prints one JSON line. Standard library only, plus ffmpeg for ad sizes.
import base64
import calendar
import csv
import datetime as dt
import email.utils
import html
import json
import math
import mimetypes
import os
import random
import re
import shutil
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

mimetypes.add_type("image/webp", ".webp")
# A user's bots share /workspace, so every file lives beside this script in the folder the install picked.
HOME = os.environ.get("DISTRO_HOME") or os.path.dirname(os.path.abspath(__file__))
P = {k: os.path.join(HOME, v) for k, v in (("state", "state.json"), ("perf", "perf.csv"), ("changes", "changes.jsonl"),
                                           ("playbook", "playbook.md"), ("topics", "topics.jsonl"), ("leads", "leads.csv"),
                                           ("sends", "sends.csv"), ("suppress", "suppress.txt"))}
ENV = os.environ.get
FAL_QUEUE, FAL_API, FAL_REST = ENV("DISTRO_FAL_QUEUE", "https://queue.fal.run"), ENV("DISTRO_FAL_API", "https://api.fal.ai"), ENV("DISTRO_FAL_REST", "https://rest.alpha.fal.ai")
XAI_API, HF_API = ENV("DISTRO_XAI_API", "https://api.x.ai/v1"), ENV("DISTRO_HF_API", "https://api.higgsfield.ai")
HN_API, NEWS_RSS = ENV("DISTRO_HN_API", "https://hn.algolia.com/api/v1"), ENV("DISTRO_NEWS_RSS", "https://news.google.com/rss/search")
SECRET_FILES = [p for p in (ENV("DISTRO_SECRETS", ""), "/home/box/agent-data/box-secrets.json") if p]
KEYS = ("FAL_KEY", "XAI_API_KEY", "HF_KEY")
UA = "Mozilla/5.0 (X11; Linux x86_64) distro-bot/1.0"
ROUTINES = ("Campaign check", "Trend scan", "Outbound replies", "Weekly distro review")
ROLES, ACCESS = ("sales", "voice", "intel", "seo", "qa"), ("connector", "browser", "export", "off")
SPEND_KINDS = ("budget", "bid", "launch", "pause")
KINDS = SPEND_KINDS + ("creative", "targeting")
LEARN_KINDS = ("hook", "angle", "offer", "audience", "format", "channel", "timing", "voice", "avoid", "other")
STAGES = ("new", "drafted", "sent", "replied", "handed_off", "closed")
STOP_WHY = ("optout", "bounce", "customer", "no", "other")
GAPS, MIN_IMPR = (3, 5, 7), 1000
FIELDS = ["date", "platform", "campaign", "adset", "ad", "spend", "impressions", "clicks", "conversions", "revenue",
          "engagements", "reach", "currency", "source", "read_at"]
NUMS = FIELDS[5:12]
LEAD_FIELDS = ["email", "name", "company", "title", "domain", "source", "stage", "step", "last_touch", "next_touch",
               "thread", "said", "replied_at", "handed_to", "note", "added"]
FREE_MAIL = set("gmail.com googlemail.com yahoo.com outlook.com hotmail.com live.com icloud.com me.com aol.com proton.me "
                "protonmail.com gmx.com mail.com yandex.com zoho.com".split())
ALIASES = {"facebook": "meta", "instagram": "meta", "meta ads": "meta", "google ads": "google", "adwords": "google",
           "twitter": "x", "x ads": "x", "x posts": "x-organic", "x organic": "x-organic", "linkedin ads": "linkedin",
           "tiktok ads": "tiktok", "reddit ads": "reddit", "bing": "microsoft", "microsoft ads": "microsoft"}
FORBIDDEN_INPUT = re.compile(r"(api_?key|token|secret|password)", re.I)
GROK_IMAGE, GROK_VIDEO = "grok-imagine-image-2.0", "grok-imagine-video-1.5"
HF_IMAGE, HF_VIDEO = "higgsfield-ai/soul/v2/standard", "bytedance/seedance-2.0/image-to-video"
# xAI list prices per second of video on 2026-10-01. /v1/models returns live image prices but none for video.
GROK_VIDEO_USD = {"grok-imagine-video": 0.05, "grok-imagine-video-1.5": 0.08}
PLACEMENTS = {"meta": [("square", 1080, 1080), ("portrait", 1080, 1350), ("story", 1080, 1920)],
              "google": [("square", 1200, 1200), ("landscape", 1200, 628), ("portrait", 960, 1200)],
              "x": [("square", 1200, 1200), ("landscape", 1200, 628)],
              "linkedin": [("square", 1200, 1200), ("landscape", 1200, 628)],
              "tiktok": [("story", 1080, 1920)],
              "reddit": [("square", 1200, 1200), ("portrait", 1080, 1350), ("landscape", 1920, 1080)]}
REPAIRED = []  # tools reinstalled after a computer update dropped them


# ---------- basics ----------

def now_dt():
    v = ENV("DISTRO_NOW")
    d = dt.datetime.fromisoformat(v.replace("Z", "+00:00")) if v else dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)


def now():
    return now_dt().isoformat()


def today():
    return dt.date.fromisoformat(ENV("DISTRO_TODAY")) if ENV("DISTRO_TODAY") else dt.date.today()


def emit(**data):
    if REPAIRED:
        data.setdefault("repaired", REPAIRED)
    print(json.dumps(data, ensure_ascii=False, default=str))


def die(message, **extra):
    emit(error=message, **extra)
    sys.exit(1)


def opts_of(args):
    opts, rest, i = {}, [], 0
    while i < len(args):
        if args[i].startswith("--"):
            key, vals = args[i][2:], []
            while i + 1 < len(args) and not args[i + 1].startswith("--"):
                vals.append(args[i + 1])
                i += 1
            opts[key] = vals[0] if len(vals) == 1 else (vals or True)
        else:
            rest.append(args[i])
        i += 1
    return opts, rest


def topt(opts, key):
    v = opts.get(key)
    return " ".join(v) if isinstance(v, list) else v if isinstance(v, str) else ""


def fopt(opts, key, default=None):
    v = topt(opts, key)
    if not v:
        return default
    try:
        return float(v)
    except ValueError:
        die("--%s must be a number" % key)


def r2(v):
    return None if v is None else round(v, 2)


def div(a, b):
    return round(a / b, 2) if b else None


def pct(a, b):
    return round(100.0 * a / b, 2) if b else None


def fmtnum(v):
    return ("%.6f" % v).rstrip("0").rstrip(".")


def slug(text, n=40):
    return re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")[:n].rstrip("-") or "item"


def num(v):
    if v is None or isinstance(v, (int, float)):
        return None if v is None else float(v)
    s = re.sub(r"^[^\d\-.]+", "", str(v).strip().replace(",", "").replace("\u00a0", "")).rstrip("%").strip()
    try:
        return float(s)
    except ValueError:
        return None


def parse_date(s, dayfirst=False):
    if isinstance(s, dt.date):
        return s
    s = str(s or "").strip()
    try:
        m = re.match(r"(\d{4})-(\d{1,2})-(\d{1,2})", s)
        if m:
            return dt.date(int(m[1]), int(m[2]), int(m[3]))
        m = re.match(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", s)
        if m:
            a, b, y = int(m[1]), int(m[2]), int(m[3])
            return dt.date(y + 2000 if y < 100 else y, *((b, a) if dayfirst else (a, b)))
    except ValueError:
        return None
    for fmt in ("%b %d, %Y", "%B %d, %Y", "%d %b %Y", "%Y/%m/%d"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    w = parse_when(s)
    return w.date() if w else None


def parse_when(s):
    """A timestamp from ISO, RFC 822, or epoch text, as an aware datetime, or None."""
    s = str(s or "").strip()
    if not s:
        return None
    try:
        d = dt.datetime.fromtimestamp(float(s), dt.timezone.utc) if re.fullmatch(r"\d{9,10}(\.\d+)?", s) else \
            dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        try:
            d = email.utils.parsedate_to_datetime(s)
        except (TypeError, ValueError, IndexError):
            try:
                d = dt.datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y")
            except ValueError:
                return None
    return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)


def jsonl(path):
    out = []
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            try:
                out.append(json.loads(line))
            except ValueError:
                continue
    return out


def write_jsonl(path, items):
    with open(path + ".tmp", "w", encoding="utf-8") as f:
        f.writelines(json.dumps(i, ensure_ascii=False) + "\n" for i in items)
    os.replace(path + ".tmp", path)


def next_id(items, prefix):
    return prefix + str(max([int(i["id"][1:]) for i in items if re.fullmatch(prefix + r"\d+", i.get("id", ""))], default=0) + 1)


# ---------- secrets, http, tools ----------

def secret(name):
    value = ENV(name, "").strip()
    for path in SECRET_FILES:
        if value:
            break
        try:
            data = json.load(open(path, encoding="utf-8"))
            value = str((data.get("card") or {}).get(name) or data.get(name) or "").strip()
        except (OSError, ValueError, AttributeError):
            continue
    return value


def scrub(text):
    for k in KEYS:
        v = secret(k)
        for part in ([v] + [p for p in v.split(":") if len(p) >= 8]) if v else []:
            text = text.replace(part, "[" + k + "]")
    return text


def http(method, url, body=None, headers=None, raw=None, timeout=60):
    h = {"User-Agent": "distro-bot", "Accept": "application/json", **(headers or {})}
    if body is not None:
        raw, h["Content-Type"] = json.dumps(body).encode(), "application/json"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=raw, method=method, headers=h), timeout=timeout) as r:
            code, data = r.status, r.read()
    except urllib.error.HTTPError as err:
        code, data = err.code, err.read()
    except (urllib.error.URLError, OSError) as err:
        return 0, {"detail": scrub(str(err))[:160]}
    try:
        return code, json.loads(data.decode() or "{}")
    except (ValueError, UnicodeDecodeError):
        return code, {"detail": data[:200].decode("utf-8", "replace")}


def fetch_text(url, limit=3 << 20):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw, final, code, ctype = r.read(limit), r.geturl(), r.status, r.headers.get("Content-Type", "")
    except urllib.error.HTTPError as err:
        return err.code, url, ""
    except (urllib.error.URLError, OSError, ValueError) as err:
        return 0, url, str(err)[:160]
    m = re.search(r"charset=([\w-]+)", ctype)
    try:
        return code, final, raw.decode(m[1] if m else "utf-8", "replace")
    except LookupError:
        return code, final, raw.decode("utf-8", "replace")


def download(url, dest, limit=500 << 20):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if url.startswith("data:"):
        head, _, payload = url.partition(",")
        open(dest, "wb").write(base64.b64decode(payload) if ";base64" in head else urllib.parse.unquote_to_bytes(payload))
        return
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "distro-bot"}), timeout=300) as r, open(dest, "wb") as f:
        total = 0
        for chunk in iter(lambda: r.read(1 << 20), b""):
            total += len(chunk)
            if total > limit:
                raise OSError("file over the download limit")
            f.write(chunk)


def repair_tools():
    """An image update of the computer drops apt packages, so reinstall ffmpeg when it is gone."""
    if all(shutil.which(t) for t in ("ffmpeg", "ffprobe")):
        return ""
    if ENV("DISTRO_APT"):
        cmd = [ENV("DISTRO_APT")]
    elif not shutil.which("apt-get"):
        return "no apt-get on this computer"
    else:
        cmd = ["apt-get"] if os.geteuid() == 0 else ["sudo", "-n", "apt-get"] if shutil.which("sudo") else None
        if not cmd:
            return "not root and no sudo"
    for args in (["update", "-qq"], ["install", "-y", "-qq", "ffmpeg"]):
        try:
            r = subprocess.run(cmd + args, capture_output=True, text=True, timeout=900, env={**os.environ, "DEBIAN_FRONTEND": "noninteractive"})
        except (OSError, subprocess.TimeoutExpired) as err:
            return str(err)[:160]
        if r.returncode:
            return ((r.stderr or r.stdout).strip().splitlines() or ["apt-get failed"])[-1][:160]
    if shutil.which("ffmpeg"):
        REPAIRED.append("ffmpeg")
    return ""


def ff(cmd):
    if not shutil.which("ffmpeg"):
        err = repair_tools()
        if not shutil.which("ffmpeg"):
            die("ffmpeg is missing, likely dropped by a computer update, and reinstalling it failed: " + (err or "not found"))
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    if r.returncode:
        die(cmd[0] + " failed", detail=r.stderr.strip().splitlines()[-3:])
    return r


# ---------- state ----------

def fresh_state():
    return {"version": 1, "created": now(), "setup": "step 1", "product": "", "site": "", "audience": "", "goal": "",
            "conversion": "", "currency": "USD", "monthly_cap": 0.0, "daily_cap": 0.0, "max_step_pct": 20, "autopilot": False,
            "creative_cap": 2.0, "media": "", "send_cap": 20, "steps": 3, "keywords": [], "competitors": [], "platforms": {},
            "teammates": {}, "routines_on": [], "last": {}, "jobs": {}}


def load():
    if not os.path.exists(P["state"]):
        die("no state yet, run: distro.py init")
    s = json.load(open(P["state"], encoding="utf-8"))
    for k, v in fresh_state().items():
        s.setdefault(k, v)
    return s


def save(s):
    os.makedirs(HOME, exist_ok=True)
    json.dump(s, open(P["state"] + ".tmp", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    os.replace(P["state"] + ".tmp", P["state"])


def cmd_install(a):
    base, home, n = ENV("DISTRO_BASE", "/workspace"), ENV("DISTRO_DIR", ""), 1
    default = os.path.join(base, "distro-bot")
    while not home:
        d = default + ("-%d" % n if n > 1 else "")
        home, n = ("" if os.path.exists(os.path.join(d, "state.json")) else d), n + 1
    code = open(os.path.abspath(__file__), encoding="utf-8").read()
    compile(code, "distro.py", "exec")
    os.makedirs(home, exist_ok=True)
    dest = os.path.join(home, "distro.py")
    if os.path.abspath(__file__) != dest:
        open(dest, "w", encoding="utf-8").write(code)
    err = repair_tools()
    moved = home != default and not ENV("DISTRO_DIR")
    emit(ok=True, installed=dest, home=home, moved=moved, ffmpeg=bool(shutil.which("ffmpeg")), tool_error=err,
         note="Another Distro Bot owns %s, so rewrite your STATE memory line to python3 %s" % (default, dest) if moved else "")


def cmd_init(a):
    existed = os.path.exists(P["state"])
    if not existed:
        save(fresh_state())
    emit(ok=True, existed=existed, home=HOME, setup=load()["setup"])


def resume_cmd(rid, job):
    return {"xai": "distro.py grok result " + rid, "higgs": "distro.py higgs result " + rid}.get(
        job.get("provider"), "distro.py fal result %s %s" % (job.get("endpoint"), rid))


def latest(rows):
    out = {}
    for r in rows:
        out[r["platform"]] = max(out.get(r["platform"], r["date"]), r["date"])
    return out


def cmd_status(a):
    s, rows, ch, leads, t = load(), read_perf(), jsonl(P["changes"]), read_leads(), today()
    emit(home=HOME, setup=s["setup"], **{k: s[k] for k in ("product", "site", "audience", "goal", "conversion", "currency")},
         caps={"monthly": s["monthly_cap"], "daily": s["daily_cap"], "max_step_pct": s["max_step_pct"]},
         autopilot=s["autopilot"], creative_cap=s["creative_cap"], media=s["media"], keys={k: bool(secret(k)) for k in KEYS},
         **{k: s[k] for k in ("platforms", "teammates", "routines_on", "keywords", "competitors", "last")},
         spend=spend_numbers(s, rows, frame=t) if rows else None,
         freshness={p: {"latest": d.isoformat(), "days_old": (t - d).days} for p, d in sorted(latest(rows).items())},
         changes={"waiting_yes": sum(c["status"] == "proposed" and c["lane"] == "ask" for c in ch),
                  "approved_not_applied": sum(c["status"] == "approved" for c in ch),
                  "autopilot_ready": sum(c["status"] == "proposed" and c["lane"] == "autopilot" for c in ch)},
         media_jobs_pending=[{"id": k, "resume": resume_cmd(k, j)} for k, j in s["jobs"].items() if j.get("status") not in ("COMPLETED", "FAILED")],
         leads={"due": len(due_leads(s, leads)), "replied_not_handed": sum(x["stage"] == "replied" for x in leads),
                "sent_today": sends_on(t), "send_cap": s["send_cap"], "steps": s["steps"]},
         topics_new=sum(x.get("status") == "new" for x in jsonl(P["topics"])),
         playbook_entries=sum(len(v) for v in read_playbook().values()), ffmpeg=bool(shutil.which("ffmpeg")))


SET_TEXT = ("setup", "product", "site", "audience", "goal", "conversion")
SET_NUM = {"monthly_cap": (0, 1e9, float), "daily_cap": (0, 1e9, float), "creative_cap": (0, 1e6, float),
           "max_step_pct": (1, 100, int), "send_cap": (0, 500, int), "steps": (1, 6, int)}


def cmd_set(a):
    if len(a) < 2:
        die("usage: distro.py set <key> <value>. Keys: %s, %s, currency, autopilot on|off, media fal|higgs|grok|none, keywords a,b, "
            "competitors a,b, platform <name> <%s> [account], teammate <%s> <id or name|none>, routine \"<name>\" on|off, last <name>"
            % (", ".join(SET_TEXT), ", ".join(SET_NUM), "|".join(ACCESS), "|".join(ROLES)))
    s, key, rest = load(), a[0], a[1:]
    value, out = " ".join(rest).strip(), {}
    if key in SET_TEXT:
        s[key] = value
    elif key in SET_NUM:
        lo, hi, kind = SET_NUM[key]
        v = num(value)
        if v is None or not lo <= v <= hi:
            die("%s must be a number from %s to %s" % (key, lo, int(hi)))
        s[key] = kind(round(v, 2))
        if key == "monthly_cap" and v and not s["daily_cap"]:
            s["daily_cap"] = out["daily_cap"] = round(v / 30.0, 2)
    elif key == "currency" and re.fullmatch(r"[A-Za-z]{3}", value):
        s[key] = value.upper()
    elif key == "autopilot" and value.lower() in ("on", "off"):
        s[key] = value.lower() == "on"
    elif key == "media" and value in ("fal", "higgs", "grok", "none"):
        s[key] = value
    elif key in ("keywords", "competitors"):
        s[key] = [x.strip() for x in value.split(",") if x.strip()]
    elif key == "platform" and len(rest) >= 2 and rest[1] in ACCESS:
        name = out["platform"] = norm_platform(rest[0])
        s["platforms"].pop(name, None)
        if rest[1] != "off":
            s["platforms"][name] = {"access": rest[1], "account": " ".join(rest[2:]), "since": today().isoformat()}
    elif key == "teammate" and rest[0] in ROLES:
        who = " ".join(rest[1:]).strip()
        s["teammates"].pop(rest[0], None)
        if who.lower() not in ("", "none", "off"):
            s["teammates"][rest[0]] = who
    elif key == "routine" and len(rest) >= 2 and rest[-1] in ("on", "off"):
        name = next((r for r in ROUTINES if r.lower() == " ".join(rest[:-1]).strip().strip('"').lower()), None)
        if not name:
            die("routines: " + ", ".join(ROUTINES))
        s["routines_on"] = [r for r in s["routines_on"] if r != name] + ([name] if rest[-1] == "on" else [])
    elif key == "last":
        s["last"][slug(value, 20)] = now()
    else:
        die("bad setting: %s %s. Run distro.py set for the keys and values." % (key, value))
    save(s)
    emit(ok=True, key=key, value={"platform": s["platforms"], "teammate": s["teammates"], "routine": s["routines_on"],
                                  "last": s["last"]}.get(key, s.get(key)), **out)


# ---------- performance data ----------

PREFIXES = ("public metrics ", "non public metrics ", "organic metrics ", "promoted metrics ", "metrics ", "segments ", "insights ")
SYN = [("date", "date|day|reporting starts|date start|start date|start date in utc|gregorian date|by day|created at|time period"),
       ("campaign", "campaign name|campaign|campaign title"),
       ("adset", "ad set name|ad set|adset name|adset|ad group name|ad group|adgroup name|adgroup|line item name|line item|ad squad name|ad squad"),
       ("ad", "ad name|ad|creative name|creative|promoted tweet|tweet text|post text|text|tweet|post|tweet id|post id|id"),
       ("spend", "amount spent|spend|cost|total spent|billed charge local micro|cost micros|costmicros|spend micros"),
       ("impressions", "impressions|impression count|impression|impr"),
       ("clicks", "link clicks|url link clicks|url clicks|inline link clicks|outbound clicks|clicks destination|clicks|clicks all"),
       ("conversions", "conversions|results|website purchases|purchases|leads|website leads|sign ups|signups|registrations completed|complete registration|all conv|conv"),
       ("revenue", "conversion value|conversions value|conversionsvalue|purchases conversion value|website purchases conversion value|purchase value|total conversion value|conv value|revenue|value"),
       ("engagements", "engagements|total engagements|post engagements|engagement count"),
       ("reach", "reach"), ("currency", "currency|account currency|currency code")]
ENGAGE_PARTS = set("like count|likes|retweet count|repost count|retweets|reposts|reply count|replies|quote count|quotes|bookmark count|bookmarks".split("|"))
SPEND_RE = re.compile(r"^(amount spent|spend|total spent|cost)( [a-z]{3})?$")
TEXT_AD = ("tweet text", "post text", "text")


def norm_header(h):
    h = re.sub(r"[^a-z0-9]+", " ", re.sub(r"([a-z])([A-Z])", r"\1 \2", str(h)).lower()).strip()
    for _ in range(3):
        for p in PREFIXES:
            if h.startswith(p) and len(h) > len(p):
                h = h[len(p):]
    return h


def norm_platform(p):
    p = re.sub(r"[\s_-]+", " ", str(p).strip().lower())
    if p not in ALIASES and p.endswith(" ads"):
        p = p[:-4]
    return ALIASES.get(p, p).replace(" ", "-")


def map_headers(headers):
    normed, mapping = {h: norm_header(h) for h in headers}, {}
    for field, syns in SYN:
        for syn in syns.split("|"):
            hit = next((h for h, n in normed.items() if (n == syn or field == "spend" and SPEND_RE.match(n)) and h not in mapping.values()), None)
            if hit is not None:
                mapping[field] = hit
                break
    parts = [h for h, n in normed.items() if n in ENGAGE_PARTS and h not in mapping.values()]
    return mapping, parts, [h for h in headers if h not in mapping.values() and h not in parts]


def flatten(d, prefix=""):
    out = {}
    for k, v in d.items():
        key = "%s.%s" % (prefix, k) if prefix else str(k)
        if isinstance(v, dict):
            out.update(flatten(v, key))
        elif not isinstance(v, list):
            out[key] = v
    return out


def read_table(path, plain=False):
    text = open(path, encoding="utf-8-sig", errors="replace").read()
    if not plain and text.lstrip()[:1] in ("[", "{"):
        data = json.loads(text)
        if isinstance(data, dict):
            data = next((data[k] for k in ("data", "rows", "results", "items", "posts") if isinstance(data.get(k), list)), [data])
        rows = [flatten(x) for x in data if isinstance(x, dict)]
        return list(dict.fromkeys(k for r in rows for k in r)), rows
    lines = text.splitlines()
    delim = max("\t,;", key=lambda d: sum(ln.count(d) for ln in lines[:6]))
    start = 0 if plain else next((i for i, ln in enumerate(lines[:12]) if len(map_headers(next(csv.reader([ln], delimiter=delim), []))[0]) >= 2), 0)
    reader = csv.DictReader(lines[start:], delimiter=delim)
    return reader.fieldnames or [], [r for r in reader if any(isinstance(v, str) and v.strip() for v in r.values())]


def read_perf():
    out = []
    if os.path.exists(P["perf"]):
        for r in csv.DictReader(open(P["perf"], newline="", encoding="utf-8")):
            row = {k: r.get(k) or "" for k in FIELDS}
            row["date"] = parse_date(row["date"])
            if row["date"]:
                out.append({**row, **{k: num(row[k]) for k in NUMS}})
    return out


def write_perf(rows):
    rows.sort(key=lambda r: tuple(str(r[k]) for k in FIELDS[:5]))
    with open(P["perf"] + ".tmp", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k].isoformat() if k == "date" else ("" if r[k] is None else fmtnum(r[k])) if k in NUMS else r[k] for k in FIELDS})
    os.replace(P["perf"] + ".tmp", P["perf"])


def cmd_ingest(a):
    opts, args = opts_of(a)
    platform = norm_platform(topt(opts, "platform"))
    if not args or not os.path.isfile(args[0]) or not platform:
        die("usage: distro.py ingest <csv, tsv, or json> --platform <meta|google|x|linkedin|tiktok|reddit|x-organic|...> "
            "[--source \"connector 2026-10-01\"] [--date YYYY-MM-DD for a one-day file] [--dayfirst]")
    headers, table = read_table(args[0])
    mapping, parts, unmapped = map_headers(headers)
    fixed = parse_date(topt(opts, "date")) if topt(opts, "date") else None
    if "date" not in mapping and not fixed:
        die("no date column. Export by day, or pass --date YYYY-MM-DD for a one-day file", columns=headers[:30])
    if not ({"spend", "impressions", "engagements"} & set(mapping)) and not parts:
        die("found no spend, impressions, or engagement columns", columns=headers[:30])
    micro = "micro" in norm_header(mapping.get("spend", ""))
    id_col = next((h for h in headers if norm_header(h) in ("id", "tweet id", "post id")), None) \
        if norm_header(mapping.get("ad", "")) in TEXT_AD else None
    get = lambda raw, f: raw.get(mapping[f]) if f in mapping else None  # noqa: E731
    existing = {tuple(r[k] for k in FIELDS[:5]): r for r in read_perf()}
    added = replaced = skipped = 0
    dates, spend, currencies, camps, stamp = [], 0.0, set(), set(), now()
    for raw in table:
        camp = str(get(raw, "campaign") or "").strip()
        d = parse_date(get(raw, "date"), bool(opts.get("dayfirst"))) if "date" in mapping else fixed
        if not d or str(next(iter(raw.values()), "") or "").strip().lower().startswith("total") or camp.lower().startswith("total"):
            skipped += 1
            continue
        ad = " ".join(str(get(raw, "ad") or "").split())
        if id_col and raw.get(id_col):
            ad = "%s %s" % (raw[id_col], ad[:50])
        row = {"date": d, "platform": platform, "campaign": camp or ("(all)" if "spend" in mapping else "organic"),
               "adset": str(get(raw, "adset") or "").strip(), "ad": ad.strip()[:120], **{k: num(get(raw, k)) for k in NUMS},
               "currency": str(get(raw, "currency") or "").strip().upper(), "source": topt(opts, "source") or "file " + os.path.basename(args[0]),
               "read_at": stamp}
        if micro and row["spend"] is not None:
            row["spend"] /= 1e6
        vals = [num(raw.get(h)) for h in parts]
        if row["engagements"] is None and any(v is not None for v in vals):
            row["engagements"] = sum(v for v in vals if v is not None)
        key = tuple(row[k] for k in FIELDS[:5])
        replaced, added = replaced + (key in existing), added + (key not in existing)
        existing[key] = row
        dates.append(d)
        spend += row["spend"] or 0
        camps.add(row["campaign"])
        currencies |= {row["currency"]} - {""}
    if not dates:
        die("no rows with a readable date", columns=headers[:30], skipped=skipped)
    write_perf(list(existing.values()))
    warnings = [w for c, w in (("spend" not in mapping, "no spend column, so cost metrics are blank for these rows"),
                               ("conversions" not in mapping and "spend" in mapping, "no results column, so cost per result is blank"),
                               (len(currencies) > 1, "several currencies: " + ", ".join(sorted(currencies)))) if c]
    emit(ok=True, platform=platform, added=added, replaced=replaced, skipped=skipped, start=min(dates), end=max(dates),
         campaigns=len(camps), spend=r2(spend), currency=sorted(currencies), mapped=mapping, engagement_parts=parts,
         unmapped=unmapped[:20], warnings=warnings)


# ---------- analysis ----------

def sums(rows):
    return {k: sum(r[k] for r in rows if r[k] is not None) for k in NUMS}


def kpis(s):
    sp, im, cl, cv, rv, en = (s[k] for k in ("spend", "impressions", "clicks", "conversions", "revenue", "engagements"))
    return {"spend": r2(sp), "impressions": int(im), "clicks": int(cl), "conversions": r2(cv), "ctr": pct(cl, im), "cpc": div(sp, cl),
            "cpm": div(sp * 1000, im), "cvr": pct(cv, cl), "cpa": div(sp, cv), "revenue": r2(rv) or None,
            "roas": div(rv, sp) if rv else None, "er": pct(en, im) if en else None}


def delta(cur, prev):
    return {k: round(100.0 * (cur[k] - prev[k]) / prev[k], 1) for k in ("spend", "conversions", "ctr", "cpc", "cpm", "cvr", "cpa", "roas", "er")
            if cur.get(k) is not None and prev.get(k)}


def group(rows, keys):
    g = {}
    for r in rows:
        g.setdefault(tuple(r[k] for k in keys), []).append(r)
    return g


def paid(rows):
    return [r for r in rows if (r["spend"] or 0) > 0]


def daily(rows):
    return {d: sums(v) for (d,), v in group(rows, ["date"]).items()}


def prob_best(arms, draws=4000):
    """Chance each arm (successes, trials) has the highest true rate, from Beta(1,1) posteriors."""
    rnd, wins = random.Random(7), [0] * len(arms)
    for _ in range(draws):
        vals = [rnd.betavariate(x + 1, max(n - x, 0) + 1) for x, n in arms]
        wins[vals.index(max(vals))] += 1
    return [round(w / draws, 3) for w in wins]


def spend_numbers(s, rows, end=None, frame=None):
    """Month pacing. end is the last day with data, frame picks the month: today for a live change, end for a report."""
    end = end or (max(r["date"] for r in rows) if rows else today())
    frame, pr = frame or end, paid(rows)
    start, through = frame.replace(day=1), min(end, frame)
    days_in = calendar.monthrange(frame.year, frame.month)[1]
    remaining = days_in - through.day if through >= start else days_in
    mtd = sum(r["spend"] for r in pr if start <= r["date"] <= through)
    recent = [r for r in pr if end - dt.timedelta(days=6) <= r["date"] <= end]
    days = len({r["date"] for r in recent})
    rate = sum(r["spend"] for r in recent) / days if days else 0.0
    room = (s["monthly_cap"] - mtd) / remaining - rate if s["monthly_cap"] and remaining > 0 else None
    return {"month": frame.strftime("%Y-%m"), "as_of": end.isoformat(), "currency": s["currency"], "month_to_date": r2(mtd),
            "run_rate_per_day": r2(rate), "projected_month": r2(mtd + rate * remaining), "monthly_cap": s["monthly_cap"],
            "daily_cap": s["daily_cap"], "remaining_days": remaining, "room_per_day": r2(room)}


def anomalies(rows, end):
    flags, day = [], lambda i: end - dt.timedelta(days=i)
    for (plat, camp), rs in group(paid(rows), ["platform", "campaign"]).items():
        ser, where = daily(rs), "%s / %s" % (plat, camp)
        base = [ser[day(i)] for i in range(1, 15) if day(i) in ser]
        last = ser.get(end)
        if len(base) >= 7 and last:
            sp = [b["spend"] for b in base]
            mean, sd = statistics.mean(sp), statistics.pstdev(sp)
            if last["spend"] > max(2 * mean, mean + 3 * sd) and last["spend"] - mean >= 5:
                flags.append({"type": "spend_spike", "where": where, "detail": "spent %.2f on %s against a 14-day average of %.2f" % (last["spend"], end, mean)})
        bconv, bspend = sum(b["conversions"] for b in base), sum(b["spend"] for b in base)
        recent = [ser[day(i)] for i in range(3) if day(i) in ser]
        rconv, rspend = sum(x["conversions"] for x in recent), sum(x["spend"] for x in recent)
        if bconv >= 10 and recent and rspend >= 0.5 * len(recent) * bspend / len(base):
            rcpa = rspend / rconv if rconv else float("inf")
            if rcpa >= 1.5 * bspend / bconv:
                flags.append({"type": "cpa_jump", "where": where, "detail": "cost per result %s over the last %d days against %.2f before" %
                              ("with no results" if not rconv else "%.2f" % rcpa, len(recent), bspend / bconv)})
        if bconv >= 7 and all(x and x["spend"] > 0 and not x["conversions"] for x in (ser.get(end), ser.get(day(1)))):
            flags.append({"type": "conversions_stopped", "where": where,
                          "detail": "spend kept going with no results for 2 days. Check tracking, the landing page, and checkout"})
    return flags


def fatigue(rows, end):
    out = []
    for key, rs in group([r for r in rows if r["ad"] and r["date"] <= end], ["platform", "campaign", "adset", "ad"]).items():
        ser = daily(rs)
        days = sorted(ser)
        if len(days) < 10:
            continue
        first, last = sums([{**ser[d], "date": d} for d in days[:7]]), sums([{**ser[d], "date": d} for d in days[-3:]])
        if min(first["impressions"], last["impressions"]) < MIN_IMPR:
            continue
        c1, c2 = first["clicks"] / first["impressions"], last["clicks"] / last["impressions"]
        if c1 and c2 <= 0.7 * c1:
            out.append({"where": "%s / %s / %s" % (key[0], key[1], key[3]), "ctr_first_week": round(100 * c1, 2), "ctr_last_3_days": round(100 * c2, 2),
                        "drop_pct": round(100 * (1 - c2 / c1), 1), "frequency_last_3_days": div(last["impressions"], last["reach"])})
    return out


def ad_tests(rows):
    tests, early = [], 0
    for (plat, camp, adset), rs in group([r for r in paid(rows) if r["ad"]], ["platform", "campaign", "adset"]).items():
        ads = [(ad, sums(v)) for (ad,), v in group(rs, ["ad"]).items()]
        if len(ads) < 2:
            continue
        if sum(s["conversions"] for _, s in ads) >= 20:
            metric, arms = "results per impression", [(s["conversions"], s["impressions"]) for _, s in ads]
        elif all(s["impressions"] >= MIN_IMPR for _, s in ads):
            metric, arms = "ctr (clicks, not results)", [(s["clicks"], s["impressions"]) for _, s in ads]
        else:
            early += 1
            continue
        items = sorted(({"ad": ad, "rate_pct": pct(x, n), "impressions": int(n), "p_best": p}
                        for (ad, _), (x, n), p in zip(ads, arms, prob_best([(int(x), int(n)) for x, n in arms]))), key=lambda i: -i["p_best"])
        tests.append({"where": "%s / %s / %s" % (plat, camp, adset or "-"), "metric": metric, "ads": items,
                      "winner": items[0]["ad"] if items[0]["p_best"] >= 0.95 else None,
                      "losers": [i["ad"] for i in items if i["p_best"] <= 0.05 and i["impressions"] >= MIN_IMPR]})
    return tests, early


def build_report(s, rows, days, end, by):
    start = end - dt.timedelta(days=days - 1)
    pstart, pend = start - dt.timedelta(days=days), start - dt.timedelta(days=1)
    cur, prev = [r for r in rows if start <= r["date"] <= end], [r for r in rows if pstart <= r["date"] <= pend]
    pc, org = paid(cur), [r for r in cur if not (r["spend"] or 0) > 0]
    tot = kpis(sums(pc))
    keys = {"platform": ["platform"], "campaign": ["platform", "campaign"], "adset": ["platform", "campaign", "adset"],
            "ad": ["platform", "campaign", "adset", "ad"]}[by]
    pg = group(prev, keys)
    lines = sorted(({**dict(zip(keys, k)), **kpis(sums(v)), "change_pct": delta(kpis(sums(v)), kpis(sums(pg.get(k, []))))}
                    for k, v in group(cur, keys).items()), key=lambda g: -(g["spend"] or 0))
    total_sp, total_cv, channels = tot["spend"] or 0, tot["conversions"] or 0, []
    for (plat,), v in group(pc, ["platform"]).items():
        kp = kpis(sums(v))
        ss, cs = kp["spend"] / total_sp if total_sp else 0, (kp["conversions"] or 0) / total_cv if total_cv else None
        channels.append({"platform": plat, **kp, "spend_share_pct": round(100 * ss, 1), "result_share_pct": None if cs is None else round(100 * cs, 1),
                         "efficiency": round(cs / ss, 2) if cs is not None and ss else None})
    for (plat,), v in group(org, ["platform"]).items():
        kp = kpis(sums(v))
        channels.append({"platform": plat, "organic": True, "impressions": kp["impressions"], "clicks": kp["clicks"],
                         "engagements": int(sums(v)["engagements"]), "er": kp["er"], "ctr": kp["ctr"]})
    pacing, flags = spend_numbers(s, rows, end), []
    if pacing["monthly_cap"] and pacing["projected_month"] > pacing["monthly_cap"]:
        over = pacing["projected_month"] - pacing["monthly_cap"]
        flags.append({"type": "over_cap", "where": "all paid", "detail": "on pace to pass the monthly cap by %.2f, lower daily spend by "
                      "%.2f in total to land on it" % (over, over / max(pacing["remaining_days"], 1))})
    for d, v in sorted(daily(pc).items()):
        if pacing["daily_cap"] and v["spend"] > pacing["daily_cap"] * 1.1:
            flags.append({"type": "daily_cap", "where": d.isoformat(), "detail": "spent %.2f against a daily cap of %.2f" % (v["spend"], pacing["daily_cap"])})
    flags += anomalies(rows, end) + [{"type": "stale", "where": p, "detail": "latest numbers are from %s" % d}
                                     for p, d in latest(rows).items() if (today() - d).days > 2]
    tests, early = ad_tests(pc)
    fat = fatigue(rows, end)
    sugg = [{"kind": "creative", "what": "pause %s in %s" % (x, t["where"]), "why": "under 5%% chance of being the best ad on %s" % t["metric"]}
            for t in tests for x in t["losers"]]
    sugg += [{"kind": "creative", "what": "refresh the creative in " + f["where"], "why": "CTR down %s%% since its first week" % f["drop_pct"]} for f in fat]
    camps = sorted((dict(zip(["platform", "campaign"], k), **kpis(sums(v))) for k, v in group(pc, ["platform", "campaign"]).items()), key=lambda g: g["cpa"] or 1e18)
    camps = [g for g in camps if (g["conversions"] or 0) >= 5 and g["spend"] >= 0.05 * total_sp]
    if len(camps) >= 2 and camps[-1]["cpa"] >= 1.5 * camps[0]["cpa"]:
        move = min(0.2 * camps[-1]["spend"], s["max_step_pct"] / 100.0 * camps[0]["spend"]) / days
        sugg.append({"kind": "budget", "what": "move %.2f a day from %s to %s, total unchanged" % (move, camps[-1]["campaign"], camps[0]["campaign"]),
                     "why": "cost per result %.2f against %.2f" % (camps[-1]["cpa"], camps[0]["cpa"]), "needs": "the user's yes"})
    if pacing["room_per_day"] and pacing["projected_month"] < 0.85 * pacing["monthly_cap"]:
        sugg.append({"kind": "budget", "what": "room for %.2f a day more inside the cap" % pacing["room_per_day"], "needs": "the user's yes",
                     "why": "projected %.2f of %.2f" % (pacing["projected_month"], pacing["monthly_cap"])})
    caveats = [c for ok, c in (
        (sum(1 for c in channels if c.get("conversions")) > 1, "Results are platform-reported, so totals can count one customer twice across platforms."),
        (pc and total_cv < 30, "Fewer than 30 results in the window, so cost per result moves a lot by chance."),
        (len({r["currency"] for r in cur} - {""}) > 1, "Spend mixes currencies and totals are not converted."),
        (early, "%d ad set(s) are too early to call: each ad needs %d impressions, or 20 results across the ad set." % (early, MIN_IMPR))) if ok]
    return {"window": {"start": start.isoformat(), "end": end.isoformat(), "days": days, "compare_start": pstart.isoformat(),
                       "compare_end": pend.isoformat()}, "currency": s["currency"], "by": by,
            "paid": {**tot, "change_pct": delta(tot, kpis(sums(paid(prev))))},
            "organic": {"impressions": int(sums(org)["impressions"]), "engagements": int(sums(org)["engagements"]), "er": kpis(sums(org))["er"]},
            "channels": channels, "rows": lines[:15], "rows_total": len(lines), "pacing": pacing, "flags": flags, "tests": tests,
            "fatigue": fat, "suggestions": sugg, "caveats": caveats}


def render_html(rep):
    e = html.escape

    def cell(v):
        return "" if v is None else e(fmtnum(v) if isinstance(v, float) else str(v))

    def table(head, rows):
        return "<table><tr>%s</tr>%s</table>" % ("".join("<th>%s</th>" % h for h in head),
                                                 "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows))
    pa, pc, w = rep["paid"], rep["pacing"], rep["window"]
    paid_ch = [c for c in rep["channels"] if not c.get("organic")]
    top = max([c["spend"] for c in paid_ch] or [1]) or 1
    bars = "".join('<div class=bar><span>%s</span><i style="width:%dpx"></i>%s</div>' % (e(c["platform"]), int(300 * c["spend"] / top), cell(c["spend"])) for c in paid_ch)
    keys = ("spend", "conversions", "cpa", "ctr", "cpc", "cpm", "er")
    tests = ["%s, %s: %s" % (t["where"], t["metric"], ", ".join("%s %s%% chance best" % (a["ad"], round(100 * a["p_best"])) for a in t["ads"])) for t in rep["tests"]]
    lists = "".join("<h2>%s</h2><ul>%s</ul>" % (t, "".join("<li>%s</li>" % e(i) for i in items)) for t, items in (
        ("Flags", ["%s: %s" % (f["where"], f["detail"]) for f in rep["flags"]]), ("Ad tests", tests),
        ("Suggested changes", ["%s (%s)" % (x["what"], x["why"]) for x in rep["suggestions"]]), ("Caveats", rep["caveats"])) if items)
    room = ", room for %s more a day" % cell(pc["room_per_day"]) if pc["room_per_day"] is not None else ""
    return ("<!doctype html><meta charset=utf-8><title>Distribution report</title><style>body{font:14px/1.45 system-ui,sans-serif;margin:32px;"
            "max-width:980px;color:#1d1d1f}.k{display:inline-block;border:1px solid #ddd;border-radius:8px;padding:8px 14px;margin:0 8px 8px 0}"
            ".k b{display:block;font-size:20px}table{border-collapse:collapse;width:100%%}td,th{border-bottom:1px solid #eee;padding:6px;"
            "text-align:left}.bar span{display:inline-block;width:110px}.bar i{display:inline-block;height:12px;background:#e0a800;margin-right:8px}"
            "</style><h1>Distribution report, %s to %s</h1>%s<p>Month to date %s of a %s cap, projected %s%s.</p><h2>Spend by channel</h2>%s"
            "<h2>Channels</h2>%s<h2>By %s</h2>%s%s") % (
        e(w["start"]), e(w["end"]), "".join("<div class=k><b>%s</b>%s</div>" % (cell(pa.get(k)), lbl) for k, lbl in (
            ("spend", "spend " + e(rep["currency"])), ("conversions", "results"), ("cpa", "cost per result"), ("ctr", "CTR %"), ("roas", "ROAS"))
            if pa.get(k) is not None), cell(pc["month_to_date"]), cell(pc["monthly_cap"]), cell(pc["projected_month"]), room, bars,
        table(["Channel", "Spend", "Results", "Cost per result", "CTR %", "CPC", "CPM", "ER %"], [[e(c["platform"])] + [cell(c.get(k)) for k in keys] for c in rep["channels"]]),
        e(rep["by"]), table(["Name", "Spend", "Results", "Cost per result", "CTR %", "Change in cost per result %"],
                            [[e(" / ".join(str(g[k]) for k in ("platform", "campaign", "adset", "ad") if k in g))] + [cell(g.get(k)) for k in keys[:4]]
                             + [cell(g["change_pct"].get("cpa"))] for g in rep["rows"]]), lists)


def cmd_report(a):
    opts, _ = opts_of(a)
    s, rows = load(), read_perf()
    plat = norm_platform(topt(opts, "platform"))
    rows = [r for r in rows if not plat or r["platform"] == plat]
    if not rows:
        die("no performance data yet. Read the accounts, then distro.py ingest <file> --platform <name>")
    by = topt(opts, "by") or "campaign"
    if by not in ("platform", "campaign", "adset", "ad"):
        die("--by is platform, campaign, adset, or ad")
    end = parse_date(topt(opts, "end")) or max(r["date"] for r in rows)
    rep = build_report(s, rows, int(fopt(opts, "days", 7)), end, by)
    if opts.get("html"):
        path = topt(opts, "html") or os.path.join(HOME, "reports", "%s-report.html" % end)
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        open(path, "w", encoding="utf-8").write(render_html(rep))
        rep["html"] = path
    emit(**rep)


def cmd_winners(a):
    opts, _ = opts_of(a)
    rows = read_perf()
    if not rows:
        die("no performance data yet")
    days, top, min_impr = int(fopt(opts, "days", 90)), int(fopt(opts, "top", 5)), int(fopt(opts, "min-impr", MIN_IMPR))
    keys = {"ad": ["platform", "campaign", "ad"], "adset": ["platform", "campaign", "adset"], "campaign": ["platform", "campaign"]}.get(topt(opts, "by") or "ad")
    if not keys:
        die("--by is ad, adset, or campaign")
    end = max(r["date"] for r in rows)
    pd_, org = [], []
    for k, v in group([r for r in rows if r["date"] > end - dt.timedelta(days=days)], keys).items():
        s = sums(v)
        (pd_ if s["spend"] > 0 else org).append((s, {**dict(zip(keys, k)), **{x: y for x, y in kpis(s).items() if y is not None}}))
    if sum(s["conversions"] for s, _ in pd_) >= 10:
        metric, ranked = "cost per result", sorted([p for p in pd_ if p[0]["conversions"] >= 3], key=lambda p: p[0]["spend"] / p[0]["conversions"])
    else:
        metric, ranked = "ctr", sorted([p for p in pd_ if p[0]["impressions"] >= min_impr], key=lambda p: -p[0]["clicks"] / p[0]["impressions"])
    org = sorted([o for o in org if o[0]["impressions"] >= min(min_impr, 200) and o[0]["engagements"]], key=lambda o: -o[0]["engagements"] / o[0]["impressions"])
    emit(window_days=days, end=end, paid_metric=metric, paid_best=[i for _, i in ranked[:top]],
         paid_worst=[i for _, i in ranked[::-1][:top]] if len(ranked) > top else [], organic_best=[i for _, i in org[:top]],
         organic_worst=[i for _, i in org[::-1][:top]] if len(org) > top else [],
         note="Small samples rank by luck. Treat anything under %d impressions or 3 results as a hunch." % min_impr)


# ---------- change ledger ----------

def cmd_propose(a):
    opts, _ = opts_of(a)
    s, ch = load(), jsonl(P["changes"])
    kind, plat, camp, what, why = topt(opts, "kind"), norm_platform(topt(opts, "platform")), topt(opts, "campaign"), topt(opts, "what"), topt(opts, "why")
    if kind not in KINDS or not (plat and camp and what and why):
        die("usage: distro.py propose --kind <%s> --platform P --campaign C --what \"<the change>\" --why \"<evidence>\" [--target <ad set or ad>] "
            "[--before X] [--after Y] [--delta <change in daily spend>] [--loser]" % "|".join(KINDS))
    before, after = topt(opts, "before"), topt(opts, "after")
    b, af, d = num(before), num(after), fopt(opts, "delta")
    if d is None and kind == "budget" and b is not None and af is not None:
        d = af - b
    if d is None and kind == "launch":
        d = af
        if d is None:
            die("a launch needs --after <daily budget>")
    lane, status, reasons, env = "ask", "proposed", [], None
    if kind in SPEND_KINDS:
        reasons.append("spend change: needs the user's yes")
        if (d or 0) > 0 and not s["monthly_cap"]:
            status = "blocked"
            reasons.append("no monthly cap is set, so no spend increase is possible until the user sets one")
        elif (d or 0) > 0:
            n = spend_numbers(s, read_perf(), frame=today())
            rate = n["run_rate_per_day"] + d
            proj = n["month_to_date"] + rate * n["remaining_days"]
            env = {"month": n["month"], "run_rate_now": n["run_rate_per_day"], "run_rate_after": r2(rate), "projected_month_after": r2(proj),
                   "monthly_cap": s["monthly_cap"], "daily_cap": s["daily_cap"]}
            for bad, msg in ((s["daily_cap"] and rate > s["daily_cap"] + 1e-9, "daily spend would be %.2f, over the daily cap of %.2f" % (rate, s["daily_cap"])),
                             (proj > s["monthly_cap"] + 1e-9, "the month would land at %.2f, over the monthly cap of %.2f" % (proj, s["monthly_cap"]))):
                if bad:
                    status = "blocked"
                    reasons.append(msg)
        if kind == "budget" and b and af is not None and abs(af - b) / b * 100 > s["max_step_pct"] + 1e-9:
            status = "blocked"
            reasons.append("a %.0f%% step is over the max step of %d%%" % (abs(af - b) / b * 100, s["max_step_pct"]))
    elif not s["autopilot"]:
        reasons.append("autopilot is off: needs the user's yes")
    else:
        mine = [c for c in ch if c["platform"] == plat and c["campaign"] == camp and c["status"] == "applied" and parse_when(c.get("applied_at"))]
        week = [c for c in mine if c["lane"] == "autopilot" and now_dt() - parse_when(c["applied_at"]) < dt.timedelta(days=7)]
        last = max((parse_when(c["applied_at"]) for c in mine), default=None)
        lane = "autopilot"
        if len(week) >= 3:
            lane = "ask"
            reasons.append("3 autopilot changes already landed on this campaign this week")
        if last and now_dt() - last < dt.timedelta(hours=72) and not opts.get("loser"):
            lane = "ask"
            reasons.append("a change landed on this campaign under 3 days ago, so its numbers have not settled")
        reasons.append("autopilot: inside the guardrails, apply it and report it with its undo" if lane == "autopilot" else "needs the user's yes")
    rec = {"id": next_id(ch, "c"), "ts": now(), "kind": kind, "platform": plat, "campaign": camp, "target": topt(opts, "target"), "what": what,
           "why": why, "before": before, "after": after, "delta": d, "lane": lane, "status": status, "reasons": reasons, "envelope": env}
    write_jsonl(P["changes"], ch + [rec])
    emit(ok=True, id=rec["id"], lane=lane, status=status, reasons=reasons, envelope=env)


def update_change(cid, ok_from, **fields):
    ch = jsonl(P["changes"])
    c = next((c for c in ch if c["id"] == cid), None) or die("no change " + cid)
    bad = ok_from(c)
    if bad:
        die(bad)
    c.update(fields)
    write_jsonl(P["changes"], ch)
    return c


def cmd_approve(a):
    opts, args = opts_of(a)
    words = topt(opts, "words").strip()
    if not args or len(words) < 2:
        die("usage: distro.py approve <id> --words \"<the user's exact words>\". Only the user's own yes in this conversation counts.")
    c = update_change(args[0], lambda c: "blocked: %s. Change the proposal or the caps first." % "; ".join(c["reasons"][1:] or c["reasons"])
                      if c["status"] == "blocked" else None if c["status"] == "proposed" else "%s is already %s" % (c["id"], c["status"]),
                      status="approved", approved_at=now(), words=words[:300])
    emit(ok=True, id=c["id"], status="approved", next="apply it, read it back, then distro.py applied %s --note \"<what you verified>\"" % c["id"])


def cmd_applied(a):
    opts, args = opts_of(a)
    if not args:
        die("usage: distro.py applied <id> --note \"<what you verified>\"")
    auto = load()["autopilot"]
    c = update_change(args[0], lambda c: None if c["status"] == "approved" or (c["status"] == "proposed" and c["lane"] == "autopilot" and auto
                                                                                and c["kind"] not in SPEND_KINDS) else
                      "%s needs the user's yes first: show it, then distro.py approve %s --words \"<their words>\"" % (c["id"], c["id"]),
                      status="applied", applied_at=now(), note=topt(opts, "note")[:300])
    emit(ok=True, id=c["id"], status="applied", undo="if the user says undo %s, revert it, then distro.py revert %s" % (c["id"], c["id"]))


def mark_change(a, status, allowed):
    opts, args = opts_of(a)
    if not args:
        die("usage: distro.py %s <id> [--note text]" % ("revert" if status == "reverted" else "reject"))
    c = update_change(args[0], lambda c: None if c["status"] in allowed else "%s is %s, so it cannot be marked %s" % (c["id"], c["status"], status),
                      status=status, closed_at=now(), close_note=topt(opts, "note")[:300])
    emit(ok=True, id=c["id"], status=status)


def cmd_changes(a):
    opts, _ = opts_of(a)
    since = now_dt() - dt.timedelta(days=fopt(opts, "days", 3650))
    out = [{k: c.get(k) for k in ("id", "ts", "kind", "platform", "campaign", "target", "what", "lane", "status", "words", "applied_at", "note")}
           for c in jsonl(P["changes"]) if (not opts.get("open") or c["status"] in ("proposed", "approved"))
           and (parse_when(c["ts"]) or now_dt()) >= since and (not topt(opts, "campaign") or c["campaign"] == topt(opts, "campaign"))]
    emit(changes=out[-50:], count=len(out))


# ---------- playbook ----------

def read_playbook():
    kinds, cur = {}, None
    if os.path.exists(P["playbook"]):
        for line in open(P["playbook"], encoding="utf-8"):
            line = line.rstrip("\n")
            if line.startswith("## "):
                cur = kinds.setdefault(line[3:].strip(), [])
            elif line.startswith("- ") and cur is not None:
                parts = (line[2:].split(" | ") + [""] * 4)[:4]
                cur.append(dict(zip(("date", "note", "evidence", "source"), (p.strip() for p in parts))))
    return kinds


def cmd_learn(a):
    opts, _ = opts_of(a)
    clean = lambda k, n: " ".join(topt(opts, k).replace("|", "/").split())[:n]  # noqa: E731
    kind, note = topt(opts, "kind"), clean("note", 240)
    if kind not in LEARN_KINDS or not note:
        die("usage: distro.py learn --kind <%s> --note \"<the pattern>\" [--evidence \"<numbers, source, date>\"] [--source <ad, post, or email>]" % "|".join(LEARN_KINDS))
    kinds = read_playbook()
    entries = kinds.setdefault(kind, [])
    same = [e for e in entries if e["note"].lower() == note.lower()]
    entries[:] = ([{"date": today().isoformat(), "note": note, "evidence": clean("evidence", 200), "source": clean("source", 120)}]
                  + [e for e in entries if e not in same])[:25]
    lines = ["# Playbook", "", "What worked and what flopped, newest first. distro.py learn adds lines.", ""]
    for k in list(LEARN_KINDS) + [k for k in kinds if k not in LEARN_KINDS]:
        if kinds.get(k):
            lines += ["## " + k] + ["- " + " | ".join(x[f] for f in ("date", "note", "evidence", "source")).rstrip(" |") for x in kinds[k]] + [""]
    open(P["playbook"] + ".tmp", "w", encoding="utf-8").write("\n".join(lines))
    os.replace(P["playbook"] + ".tmp", P["playbook"])
    emit(ok=True, kind=kind, updated=bool(same), entries=len(entries))


def cmd_playbook(a):
    opts, _ = opts_of(a)
    kind, kinds = topt(opts, "kind"), read_playbook()
    if kind:
        kinds = {kind: kinds.get(kind, [])}
    emit(path=P["playbook"], kinds={k: v[:int(fopt(opts, "top", 6))] for k, v in kinds.items() if v},
         total=sum(len(v) for v in kinds.values()), empty=[k for k in LEARN_KINDS if not kinds.get(k)] if not kind else [])


# ---------- site snapshots ----------

TAGS = {"meta": r"connect\.facebook\.net/[^\"']*fbevents\.js|\bfbq\(\s*['\"]init",
        "google_ads": r"gtag/js\?id=AW-|['\"]AW-\d{6,}|googleadservices\.com",
        "x": r"static\.ads-twitter\.com/uwt\.js|\btwq\(\s*['\"](init|config)",
        "linkedin": r"snap\.licdn\.com/li\.lms-analytics|_linkedin_partner_id",
        "tiktok": r"analytics\.tiktok\.com/i18n/pixel|\bttq\.load\(", "reddit": r"redditstatic\.com/ads/pixel\.js|\brdt\(\s*['\"]init",
        "microsoft": r"bat\.bing\.com/bat\.js|\buetq\b", "ga4": r"gtag/js\?id=G-|['\"]G-[A-Z0-9]{6,}['\"]",
        "gtm": r"googletagmanager\.com/gtm\.js|['\"]GTM-[A-Z0-9]{4,}['\"]", "posthog": r"posthog", "segment": r"cdn\.segment\.com",
        "hubspot": r"js\.hs-scripts\.com|js\.hsforms\.net"}
AD_TAGS = {"meta": "Meta ads", "google_ads": "Google ads", "x": "X ads", "linkedin": "LinkedIn ads", "tiktok": "TikTok ads",
           "reddit": "Reddit ads", "microsoft": "Microsoft ads"}
CTA_RE = re.compile(r"\b(start|try|get|book|sign|join|buy|demo|free|download|contact|talk|request|subscribe|install|create|watch|"
                    r"apply|claim|schedule|pricing)\b", re.I)
PRICE_RE = re.compile(r"(?:\$|USD ?|EUR ?|\u20ac|\u00a3)\s?\d[\d,]*(?:\.\d+)?(?:\s*/\s*(?:month|mo|year|yr|user|seat))?", re.I)


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self.meta, self.h1, self.h2, self.links, self.stack, self.skip, self.chars = "", {}, [], [], [], [], 0, 0

    def handle_starttag(self, tag, attrs):
        a = {k: v or "" for k, v in attrs}
        self.skip += tag in ("script", "style", "noscript", "svg")
        if tag == "meta" and (a.get("name") or a.get("property")) and a.get("content"):
            self.meta[(a.get("name") or a.get("property")).lower()] = a["content"][:300]
        if tag in ("title", "h1", "h2", "a", "button"):
            self.stack.append([tag, []])

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg"):
            self.skip = max(0, self.skip - 1)
        if self.stack and self.stack[-1][0] == tag:
            t, parts = self.stack.pop()
            text = " ".join(" ".join(parts).split())
            if text:
                (self.h1 if t == "h1" else self.h2 if t == "h2" else self.links if t != "title" else []).append(text[:160])
                self.title = self.title or (text[:160] if t == "title" else "")
                if self.stack:
                    self.stack[-1][1].append(text)

    def handle_data(self, data):
        if not self.skip:
            self.chars += len(data.strip())
            if self.stack:
                self.stack[-1][1].append(data)


def snapshot(url):
    url = url if re.match(r"https?://", url) else "https://" + url
    code, final, text = fetch_text(url)
    if code != 200 or not text:
        die("could not read %s (status %s). Open it in my browser instead." % (url, code))
    p = Page()
    try:
        p.feed(text)
    except Exception:  # noqa: BLE001 - a broken page still yields what was parsed
        pass
    tags = sorted(k for k, pat in TAGS.items() if re.search(pat, text))
    plain = html.unescape(re.sub(r"<[^>]+>", " ", text))
    return {"url": url, "final_url": final, "title": p.title, "description": p.meta.get("description", ""), "og_title": p.meta.get("og:title", ""),
            "h1": p.h1[:4], "h2": p.h2[:8], "ctas": list(dict.fromkeys(x for x in p.links if len(x) <= 40 and CTA_RE.search(x)))[:10],
            "prices": list(dict.fromkeys(" ".join(m.split()) for m in PRICE_RE.findall(plain)))[:8], "tags": tags,
            "ad_platforms": [AD_TAGS[t] for t in tags if t in AD_TAGS], "text_chars": p.chars, "thin": p.chars < 300, "read_at": now()}


def cmd_site(a):
    opts, args = opts_of(a)
    if not args:
        die("usage: distro.py site <url> [--save <name>]")
    snap, name = snapshot(args[0]), topt(opts, "save")
    if name:
        path = os.path.join(HOME, "pages", slug(name) + ".json")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        hist = json.load(open(path, encoding="utf-8"))["history"] if os.path.exists(path) else []
        diff = {}
        if hist:
            old = hist[-1]
            diff = {k: {"was": old.get(k), "now": snap[k]} for k in ("title", "description", "h1") if old.get(k) != snap[k]}
            for k in ("ctas", "prices", "tags", "h2"):
                add, gone = [x for x in snap[k] if x not in old.get(k, [])], [x for x in old.get(k, []) if x not in snap[k]]
                if add or gone:
                    diff[k] = {"added": add, "removed": gone}
        json.dump({"name": name, "history": (hist + [snap])[-10:]}, open(path, "w", encoding="utf-8"), indent=1)
        snap.update(saved=path, changes_since_last=diff if hist else "first snapshot")
    if snap["thin"]:
        snap["hint"] = "little text in the HTML, so the page likely renders in the browser. Read it in my browser too."
    emit(**snap)


# ---------- topic scans ----------

def norm_url(u):
    p = urllib.parse.urlsplit(u.strip())
    return urllib.parse.urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path.rstrip("/"), p.query, ""))


def scan_hn(q, days, limit):
    code, d = http("GET", HN_API + "/search_by_date?" + urllib.parse.urlencode(
        {"query": q, "tags": "story", "numericFilters": "created_at_i>%d" % (time.time() - days * 86400), "hitsPerPage": limit}))
    if code != 200:
        die("Hacker News search failed (status %s). Use WebSearch instead." % code)
    item = "https://news.ycombinator.com/item?id=%s"
    return [{"source": "hn", "title": h.get("title") or h.get("story_title") or "", "url": h.get("url") or item % h.get("objectID"),
             "discussion": item % h.get("objectID"), "when": h.get("created_at", ""), "points": h.get("points") or 0,
             "comments": h.get("num_comments") or 0, "where": "Hacker News"} for h in d.get("hits") or []]


def scan_news(q, days, limit):
    code, _, text = fetch_text(NEWS_RSS + "?" + urllib.parse.urlencode({"q": "%s when:%dd" % (q, days), "hl": "en-US", "gl": "US", "ceid": "US:en"}))
    try:
        items = list(ET.fromstring(text).iter("item")) if code == 200 else None
    except ET.ParseError:
        items = None
    if items is None:
        die("news search failed (status %s). Use WebSearch instead." % code)
    return [{"source": "news", "title": (i.findtext("title") or "").strip(), "url": (i.findtext("link") or "").strip(),
             "when": (i.findtext("pubDate") or "").strip(), "points": 0, "comments": 0, "where": (i.findtext("source") or "news").strip()}
            for i in items[:limit]]


def score_item(it, words):
    when = parse_when(it.get("when"))
    age = (now_dt() - when).total_seconds() / 3600 if when else 1e9
    return round(2 * sum(1 for w in words if w and w.lower() in it["title"].lower())
                 + math.log1p((it.get("points") or 0) + 2 * (it.get("comments") or 0)) + (2 if age <= 24 else 1 if age <= 48 else 0), 2)


def add_topics(items):
    topics = jsonl(P["topics"])
    seen, fresh = {norm_url(t["url"]) for t in topics if t.get("url")}, []
    for it in items:
        if it.get("url") and norm_url(it["url"]) not in seen:
            rec = {"id": next_id(topics, "t"), "status": "new", "first_seen": now(), **it}
            topics.append(rec)
            fresh.append(rec)
            seen.add(norm_url(it["url"]))
    write_jsonl(P["topics"], topics)
    return fresh


def cmd_scan(a):
    opts, args = opts_of(a)
    if len(args) < 2 or args[0] not in ("hn", "news"):
        die("usage: distro.py scan <hn|news> \"<keyword>\" [--days 2] [--limit 15]. For Reddit, use WebSearch with site:reddit.com.")
    s, q = load(), " ".join(args[1:])
    days, limit = max(1, int(fopt(opts, "days", 2))), min(50, int(fopt(opts, "limit", 15)))
    items = (scan_hn if args[0] == "hn" else scan_news)(q, days, limit)
    for it in items:
        it.update(score=score_item(it, s["keywords"] + s["competitors"] + [q]), keyword=q)
    fresh = sorted(add_topics(items), key=lambda t: -t["score"])
    s["last"]["scan_" + args[0]] = now()
    save(s)
    emit(source=args[0], query=q, found=len(items), new=len(fresh), items=fresh[:limit])


def cmd_topic(a):
    opts, args = opts_of(a)
    if args[:1] == ["add"] and topt(opts, "title") and topt(opts, "url"):
        s = load()
        it = {"source": topt(opts, "source") or "x", "title": topt(opts, "title")[:300], "url": topt(opts, "url"), "when": topt(opts, "when") or now(),
              "points": int(fopt(opts, "points", 0)), "comments": int(fopt(opts, "comments", 0)), "where": topt(opts, "where") or topt(opts, "source") or "x",
              "note": topt(opts, "note")[:300]}
        it["score"] = fopt(opts, "score", score_item(it, s["keywords"] + s["competitors"]))
        fresh = add_topics([it])
        emit(ok=True, added=bool(fresh), id=fresh[0]["id"] if fresh else None, note="" if fresh else "already in the topic ledger")
    elif args[:1] == ["mark"] and len(args) >= 3 and args[2] in ("new", "drafted", "posted", "skipped"):
        topics = jsonl(P["topics"])
        t = next((t for t in topics if t["id"] == args[1]), None) or die("no topic " + args[1])
        t.update(status=args[2], marked_at=now(), **({"note": topt(opts, "note")[:300]} if topt(opts, "note") else {}))
        write_jsonl(P["topics"], topics)
        emit(ok=True, id=t["id"], status=t["status"])
    else:
        die("usage: distro.py topic add --title \"...\" --url <link> [--source x] [--score N] [--note \"...\"] | topic mark <id> <new|drafted|posted|skipped>")


STOP = set("the and for with from this that its how why what new your you our they their about into over after more than just will can has have "
           "not but all one out are was were been".split())


def cmd_topics(a):
    opts, _ = opts_of(a)
    s, days, status = load(), fopt(opts, "days", 7), topt(opts, "status")
    since = now_dt() - dt.timedelta(days=days)
    items = sorted((t for t in jsonl(P["topics"]) if (parse_when(t.get("first_seen")) or now_dt()) >= since and (not status or t.get("status") == status)),
                   key=lambda t: -(t.get("score") or 0))
    words = {}
    for t in items:
        for w in set(re.findall(r"[a-z][a-z0-9+.-]{3,}", t["title"].lower())) - STOP:
            words[w] = words.get(w, 0) + 1
    emit(days=days, count=len(items), by_status={k: sum(t.get("status") == k for t in items) for k in ("new", "drafted", "posted", "skipped")},
         keyword_counts={k: sum(k.lower() in t["title"].lower() for t in items) for k in s["keywords"] + s["competitors"]},
         recurring_words=sorted(words.items(), key=lambda kv: -kv[1])[:12],
         items=[{k: t.get(k) for k in ("id", "status", "source", "title", "url", "where", "score", "when")} for t in items[:int(fopt(opts, "limit", 20))]])


# ---------- outbound ledger ----------

EMAIL_RE = re.compile(r"^[^@\s,;<>]+@[^@\s,;<>]+\.[a-z]{2,}$", re.I)
LEAD_SYN = {"email": "email|email address|work email|e mail", "name": "name|full name", "first": "first name|firstname",
            "last": "last name|lastname", "company": "company|company name|organization|account|account name",
            "title": "title|job title|position|role", "domain": "website|domain|company domain|url", "source": "source|list",
            "note": "note|notes|linkedin|linkedin url"}


def read_leads():
    return [{k: r.get(k) or "" for k in LEAD_FIELDS} for r in csv.DictReader(open(P["leads"], newline="", encoding="utf-8"))] if os.path.exists(P["leads"]) else []


def write_leads(leads):
    with open(P["leads"] + ".tmp", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=LEAD_FIELDS)
        w.writeheader()
        w.writerows(leads)
    os.replace(P["leads"] + ".tmp", P["leads"])


def sends_on(day):
    return sum(1 for r in csv.DictReader(open(P["sends"], newline="", encoding="utf-8")) if r["date"] == day.isoformat()) if os.path.exists(P["sends"]) else 0


def suppressed():
    return {ln.strip().lower() for ln in open(P["suppress"], encoding="utf-8") if ln.strip()} if os.path.exists(P["suppress"]) else set()


def is_suppressed(addr, sup=None):
    sup = suppressed() if sup is None else sup
    return addr.lower() in sup or "@" + addr.lower().split("@")[-1] in sup


def add_suppress(entry):
    if entry.lower() not in suppressed():
        open(P["suppress"], "a", encoding="utf-8").write(entry.lower() + "\n")


def due_leads(s, leads):
    t = today().isoformat()
    return [x for x in leads if x["stage"] == "new" or (x["stage"] in ("sent", "drafted") and 0 < int(x["step"] or 0) < s["steps"]
                                                        and x["next_touch"] and x["next_touch"] <= t)]


def new_lead(rec, sup, leads, source):
    e = (rec.get("email") or "").strip().lower()
    if not EMAIL_RE.match(e):
        return "invalid"
    if is_suppressed(e, sup):
        return "suppressed"
    if any(x["email"] == e for x in leads):
        return "duplicate"
    dom = re.sub(r"^https?://(www\.)?", "", (rec.get("domain") or "").strip().lower()).split("/")[0] or e.split("@")[1]
    leads.append({**dict.fromkeys(LEAD_FIELDS, ""), **{k: (rec.get(k) or "").strip()[:80] for k in ("name", "company", "title")}, "email": e,
                  "domain": dom, "source": (rec.get("source") or source).strip()[:60], "stage": "new", "step": "0",
                  "note": (rec.get("note") or "").strip()[:200], "added": today().isoformat()})
    return "added"


def lead_stats():
    leads = read_leads()
    contacted = [x for x in leads if int(x["step"] or 0) >= 1]

    def rate(items):
        rep = sum(1 for x in items if x["replied_at"])
        return {"contacted": len(items), "replied": rep, "reply_rate_pct": pct(rep, len(items)),
                "bounced": sum("stopped: bounce" in x["note"] for x in items), "opted_out": sum("stopped: optout" in x["note"] for x in items)}
    by_touch = {}
    for x in contacted:
        if x["replied_at"]:
            by_touch[x["step"]] = by_touch.get(x["step"], 0) + 1
    emit(by_stage={k: sum(x["stage"] == k for x in leads) for k in STAGES}, overall=rate(contacted),
         by_source={src: rate([x for x in contacted if x["source"] == src]) for src in sorted({x["source"] for x in contacted})},
         replies_by_touch=by_touch, suppressed=len(suppressed()))


def handoff_text(s, x):
    who = ", ".join(p for p in (x["name"], " at ".join(p for p in (x["title"], x["company"]) if p)) if p) or x["email"]
    return ("Lead replied to outbound. %s (%s%s). Their reply on %s: \"%s\". How we reached them: %s, touch %s of %d. Thread: %s. "
            "Notes: %s. My sequence for them is stopped. Please take it from here." %
            (who, x["email"], ", " + x["domain"] if x["domain"] else "", x["replied_at"], x["said"], x["source"] or "outbound",
             x["step"] or "1", s["steps"], x["thread"] or "in the user's inbox", x["note"] or "none"))


def cmd_lead(a):
    opts, args = opts_of(a)
    sub, s, leads = (args or [""])[0], load(), read_leads()
    if sub == "import" and len(args) > 1 and os.path.isfile(args[1]):
        headers, table = read_table(args[1], plain=True)
        cols = {k: next((h for h in headers if norm_header(h) in syn.split("|")), None) for k, syn in LEAD_SYN.items()}
        if not cols["email"]:
            die("no email column", columns=headers[:20])
        sup, tally, personal = suppressed(), dict.fromkeys(("added", "duplicate", "suppressed", "invalid"), 0), 0
        for r in table:
            rec = {k: r.get(cols[k]) or "" if cols[k] else "" for k in LEAD_SYN}
            rec["name"] = rec["name"] or " ".join(p for p in (rec["first"], rec["last"]) if p)
            res = new_lead(rec, sup, leads, topt(opts, "source") or os.path.basename(args[1]))
            tally[res] += 1
            personal += res == "added" and rec["email"].strip().lower().split("@")[-1] in FREE_MAIL
        write_leads(leads)
        return emit(ok=True, **tally, personal_addresses=personal, total=len(leads))
    if sub == "add":
        res = new_lead({k: topt(opts, k) for k in LEAD_SYN}, suppressed(), leads, topt(opts, "source") or "manual")
        if res != "added":
            die("not added: " + res)
        write_leads(leads)
        return emit(ok=True, email=leads[-1]["email"], total=len(leads))
    if sub == "stats":
        return lead_stats()
    if sub == "due":
        due, sent = due_leads(s, leads), sends_on(today())
        return emit(due=[{k: x[k] for k in ("email", "name", "company", "title", "stage", "step", "last_touch", "thread")} for x in due[:int(fopt(opts, "limit", 25))]],
                    count=len(due), sent_today=sent, cap_left=max(0, s["send_cap"] - sent))
    if sub not in ("drafted", "sent", "reply", "handed", "stop") or len(args) < 2:
        die("usage: distro.py lead import <csv> [--source s] | add --email E [--name --company --title --source --note] | due | stats | "
            "drafted <email> [--thread T] | sent <email> [--thread T] | reply <email> --said \"<their words>\" | handed <email> --to sales|user | "
            "stop <email> --why <%s>" % "|".join(STOP_WHY))
    x = next((x for x in leads if x["email"] == args[1].strip().lower()), None) or die("no lead " + args[1])
    done = x["stage"] in ("replied", "handed_off", "closed")
    if sub == "drafted":
        if done:
            die("%s is %s, so no more drafts" % (x["email"], x["stage"]))
        x.update(stage="drafted", thread=topt(opts, "thread") or x["thread"])
    elif sub == "sent":
        if done or is_suppressed(x["email"]):
            die("%s is %s, so never send to it again" % (x["email"], "on the do-not-contact list" if not done else x["stage"]))
        if sends_on(today()) >= s["send_cap"]:
            die("daily send cap of %d reached, the rest wait for tomorrow" % s["send_cap"])
        step = int(x["step"] or 0) + 1
        x.update(stage="sent", step=str(step), last_touch=today().isoformat(), thread=topt(opts, "thread") or x["thread"],
                 next_touch=(today() + dt.timedelta(days=GAPS[min(step, len(GAPS)) - 1])).isoformat() if step < s["steps"] else "")
        new = not os.path.exists(P["sends"])
        with open(P["sends"], "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new:
                w.writerow(["date", "email", "step"])
            w.writerow([today().isoformat(), x["email"], step])
    elif sub == "reply":
        said = " ".join(topt(opts, "said").split())[:400]
        if not said:
            die("usage: distro.py lead reply <email> --said \"<their words>\"")
        x.update(stage="replied", said=said, replied_at=topt(opts, "date") or today().isoformat(), next_touch="")
        write_leads(leads)
        return emit(ok=True, email=x["email"], stage="replied", handoff=handoff_text(s, x), to=s["teammates"].get("sales") or "the user",
                    next="sales teammate: SendToAgent with this text, priority true, then distro.py lead handed %s --to sales. No sales teammate: "
                         "show it to the user with a suggested reply, then --to user." % x["email"])
    elif sub == "handed":
        if topt(opts, "to") not in ("sales", "user"):
            die("--to is sales or user")
        x.update(stage="handed_off", handed_to=topt(opts, "to"))
    else:
        why = topt(opts, "why")
        if why not in STOP_WHY:
            die("--why is " + ", ".join(STOP_WHY))
        x.update(stage="closed", next_touch="", note=("%s stopped: %s" % (x["note"], why)).strip()[:200],
                 replied_at=x["replied_at"] or (today().isoformat() if why == "no" else ""))
        if why in ("optout", "bounce", "customer"):
            add_suppress(x["email"])
    write_leads(leads)
    emit(ok=True, email=x["email"], stage=x["stage"], step=x["step"], next_touch=x["next_touch"])


def cmd_leads(a):
    opts, _ = opts_of(a)
    leads = [x for x in read_leads() if not topt(opts, "stage") or x["stage"] == topt(opts, "stage")]
    emit(count=len(leads), leads=[{k: x[k] for k in ("email", "name", "company", "stage", "step", "next_touch", "source")} for x in leads[:int(fopt(opts, "limit", 30))]])


def cmd_suppress(a):
    if not a or not (EMAIL_RE.match(a[0]) or re.fullmatch(r"@[^@\s]+\.[a-z]{2,}", a[0], re.I)):
        die("usage: distro.py suppress <email or @domain>")
    add_suppress(a[0])
    emit(ok=True, suppressed=a[0].lower(), total=len(suppressed()))


# ---------- creative on the user's own key ----------

HINTS = {"FAL_KEY": "Ad images and video run on your FAL account: fal.ai/dashboard/keys, add credits, create a key.",
         "HF_KEY": "Ad images and video run on your Higgsfield API account: console.higgsfield.ai, add funds, create an API key, and paste it as KEY_ID:KEY_SECRET.",
         "XAI_API_KEY": "Ad images and video run on Grok Imagine with your xAI key: console.x.ai, add credits, create an API key."}
ERRORS = {401: "the provider rejected the key, make a new one", 402: "the balance is empty, add funds", 403: "the key lacks access or credits",
          404: "no such model or request", 422: "the provider rejected the input, check the model's docs", 423: "that model is locked for this account",
          429: "rate or spend limit, retry shortly", 503: "that model is unavailable right now"}


def auth(name):
    key = secret(name)
    if not key:
        die("no %s saved. Ask the user with a secret-request named %s and this line: %s" % (name, name, HINTS[name]))
    if name == "HF_KEY" and ":" not in key:
        die("HF_KEY needs both parts, KEY_ID:KEY_SECRET. Ask again with a secret-request named HF_KEY")
    return {"Authorization": ("Bearer " if name == "XAI_API_KEY" else "Key ") + key}


def ok(code, data, what):
    if code not in (200, 201, 202):
        die("%s: %s" % (what, ERRORS.get(code, "failed")), status=code, detail=scrub(json.dumps(data))[:300])
    return data


def check_input(payload, path=""):
    if isinstance(payload, dict):
        for k, v in payload.items():
            if FORBIDDEN_INPUT.search(k):
                die("never pass %s: models run on the user's own account with this provider, never through another provider's key" % (path + k))
            check_input(v, path + k + ".")
    elif isinstance(payload, list):
        for v in payload:
            check_input(v, path)


def json_input(opts):
    src = opts.get("input")
    try:
        payload = json.loads((open(src, encoding="utf-8").read() if isinstance(src, str) and os.path.isfile(src) else src if isinstance(src, str) else "") or "{}")
    except ValueError:
        die("--input must be JSON or a file holding JSON")
    check_input(payload)
    return payload


def swap_paths(v, uploader, seen=None):
    seen = {} if seen is None else seen
    if isinstance(v, dict):
        return {k: swap_paths(x, uploader, seen) for k, x in v.items()}
    if isinstance(v, list):
        return [swap_paths(x, uploader, seen) for x in v]
    p = v[7:] if isinstance(v, str) and v.startswith("file://") else v
    if isinstance(p, str) and p.startswith("/") and os.path.isfile(p):
        seen[p] = seen.get(p) or uploader(p)
        return seen[p]
    return v


def media_urls(obj, found=None):
    found = [] if found is None else found
    if isinstance(obj, dict):
        if isinstance(obj.get("url"), str) and obj["url"].startswith(("http", "data:")):
            found.append((obj["url"], obj.get("content_type") or obj.get("file_name") or ""))
        for k, v in obj.items():
            if k != "url":
                media_urls(v, found)
    elif isinstance(obj, list):
        for v in obj:
            media_urls(v, found)
    return found


def ext_for(url, hint):
    if url.startswith("data:"):
        return mimetypes.guess_extension(url[5:].split(";")[0]) or ".bin"
    ext = os.path.splitext(urllib.parse.urlparse(url).path)[1]
    return ext if ext and len(ext) <= 5 else (mimetypes.guess_extension(hint) or ".bin") if "/" in hint else (os.path.splitext(hint)[1] or ".bin")


def media_dir(opts, name):
    out = topt(opts, "out") or os.path.join(HOME, "media", "%s-%s" % (today(), slug(name)))
    os.makedirs(out, exist_ok=True)
    return out


def save_files(urls, out, name):
    files = []
    for n, (url, hint) in enumerate(urls[:20], 1):
        dest = os.path.join(out, "%s-%02d%s" % (name, n, ext_for(url, hint)))
        try:
            download(url, dest)
            files.append(dest)
        except (OSError, urllib.error.URLError, ValueError):
            continue
    return files


def finish(s, rid, job, data, started, **extra):
    files = save_files(media_urls(data), job["out"], job["name"])
    if not files:
        job["status"] = "FAILED"
        save(s)
        die("the job finished without a file", detail=scrub(json.dumps(data))[:300], request_id=rid)
    json.dump(data, open(os.path.join(job["out"], job["name"] + "-result.json"), "w", encoding="utf-8"), indent=1)
    job.update(status="COMPLETED", files=files, done=now())
    save(s)
    emit(ok=True, request_id=rid, model=job["endpoint"], files=files, waited=round(time.time() - started), **extra)


def poll(s, rid, job, opts, url, headers, done, failed, every):
    """Wait for a queued job. Returns its final status body, or prints a resume command and stops when time runs out."""
    end, started = time.time() + float(opts.get("minutes", 10)) * 60, time.time()
    while True:
        code, d = http("GET", url, headers=headers)
        state = str(ok(code, d, "status").get("status", ""))
        if state in done:
            return d, started
        if state in failed:
            job["status"] = "FAILED"
            save(s)
            die("the job ended %s%s" % (state, ", held back by moderation and not charged" if state == "nsfw" else ""),
                detail=scrub(json.dumps(d.get("error") or {}))[:300], request_id=rid)
        if time.time() >= end:
            save(s)
            emit(ok=True, pending=True, request_id=rid, resume=resume_cmd(rid, job))
            sys.exit(0)
        time.sleep(float(opts.get("every", every)))


def fal_upload(path):
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    code, d = http("POST", FAL_REST + "/storage/upload/initiate?storage_type=fal-cdn-v3", {"file_name": os.path.basename(path), "content_type": mime}, headers=auth("FAL_KEY"))
    d = ok(code, d, "upload")
    if http("PUT", d["upload_url"], raw=open(path, "rb").read(), headers={"Content-Type": mime}, timeout=300)[0] not in (200, 201, 204):
        die("upload failed")
    return d["file_url"]


def cmd_fal(a):
    if not a or a[0] not in ("price", "run", "result"):
        die("usage: distro.py fal price <endpoint> [...] | run <endpoint> --input <json or file> [--name n] [--minutes 10] | result <endpoint> <request id>. "
            "Inputs for any model: WebFetch https://fal.ai/models/<endpoint>/llms.txt")
    opts, args = opts_of(a[1:])
    if not args:
        die("name the endpoint, for example fal-ai/nano-banana-pro")
    s = load()
    if a[0] == "price":
        code, d = http("GET", FAL_API + "/v1/models/pricing?" + urllib.parse.urlencode([("endpoint_id", e) for e in args]), headers=auth("FAL_KEY"))
        return emit(prices=[{k: p.get(k) for k in ("endpoint_id", "unit_price", "unit", "currency")} for p in ok(code, d, "pricing").get("prices") or []],
                    creative_cap=s["creative_cap"])
    endpoint = args[0].strip("/")
    base = "%s/%s/requests/" % (FAL_QUEUE, "/".join(endpoint.split("/")[:2]))
    if a[0] == "result":
        rid = args[1] if len(args) > 1 else die("usage: distro.py fal result <endpoint> <request id>")
        job = s["jobs"].setdefault(rid, {"provider": "fal", "endpoint": endpoint, "name": slug(endpoint.split("/")[-1]), "out": media_dir({}, endpoint.split("/")[-1])})
    else:
        payload = swap_paths(json_input(opts), fal_upload)
        code, sub = http("POST", "%s/%s" % (FAL_QUEUE, endpoint), payload, headers=auth("FAL_KEY"), timeout=120)
        rid = ok(code, sub, "submit").get("request_id") or die("FAL returned no request id")
        name = topt(opts, "name") or slug(endpoint.split("/")[-1])
        job = s["jobs"][rid] = {"provider": "fal", "endpoint": endpoint, "name": name, "out": media_dir(opts, name), "status": "IN_QUEUE",
                                "created": now(), "status_url": sub.get("status_url") or base + rid + "/status", "response_url": sub.get("response_url") or base + rid}
        save(s)
    _, started = poll(s, rid, job, opts, job.get("status_url") or base + rid + "/status", auth("FAL_KEY"), ("COMPLETED",), ("FAILED", "ERROR"), 3)
    code, res = http("GET", job.get("response_url") or base + rid, headers=auth("FAL_KEY"), timeout=120)
    finish(s, rid, job, ok(code, res, "result"), started)


def hf_upload(path):
    mime = (mimetypes.guess_type(path)[0] or "application/octet-stream").replace("image/jpg", "image/jpeg")
    code, d = http("POST", HF_API + "/files/generate-upload-url", {"content_type": mime}, headers=auth("HF_KEY"))
    d = ok(code, d, "upload")
    if http("PUT", d["upload_url"], raw=open(path, "rb").read(), headers=d.get("upload_headers") or {"Content-Type": mime}, timeout=300)[0] not in (200, 201, 204):
        die("Higgsfield upload failed")
    return d["public_url"]


def cmd_higgs(a):
    if not a or a[0] not in ("run", "result", "price"):
        die("usage: distro.py higgs run <model id> --input <json or file> [--name n] [--minutes 10] | result <request id> | price [<model id>] [--input <json>]")
    opts, args = opts_of(a[1:])
    s = load()
    if a[0] == "price":
        model = (args[0] if args else HF_IMAGE).strip("/")
        payload = swap_paths(json_input(opts) if opts.get("input") else {"prompt": "price check"}, lambda p: "https://example.com/" + os.path.basename(p))
        code, d = http("POST", "%s/estimate/%s" % (HF_API, model), payload, headers=auth("HF_KEY"))
        d = ok(code, d, "estimate")
        return emit(model=model, usd=d.get("usd"), credits=d.get("credits"), defaults={"image": HF_IMAGE, "video": HF_VIDEO}, creative_cap=s["creative_cap"])
    if not args:
        die("name the model or request id")
    if a[0] == "result":
        rid = args[0]
        job = s["jobs"].setdefault(rid, {"provider": "higgs", "endpoint": "higgs", "name": "higgs", "out": media_dir({}, "higgs")})
    else:
        model = args[0].strip("/")
        code, sub = http("POST", "%s/%s" % (HF_API, model), swap_paths(json_input(opts), hf_upload), headers=auth("HF_KEY"), timeout=120)
        rid = ok(code, sub, "submit").get("request_id") or die("Higgsfield returned no request id")
        name = topt(opts, "name") or slug("-".join(model.split("/")[1:]) or model)
        job = s["jobs"][rid] = {"provider": "higgs", "endpoint": model, "name": name, "out": media_dir(opts, name), "status": "queued",
                                "created": now(), "status_url": sub.get("status_url") or "%s/requests/%s/status" % (HF_API, rid)}
        save(s)
    d, started = poll(s, rid, job, opts, job.get("status_url") or "%s/requests/%s/status" % (HF_API, urllib.parse.quote(rid)), auth("HF_KEY"),
                      ("completed",), ("failed", "nsfw", "canceled"), 4)
    finish(s, rid, job, d, started)


def inline(ref):
    path = ref[7:] if ref.startswith("file://") else ref
    if os.path.isfile(path):
        mime = mimetypes.guess_type(path)[0] or ""
        if mime not in ("image/png", "image/jpeg", "image/webp") or os.path.getsize(path) > 20 << 20:
            die("Grok Imagine takes png, jpeg, or webp under 20 MB, not " + os.path.basename(path))
        return "data:%s;base64,%s" % (mime, base64.b64encode(open(path, "rb").read()).decode("ascii"))
    return ref if ref.startswith(("https://", "http://", "data:")) else die("no such file: " + ref)


def usd(usage):
    ticks = usage.get("cost_in_usd_ticks") if isinstance(usage, dict) else None
    return round(ticks / 1e10, 4) if isinstance(ticks, (int, float)) else None


def cmd_grok(a):
    if not a or a[0] not in ("image", "video", "result", "price"):
        die("usage: distro.py grok image <prompt> [--image <file or url> ...] [--n 2] [--aspect 4:5] [--name n] | grok video <prompt> "
            "[--image <start frame>] [--duration 6] [--aspect 9:16] [--name n] | grok result <request id> | grok price")
    opts, args = opts_of(a[1:])
    s, prompt = load(), " ".join(args).strip()
    if a[0] == "price":
        code, d = http("GET", XAI_API + "/models", headers=auth("XAI_API_KEY"))
        prices = [{"model": m["id"], "usd": round(m["image_price"] / 1e10, 4), "unit": "image", "source": "live"}
                  for m in ok(code, d, "model list").get("data") or [] if str(m.get("id", "")).startswith("grok-imagine") and isinstance(m.get("image_price"), (int, float))]
        return emit(prices=prices + [{"model": k, "usd": v, "unit": "second", "source": "list price 2026-10-01"} for k, v in GROK_VIDEO_USD.items()],
                    defaults={"image": GROK_IMAGE, "video": GROK_VIDEO}, creative_cap=s["creative_cap"])
    body = {k2: topt(opts, k1) for k1, k2 in (("aspect", "aspect_ratio"), ("res", "resolution")) if topt(opts, k1)}
    refs = opts.get("image") if isinstance(opts.get("image"), list) else [opts["image"]] if isinstance(opts.get("image"), str) else []
    if a[0] == "image":
        if not prompt or len(refs) > 3:
            die("a Grok Imagine image needs a prompt, and edits take up to 3 images")
        body.update(model=topt(opts, "model") or GROK_IMAGE, prompt=prompt, n=int(fopt(opts, "n", 1)))
        if refs:
            body.update({"image": {"url": inline(refs[0])}} if len(refs) == 1 else {"images": [{"url": inline(r)} for r in refs]})
        started = time.time()
        code, d = http("POST", XAI_API + ("/images/edits" if refs else "/images/generations"), body, headers=auth("XAI_API_KEY"), timeout=300)
        name = topt(opts, "name") or slug(prompt, 30)
        urls = [(i.get("url") or "data:%s;base64,%s" % (i.get("mime_type") or "image/png", i.get("b64_json", "")), i.get("mime_type") or "image/png")
                for i in ok(code, d, "image").get("data") or [] if i.get("url") or i.get("b64_json")]
        files = save_files(urls, media_dir(opts, name), name) or die("Grok Imagine sent back no image", detail=scrub(json.dumps(d))[:300])
        return emit(ok=True, model=body["model"], files=files, cost_usd=usd(d.get("usage")), seconds=round(time.time() - started))
    if a[0] == "video":
        if not prompt and not refs:
            die("a Grok Imagine video needs a prompt or a start image")
        body.update(model=topt(opts, "model") or GROK_VIDEO, duration=int(fopt(opts, "duration", 6)), **({"prompt": prompt} if prompt else {}),
                    **({"image": {"url": inline(refs[0])}} if refs else {}))
        code, d = http("POST", XAI_API + "/videos/generations", body, headers=auth("XAI_API_KEY"), timeout=300)
        rid = ok(code, d, "video").get("request_id") or die("Grok Imagine returned no request id")
        name = topt(opts, "name") or slug(prompt or "grok-video", 30)
        job = s["jobs"][rid] = {"provider": "xai", "endpoint": body["model"], "name": name, "out": media_dir(opts, name), "status": "pending",
                                "created": now(), "est_usd": round(body["duration"] * GROK_VIDEO_USD.get(body["model"], 0.08), 2)}
        save(s)
    else:
        rid = args[0] if args else die("usage: distro.py grok result <request id>")
        job = s["jobs"].setdefault(rid, {"provider": "xai", "endpoint": GROK_VIDEO, "name": "grok-video", "out": media_dir({}, "grok-video")})
    d, started = poll(s, rid, job, opts, "%s/videos/%s" % (XAI_API, urllib.parse.quote(rid)), auth("XAI_API_KEY"), ("done",), ("failed", "expired"), 5)
    if not (d.get("video") or {}).get("url"):
        job["status"] = "FAILED"
        save(s)
        die("Grok Imagine held this video back for moderation, change the prompt", request_id=rid)
    finish(s, rid, job, {"video": {"content_type": "video/mp4", **d["video"]}}, started, cost_usd=usd(d.get("usage")), est_usd=job.get("est_usd"))


# ---------- ad sizes ----------

def cmd_sizes(a):
    opts, args = opts_of(a)
    plats = [p.strip().lower() for p in (topt(opts, "for") or "meta").split(",") if p.strip()]
    fit, color = topt(opts, "fit") or "crop", topt(opts, "color") or "black"
    if not args or not os.path.isfile(args[0]) or set(plats) - set(PLACEMENTS) or fit not in ("crop", "pad") or not re.fullmatch(r"[a-z]+|0x[0-9a-fA-F]{6}", color):
        die("usage: distro.py sizes <image or video> --for <%s> [--fit crop|pad] [--color black]" % ",".join(PLACEMENTS))
    src = args[0]
    video = (mimetypes.guess_type(src)[0] or "").startswith("video")
    base, ext = os.path.splitext(src)
    out_ext = ".mp4" if video else ".jpg" if ext.lower() in (".jpg", ".jpeg") else ".png"
    venc = next((n for n in ("libx264", "mpeg4") if re.search(r"\s%s\s" % n, ff(["ffmpeg", "-hide_banner", "-encoders"]).stdout)), "mpeg4") if video else ""
    files = {}
    for p in plats:
        for shape, w, h in PLACEMENTS[p]:
            if (w, h) in files:
                files[(w, h)]["for"].append(p)
                continue
            out = "%s-%dx%d%s" % (base, w, h, out_ext)
            vf = ("scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d,setsar=1" % (w, h, w, h) if fit == "crop" else
                  "scale=%d:%d:force_original_aspect_ratio=decrease,pad=%d:%d:(ow-iw)/2:(oh-ih)/2:color=%s,setsar=1" % (w, h, w, h, color))
            extra = ["-c:v", venc, "-pix_fmt", "yuv420p", "-c:a", "aac", "-movflags", "+faststart"] + (["-crf", "20"] if venc == "libx264" else []) if video else ["-frames:v", "1"]
            ff(["ffmpeg", "-y", "-v", "error", "-i", src, "-vf", vf] + extra + [out])
            files[(w, h)] = {"size": "%dx%d" % (w, h), "shape": shape, "for": [p], "path": out, "bytes": os.path.getsize(out)}
    emit(ok=True, fit=fit, files=list(files.values()))


COMMANDS = {"install": cmd_install, "init": cmd_init, "status": cmd_status, "set": cmd_set, "ingest": cmd_ingest, "report": cmd_report,
            "winners": cmd_winners, "propose": cmd_propose, "approve": cmd_approve, "applied": cmd_applied,
            "revert": lambda a: mark_change(a, "reverted", ("applied",)), "reject": lambda a: mark_change(a, "rejected", ("proposed", "approved", "blocked")),
            "changes": cmd_changes, "learn": cmd_learn, "playbook": cmd_playbook, "site": cmd_site, "scan": cmd_scan, "topic": cmd_topic,
            "topics": cmd_topics, "lead": cmd_lead, "leads": cmd_leads, "suppress": cmd_suppress, "fal": cmd_fal, "higgs": cmd_higgs,
            "grok": cmd_grok, "sizes": cmd_sizes}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        die("commands: " + ", ".join(COMMANDS))
    try:
        COMMANDS[sys.argv[1]](sys.argv[2:])
    except subprocess.TimeoutExpired:
        die("timed out")
    except KeyboardInterrupt:
        die("stopped")
```
