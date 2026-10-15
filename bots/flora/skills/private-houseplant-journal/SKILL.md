---
name: private-houseplant-journal
description: "use this when creating or updating the private houseplant journal on the houseplant care Bot’s Grok Bot computer, including first-run when the helper script did not copy"
---

# Private houseplant journal

Part of the Flora agent preset.

---
name: Private houseplant journal
description: >-
  use this when creating or updating the private houseplant journal on the
  houseplant care Bot’s Grok Bot computer, including first-run when the helper
  script did not copy
---
# Private houseplant journal

Use this when creating or updating the private houseplant journal on this Bot's Grok Bot computer. The journal files and the helper script do not copy with a template. On first-run, write the helper from this skill, then build an empty book, then show pictures. After that, rebuild whenever a plant is added or changed.

## Where it lives

On this Bot's Grok Bot computer, not the owner's Windows PC. `/workspace/plants/` (`index.html`, `plants.json`, `photos/`, `cards/`). Private. Not live.

## What it is

A page-through of cards, like a small book of playing cards:

1. Cover (location, plants now, plants ever logged, nicknames, how to open it)
2. A–Z index (search by the name they use; jump to that page)
3. One plant page per real plant (care-log card)
4. Optional sample pages, labeled SAMPLE, not counted as theirs
5. Blank pages (always; waiting for a plant)
6. Species guides labeled GUIDE (not their pots)
7. Glossary of terms (not a species encyclopedia)

Left/right (buttons or arrow keys), page number, Index, Glossary. Open a named plant with `floraJournal.goName("pothos")` after the page is open.

## What the owner sees

Never attach `index.html`, `plants.json`, or file paths unless they explicitly ask for the files or ask to publish. When they want the journal, they say **show my journal** or **open the journal** (also: plant journal, show the journal). Open `index.html` in the browser on this computer so they can click around. Tell them, in the desktop app: click my name at the top of this chat, then click the computer preview to open it full screen (or Cmd+Shift+I, then the preview). Do not invent another menu. Also send a cover picture in chat. Do not wait for a second confirmation after those phrases.

## First-run (empty install)

1. Create `/workspace/plants/`, `photos/`, `cards/`.
2. If `/workspace/notes/templates/flora-care-card/generate_journal.py` is missing, write it from the helper source in this skill.
3. Write `/workspace/plants/plants.json` as an empty collection (no owner plants, no samples):

```json
{
  "private": true,
  "published": false,
  "live_url": null,
  "owner": {
    "location": "Location not set yet",
    "journal_title": "Plant journal"
  },
  "counts": { "current": 0, "ever": 0 },
  "plants": []
}
```

4. Run `python3 /workspace/notes/templates/flora-care-card/generate_journal.py`.
5. The empty book must still have cover, index, three blank pages, five species guides, glossary.
6. Then do the journal walkthrough from the Houseplant care first-run skill.

Do not copy another owner's plants into a new install.

## After a plant is added or changed

Update `plants.json`, then run the generator again. Cover counts: current = plants still in the collection; ever = plants ever added (a death or giveaway drops current, not ever). Nicknames belong on the cover and in the index.

## Samples

Only if they ask for a filled-out look. Add plants with `"sample": true` and a SAMPLE banner. Do not count samples in current/ever. Do not treat them as the owner's collection. Do not ship samples in a new install.

## Showing pages

Open `index.html` on this computer, screenshot the card (cover, then index, then a blank, then glossary on first-run; later, the named plant). Send those pictures in chat.

## Live site

Do not publish without an explicit yes. SearchPlugins first. Say what would go public.

## Helper source

This Python file does not copy with a template. If it is missing, write it to `/workspace/notes/templates/flora-care-card/generate_journal.py` exactly, then run it.

