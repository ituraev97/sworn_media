#!/usr/bin/env python3
"""YouTube description for the long video. usage: describe.py <episode_dir> <workdir>
Needs <episode_dir>/meta.json: {"summary": "...", "sources": [["title","url"],...], "tags": [...]}"""
import json, sys
E, W = sys.argv[1], sys.argv[2]
M = json.load(open(f"{E}/meta.json")); T = json.load(open(f"{W}/timeline.json"))
def ts(x): x = int(x); return f"{x // 60}:{x % 60:02d}"
ch = [(0, "Cold open")] + [(c[0], c[1]) for c in T["chapters"]]
out = [M["summary"], "", "Chapters:"] + [f"{ts(a)} {t}" for a, t in ch] + ["", "Sources (public records and reporting):"]
out += [f"- {t}: {u}" for t, u in M["sources"]]
out += ["", "Every quotation on screen is verbatim from the source shown with it. Documents shown are U.S. government works (public domain).",
        "Narration uses a synthetic voice.",
        "SWORN is an independent channel and is not affiliated with any court or government agency.",
        "", "#truecrime #courtcase #fraud #documentary"]
open(f"{W}/out/youtube_description.txt", "w").write("\n".join(out)); print("\n".join(out))
