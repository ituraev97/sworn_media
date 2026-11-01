#!/usr/bin/env python3
"""Narration, voice B = Kokoro am_michael + SWORN processing.
usage: tts.py <spec.json> <workdir> [speed]
spec = {"lines":[{"say":..., "show":..., "scene":{...}}, ...]}
Writes <workdir>/vo/l_NN.wav (48 kHz mono, processed) and <workdir>/vo/durs.json.
Re-uses a line's audio when its text and speed did not change (vo/cache.json)."""
import sys, os, json, hashlib, subprocess
import soundfile as sf
spec = json.load(open(sys.argv[1])); W = os.path.abspath(sys.argv[2])
speed = float(sys.argv[3]) if len(sys.argv) > 3 else 1.02
os.makedirs(f"{W}/vo", exist_ok=True)
cache_f = f"{W}/vo/cache.json"; cache = json.load(open(cache_f)) if os.path.exists(cache_f) else {}
M = os.environ.get("KOKORO_DIR", "/home/claude/tts")
k = None
# Voice B processing (owner's choice 02.11.2026): pitch x0.96 with tempo kept, broadcast EQ, compression, short room.
CHAIN = ("asetrate={sr}*0.96,aresample=48000,atempo=1/0.96,highpass=f=70,equalizer=f=140:t=q:w=1:g=2.5,"
         "equalizer=f=450:t=q:w=1.2:g=-2,equalizer=f=3200:t=q:w=1:g=2.5,equalizer=f=7500:t=q:w=2:g=-2.5,"
         "acompressor=threshold=-20dB:ratio=3.5:attack=8:release=120:makeup=4dB,aecho=0.8:0.6:28|47:0.10|0.06,alimiter=limit=0.9")
durs = []
for i, ln in enumerate(spec["lines"]):
    out = f"{W}/vo/l_{i:02d}.wav"
    key = hashlib.md5(f"{ln['say']}|{speed}".encode()).hexdigest()
    if cache.get(str(i)) != key or not os.path.exists(out):
        if k is None:
            from kokoro_onnx import Kokoro
            k = Kokoro(f"{M}/kokoro-v1.0.onnx", f"{M}/voices-v1.0.bin")
        a, sr = k.create(ln["say"], voice="am_michael", speed=speed, lang="en-us")
        raw = f"{W}/vo/raw_{i:02d}.wav"; sf.write(raw, a, sr)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", raw, "-af", CHAIN.format(sr=sr), "-ar", "48000", "-ac", "1", out], check=True)
        cache[str(i)] = key
    durs.append(sf.info(out).duration)
json.dump(cache, open(cache_f, "w")); json.dump(durs, open(f"{W}/vo/durs.json", "w"))
print("lines", len(durs), "speech s", round(sum(durs), 1))
