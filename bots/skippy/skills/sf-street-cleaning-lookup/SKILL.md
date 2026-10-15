---
name: sf-street-cleaning-lookup
description: "Use when the user asks where they can park, when street cleaning is, or whether they should move the car in San Francisco."
---

# SF street cleaning lookup

Part of the skippy agent preset.

---
name: SF street cleaning lookup
description: >-
  Use when the user asks where they can park, when street cleaning is, or
  whether they should move the car in San Francisco.
---
Phase 1 only: posted street-sweeping schedule for a curb. Never say a stall is legal. Color curbs, temp tow signs, and live meter hours are not in the data.

Local stack (on the bot's computer):
- /workspace/sf-parking/lookup.py — CLI for a point, Maps URL, address, intersection, or saved place
- /workspace/sf-parking/refresh.py — re-download DataSF extracts
- /workspace/sf-parking/data/ — cached sweep schedule (yhqp-riqs), streets (3psu-pn9h), EAS addresses (3mea-di5p), intersections
- /workspace/sf-parking/holidays.json — SFMTA holiday enforcement (daytime vs nightly)
- /workspace/sf-parking/places.json — saved spots (home / work / car). Do not invent these.

How to answer a live question:
1. Get a point. Pasted Maps link or lat,lng → python /workspace/sf-parking/lookup.py --url '...' or --lat ... --lng .... Address → --address. Intersection → --intersection. Saved label → --place home (or car / work).
2. Prefer the dropped pin (!3d/!4d) over map-center (/@).
3. Join is nearest sweep LineString, not rooftop address. If the tool flags needs_side, ask which side of the street.
4. Apply the holiday table: weekday daytime sweeping (about 6am–2pm) is not enforced on legal holidays; nightly usually is, except New Year's / Thanksgiving / Christmas.
5. Tell them: street, between-streets, side, next window, holiday exception if any.
6. Always add: they can park after the sweeper has passed; signs within 100 ft still win; this is the posted schedule, not a legal guarantee.

Saved places: read/write /workspace/sf-parking/places.json. After a successful lookup they confirm, save label + cnn + side + lat/lng. car updates every time they say they parked.

Alerts: a weekday morning routine should run lookup.py --place car (and home/work if saved) and only message if a sweep window is today. Stay quiet if no places or nothing due.

Refresh: re-run refresh.py if the schedule looks stale or Public Works announces changes. Sweep data updates as-needed; streets/addresses more often.
