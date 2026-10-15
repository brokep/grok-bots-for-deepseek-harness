---
name: qa-scripts
description: "The qa.py state tool, copied out by the install command in qa-setup. Never read or retype it."
---

# qa-scripts

Part of the Startup QA Bot agent preset.

# qa-scripts

The qa.py state tool. The install command in qa-setup copies it out by its marker, so never read or retype it. Commands: init, status, set, password, browser (start, open, errors, stop my own Chrome), walk, surface, surfaces, check, find, decide, fixed, sent, rundown, shot, export. Each prints one JSON line.

```python
#!/usr/bin/env python3
# STARTUP_QA_TOOLS_V1: Startup QA Bot state. The surface map, daily walks, findings, rundowns, and the test
# account. Every command prints one JSON line.
import csv
import datetime
import json
import os
import re
import secrets
import shutil
import signal
import string
import subprocess
import sys
import time

# Everything lives beside this file, so a second Startup QA Bot on a shared computer can use its own folder.
HOME = os.environ.get("QA_HOME") or os.path.dirname(os.path.abspath(__file__))
RUNS = os.environ.get("QA_RUNS") or os.path.join(HOME, "runs")
STATE = os.path.join(HOME, "state.json")
PASSWORD = os.path.join(HOME, "password")
# The bot's own Chrome profile. The browser tools share cookies and saved logins with the user's other bots.
PROFILE = os.path.join(HOME, "browser")
# A computer update restores /workspace but not /tmp, so the regenerable disk cache stays out of the synced folder.
CACHE = os.path.join("/tmp", "startup-qa-cache-" + re.sub(r"[^a-z0-9]+", "-", HOME.lower()).strip("-"))
PLATFORM_PROFILE = os.environ.get("QA_PLATFORM_PROFILE", "/home/box/chrome-profile")
BROWSERS = ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser")
BROWSER_PATHS = ("/opt/google/chrome/chrome", "/usr/lib/chromium/chromium", "/usr/lib/chromium-browser/chromium-browser")
BROWSER_WAIT = float(os.environ.get("QA_BROWSER_WAIT", "6"))
X11_DIR = os.environ.get("QA_X11_DIR", "/tmp/.X11-unix")
CONSOLE_RE = re.compile(r'INFO:CONSOLE[^\]]*\] "(.*)", source: (\S*)')
ERROR_RE = re.compile(r"(?i)uncaught|error|exception|failed|refused|denied|status of [45]\d\d")
DAYS = ("weekdays", "daily", "weekly", "manual")
CHANGES = ("github", "linear", "changelog", "none")
KINDS = ("shipped", "unshipped", "broke", "decision")
INBOXES = ("agentmail", "other")
DEFAULTS = {
    "product": "",
    "product_url": "",
    "email": "",
    "inbox": "",
    "account": "",
    "changes": [],
    "changelog": "",
    "triage": "",
    "days": "weekdays",
    "routine": False,
    "setup": False,
}


def now():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def today():
    return datetime.date.today().isoformat()


def stamp():
    return datetime.date.today().strftime("%Y%m%d")


def emit(**data):
    print(json.dumps(data, ensure_ascii=False))


def die(message):
    emit(error=message)
    sys.exit(1)


def opts_of(args):
    opts, i = {}, 0
    while i < len(args):
        if args[i].startswith("--"):
            key = args[i][2:]
            if i + 1 < len(args) and not args[i + 1].startswith("--"):
                opts[key] = args[i + 1]
                i += 1
            else:
                opts[key] = True
        i += 1
    return opts


def load():
    if not os.path.exists(STATE):
        die("no state yet, run: qa.py init")
    with open(STATE, encoding="utf-8") as f:
        s = json.load(f)
    for k, v in DEFAULTS.items():
        s["settings"].setdefault(k, v)
    for k, v in (("surfaces", {}), ("findings", {}), ("runs", []), ("walk", None), ("next_id", 0)):
        s.setdefault(k, v)
    return s


def save(s):
    tmp = STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(s, f, indent=1, ensure_ascii=False)
    os.replace(tmp, STATE)


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:40].strip("-") or "item"


def cmd_init(a):
    os.makedirs(HOME, exist_ok=True)
    new = not os.path.exists(STATE)
    if new:
        save({"version": 3, "settings": dict(DEFAULTS), "surfaces": {}, "findings": {}, "runs": [], "walk": None, "next_id": 0})
    emit(ok=True, new=new, home=HOME)


def cmd_status(a):
    s = load()
    st = s["settings"]
    open_f = [f for f in s["findings"].values() if f["status"] in ("open", "sent")]
    emit(
        setup=st["setup"],
        routine=st["routine"],
        settings={k: v for k, v in st.items() if k not in ("setup", "routine")},
        password_saved=os.path.exists(PASSWORD),
        surfaces=len(s["surfaces"]),
        open_bugs=sum(f["kind"] == "broke" for f in open_f),
        open_decisions=sum(f["kind"] == "decision" for f in open_f),
        walk_open=bool(s["walk"]),
        last_walk=s["runs"][-1]["date"] if s["runs"] else "",
    )


def cmd_set(a):
    if len(a) < 2:
        die("usage: qa.py set <key> <value>")
    s = load()
    key, val = a[0], " ".join(a[1:]).strip()
    st = s["settings"]
    if key in ("routine", "setup"):
        st[key] = val.lower() in ("on", "yes", "true", "done")
    elif key in ("product_url", "changelog") and (val == "" or re.match(r"https?://\S+$", val)):
        st[key] = val
    elif key == "email" and re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", val):
        st["email"] = val.lower()
    elif key == "inbox" and val in INBOXES:
        st["inbox"] = val
    elif key == "changes":
        picked = [v.strip() for v in val.split(",") if v.strip()]
        if not picked or any(v not in CHANGES for v in picked):
            die("changes: comma list of " + ", ".join(CHANGES))
        st["changes"] = [v for v in picked if v != "none"]
    elif key == "triage":
        st["triage"] = "" if val.lower() in ("none", "off", "me") else val[:120]
    elif key == "days" and val in DAYS:
        st["days"] = val
    elif key in ("product", "account") and len(val) <= 200:
        st[key] = val
    else:
        die(
            "keys: product, product_url, email, inbox agentmail|other, account, changes, changelog, triage, "
            "days weekdays|daily|weekly|manual, routine on|off, setup done|pending"
        )
    save(s)
    emit(ok=True, settings=st)


def cmd_password(a):
    load()
    made = bool(opts_of(a).get("new")) or not os.path.exists(PASSWORD)
    if made:
        pool = string.ascii_letters + string.digits
        # The fixed tail meets the usual upper, lower, digit, and symbol rules.
        value = "".join(secrets.choice(pool) for _ in range(20)) + "Qa7!"
        fd = os.open(PASSWORD, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w") as f:
            f.write(value)
    os.chmod(PASSWORD, 0o600)
    with open(PASSWORD, encoding="utf-8") as f:
        emit(password=f.read().strip(), new=made)


def walk_open(s):
    if not s.get("walk"):
        die("no walk open, run qa.py walk")
    return s["walk"]


def surface_of(s, ref):
    ref = str(ref).strip()
    for k, c in s["surfaces"].items():
        if ref in (str(c["id"]), k) or slug(ref) == k:
            return k, c
    die(f"no surface {ref}")


def brief_s(c):
    return {"id": c["id"], "name": c["name"], "where": c.get("where", ""), "status": c["status"], "last_seen": c.get("last_seen", "")}


def brief_f(f):
    return {k: f[k] for k in ("id", "kind", "title", "status", "surface") if f.get(k) is not None}


def finding_of(s, ref):
    for f in s["findings"].values():
        if str(f["id"]) == str(ref).strip():
            return f
    die(f"no finding {ref}")


def note_in_walk(s, bucket, fid):
    w = s.get("walk")
    if w is not None:
        w.setdefault(bucket, [])
        if fid not in w[bucket]:
            w[bucket].append(fid)


def add_finding(s, kind, title, surface=None, fields=None):
    key = f"{kind}:{slug(title)}:{surface or ''}"
    f = s["findings"].get(key)
    if f is None:
        s["next_id"] += 1
        f = {"id": s["next_id"], "kind": kind, "title": title, "surface": surface, "status": "open", "first_seen": today()}
        s["findings"][key] = f
        result = "new"
    elif f["status"] == "decided":
        result = "decided"
    elif f["status"] in ("fixed", "reported"):
        f.update(status="open", reopened=today())
        result = "reopened"
    else:
        result = "known"
    f["last_seen"] = today()
    for k, v in (fields or {}).items():
        if v:
            f[k] = v
    if result in ("new", "reopened"):
        note_in_walk(s, "found", f["id"])
    return f, result


def cmd_surface(a):
    if not a or a[0].startswith("--"):
        die('usage: qa.py surface "<name>" --where "<url or click path>" [--expect "<what should be there>"] [--new]')
    s = load()
    o = opts_of(a[1:])
    key = slug(a[0])
    c = s["surfaces"].get(key)
    added = c is None
    if added:
        s["next_id"] += 1
        c = {"id": s["next_id"], "name": a[0], "status": "live", "first_seen": today()}
        s["surfaces"][key] = c
    for k in ("where", "expect"):
        if isinstance(o.get(k), str):
            c[k] = o[k]
    c.update(status="live", last_seen=today())
    shipped = None
    if added and o.get("new"):
        f, result = add_finding(s, "shipped", f"New: {a[0]}", c["id"], {"note": c.get("where", "")})
        shipped = brief_f(f)
    if s.get("walk") is not None:
        s["walk"]["checks"][str(c["id"])] = {"result": "ok", "note": "added", "shot": ""}
    save(s)
    emit(added=added, surface=brief_s(c), shipped=shipped, surfaces=len(s["surfaces"]))


def cmd_surfaces(a):
    s = load()
    rows = sorted(s["surfaces"].values(), key=lambda c: c["id"])
    emit(count=len(rows), surfaces=[brief_s(c) for c in rows])


def cmd_walk(a):
    s = load()
    w = s.get("walk")
    resumed = bool(w) and w.get("date") == today()
    if not resumed:
        base = os.path.join(RUNS, stamp())
        folder, n = base, 1
        while os.path.exists(folder):
            n += 1
            folder = f"{base}-{n}"
        os.makedirs(os.path.join(folder, "screens"))
        w = {"date": today(), "folder": folder, "checks": {}, "found": [], "fixed": [], "started": now()}
        s["walk"] = w
        save(s)
    rows = sorted(s["surfaces"].values(), key=lambda c: (c["status"] == "live", c["id"]))
    todo = [brief_s(c) for c in rows if str(c["id"]) not in w["checks"]]
    bugs = [brief_f(f) for f in s["findings"].values() if f["kind"] == "broke" and f["status"] in ("open", "sent")]
    st = s["settings"]
    emit(resumed=resumed, folder=w["folder"], baseline=not s["surfaces"], url=st["product_url"], since=s["runs"][-1]["date"] if s["runs"] else "", changes=st["changes"], todo=todo, recheck=bugs)


def cmd_check(a):
    if len(a) < 2 or a[1] not in ("ok", "missing", "broken"):
        die("usage: qa.py check <surface id> ok|missing|broken [--note N] [--shot P]")
    s = load()
    w = walk_open(s)
    o = opts_of(a[2:])
    k, c = surface_of(s, a[0])
    prev, result = c["status"], a[1]
    note = o["note"] if isinstance(o.get("note"), str) else ""
    c.update(status={"ok": "live", "missing": "missing", "broken": "broken"}[result], last_checked=today())
    if result == "ok":
        c["last_seen"] = today()
    w["checks"][str(c["id"])] = {"result": result, "note": note, "shot": o["shot"] if isinstance(o.get("shot"), str) else ""}
    auto = None
    if result == "missing" and prev != "missing":
        f, r = add_finding(s, "unshipped", f"Gone: {c['name']}", c["id"], {"note": note or c.get("where", "")})
        auto = brief_f(f) | {"result": r}
    elif result == "ok" and prev == "missing":
        for f in s["findings"].values():
            if f["kind"] == "unshipped" and f.get("surface") == c["id"] and f["status"] in ("open", "sent"):
                f.update(status="fixed", fixed=today())
                note_in_walk(s, "fixed", f["id"])
        f, r = add_finding(s, "shipped", f"Back: {c['name']}", c["id"])
        auto = brief_f(f) | {"result": r}
    save(s)
    emit(ok=True, surface=brief_s(c), was=prev, finding=auto, left=sum(str(x["id"]) not in w["checks"] for x in s["surfaces"].values()))


def cmd_find(a):
    if len(a) < 2 or a[0] not in KINDS:
        die('usage: qa.py find shipped|unshipped|broke|decision "<title>" [--surface id] [--repro R] [--expected E] [--actual A] [--shot P] [--link L]')
    s = load()
    o = opts_of(a[2:])
    sid = surface_of(s, o["surface"])[1]["id"] if isinstance(o.get("surface"), str) else None
    fields = {k: o[k] for k in ("repro", "expected", "actual", "shot", "link", "note") if isinstance(o.get(k), str)}
    f, result = add_finding(s, a[0], a[1], sid, fields)
    save(s)
    emit(result=result, finding=brief_f(f))


def cmd_decide(a):
    if len(a) < 2:
        die('usage: qa.py decide <finding id> "<the call>"')
    s = load()
    f = finding_of(s, a[0])
    f.update(status="decided", decision=" ".join(a[1:]).strip(), decided=today())
    save(s)
    emit(ok=True, finding=brief_f(f), decision=f["decision"])


def cmd_fixed(a):
    s = load()
    f = finding_of(s, a[0] if a else "")
    f.update(status="fixed", fixed=today())
    note_in_walk(s, "fixed", f["id"])
    save(s)
    emit(ok=True, finding=brief_f(f))


def cmd_sent(a):
    s = load()
    f = finding_of(s, a[0] if a else "")
    f.update(status="sent", sent=today())
    save(s)
    emit(ok=True, finding=brief_f(f))


def cmd_rundown(a):
    s = load()
    w = walk_open(s)
    st = s["settings"]
    byid = {f["id"]: f for f in s["findings"].values()}
    new = [byid[i] for i in sorted(set(w.get("found", []))) if i in byid and byid[i]["status"] != "decided"]
    groups = {k: [f for f in new if f["kind"] == k] for k in KINDS}
    fixed = [byid[i] for i in sorted(set(w.get("fixed", []))) if i in byid]
    still = [f for f in byid.values() if f["status"] in ("open", "sent") and f["kind"] != "shipped" and f not in new]
    checks = w["checks"]
    counts = {r: sum(v["result"] == r for v in checks.values()) for r in ("ok", "missing", "broken")}
    names = {c["id"]: c["name"] for c in s["surfaces"].values()}
    unchecked = [c["name"] for c in s["surfaces"].values() if str(c["id"]) not in checks]

    def line(f):
        name = names.get(f.get("surface"), "")
        return f["title"] + (f" ({name})" if name and name.lower() not in f["title"].lower() else "")

    titles = {"shipped": "Shipped", "unshipped": "Unshipped", "broke": "Broke", "decision": "Decisions needed"}
    product = st["product"] or st["product_url"] or "Product"
    md = f"# Product QA: {today()}\n\n{product}: walked {len(checks)} of {len(s['surfaces'])} surfaces, "
    md += f"{counts['ok']} fine, {counts['missing']} missing, {counts['broken']} broken.\n"
    for k in KINDS:
        md += f"\n## {titles[k]}\n\n" + ("" if groups[k] else "None.\n")
        for f in groups[k]:
            md += f"- {line(f)}\n"
            for label, key in (("Repro", "repro"), ("Expected", "expected"), ("Actual", "actual"), ("Note", "note"), ("Link", "link"), ("Shot", "shot")):
                if f.get(key):
                    md += f"  {label}: {f[key]}\n"
    md += "\n## Fixed since the last walk\n\n" + ("\n".join(f"- {line(f)}" for f in fixed) or "None.") + "\n"
    label = {"broke": "Bug", "unshipped": "Gone", "decision": "Decision"}
    md += "\n## Still open\n\n" + ("\n".join(f"- {label[f['kind']]} {f['id']}: {line(f)}" for f in still) or "None.") + "\n"
    md += "\n## Not checked\n\n" + (", ".join(unchecked) or "Nothing.") + "\n"
    path = os.path.join(w["folder"], "report.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(os.path.join(w["folder"], "walk.json"), "w", encoding="utf-8") as fh:
        json.dump({"walk": w, "found": new, "fixed": fixed}, fh, indent=1, ensure_ascii=False)
    for f in groups["shipped"]:
        f["status"] = "reported"
    quiet = not new and not fixed
    if quiet:
        message = f"Walked {len(checks)} surfaces, nothing changed."
        if still:
            message += f" Still open: {len(still)}."
    else:
        head = ", ".join(f"{len(groups[k])} {'to decide' if k == 'decision' else k}" for k in KINDS if groups[k])
        lines = [f"Product QA {today()}: " + ", ".join(x for x in (head, f"{len(fixed)} fixed" if fixed else "") if x) + "."]
        for k, tag in (("shipped", "Shipped"), ("unshipped", "Unshipped"), ("broke", "Broke"), ("decision", "Decide")):
            if groups[k]:
                more = f", and {len(groups[k]) - 4} more" if len(groups[k]) > 4 else ""
                lines.append(f"{tag}: " + ", ".join(line(f) for f in groups[k][:4]) + more)
        lines.append("Repro steps and shots are in the attached report.")
        message = "\n".join(lines)
    s["runs"].append({"date": today(), "folder": w["folder"], "walked": len(checks), **counts, "new": len(new)})
    s["walk"] = None
    save(s)
    emit(quiet=quiet, message=message, report=path, counts={k: len(groups[k]) for k in KINDS}, fixed=len(fixed), handoff=[brief_f(f) for f in groups["broke"]] if st["triage"] else [], triage=st["triage"])


def cmd_shot(a):
    if not a:
        die("usage: qa.py shot <screenshot file> [name]")
    s = load()
    o = opts_of(a[2:])
    folder = o["folder"] if isinstance(o.get("folder"), str) else (s["walk"] or {}).get("folder")
    if not folder:
        folder = os.path.join(HOME, "setup")
    src, name = re.sub(r"^file://", "", a[0]), slug(a[1] if len(a) > 1 and not a[1].startswith("--") else "shot")
    if not os.path.isfile(src):
        die(f"no file at {src}")
    screens = os.path.join(folder, "screens")
    os.makedirs(screens, exist_ok=True)
    n = len(os.listdir(screens))
    path = os.path.join(screens, f"{n:02d}-{name}{os.path.splitext(src)[1] or '.png'}")
    shutil.copyfile(src, path)
    emit(ok=True, path=path, count=n + 1)


def browser_binary():
    if os.environ.get("QA_BROWSER_BIN"):
        return shutil.which(os.environ["QA_BROWSER_BIN"])
    # The box's own Chrome comes with its image, so a computer update never drops it. Never install one.
    for d in os.listdir("/proc"):
        if d.isdigit():
            try:
                with open(f"/proc/{d}/cmdline", "rb") as f:
                    args = f.read().decode(errors="ignore").split("\x00")
                exe = os.readlink(f"/proc/{d}/exe")
            except OSError:
                continue
            if any(x.startswith("--user-data-dir=" + PLATFORM_PROFILE) for x in args) and not any(x.startswith("--type=") for x in args) and os.access(exe, os.X_OK):
                return exe
    for name in BROWSERS:
        found = shutil.which(name)
        if found:
            return found
    return next((p for p in BROWSER_PATHS if os.access(p, os.X_OK)), None)


def profile_procs():
    want, me, procs = f"--user-data-dir={PROFILE}", os.getpid(), []
    for d in os.listdir("/proc"):
        if d.isdigit() and int(d) != me:
            try:
                with open(f"/proc/{d}/cmdline", "rb") as f:
                    args = f.read().decode(errors="ignore").split("\x00")
            except OSError:
                continue
            if want in args:
                procs.append((int(d), not any(x.startswith("--type=") for x in args)))
    return procs


def browser_launch(binary, display, args):
    env = dict(os.environ, DISPLAY=display)
    log = open(os.path.join(HOME, "browser.log"), "a")
    return subprocess.Popen([binary, f"--user-data-dir={PROFILE}"] + args, env=env, stdout=log, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, start_new_session=True)


def thumb(args):
    try:
        r = subprocess.run(["ffmpeg", "-loglevel", "error"] + args + ["-frames:v", "1", "-vf", "scale=32:20,format=gray", "-f", "rawvideo", "-"], capture_output=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return b""
    return r.stdout if len(r.stdout) == 640 else b""


def match_display(shot):
    mine = thumb(["-i", re.sub(r"^file://", "", shot)])
    if not mine:
        die("could not read that screenshot")
    scores = []
    for name in sorted(os.listdir(X11_DIR)) if os.path.isdir(X11_DIR) else []:
        if re.fullmatch(r"X\d+", name):
            t = thumb(["-f", "x11grab", "-i", ":" + name[1:]])
            if t:
                scores.append((round(sum(abs(x - y) for x, y in zip(mine, t)) / 640, 1), ":" + name[1:]))
    scores.sort()
    clear = scores and scores[0][0] < 40 and (len(scores) == 1 or scores[1][0] - scores[0][0] >= 8)
    return (scores[0][1] if clear else None), scores


def cmd_browser(a):
    s = load()
    sub, rest = (a[0] if a else "status"), a[1:]
    o = opts_of(rest)
    plain = [x for i, x in enumerate(rest) if not x.startswith("--") and not (i and rest[i - 1] in ("--display", "--match"))]
    b = s.setdefault("browser", {})
    binary, procs = browser_binary(), profile_procs()
    display = o["display"] if isinstance(o.get("display"), str) else b.get("display") or os.environ.get("DISPLAY", "")
    if sub == "status":
        emit(running=bool(procs), display=display, profile=PROFILE, browser=binary or "")
    elif sub == "start":
        if not binary:
            die("no Chrome or Chromium on this computer")
        if procs:
            emit(ok=True, already=True, display=b.get("display", display), profile=PROFILE)
            return
        if isinstance(o.get("match"), str):
            display, scores = match_display(o["match"])
            if not display:
                emit(error="can't tell which display is mine, pass --display :N from your prompt", scores=scores[:4])
                sys.exit(1)
        elif not isinstance(o.get("display"), str):
            die("pass --match <screenshot> or --display :N, displays can change after a restart")
        if not re.fullmatch(r":\d+(\.\d+)?", display or ""):
            die("not a display, pass --display :N")
        # A profile restored onto a recreated box keeps the old box's lock, and Chrome refuses to open it.
        for name in ("SingletonLock", "SingletonSocket", "SingletonCookie"):
            if os.path.lexists(os.path.join(PROFILE, name)):
                os.remove(os.path.join(PROFILE, name))
        url = plain[0] if plain else s["settings"]["product_url"]
        base = ["--no-first-run", "--no-default-browser-check", "--password-store=basic", "--disable-sync", "--enable-logging", "--start-maximized", f"--disk-cache-dir={CACHE}"]
        extra = []
        p = browser_launch(binary, display, base + ([url] if url else []))
        time.sleep(BROWSER_WAIT)
        if p.poll() is not None and not profile_procs():
            extra = ["--no-sandbox"]
            p = browser_launch(binary, display, base + extra + ([url] if url else []))
            time.sleep(BROWSER_WAIT)
        ok = bool(profile_procs())
        b.update(display=display, flags=extra, log_offset=0)
        save(s)
        emit(ok=ok, display=display, profile=PROFILE, no_sandbox=bool(extra), url=url)
        if not ok:
            sys.exit(1)
    elif sub == "open":
        if not plain or not re.match(r"https?://\S+$", plain[0]):
            die("usage: qa.py browser open <link>")
        if not binary or not procs:
            die("my browser is not running, run qa.py browser start")
        p = browser_launch(binary, b.get("display", display), b.get("flags", []) + [plain[0]])
        try:
            p.wait(timeout=20)
        except subprocess.TimeoutExpired:
            pass
        emit(ok=True, url=plain[0], handed_off=p.poll() is not None)
    elif sub == "errors":
        path = os.path.join(PROFILE, "chrome_debug.log")
        size = os.path.getsize(path) if os.path.exists(path) else 0
        start = b.get("log_offset", 0) if b.get("log_offset", 0) <= size else 0
        text = ""
        if size:
            with open(path, "rb") as f:
                f.seek(start)
                text = f.read().decode(errors="ignore")
        b["log_offset"] = size
        save(s)
        msgs = [(m.group(1), m.group(2)) for m in CONSOLE_RE.finditer(text)]
        errs = [{"message": m[:300], "source": src[:200]} for m, src in msgs if ERROR_RE.search(m)]
        emit(errors=errs[:20], more=max(0, len(errs) - 20), other=len(msgs) - len(errs))
    elif sub == "stop":
        main = [pid for pid, top in procs if top] or [pid for pid, top in procs]
        for pid in main:
            try:
                os.kill(pid, signal.SIGTERM)
            except OSError:
                pass
        emit(ok=True, stopped=len(main))
    else:
        die("browser commands: status, start [--match <screenshot>] [--display :N] [url], open <link>, errors, stop")


def cmd_export(a):
    s = load()
    spath, fpath = os.path.join(HOME, "surfaces.csv"), os.path.join(HOME, "findings.csv")
    with open(spath, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "where", "expect", "status", "first_seen", "last_seen"])
        for c in sorted(s["surfaces"].values(), key=lambda c: c["id"]):
            w.writerow([c["id"], c["name"], c.get("where", ""), c.get("expect", ""), c["status"], c["first_seen"], c.get("last_seen", "")])
    names = {c["id"]: c["name"] for c in s["surfaces"].values()}
    with open(fpath, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "kind", "title", "surface", "status", "first_seen", "last_seen", "repro", "decision"])
        for x in sorted(s["findings"].values(), key=lambda x: x["id"]):
            w.writerow([x["id"], x["kind"], x["title"], names.get(x.get("surface"), ""), x["status"], x["first_seen"], x.get("last_seen", ""), x.get("repro", ""), x.get("decision", "")])
    emit(ok=True, surfaces=spath, findings=fpath, surface_count=len(s["surfaces"]), finding_count=len(s["findings"]))


COMMANDS = {
    "init": cmd_init,
    "status": cmd_status,
    "set": cmd_set,
    "password": cmd_password,
    "surface": cmd_surface,
    "surfaces": cmd_surfaces,
    "walk": cmd_walk,
    "check": cmd_check,
    "find": cmd_find,
    "decide": cmd_decide,
    "fixed": cmd_fixed,
    "sent": cmd_sent,
    "rundown": cmd_rundown,
    "shot": cmd_shot,
    "browser": cmd_browser,
    "export": cmd_export,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        die("commands: " + ", ".join(COMMANDS))
    COMMANDS[sys.argv[1]](sys.argv[2:])
```
