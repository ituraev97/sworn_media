#!/usr/bin/env python3
"""Score + SFX + voice mix at -14 LUFS.  usage: audio.py <workdir>  -> <workdir>/mix.wav
Music: slow D-minor pad + soft pulse (stops before a verdict stamp). SFX by scene type:
quote = typewriter synced to typing, doc/list = paper, list rows = ticks, verdict = stamp hit, chapter/title = whoosh + low hit."""
import json, sys, subprocess, numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt, fftconvolve
WD = sys.argv[1]; T = json.load(open(f"{WD}/timeline.json")); S = T["starts"]; TOT = T["total"]; SR = 48000; N = int(TOT * SR) + SR
t = np.arange(N) / SR; rng = np.random.default_rng(11)
lp = lambda x, f, o=4: sosfilt(butter(o, f, "low", fs=SR, output="sos"), x)
bp = lambda x, a, b: sosfilt(butter(2, [a, b], "band", fs=SR, output="sos"), x)
irl = int(2.2 * SR); ir = rng.standard_normal(irl) * np.exp(-np.arange(irl) / (0.5 * SR)); ir = lp(ir, 4500); ir /= np.sqrt(np.sum(ir ** 2)) * 3
chords = [[73.42, 110, 146.83, 174.61], [58.27, 116.54, 146.83, 174.61], [87.31, 130.81, 174.61, 220], [65.41, 130.81, 164.81, 196]]
pad = np.zeros(N); seg = 8.0
for k in range(int(TOT / seg) + 2):
    c = chords[k % 4]; a0 = int(k * seg * SR); L = int((seg + 2) * SR); tt = np.arange(L) / SR
    env = np.minimum(1, tt / 1.5) * np.minimum(1, np.maximum(0, (seg + 2 - tt) / 2))
    x = sum(np.sin(2 * np.pi * f * tt + 0.3 * np.sin(2 * np.pi * 0.2 * tt + j)) * (0.5 if j == 0 else 0.22) for j, f in enumerate(c))
    j1 = min(N, a0 + L)
    if a0 < N: pad[a0:j1] += (x * env)[:j1 - a0]
pad = lp(pad, 1800)
def thump(amp, f0=50):
    L = int(.45 * SR); tt = np.arange(L) / SR; f = f0 * (1 + 1.5 * np.exp(-tt * 30)); return amp * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 9)
pulse = np.zeros(N); x0 = 0.0
while x0 < TOT - 3:
    i0 = int(x0 * SR); th = thump(.5); pulse[i0:i0 + len(th)] += th[:max(0, min(len(th), N - i0))]; x0 += 1.2
fx = np.zeros(N)
def put(x, at):
    i0 = int(max(0, at) * SR); j = min(N, i0 + len(x))
    if i0 < N: fx[i0:j] += x[:j - i0]
def click(amp=.3):
    L = int(.035 * SR); tt = np.arange(L) / SR; x = bp(rng.standard_normal(L), 1500, 6000) * np.exp(-tt * 160) + np.sin(2 * np.pi * 190 * tt) * np.exp(-tt * 120) * .5
    return amp * x / np.abs(x).max()
def rustle(d=.7, amp=.3):
    L = int(d * SR); x = bp(rng.standard_normal(L), 900, 7000) * (np.abs(lp(rng.standard_normal(L), 18)) * 8) * np.sin(np.pi * np.arange(L) / L); return amp * x / np.abs(x).max()
def whoosh(amp=.25):
    L = int(.6 * SR); tt = np.arange(L) / SR; x = bp(rng.standard_normal(L), 400, 3500) * np.sin(np.pi * tt / tt[-1]) ** 2; return amp * x / np.abs(x).max()
def hit(amp=1.0, f0=42, dec=2.2):
    L = int(2.5 * SR); tt = np.arange(L) / SR; f = f0 * (1 + 2.2 * np.exp(-tt * 14))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * dec) + lp(rng.standard_normal(L), 2500) * np.exp(-tt * 28) * .9
    x = x + fftconvolve(x, ir)[:L] * .6; return amp * x / np.abs(x).max()
music_gain = np.ones(N)
for j, bl in enumerate(T["blocks"]):
    s = bl["spec"]; a, b = bl["a"], bl["b"]; ty = s.get("type")
    if j > 0 and ty not in ("chapter",): put(whoosh(.18), a - 0.3)
    if ty in ("title", "chapter"): put(whoosh(.35), a - 0.35); put(hit(.45 if ty == "chapter" else .7, 50, 3.0), a + 0.05)
    if ty in ("doc", "list", "photo"): put(rustle(.8, .25), a + 0.05)
    if ty == "list":
        n = len(s.get("items", [])); step = min(0.45, max(0.14, (b - a - 1) / max(1, n)))
        for i in range(n): put(click(.28), a + 0.15 + i * step)
    if ty == "quote":
        q = s.get("q", ""); d = (b - a) * 0.86; n = max(1, len(q)); step = d / n; c = 0
        while c < n: put(click(.2 + .08 * rng.random()), a + 0.15 + c * step + rng.random() * 0.01); c += max(1, int(round(0.075 / step)))
        put(click(.38), a + 0.15 + d)
    if ty == "verdict":
        k = a + s.get("at", 0.7); put(hit(1.0), k)
        g0, g1, g2 = int((k - 0.6) * SR), int((k + 0.05) * SR), int((k + 1.2) * SR)
        music_gain[g0:g1] *= np.linspace(1, 0.12, g1 - g0); music_gain[g1:g2] *= np.linspace(0.12, 1, g2 - g1)
        pulse[int((k - 1.0) * SR):int((k + 2.0) * SR)] = 0
    if ty == "end": put(hit(.5), a + 0.05)
music = pad * 0.55 + pulse * 0.4
music = music + fftconvolve(music, ir[:SR])[:N] * .2
fade = np.ones(N); fi = int(1.5 * SR); fade[:fi] = np.linspace(0, 1, fi); eo = int((TOT - 2.2) * SR); fade[eo:] = np.linspace(1, 0, N - eo)
music *= fade * music_gain
voice = np.zeros(N)
for i, s in enumerate(S):
    x, sr = sf.read(f"{WD}/vo/l_{i:02d}.wav"); i0 = int(s * SR); voice[i0:i0 + len(x)] += x[:N - i0]
venv = np.convolve(np.abs(voice), np.ones(int(.25 * SR)) / int(.25 * SR), mode="same"); duck = 1 - 0.55 * np.clip(venv / (venv.max() * .12 + 1e-9), 0, 1)
music *= duck
for n, a, g in [("voice", voice, .9), ("music", music, .5), ("fx", fx, .6)]:
    sf.write(f"{WD}/{n}.wav", (a / max(1e-9, np.abs(a).max()) * g).astype(np.float32), SR)
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", f"{WD}/voice.wav", "-i", f"{WD}/music.wav", "-i", f"{WD}/fx.wav", "-filter_complex",
    "[0:a]aformat=channel_layouts=stereo[v];[1:a]aformat=channel_layouts=stereo,volume=0.42[m];[2:a]aformat=channel_layouts=stereo,volume=0.55[f];"
    "[v][m][f]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11", "-t", f"{TOT:.3f}", "-ar", "48000", f"{WD}/mix.wav"], check=True)
print("mix done")
