# GROWTH RULES — all channels (owner 2026-11-28)
Source: YouTube Help Center / Creator Insider (Todd Beaupré, Sep 2026) / YPP policy + our own YouTube Analytics (28 days).

## What our numbers say
- 85–97% of our views come from the **Shorts feed**; long videos get almost nothing from Home/Suggested. The fastest growth lever is turning Shorts viewers into long-video viewers and packaging long videos better.
- New channels get tested on non-subscribers in the first hour; if nobody clicks AND watches, impressions stop. One weak video does not hurt the channel — repeated ignored videos do.

## Every long video
1. The promise of the title/thumbnail is paid off in the first 30 s (show it, don't tease it). No slow intros, no logo stings longer than 2 s.
2. Length follows the story: for channels under 10k subs aim for **10–15 min**; 30–50 min episodes are not watched (retention 14% at the halfway point on NMTK).
3. Original script with a clear thesis + analysis + sources. Vary structure and visuals between episodes — YouTube's "inauthentic content" policy (Jul 2025) demonetizes whole channels for "templated, mass-produced" videos with minimal variation. No still image on screen > 6 s; use maps, diagrams, timelines, real footage.
4. Title ≤ 70 chars, the plain topic keywords (who/what) in the first 5 words; title and thumbnail complement each other, never repeat the same words.
5. Make 2–3 thumbnail variants for Test & Compare (YouTube picks the winner by WATCH-TIME share, not CTR).
6. Description: 2-line summary, chapters, sources. Tags barely matter.
7. Realistic AI reconstructions of real people/events → tick "altered or synthetic content". Plain AI narration needs no label. Never generate a real person's face with AI.

## Every Short
- Standalone: number / famous name / paradox in second 0, payoff at the end, 20–40 s. A steady daily flow matters more than volume (Shorts older than ~30 days fade).
- Cut Shorts FROM the long video and name the long topic, so the Shorts → long path exists ("related video" link is set in Studio).

## Thumbnails (all channels)
- ONE focal point a phone viewer gets in 0.5 s: a human face with a strong emotion, or one iconic object. Max 3 big words. High contrast, warm/saturated colours beat dark empty scenes.
- Not the same template every time (inauthentic-content risk) — rotate 3–4 layouts.
- Never AI-generated faces of real people; real photos only (government releases, archive), AI may only relight/extend.

## Voice (all channels)
- Long narration 150–170 words/min, Shorts 160–180. No silence > 0.6 s inside narration except one deliberate beat before a reveal.
- Use tone tags: ~25% "hype" on reveals/numbers/verdicts, ~15% "calm" for context, the rest "normal". Short punchy sentences, rhetorical questions, one dry joke per chapter.
- Never ElevenLabs (owner 2026-11-28). Chatterbox (relay) or the livelier Kokoro method only.

## This channel
- Thumbnails: ONE face (the defendant from official photos) + 2–3 words + at most one stamp. Drop the document collage (4–5 elements) — winners in the niche are a single emotional face and a short phrase.
- Prefer famous cases/names people search (Theranos/Holmes-type) for longs; Shorts drive 82% of views, search 12% — use the person's name early in the title.
- MONETIZATION PUSH: channel is 4 weeks old; first goal 1,000 subs via Shorts (1–2/day, best-first by the HOOK scorecard), each Short linked to its long.

## Voice
- Voice audit 2026-11-28: SWORN narration is the flattest of all channels (pitch variation 2.6–2.7 semitones, loudness range 10 dB = monotone). Every run must really use Chatterbox via the TTS relay; if it falls back to Kokoro, use the 'livelier Kokoro' method from coldwarrant-media pipeline/tts_ep.py (commit 54a45a8, owner choice 2026-11-27): blend of voices, per-sentence synthesis, short sentences slower + longer pause, long ones quicker, ±2% jitter — measured on COLD WARRANT as lively as Chatterbox.
- Mark ~25% of paragraphs tone "hype" (verdicts, the moment the fraud is exposed, numbers) and ~15% "calm" (context) — the relay engine became more expressive today.
- Target 150–165 words/min for longs, no silence > 0.6 s except one deliberate beat before a reveal.
