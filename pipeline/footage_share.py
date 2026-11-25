#!/usr/bin/env python3
"""Real-footage share of a built video (owner rule 2026-11-26: real footage 60–75 % of the long video).
usage: footage_share.py <workdir> [min_pct=60]
Reads <workdir>/timeline.json (written by timeline.py) and sums the on-screen time of `clip` blocks whose file
was found (_path set). Prints total, footage seconds, share, longest single clip run and the gaps between
footage runs. Exit code 1 if the share is below min_pct (the run then reports why — e.g. the relay sent too few clips)."""
import json, sys
W = sys.argv[1]; MIN = float(sys.argv[2]) if len(sys.argv) > 2 else 60
T = json.load(open(f"{W}/timeline.json")); B = T["blocks"]; TOT = T["total"]
foot = 0.0; missing = 0; longest = 0.0; run = 0.0; gaps = []; gap = 0.0
for b in B:
    d = b["b"] - b["a"]; sp = b["spec"]
    if sp.get("type") == "clip" and sp.get("_path"):
        foot += d; run += d; longest = max(longest, run)
        if gap: gaps.append(gap); gap = 0.0
    else:
        if sp.get("type") == "clip": missing += 1
        run = 0.0; gap += d
share = 100 * foot / TOT if TOT else 0
print(json.dumps({"total_s": round(TOT, 1), "footage_s": round(foot, 1), "share_pct": round(share, 1),
                  "clip_blocks": sum(1 for b in B if b["spec"].get("type") == "clip"), "missing_files": missing,
                  "longest_footage_run_s": round(longest, 1), "longest_non_footage_gap_s": round(max(gaps + [gap]), 1)}))
sys.exit(0 if share >= MIN else 1)
