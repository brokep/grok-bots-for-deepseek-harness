---
name: pfp-scripts
description: "The pfp.py script, copied out by the install command in icon-setup. Never read or retype it."
---

# pfp-scripts

Part of the Pfp Bot agent preset.

# pfp-scripts

The pfp.py script. The install command in icon-setup copies it out by its marker, so never read or retype it. Commands: warm, prep, preview, finish, love, tweak, state. Each prints one JSON line.

```python
#!/usr/bin/env python3
# PFP_TOOLS_V1: file chores for Pfp Bot, using only Python and the box's own ffmpeg.
# Every command prints one JSON line.
import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import time
import urllib.request

HOME = os.environ.get("PFP_HOME", "/workspace/pfp-bot")
AGENTS = os.environ.get("PFP_AGENTS", "/home/box/agent-data/agents")
FFMPEG = os.environ.get("PFP_FFMPEG", shutil.which("ffmpeg") or "")
STATE = os.path.join(HOME, "state.json")
OUT = os.path.join(HOME, "out")
DONE = os.path.join(HOME, "warm.done")
LOCK = os.path.join(HOME, "warm.lock")
SITE = "https://grokbot-icon-studio.serio-ai.chatgpt.site/images/"
SITE_REFS = [
    ("pink.png", "style-ref-site-1.png"),
    ("blonde.jpg", "style-ref-site-2.jpg"),
    ("teal.jpg", "style-ref-site-3.jpg"),
]
SQUARE = "crop='min(iw,ih)':'min(iw,ih)':0:'ih-min(iw,ih)'"


def load():
    try:
        with open(STATE) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {"next": 1, "tweaks": [], "loved": [], "candidates": {}}


def save(st):
    os.makedirs(HOME, exist_ok=True)
    with open(STATE, "w") as f:
        json.dump(st, f, indent=1)


def fetch(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 pfp-bot"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    with open(dest, "wb") as f:
        f.write(data)


def kind(path):
    with open(path, "rb") as f:
        head = f.read(12)
    if head.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if head.startswith(b"\x89PNG"):
        return ".png"
    if head.startswith(b"RIFF") and head[8:12] == b"WEBP":
        return ".webp"
    return None


def check(path):
    ext = kind(path)
    w = h = None
    if FFMPEG:
        info = subprocess.run([FFMPEG, "-hide_banner", "-i", path], capture_output=True, text=True).stderr
        m = re.search(r"Video:.*?\b(\d{2,5})x(\d{2,5})\b", info)
        if m:
            w, h = int(m.group(1)), int(m.group(2))
    if ext is None and w is None:
        raise ValueError("not a readable image")
    return {"path": path, "w": w, "h": h, "small": bool(w and min(w, h) < 200)}


def ffmpeg(src, dest, vf=None):
    cmd = [FFMPEG, "-y", "-v", "error", "-i", src, "-frames:v", "1", "-update", "1"]
    if vf:
        cmd += ["-vf", vf]
    if dest.endswith(".jpg"):
        cmd += ["-q:v", "2"]
    subprocess.run(cmd + [dest], check=True, capture_output=True)
    return dest


def sized(src, dest, px):
    if FFMPEG:
        try:
            return ffmpeg(src, dest, SQUARE + ",scale=%d:%d:flags=lanczos" % (px, px))
        except (OSError, subprocess.CalledProcessError):
            pass
    return src


def stage(src, stem):
    # GenerateImage reads the image type from the file extension, so copies get the real one.
    ext = kind(src)
    if FFMPEG and ext not in (".jpg", ".png"):
        return check(ffmpeg(src, stem + ".jpg"))
    if ext is None:
        raise ValueError("not a JPEG, PNG, or WebP image")
    shutil.copyfile(src, stem + ext)
    return check(stem + ext)


def agent_of(path):
    parts = os.path.normpath(path).split(os.sep)
    for i in range(len(parts) - 3):
        if parts[i] == "agents" and parts[i + 2] in ("attachments", "assets", "downloads"):
            return os.sep.join(parts[: i + 2])
    return None


def find_media(name):
    hits = []
    for p in glob.glob(os.path.join(AGENTS, "*", "profile.json")):
        try:
            with open(p) as f:
                if json.load(f).get("name", "").strip().lower() == name.strip().lower():
                    hits.append((os.path.getmtime(p), os.path.dirname(p)))
        except (OSError, ValueError):
            pass
    return [d for _, d in sorted(hits, reverse=True)]


def pick_refs(st):
    loved = [p for p in st.get("loved", []) if os.path.exists(p)]
    site = [p for p in st.get("site_refs", []) if os.path.exists(p)]
    return (loved[::-1] + site)[:2]


def rehome(st, media):
    os.makedirs(media, exist_ok=True)

    def move(path):
        dest = os.path.join(media, os.path.basename(path))
        if os.path.exists(path) and not os.path.exists(dest):
            shutil.copyfile(path, dest)
        return dest if os.path.exists(dest) else None

    st["media"] = media
    st["site_refs"] = [p for p in map(move, st.get("site_refs", [])) if p]
    st["loved"] = [p for p in map(move, st.get("loved", [])) if p]
    st["sources"] = [check(p) for p in (move(s["path"]) for s in st.get("sources", [])) if p]
    st["refs"] = pick_refs(st)
    save(st)


def warm(args):
    st = load()
    media = args.media or st.get("media")
    if not media:
        hits = find_media(args.name)
        if not hits:
            return {"ok": False, "error": "media_not_found"}
        media = os.path.join(hits[0], "assets")
    os.makedirs(media, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    st["media"] = media
    for src, dst in SITE_REFS:
        dest = os.path.join(media, dst)
        if os.path.exists(dest):
            continue
        try:
            fetch(SITE + src, dest)
            if kind(dest) is None:
                raise ValueError("not an image")
        except Exception:
            if os.path.exists(dest):
                os.remove(dest)
    st["site_refs"] = sorted(glob.glob(os.path.join(media, "style-ref-site-*")))
    save(st)
    result = {"ok": True, "media": media, "site_refs": st["site_refs"]}
    with open(DONE, "w") as f:
        json.dump(result, f)
    return result


def ensure_warm(args):
    if os.path.exists(DONE) and load().get("media"):
        return {"ok": True}
    try:
        with open(LOCK) as f:
            os.kill(int(f.read()), 0)
        for _ in range(60):
            if os.path.exists(DONE) or not os.path.exists(LOCK):
                break
            time.sleep(1)
    except (OSError, ValueError):
        pass
    if os.path.exists(DONE) and load().get("media"):
        return {"ok": True}
    return warm(args)


def prep(args):
    st = load()
    for path in args.photo:
        found = agent_of(path)
        if found:
            args.media = os.path.join(found, "assets")
            break
    if args.media and st.get("media") and os.path.realpath(args.media) != os.path.realpath(st["media"]):
        rehome(st, args.media)
    ready = ensure_warm(args)
    if not ready.get("ok"):
        return ready
    st = load()
    media = st["media"]
    sources = []
    handle = re.sub(r"^(https?://)?(www\.)?(x|twitter)\.com/", "", (args.handle or "").strip())
    handle = handle.lstrip("@").strip("/")
    if args.url or handle:
        if args.url:
            url = args.url.replace("_normal.", "_400x400.")
        else:
            url = "https://unavatar.io/x/" + handle + "?fallback=false"
        raw = os.path.join(media, "pfp-source-x.download")
        try:
            if "default_profile_images" in url:
                raise ValueError("default avatar, no real photo")
            fetch(url, raw)
            sources.append(stage(raw, os.path.join(media, "pfp-source-x")))
        except Exception as err:
            return {"ok": False, "error": "no_x_photo", "detail": str(err)}
        finally:
            if os.path.exists(raw):
                os.remove(raw)
        if handle:
            st["handle"] = "@" + handle
    for i, path in enumerate(args.photo):
        try:
            sources.append(stage(path, os.path.join(media, "pfp-source-" + str(i + 1))))
        except Exception as err:
            return {"ok": False, "error": "unreadable_photo", "path": path, "detail": str(err)}
    st["source"] = args.source or ("x" if (args.url or handle) else "upload")
    st["sources"] = sources
    st["refs"] = pick_refs(st)
    st["candidates"] = {}
    slug = re.sub(r"[^a-z0-9]+", "-", (st.get("handle") or "me").lower()).strip("-") or "me"
    save(st)
    return {
        "ok": True,
        "media": media,
        "sources": sources,
        "refs": st["refs"],
        "base": "pfp-" + slug + "-" + str(st.get("next", 1)),
        "tweaks": st.get("tweaks", []),
    }


def preview(args):
    st = load()
    cands = st.setdefault("candidates", {})
    if args.edit:
        items = [("e" + str(len([k for k in cands if k.startswith("e")]) + 1), args.edit)]
    elif args.a:
        items = [("a", args.a)] + ([("b", args.b)] if args.b else [])
    else:
        return {"ok": False, "error": "pass --a, --a and --b, or --edit"}
    found = agent_of(items[0][1])
    media = st.get("media")
    if found and media and os.path.realpath(found) != os.path.realpath(os.path.dirname(media)):
        rehome(st, os.path.join(found, "assets"))
        return {"ok": False, "error": "folder_moved", "sources": st["sources"], "refs": st["refs"]}
    os.makedirs(OUT, exist_ok=True)
    previews = {}
    for label, path in items:
        dest = os.path.join(OUT, (args.base or "pfp") + "-" + label + "-preview.jpg")
        previews[label] = sized(path, dest, 512)
        cands[label] = path
    save(st)
    return {"ok": True, "previews": previews}


def finish(args):
    st = load()
    path = args.image or st.get("candidates", {}).get(args.pick or "")
    if not path or not os.path.exists(path):
        return {"ok": False, "error": "unknown_pick", "candidates": st.get("candidates", {})}
    base = args.base or ("pfp-" + str(st.get("next", 1)))
    os.makedirs(OUT, exist_ok=True)
    hd = sized(path, os.path.join(OUT, base + "-hd.png"), 2048)
    x400 = sized(path, os.path.join(OUT, base + "-400.png"), 400)
    st["picked"] = path
    st["next"] = st.get("next", 1) + 1
    save(st)
    return {"ok": True, "hd": hd, "x400": x400, "resized": hd != path}


def love(args):
    st = load()
    src = args.image or st.get("picked")
    if not src or not os.path.exists(src):
        return {"ok": False, "error": "nothing_picked"}
    loved = [p for p in st.get("loved", []) if os.path.exists(p) and p != src] + [src]
    st["loved"] = loved[-3:]
    save(st)
    return {"ok": True, "loved": st["loved"]}


def tweak(args):
    st = load()
    st.setdefault("tweaks", []).append(args.text)
    save(st)
    return {"ok": True, "tweaks": st["tweaks"]}


def show(args):
    return dict({"ok": True}, **load())


def main():
    ap = argparse.ArgumentParser(prog="pfp.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("warm", "prep"):
        p = sub.add_parser(name)
        p.add_argument("--name", default="")
        p.add_argument("--media")
        if name == "prep":
            p.add_argument("--handle")
            p.add_argument("--url")
            p.add_argument("--photo", nargs="*", default=[])
            p.add_argument("--source")
    p = sub.add_parser("preview")
    for flag in ("--a", "--b", "--edit", "--base"):
        p.add_argument(flag)
    p = sub.add_parser("finish")
    for flag in ("--pick", "--image", "--base"):
        p.add_argument(flag)
    sub.add_parser("love").add_argument("--image")
    sub.add_parser("tweak").add_argument("text")
    sub.add_parser("state")
    args = ap.parse_args()
    commands = {
        "warm": warm,
        "prep": prep,
        "preview": preview,
        "finish": finish,
        "love": love,
        "tweak": tweak,
        "state": show,
    }
    try:
        if args.cmd == "warm":
            os.makedirs(HOME, exist_ok=True)
            with open(LOCK, "w") as f:
                f.write(str(os.getpid()))
        result = commands[args.cmd](args)
    except Exception as err:
        result = {"ok": False, "error": type(err).__name__, "detail": str(err)}
    finally:
        if args.cmd == "warm" and os.path.exists(LOCK):
            os.remove(LOCK)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
```
