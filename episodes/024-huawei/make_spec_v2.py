#!/usr/bin/env python3
"""Episode 024 v2 (owner 2026-11-26: real footage >= 60 %): splits every narration line into sentences, keeps a graphic (document/card)
only for the first part of a doc/big line and covers the rest with relay clips (3-10 s cuts). Words of `say`/`show` are untouched.
usage: make_spec_v2.py <workdir> > episode.json   (needs <workdir>/footage/*.mp4 and <workdir>/vo/durs_v1.json for estimates)"""
import json, re, os, subprocess, sys, copy
HERE = os.path.dirname(os.path.abspath(__file__)); W = sys.argv[1]
V1 = json.load(open(f"{HERE}/episode_v1.json"))["lines"]; D1 = json.load(open(f"{W}/vo/durs_v1.json"))
LABELS = json.load(open(f"{HERE}/clip_labels.json"))      # name -> {"label":..., "skip":[[a,b],...]}
POOLS = json.load(open(f"{HERE}/clip_pools.json"))        # line index -> [clip names] (used in order, cycling)
OVER = json.load(open(f"{HERE}/clip_overrides.json")) if os.path.exists(f"{HERE}/clip_overrides.json") else {}
sp = lambda t: re.split(r'(?<=[.!?])\s+(?=[A-Z“"])', t)
def clen(n):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{W}/footage/{n}.mp4"], capture_output=True, text=True)
    return float(r.stdout.strip() or 0)
CL = {n: clen(n) for n in LABELS if os.path.exists(f"{W}/footage/{n}.mp4")}
ptr = {n: (LABELS[n].get("start", 0.0)) for n in CL}
def take(n, d):
    """next window of d seconds from clip n, skipping bad ranges; cycles."""
    a = ptr[n]
    for _ in range(3):
        bad = [s for s in LABELS[n].get("skip", []) if a < s[1] and a + d > s[0]]
        if bad: a = max(b[1] for b in bad)
        if a + d <= CL[n] - 0.2: break
        a = LABELS[n].get("start", 0.0)
    ptr[n] = a + d + 0.6
    return round(a, 2)
ALWAYS_G = {"chapter", "title", "verdict", "end", "quote", "stat", "timeline"}
out = []; cur = None; ci = {}
for i, l in enumerate(V1):
    sc = l.get("scene"); cur = sc or cur
    T = cur["type"]; ss = sp(l["say"]); sh = sp(l["show"]) if "show" in l else None
    if sh is not None and len(sh) != len(ss): sh = None; sys.stderr.write(f"WARN line {i}: show/say sentence mismatch - not split\n"); ss = [l["say"]]
    est = [len(x) for x in ss]; tot = sum(est); dur = [D1[i] * e / tot for e in est]
    plan = OVER.get(str(i))                                  # explicit: list of "G"/"C" per sentence
    if plan is None:
        if T in ALWAYS_G and T not in ("title", "timeline"): plan = ["G"] * len(ss)
        elif T == "title": plan = ["G"] + ["C"] * (len(ss) - 1)
        elif T == "timeline": plan = ["G", "G"] + ["C"] * (len(ss) - 2)
        elif len(ss) == 1: plan = ["G"] if dur[0] > 12.5 or str(i) not in POOLS else ["C"]
        else:
            plan = []; acc = 0.0
            for k in range(len(ss)):
                if acc < 5.0: plan.append("G"); acc += dur[k]
                else: plan.append("C")
    # merge consecutive C sentences into shots <= 10 s
    k = 0; first = True; last_kind = None; pool = POOLS.get(str(i), []); pi = ci.get(i, 0)
    while k < len(ss):
        if plan[k] == "G":
            j = k
            while j + 1 < len(ss) and plan[j + 1] == "G": j += 1
            say = " ".join(ss[k:j + 1]); item = {"say": say}
            if sh: item["show"] = " ".join(sh[k:j + 1])
            if (k == 0 and sc) : item["scene"] = copy.deepcopy(sc)
            elif last_kind == "C" or (k == 0 and not sc and (not out or out[-1].get("_c"))):
                item["scene"] = copy.deepcopy(cur)
                if cur["type"] == "doc": item["scene"]["pan"] = [min(0.5, (cur.get("pan") or [0, 0])[0] + 0.08), (cur.get("pan") or [0, 0])[1]]
            out.append(item); last_kind = "G"; k = j + 1
        else:
            j = k; d = dur[k]
            while j + 1 < len(ss) and plan[j + 1] == "C" and d + dur[j + 1] <= 13.0: j += 1; d += dur[j]
            name = pool[pi % len(pool)] if pool else None; pi += 1
            if name not in CL: raise SystemExit(f"line {i}: clip {name!r} missing (have {sorted(CL)})")
            say = " ".join(ss[k:j + 1]); item = {"say": say, "_c": 1}
            if sh: item["show"] = " ".join(sh[k:j + 1])
            n = max(1, -(-int(d * 10) // 85))          # shots of <= ~8.5 s: long sentences get mid-line cuts
            mk = lambda nm, dd: {"type": "clip", "file": f"footage/{nm}.mp4", "from": take(nm, dd + 1.0), "label": LABELS[nm]["label"]}
            item["scene"] = mk(name, d / n)
            if n > 1:
                item["cuts"] = []
                for q in range(1, n):
                    nm2 = pool[pi % len(pool)] if len(pool) > 1 else name; pi += 1 if len(pool) > 1 else 0
                    item["cuts"].append({"at": round(q / n, 3), "scene": mk(nm2, d / n)})
            out.append(item); last_kind = "C"; k = j + 1
    ci[i] = pi
for o in out: o.pop("_c", None)
json.dump({"label": json.load(open(f"{HERE}/episode_v1.json"))["label"], "lines": out}, sys.stdout, indent=1, ensure_ascii=False)
