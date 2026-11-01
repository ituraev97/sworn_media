#!/usr/bin/env python3
"""Build timeline.json from a spec + narration durations.
usage: timeline.py <spec.json> <workdir> <long|short>
A line's "scene" starts a new block; a line without "scene" continues the previous block.
Optional per line: "pause" (extra seconds after it)."""
import sys, json, re
spec = json.load(open(sys.argv[1])); W = sys.argv[2]; mode = sys.argv[3]
durs = json.load(open(f"{W}/vo/durs.json"))
L = spec["lines"]; assert len(L) == len(durs), "run tts.py first"
t = 0.45; starts = []
for i, ln in enumerate(L):
    sc = ln.get("scene", {})
    if sc.get("type") == "chapter" and i > 0: t += 0.6
    starts.append(round(t, 3))
    t += durs[i] + 0.32 + ln.get("pause", 0)
    if sc.get("type") == "title": t += 0.5
total = round(t + (3.2 if mode == "long" else 1.4), 2)
blocks = []
for i, ln in enumerate(L):
    if "scene" in ln or not blocks:
        blocks.append({"spec": ln.get("scene", {"type": "big", "lines": [""]}), "a": starts[i] - 0.12, "lines": []})
    blocks[-1]["lines"].append(starts[i])
for j, b in enumerate(blocks):
    b["b"] = blocks[j + 1]["a"] if j + 1 < len(blocks) else total
subs = []
maxw = 3 if mode == "short" else 99
maxc = 18 if mode == "short" else 44
for i, ln in enumerate(L):
    words = ln.get("show", ln["say"]).split(); chunks = []; cur = []
    for w in words:
        if cur and (len(" ".join(cur + [w])) > maxc or len(cur) >= maxw): chunks.append(" ".join(cur)); cur = []
        cur.append(w)
        if re.search(r'[.!?:;]["”]?$', w) and len(" ".join(cur)) > maxc * 0.45: chunks.append(" ".join(cur)); cur = []
    if cur:
        if chunks and len(cur) == 1 and len(chunks[-1]) + len(cur[0]) < maxc + 6: chunks[-1] += " " + cur[0]
        else: chunks.append(" ".join(cur))
    tot = sum(len(c) for c in chunks); a = starts[i]
    for c in chunks:
        b = a + durs[i] * len(c) / tot; subs.append([round(a, 3), round(b, 3), c]); a = b
chap = [[round(bl["a"] + 0.12, 2), bl["spec"].get("title", "")] for bl in blocks if bl["spec"].get("type") == "chapter"]
out = {"mode": mode, "total": total, "starts": starts, "durs": durs, "blocks": blocks, "subs": subs, "chapters": chap,
       "hook": spec.get("hook", ""), "label": spec.get("label", "")}
json.dump(out, open(f"{W}/timeline.json", "w"), indent=0)
print(mode, "total", total, "blocks", len(blocks))
