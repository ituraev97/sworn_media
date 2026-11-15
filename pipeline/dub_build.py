#!/usr/bin/env python3
"""Build a YouTube dubbing track for a SWORN long episode.
usage: dub_build.py <episode_dir> <workdir> <lang> [max_speed=1.25]
Needs: <workdir>/timeline.json, music.wav, fx.wav (from make.sh / audio.py of the English build),
       <episode_dir>/dub/<lang>/script.txt (one translated line per episode line, same order),
       /home/claude/dub_tts.py (Projects doc claude/dub_tts.py).
Each line is voiced, sped up only as much as needed to fit its original slot (owner 2026-11-15: change tempo if needed),
placed at its original start (or right after the previous line if that one ran long; drift is absorbed by later pauses),
mixed with the original music + SFX (no English voice) at -14 LUFS, exactly the video length.
Output: <workdir>/dub/<lang>/<slug>_<lang>.mp3 and report.json"""
import hashlib, json, os, subprocess, sys
import numpy as np, soundfile as sf

E, W, L = sys.argv[1], sys.argv[2], sys.argv[3]
MAXS = float(sys.argv[4]) if len(sys.argv) > 4 else 1.25
SR = 48000
T = json.load(open(f"{W}/timeline.json")); S = T["starts"]; TOT = T["total"]
lines = [x.strip() for x in open(f"{E}/dub/{L}/script.txt", encoding="utf-8").read().split("\n") if x.strip()]
assert len(lines) == len(S), f"{L}: {len(lines)} lines vs {len(S)} in timeline"
D = f"{W}/dub/{L}"; os.makedirs(f"{D}/l", exist_ok=True)


def tts(i, text, speed):
    h = hashlib.md5(f"{L}|{speed:.3f}|{text}".encode()).hexdigest()[:10]
    out = f"{D}/l/{i:02d}_{h}.wav"
    if not os.path.exists(out):
        open(f"{D}/l/in.txt", "w", encoding="utf-8").write(text)
        r = subprocess.run(["python3", "/home/claude/dub_tts.py", "--lang", L, "--in", f"{D}/l/in.txt", "--out", out, "--speed", f"{speed:.3f}"],
                           capture_output=True, text=True)
        if r.returncode: sys.exit(r.stderr)
        if "falling back" in r.stderr: open(f"{D}/fallback.txt", "a").write(f"line {i}: {r.stderr.strip()}\n")
    x, sr = sf.read(out, dtype="float32")
    if x.ndim > 1: x = x.mean(1)
    if sr != SR:
        n = int(len(x) * SR / sr); x = np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x).astype(np.float32)
    nz = np.where(np.abs(x) > 0.01)[0]  # trim leading/trailing silence
    return x[max(0, nz[0] - 480):nz[-1] + 2400] if len(nz) else x


voice = np.zeros(int(TOT * SR) + SR, np.float32)
rep, cur, maxdrift = [], 0.0, 0.0
for i, txt in enumerate(lines):
    nxt = S[i + 1] if i + 1 < len(S) else TOT - 1.2
    slot = nxt - S[i] - 0.12
    sp = 1.0; x = tts(i, txt, sp); d = len(x) / SR
    if d > slot:
        sp = min(MAXS, round(1.0 * d / slot * 1.03, 3)); x = tts(i, txt, sp); d = len(x) / SR
    at = max(S[i], cur + 0.15)
    i0 = int(at * SR); voice[i0:i0 + len(x)] += x[:len(voice) - i0]
    cur = at + d; drift = at - S[i]; maxdrift = max(maxdrift, drift)
    rep.append({"i": i, "speed": sp, "dur": round(d, 2), "slot": round(slot, 2), "start": round(S[i], 2), "placed": round(at, 2), "drift": round(drift, 2)})
vpath = f"{D}/voice.wav"; sf.write(vpath, voice / max(1e-9, np.abs(voice).max()) * 0.9, SR)
slug = os.path.basename(os.path.normpath(E)); mp3 = f"{D}/{slug}_{L}.mp3"
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", vpath, "-i", f"{W}/music.wav", "-i", f"{W}/fx.wav", "-filter_complex",
                "[0:a]aformat=channel_layouts=stereo[v];[1:a]aformat=channel_layouts=stereo,volume=0.42[m];[2:a]aformat=channel_layouts=stereo,volume=0.55[f];"
                "[v][m][f]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11", "-t", f"{TOT:.3f}", "-ar", "48000", "-b:a", "192k", mp3], check=True)
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", mp3], capture_output=True, text=True).stdout)
summary = {"voice_end": round(cur, 2), "lang": L, "file": mp3, "duration": round(dur, 2), "video": TOT, "max_speed": max(r["speed"] for r in rep),
           "lines_sped": sum(r["speed"] > 1 for r in rep), "max_drift": round(maxdrift, 2), "fallback": os.path.exists(f"{D}/fallback.txt")}
json.dump({"summary": summary, "lines": rep}, open(f"{D}/report.json", "w"), indent=1)
print(json.dumps(summary))
if cur > TOT - 0.3: sys.exit(f"voice runs past the end ({cur:.1f} > {TOT:.1f}) — shorten lines")
