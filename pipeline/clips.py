#!/usr/bin/env python3
"""Place real footage into a rendered video.  usage: clips.py <workdir>   (run right after render.js; rewrites <workdir>/video.mp4)
For every "clip" block in timeline.json with a resolved "_path", stage.html rendered a full-frame #00ff00 key area with the
source label / subtitles / Shorts hook on top. Here the clip (from "from" s, for the block's exact duration) goes underneath:
long = scaled+cropped to fill 1920x1080; Shorts = blurred darkened fill + the 16:9 clip at y=CLIP_SHORT_Y. Slight grade to match
the SWORN look. The rendered frame is chroma-keyed on top, so the label and subtitles stay pixel-identical. Always silent here
(audio: true is mixed by audio.py). Same frame count / length as the input. No clip blocks -> no-op. A broken clip never
fails the build: it is skipped with a warning (the green would stay, so then the block is filled dark instead)."""
import json, os, subprocess, sys
WD = sys.argv[1]; FPS = 30
CLIP_SHORT_Y = 590  # keep in sync with the label position in stage.html B.clip (label at 1214 = below the 608 px clip)
GRADE = "eq=contrast=1.06:saturation=0.82:brightness=-0.03:gamma=0.97,colorbalance=bs=0.04:bm=0.02:rh=-0.02"


def probe(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration",
                        "-of", "json", p], capture_output=True, text=True)
    j = json.loads(r.stdout or "{}"); st = (j.get("streams") or [{}])[0]
    return float(j.get("format", {}).get("duration") or 0), st.get("width"), st.get("height")


def main():
    global LONG, VW, VH
    T = json.load(open(f"{WD}/timeline.json")); LONG = T["mode"] == "long"; VW, VH = (1920, 1080) if LONG else (1080, 1920)
    allb = [b for b in T["blocks"] if b["spec"].get("type") == "clip"]
    if not allb: return print("clips: none")
    CH = 12  # blocks per ffmpeg pass: one graph with 100+ inputs exhausts memory/time; chunks are re-keyed on the same green windows
    for i in range(int(os.environ.get("CLIPS_START", 0)), len(allb), CH): run(allb[i:i + CH])


def run(blocks):
    src = f"{WD}/video.mp4"; vdur, _, _ = probe(src); nfr = round(vdur * FPS)
    inputs, chains, n, ni, wins = ["-i", src], [], 0, 0, []
    win = lambda a, z: f"between(t,{a - 1e-4:.4f},{z - 1e-4:.4f})"  # frame n (t = n/30) is a clip frame iff a <= t < b
    for b in blocks:
        s = b["spec"]; p = s.get("_path"); f0 = float(s.get("from", 0)); a, z = b["a"], b["b"]; d = z - a
        if d > (15.5 if s.get("audio") else 12.5): print(f"clips: WARNING {s.get('file')} runs {d:.1f}s on screen (RUNBOOK: <= ~12 s per clip shot, <= 15 s quote)")
        if not p: print(f"clips: WARNING missing {s.get('file')!r} at {a:.2f}s — dark label frame kept"); continue
        cd, cw, ch = probe(p)
        if not cd or not cw: print(f"clips: WARNING unreadable {p} — block at {a:.2f}s filled dark"); p = None
        elif f0 + d > cd + 0.05: print(f"clips: WARNING {os.path.basename(p)} ends at {cd:.1f}s < from+dur {f0 + d:.1f}s — last frame held")
        n += 1; k = f"c{n}"
        if p:
            inputs += ["-ss", f"{max(0.0, min(f0, cd - 0.1)):.3f}", "-i", p]; ni += 1
            base = f"[{ni}:v]fps={FPS},setsar=1,{GRADE},tpad=stop=-1:stop_mode=clone,trim=duration={d + 0.1:.3f}"
            if LONG:
                chains.append(f"{base},scale={VW}:{VH}:force_original_aspect_ratio=increase,crop={VW}:{VH},vignette=PI/6,format=yuv420p[{k}]")
            else:  # blurred fill + centered 16:9 (readable), 1080x608 at CLIP_SHORT_Y
                chains.append(f"{base},split[{k}a][{k}b];[{k}a]scale={VW}:{VH}:force_original_aspect_ratio=increase,crop={VW}:{VH},gblur=sigma=28,eq=brightness=-0.22:saturation=0.7[{k}bg];"
                              f"[{k}b]scale=1080:608:force_original_aspect_ratio=increase,crop=1080:608[{k}fg];[{k}bg][{k}fg]overlay=0:{CLIP_SHORT_Y},format=yuv420p[{k}]")
        else:
            chains.append(f"color=c=0x0b1020:s={VW}x{VH}:r={FPS}:d={d + 0.1:.3f},format=yuv420p[{k}]")
        chains[-1] = chains[-1][:-len(k) - 2] + f",setpts=PTS-STARTPTS+{a:.4f}/TB[{k}]"  # start the clip exactly at block a
        chains.append(f"[u{n - 1}][{k}]overlay=eof_action=pass:enable='{win(a, z)}'[u{n}]"); wins.append(win(a, z))
    if not n: return print("clips: nothing placed")
    g = [f"[0:v]setpts=PTS-STARTPTS,split[u0][top]"] + chains + \
        [f"[top]chromakey=0x00ff00:0.13:0.04:enable='{'+'.join(wins)}',despill=type=green:mix=0.6:expand=0.2:enable='{'+'.join(wins)}'[key]", f"[u{n}][key]overlay=format=auto:enable='{'+'.join(wins)}',format=yuv420p[v]"]
    tmp = f"{WD}/video.clips.mp4"
    r = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(g), "-map", "[v]", "-frames:v", str(nfr),
                        "-r", str(FPS), "-c:v", "libx264", "-preset", "ultrafast", "-crf", "16", "-pix_fmt", "yuv420p", tmp])
    if r.returncode or not os.path.exists(tmp):
        print("clips: WARNING ffmpeg failed — video.mp4 left as rendered (clip blocks show the key colour!)"); return
    os.replace(tmp, src); print(f"clips: placed {n} block(s) into {src} ({nfr} frames)")


if __name__ == "__main__":
    try: main()
    except Exception as e: print(f"clips: WARNING {e!r} — video.mp4 left as rendered")