```python
#!/usr/bin/env python3
"""Build the private plant journal as a page-through of cards. Always has a shell."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path("/workspace/plants")
JSON_PATH = ROOT / "plants.json"
OUT = ROOT / "index.html"
BLANK_PAGES = 3

GLOSSARY = [
    ("Bright, indirect light", "Strong light that is not a hot midday beam on the leaves."),
    ("Direct sun", "The plant sits in the actual sunbeam."),
    ("Drench and drain", "Water until it runs out the bottom, then empty the saucer."),
    ("Empty the saucer", "Pour off standing water under the pot after you water."),
    ("Fertilizer", "Food for growth. Mix and timing come from a named source. Skip in winter unless the source says otherwise."),
    ("Frost", "Bring tender outdoor plants in before the first freeze. US check: weather.gov for a named city."),
    ("Last watered", "The date you actually watered this pot. On the plant's log page, not the species guide."),
    ("Nickname", "The name you give this pot (for example, Kitchen pothos). Indexed with the species name."),
    ("Potting mix", "What is in the pot. Ask if unknown. Do not invent a mix."),
    ("Species guide", "A generalized card for that kind of plant. It is not one of your pots until you add it."),
    ("Winter rest", "Most houseplants want less water and little or no fertilizer unless a named source says otherwise."),
]

GUIDES = [
    ("Pothos", "Epipremnum aureum", "Bright, indirect to medium light. Water when the top of the mix is dry. Ordinary houseplant mix. Wikipedia: Epipremnum aureum."),
    ("Snake plant", "Dracaena trifasciata", "Low to bright light. Water sparingly. Well-draining mix. Wikipedia: Dracaena trifasciata."),
    ("Monstera", "Monstera deliciosa", "Bright, indirect light. Water when the top of the mix is dry. Airy mix. Wikipedia: Monstera deliciosa."),
    ("ZZ plant", "Zamioculcas zamiifolia", "Low to medium light. Let the mix dry down. Well-draining mix. Wikipedia: Zamioculcas zamiifolia."),
    ("Cactus", "Cactaceae (group)", "Direct sun if you can. Water less than leafy plants, even less in winter. Cactus mix, not a pothos mix. Wikipedia: Cactus."),
]


def esc(s):
    return html.escape("" if s is None else str(s))


def load():
    data = json.loads(JSON_PATH.read_text())
    owner = data.setdefault("owner", {})
    counts = data.setdefault("counts", {})
    plants = data.get("plants") or []
    real = [p for p in plants if not p.get("sample") and p.get("status") != "gone"]
    gone = [p for p in plants if p.get("status") == "gone"]
    samples = [p for p in plants if p.get("sample")]
    counts["current"] = len(real)
    counts["ever"] = counts.get("ever") or (len(real) + len(gone))
    if counts["ever"] < len(real) + len(gone):
        counts["ever"] = len(real) + len(gone)
    data["counts"] = counts
    JSON_PATH.write_text(json.dumps(data, indent=2) + "\n")
    real.sort(key=lambda p: (p.get("nickname") or p.get("name") or "").lower())
    return data, owner, counts, real, samples


def card(page_no, total, bar, banner, inner, kind="other", name=""):
    return f'''
<section class="page" data-page="{page_no}" data-kind="{kind}" data-name="{esc(name.lower())}">
  <div class="card">
    <header class="bar"><span>{esc(bar)}</span><span class="banner">{esc(banner)}</span></header>
    <div class="body">{inner}</div>
    <footer>Page {page_no} of {total}</footer>
  </div>
</section>'''


def plant_inner(plant):
    nick = plant.get("nickname")
    name = plant.get("name") or "Plant"
    title = nick or name
    sci = plant.get("scientific_name") or plant.get("guess_id") or ""
    photos = plant.get("photos") or []
    photo = photos[0] if photos else ""
    body = ""
    if photo:
        body += f'<img class="hero" src="{esc(photo)}" alt="{esc(title)}">'
    else:
        body += '<div class="hero placeholder">Photo goes here</div>'
    body += f"<h2>{esc(title)}</h2>"
    if nick and name:
        body += f'<p class="sci">{esc(name)}</p>'
    if sci:
        body += f'<p class="sci">{esc(sci)}</p>'
    rows = [
        ("Where", plant.get("where_it_sits") or plant.get("indoor_outdoor")),
        ("Light", plant.get("light")),
        ("Pot / mix", " · ".join(x for x in [plant.get("pot"), plant.get("potting_medium")] if x)),
        ("Last watered", plant.get("last_watered")),
        ("Last fertilized", plant.get("last_fertilized")),
        ("Last potted", plant.get("last_potted")),
        ("Next", plant.get("seasonal_move") or plant.get("next")),
        ("Source", plant.get("source_after_intake")),
    ]
    for label, val in rows:
        if val:
            body += f'<p><span class="k">{esc(label)}</span> {esc(val)}</p>'
    return body


def build(data, owner, counts, real, samples):
    location = owner.get("location") or "Location not set yet"
    title = owner.get("journal_title") or "Plant journal"
    current = counts.get("current") or 0
    ever = counts.get("ever") or current
    names = ", ".join((p.get("nickname") or p.get("name")) for p in real) or "None yet"

    n_real = len(real)
    n_samples = len(samples)
    n_blank = BLANK_PAGES
    n_guides = len(GUIDES)
    # 1 cover, 2 index, reals, samples, blanks, guides, glossary
    total = 2 + n_real + n_samples + n_blank + n_guides + 1

    page = 1
    pages = []

    cover = f'''
      <h1>{esc(title)}</h1>
      <p class="note">Private. Lives on Flora's computer. Not a live website.</p>
      <p><span class="k">Location</span> {esc(location)}</p>
      <p><span class="k">Plants now</span> {current}</p>
      <p><span class="k">Plants ever logged</span> {ever}</p>
      <p><span class="k">Names</span> {esc(names)}</p>
      <p class="note">When you get a new plant, tell Flora. She will add a page here. Say “show my journal” or “open the journal” anytime you want to see it.</p>'''
    pages.append(card(page, total, "FLORA MINDER", "Private", cover, "cover"))
    page += 1

    idx = ['<p class="note">Search by nickname or species. Jump to a page.</p>',
           '<input id="q" type="search" placeholder="Find a plant">', '<ul>']
    idx.append("<li><strong>Your plants</strong></li>")
    if real:
        for i, p in enumerate(real):
            pn = 3 + i
            label = p.get("nickname") or p.get("name") or "Plant"
            idx.append(f'<li><button type="button" data-go="{pn}">{esc(label)}</button> <span>p. {pn}</span></li>')
    else:
        idx.append("<li>None yet. Blank pages wait below.</li>")
    sample_start = 3 + n_real
    if samples:
        idx.append("<li><strong>Sample pages</strong> (not your pots)</li>")
        for i, p in enumerate(samples):
            pn = sample_start + i
            label = p.get("nickname") or p.get("name") or "Sample"
            idx.append(f'<li><button type="button" data-go="{pn}">{esc(label)}</button> <span>p. {pn}</span></li>')
    blank_start = sample_start + n_samples
    idx.append("<li><strong>Blank pages</strong></li>")
    for i in range(n_blank):
        pn = blank_start + i
        idx.append(f'<li><button type="button" data-go="{pn}">Empty page {i+1}</button> <span>p. {pn}</span></li>')
    guide_start = blank_start + n_blank
    idx.append("<li><strong>Species guides</strong> (not your pots)</li>")
    for i, (gname, _, _) in enumerate(GUIDES):
        pn = guide_start + i
        idx.append(f'<li><button type="button" data-go="{pn}">{esc(gname)} guide</button> <span>p. {pn}</span></li>')
    idx.append(f'<li><button type="button" data-go="{total}">Glossary</button> <span>p. {total}</span></li>')
    idx.append("</ul>")
    pages.append(card(page, total, "INDEX", "A–Z", "\n".join(idx), "index"))
    page += 1

    for p in real:
        banner = "Your plant"
        inner = plant_inner(p)
        nm = p.get("nickname") or p.get("name") or ""
        pages.append(card(page, total, "CARE LOG", banner, inner, "plant", nm))
        page += 1

    for p in samples:
        inner = plant_inner(p)
        nm = p.get("nickname") or p.get("name") or "sample"
        pages.append(card(page, total, "SAMPLE", "Not yours", inner, "sample", nm))
        page += 1

    for i in range(n_blank):
        inner = '''
      <div class="hero placeholder">Waiting for a plant</div>
      <h2>This page is empty</h2>
      <p class="note">When you tell Flora about a plant you bought or already have, she will turn a blank page into a log: nickname, photo, last watered, and the rest.</p>
      <p><span class="k">Nickname</span> You can name this pot.</p>
      <p><span class="k">Photo</span> Optional.</p>'''
        pages.append(card(page, total, "BLANK", "Empty", inner, "blank", f"empty {i+1}"))
        page += 1

    for gname, sci, blurb in GUIDES:
        inner = f'''
      <div class="hero placeholder">{esc(gname)}</div>
      <h2>{esc(gname)}</h2>
      <p class="sci">{esc(sci)}</p>
      <p class="note">Species guide. Not one of your plants until you add it.</p>
      <p>{esc(blurb)}</p>'''
        pages.append(card(page, total, "GUIDE", "Not yours yet", inner, "guide", gname))
        page += 1

    gloss = "<p class=\"note\">Words Flora uses. Not a species encyclopedia.</p><dl>"
    for term, meaning in GLOSSARY:
        gloss += f"<dt>{esc(term)}</dt><dd>{esc(meaning)}</dd>"
    gloss += "</dl>"
    pages.append(card(page, total, "GLOSSARY", "Terms", gloss, "glossary"))

    html_pages = "\n".join(pages)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)} (private)</title>
  <style>
    :root {{ --pot:#c15f2a; --leaf:#3d6b32; --paper:#f6f0e6; --ink:#1c1814; --muted:#6b5e52; --line:#e2d5c4; }}
    * {{ box-sizing: border-box; }}
    body {{ margin:0; background:#3a2a22; color:var(--ink); font-family: Georgia, serif; }}
    #deck {{ min-height:100vh; display:flex; flex-direction:column; align-items:center; padding:1rem 1rem 5.5rem; }}
    .page {{ display:none; width:min(420px,100%); }}
    .page.on {{ display:block; }}
    .card {{ background:var(--paper); border-radius:18px; overflow:hidden; box-shadow:0 12px 40px rgba(0,0,0,.35); min-height:640px; display:flex; flex-direction:column; }}
    .bar {{ background:var(--pot); color:#fffaf3; padding:.7rem 1rem; display:flex; justify-content:space-between; align-items:center; letter-spacing:.08em; font-size:.8rem; }}
    .banner {{ border:1px solid #fffaf3; padding:.1rem .4rem; font-size:.7rem; }}
    .body {{ padding:1.1rem 1.15rem 1.3rem; flex:1; }}
    .body h1, .body h2 {{ margin:.2rem 0 .4rem; }}
    .sci, .note {{ color:var(--muted); font-size:.95rem; }}
    .k {{ color:var(--pot); font-size:.75rem; letter-spacing:.04em; text-transform:uppercase; display:block; margin-top:.7rem; }}
    .hero {{ width:100%; height:220px; object-fit:cover; border-radius:12px; background:#e8ddcf; }}
    .placeholder {{ display:flex; align-items:center; justify-content:center; color:var(--leaf); text-align:center; padding:1rem; }}
    footer {{ padding:.6rem 1rem 1rem; color:var(--muted); font-size:.85rem; }}
    nav#pager {{ position:fixed; left:0; right:0; bottom:0; background:#2a1f18; color:#f6f0e6; display:flex; gap:.4rem; justify-content:center; align-items:center; padding:.7rem; flex-wrap:wrap; }}
    nav#pager button, nav#pager input {{ font:inherit; padding:.4rem .7rem; border-radius:8px; border:1px solid #6b5e52; background:#4a3429; color:#f6f0e6; }}
    ul {{ list-style:none; padding:0; margin:0; }}
    li {{ display:flex; justify-content:space-between; border-bottom:1px solid var(--line); padding:.4rem 0; }}
    li button {{ background:none; border:0; font:inherit; color:var(--ink); cursor:pointer; text-align:left; }}
    #q {{ width:100%; padding:.5rem; margin:.6rem 0 1rem; font:inherit; }}
    dt {{ color:var(--pot); margin-top:.8rem; }}
    dd {{ margin:.2rem 0 0; color:var(--muted); }}
  </style>
</head>
<body>
<div id="deck">
{html_pages}
</div>
<nav id="pager">
  <button type="button" id="prev">Left</button>
  <input id="num" type="number" min="1" max="{total}" value="1" style="width:4.2rem">
  <span>of {total}</span>
  <button type="button" id="next">Right</button>
  <button type="button" id="to-index">Index</button>
  <button type="button" id="to-gloss">Glossary</button>
</nav>
<script>
const pages = [...document.querySelectorAll(".page")];
const total = pages.length;
let cur = 1;
function show(n) {{
  n = Math.min(total, Math.max(1, n|0));
  cur = n;
  pages.forEach(p => p.classList.toggle("on", +p.dataset.page === n));
  document.getElementById("num").value = n;
}}
function goName(name) {{
  const needle = (name||"").toLowerCase();
  const hit = pages.find(p => (p.dataset.name||"").includes(needle) && p.dataset.kind === "plant")
    || pages.find(p => (p.dataset.name||"").includes(needle));
  if (hit) show(+hit.dataset.page);
}}
document.getElementById("prev").onclick = () => show(cur-1);
document.getElementById("next").onclick = () => show(cur+1);
document.getElementById("num").onchange = e => show(e.target.value);
document.getElementById("to-index").onclick = () => show(2);
document.getElementById("to-gloss").onclick = () => show(total);
document.querySelectorAll("[data-go]").forEach(b => b.onclick = () => show(+b.dataset.go));
const q = document.getElementById("q");
if (q) q.oninput = e => {{
  const s = e.target.value.toLowerCase();
  document.querySelectorAll("#deck [data-kind=index] li").forEach(li => {{
    li.style.display = li.textContent.toLowerCase().includes(s) ? "" : "none";
  }});
}};
document.addEventListener("keydown", e => {{
  if (e.key === "ArrowLeft") show(cur-1);
  if (e.key === "ArrowRight") show(cur+1);
}});
window.floraJournal = {{ show, goName, total }};
</script>
</body>
</html>
'''


def main():
    data, owner, counts, real, samples = load()
    OUT.write_text(build(data, owner, counts, real, samples), encoding="utf-8")
    print("wrote", OUT, "current", counts["current"], "ever", counts["ever"], "bytes", OUT.stat().st_size)


if __name__ == "__main__":
    main()
```
