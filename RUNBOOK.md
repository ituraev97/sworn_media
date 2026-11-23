# SWORN — daily production runbook

Run notes go to RUNBOOK_NOTES.md (append there, never here). Promote a note into a rule section only if it must apply to every future run.

The run fires daily, but a long video goes out only every 2nd day (next section). An **OFF run** checks Metricool and stops. A **LONG run** = publish the episode voiced since the previous long run + write and order the voice for the next one (see "Voice = Chatterbox via TTS relay"). An episode = one long video (12–15 min, ≥ 10:00, 1920×1080) + 4 vertical Short **candidates** (20–40 s, 1080×1920), of which only the best **1–2 per day are scheduled on YouTube** for 2 days, all about ONE court case, hosted here and scheduled in Metricool.
Reference episode: `episodes/001-madoff/` (make_spec.py → episode.json, make_shorts.py → short1–6.json, meta.json, thumb.json, factcheck.md). Read it before writing anything.

## Long-video cadence — owner decision 2026-11-23 (overrides every "one long per run/day" line)
Why: token cost. One long video every 2 days; the days in between carry Shorts only.
**Step 0 of every run (before anything else, no repo reading needed):** Metricool `getScheduledPosts` (blogId 7806713, timezone America/New_York, from yesterday to 3 days ahead, ET dates).
- **OFF run** — tomorrow (ET) already has its Shorts scheduled AND today or tomorrow (ET) has a long video → do nothing else (no clone, no research, no weekly review) and end with a one-line report in Russian ("OFF: long <date>, Shorts <date> already scheduled"). This keeps OFF runs nearly free.
- **Repair run** — a long exists today or tomorrow but tomorrow has NO Short → schedule tomorrow's 10:00/18:00 from the latest episode's unscheduled candidates that scored ≥ 7 (they are still in its folder; rebuild only those Shorts with `make.sh … shorts` if no hosted mp4 exists), report, stop. No new long.
- **LONG run** — anything else. Target long day **T = tomorrow** (ET; never earlier than 2 days after the last long). The run does the full flow of "Voice = Chatterbox via TTS relay" with T as the target date everywhere (its "target date = earliest free ET date ≥ tomorrow" and step 4 "tomorrow" both mean T):
  1. publishes the episode voiced since the previous long run: long at 12:00 ET on T, plus Shorts for **T and T+1** — make **4 candidates** (s1–s4), score them all, schedule up to 2 per day: T 10:00 = best non-trailer, T 18:00 = trailer for the long, T+1 10:00 and 18:00 = the next best (different templates on the same day; never pad with a candidate < 7);
  2. writes the next episode, orders its voice and footage. With a 2-day gap the Chatterbox voice (4–6 h) is always ready by the next LONG run.
- **Weekly review** (Shorts cadence section + "Performance rules"): do it on the first LONG run on or after Monday (Asia/Tashkent), never on an OFF run.

## Shorts: cadence + hook rules — owner decision 2026-11-23
Why (Metricool, 30 days, 10 channels, 546 Shorts): Shorts that open with a hard NUMBER, a FAMOUS NAME or a "WHY…?" PARADOX won by 5–50×; template clones posted 3–6 times a day decayed week over week (COLD WARRANT median 633 → 107, bookplume 329 → 42) — YouTube throttles mass-produced look-alike Shorts. This section overrides every older "3 Shorts/day", schedule and Shorts-length line in this file.
**SWORN evidence (Nov 2–20):** winners = a famous name or recent case + a dollar figure: "$12.8M of $110M by 2018, Feds Said: The Wolf's Restitution" 537 views, "$1.5M–$3M Stolen From Earl Thomas: Both Plead Guilty" 414, "3,716 Grams and $228,000 Cash: Inside the Earl Thomas Case" 185, the FTX "Is Fine" quote 197, "$240 Million Cattle Scheme. FBI Fugitive Caught at LAX." 123. Losers = historical fraud recaps (Madoff "How a Judge Got to 150 Years", Stanford "Tier 3", Fyre "$2.56 Million in Stock") 1–10 views. Shorts median only 7.5 views at 3.8 Shorts/day.

**Cadence (YouTube):**
- Make 4 Short candidates per LONG run (s1–s4, covering 2 days — see "Long-video cadence"), score each one (below), and schedule only the best **1–2** per day on YouTube — **never more than 2 a day**. SWORN has no TikTok in Metricool, so the other candidates are NOT published anywhere (keep their json in the episode folder).
- Slots: **10:00 and 18:00 ET** (the two best existing slots, 8 h apart). One Short only → 10:00. Two Shorts on one day must use different visual templates.
- On the long-video day (long 12:00 ET) the 18:00 Short is a **trailer** for that long video (ends "Full story on the channel."); the 10:00 Short is the highest-scoring other candidate. The day after carries the next best candidates (see "Long-video cadence").

**Scorecard — schedule a Short only if it scores ≥ 7/10** (write the scores into the run report):
1. Hook (0–4): the first second has a hard number, a famous name/brand, or a paradox question — on screen AND spoken. 4 = all of them, punchy; 0 = generic explainer.
2. Payoff (0–3): the hook's promise is paid in the last 2–3 s (a reveal, a number, a twist). Viewers who feel cheated swipe → YouTube stops showing the channel.
3. Freshness (0–2): new story or new angle; never the same template as yesterday's Short.
4. Clarity (0–1): understandable with sound off.
No candidate reaches 7 → rewrite the hook/payoff of the best one and rebuild it; still < 7 → no Short that day (say so in the report).

**Hook rules:**
- Second 0: no logo, no title card, no "In 2008…" slow start — start on the most surprising sentence. On-screen hook ≤ 7 words, large, centered upper third.
- Title formulas that won: [number] + [stakes] ("$12.8M of $110M…"); [famous name] + [unexpected fact] ("The Wolf of Wall Street Still Owes…"); "Why/How did…?" + paradox. ≤ 60 characters + #shorts.
- **Banned openers/titles:** quizzes ("Name this X in 3 seconds"), plain recaps of old cases without a number or a famous name (Madoff/Stanford/Fyre-style history), "Here's what happened…", "Did you know…".
- **Length 20–40 s** (completion rate drives distribution); hard cap 50 s. End on the payoff, then cut — no outro card longer than 1 s; a loopable last line is a plus.
- **Template rotation:** rotate at least 3 visual templates (footage-led / document-or-number-led / timeline-led); never the same template two days running (check yesterday's Shorts in the previous episode folder).
- Watch-time check: a Short whose average view duration in Metricool is < 5 s after 48 h → that hook style is dead, don't repeat it.

**Weekly (first LONG run on or after Monday):** the run reads the last 7 days of Shorts analytics in Metricool (views + average view duration), lists the top 3 / bottom 3 and writes one line "what won" into "Performance rules" below — repeat the winners' hook pattern, drop the losers'.

## Real footage via relay — owner decision 2026-11-23
The sandbox cannot reach youtube.com. A relay on the owner's server downloads clips (YouTube or any yt-dlp URL) and hands them over through Google Drive folder "FOOTAGE RELAY". Client: `tools/footage_client.py` (stdlib only; read its docstring).
- Creds: Projects doc `claude/google-drive-oauth.md` → `/tmp/drive_creds.json` (keys client_id, client_secret, refresh_token). Never into git.
- Find candidate videos with the YouTube Data API (the same key / yt_research.py used for research). Watch the title, channel and description; pick exact time ranges.
- `clips.json` = `[{"name","src":"<youtube id or URL>","start":"M:SS","end":"M:SS"}]`, ≤ 40 clips, ≤ 90 s each.
- Right after the script is drafted: `python3 /home/claude/sworn_media/tools/footage_client.py request <RUN> clips.json --creds /tmp/drive_creds.json` (RUN = episode number, e.g. 023). Keep working (fact-check, Shorts, thumbnails), then `python3 /home/claude/sworn_media/tools/footage_client.py wait <RUN> <workdir>/footage --creds /tmp/drive_creds.json --timeout 1800`. No answer in 30 min → build with the existing sources and say so in the report.
- **Priority 1:** official US government video — DOJ/SEC/FBI press conferences, US Attorney announcements, congressional hearings (C-SPAN), court-released video. Public domain / public record.
- **Priority 2:** news reports and courtroom footage of THIS case from news channels — short clips, under our own narration and analysis (fair use).
- **Never:** movies or TV dramas, other YouTubers' faces or commentary, victims' or jurors' faces, minors, gore.
- **Use:** real footage = 30–50% of the long video's runtime; ≤ ~12 s of one external clip at a time, then cut back to our graphics/documents; mostly muted under narration; original audio only for short key quotes (≤ 15 s, speaker named on screen); a source label on screen during every clip ("Source: DOJ press conference, Nov 20, 2026" / "Source: WCCO"); list every footage source (channel/outlet, title, date, URL) in the description.
- This overrides "Never: Court TV / Law&Crime / TV footage" and "Never news or TV frames" in §3 / v2 rule 3 for **video clips** only; thumbnails and faces keep the lawful-photo rules.

## Voice = Chatterbox via TTS relay — owner decision 2026-11-23 (overrides "voice B = Kokoro" in §0 for every episode that has relay audio)
Why: the Kokoro narrator is the weakest part of the channel (long-video median 7 views, AVD ~7%). Chatterbox (natural, emotional) runs on the owner's server, ~4–6 h per episode, so each run works on TWO episodes: it publishes the one voiced since the previous run, then writes the next one and orders its voice.
Client: `tools/tts_client.py` (stdlib only; read its docstring). Creds = the same `/tmp/drive_creds.json` as the footage relay.

**Run order (replaces the single-episode flow of §2–§9):**
1. **Publish the voiced episode first.** Find the `backlog.md` row with status `voicing NNN` (oldest first).
   `python3 /home/claude/sworn_media/tools/tts_client.py status NNN --creds /tmp/drive_creds.json`
   - `ready` → `mkdir -p $W && tts_client.py fetch NNN $W` (W = /home/claude/work/NNN), get the footage again with `footage_client.py wait NNN $W/footage` (the relay keeps clips 7 days), then build with the SAME workdir: `LONG_MAX_MB=450 LONG_CRF=18 ./make.sh ../episodes/NNN-slug $W all`. tts.py keeps the Chatterbox lines (it prints `lines N`; check in the log that it did NOT load Kokoro — if any line was re-voiced, the text changed after the request: fix the text back or accept and say so in the report). Then §6 QA, §7 host, §8 schedule (target date = earliest free ET date ≥ tomorrow), §9 close → row `done YYYY-MM-DD`.
   - `pending` → the server is still working: skip to step 2 and say so in the report.
   - `failed` or `pending` for more than 30 h → build that episode now with Kokoro (old flow, `tts.py` makes the voice) so the channel never misses a day; row → `done (kokoro)`.
2. **Write the next episode** (§2 case choice, §3 research, §4 script + Shorts candidates, §5 independent fact-check with ALL fixes applied). The text is final after the fact-check — any later edit of a `say` line breaks the voice match.
3. **Order its voice:** `python3 /home/claude/sworn_media/tools/tts_client.py request NNN /home/claude/sworn_media/episodes/NNN-slug --creds /tmp/drive_creds.json --hint "<names, companies, places in the case, comma-separated>"`. Also order the footage now (`footage_client.py request NNN clips.json`). Commit the episode folder, set its `backlog.md` row to `voicing NNN`, push. Do NOT build it in this run.
4. **Never leave tomorrow empty:** if step 1 published nothing and Metricool has no long video for tomorrow (ET), build the episode from step 2 right away with Kokoro (old flow, skip step 3), row `done (kokoro)`.

**Script for the voice:** Chatterbox reads naturally at about Kokoro speed 0.98 — keep 1,600–2,000 words for the long (12–15 min). Punctuation drives delivery: short sentences, a "!" on real punches only (it raises the energy), numbers as words, no abbreviations in `say` ("Securities and Exchange Commission" the first time, then "the SEC" is fine). Shorts lines are sped up ×1.17 automatically.

## ⚡ v2 rules (owner-approved 2026-11-14). These override older sections where they conflict
Why: channel analytics showed Shorts lose viewers in 1–2 s and long videos have no thumbnails. YouTube Studio "Inspiration" for our niche (court/true-crime news) shows that winning videos have a **big emotional face**, few words, a fresh news peg, and a title built as "name + what happened". Holmes/Balwani/Theranos items are in that feed.

**Blocker:** custom thumbnails fail ("Could not upload video thumbnail") until the owner's sister phone-verifies the channel at youtube.com/verify. Keep generating thumbnails anyway and report the blocker in every LONG run summary until uploads succeed.

1. **Case choice (fresh first).**
   - Look first at the loudest federal fraud/white-collar news of the last 72 h – 7 days: justice.gov/news (OPA + USAO), SEC litigation releases, FBI, AP/Reuters court news.
   - Prefer: a recognisable name (CEO, celebrity, politician, influencer) or a big $ amount, a guilty plea / verdict / sentence, and **a lawful face photo**.
   - Big trials go out on verdict/sentencing day.
   - Use the backlog only when no fresh case qualifies. A fresh case with no lawful face → Shorts only, or a long video with the number panel.
   - Unchanged: convicted/sentenced, or "charged/alleged" with presumption of innocence stated. Never sexual crimes or crimes involving children (so no Diddy, Russell Brand, Clancy). Independent fact-check agent before scheduling.
2. **Lawful face sources only** (record the source and license in sources.md and the description):
   - U.S. federal works: DOJ/FBI/USMS/DoD/Congress photos, which are public domain.
   - State booking photos only where the state treats them as public records.
   - **Wikimedia Commons** files licensed PD, CC0, CC BY or CC BY-SA. Search via the commons.wikimedia.org API (send a User-Agent). Download from `upload.wikimedia.org`; `thumb.wikimedia.org` is blocked. Add the credit line "Photo: <Artist>, <License> via Wikimedia Commons" to the description.
   - Never use news-agency, TV or Getty frames, and never use courtroom sketches.
   - Crop away third-party logos.
3. **Thumbnails v3 (owner 2026-11-17: "make them awesome, look at what takes off") = `pipeline/thumb2.js` with `<ep>/thumb2.json`.**
   - **Why v3:** our v2 thumbnails (red number panel + label + two text lines) all looked the same and carried 4 text blocks. In Nov 2026 the court/fraud outliers (YouTube Data API, last 30 days: 50–1000× views/subs, e.g. "WHERE'S THE $250M?", "$1.2B MEDICARE FRAUD / CAUGHT BOARDING A FLIGHT", "30 YEARS IN PRISON / $250M FOOD FRAUD") share these traits:
     - Two REAL photos side by side: a big face plus the evidence or action (cash, seized assets, FBI agents, the jet, the mansion, a wanted poster or document with a stamp). No flat colour panels.
     - At most 2 text elements, ≤ 5 words per line, and the number sits inside the line ("$27M ELDER SCAM").
     - Or a question on a dark navy half ("WHERE'S THE $250M?") next to the face.
     - Faces are large, sharp and emotional (open mouth, stare, crying); the eyes sit in the upper third.
   - **Three formats every time:**
     - **A** = face + evidence photo (`left.img` face with `cover`, `right.img` evidence with a `stamp` like GUILTY / CAPTURED / 78 MONTHS / $97M UNPAID), plus line1 white and line2 red.
     - **B** = question: `left: {"q": ["WHERE'S","THE","$27M?"]}`, face right, no bottom lines.
     - **C** = evidence or document left (split 0.42), face right, line1 white and line2 yellow.
     - Use the strongest one as thumb_A.
   - **Evidence photos, lawful only:**
     - photos inside DOJ/USAO press releases and sentencing slides (cash, seized cars, gold, mansions);
     - exhibits from court filings;
     - FBI/DEA/USMS/ICE photos;
     - DVIDS;
     - Wikimedia Commons PD/CC.
     - A document page zoomed to its key line works when there is no photo.
     - Never news or TV frames.
   - **Number panels:** the red number panel (`{"number": …}`) is allowed only when no evidence photo exists at all.
   - **Face quality:** source face ≥ 500 px tall; never stretch a tiny face; crop to the eyes and mouth.
   - **QA:** look at all three at full size AND at 168×94. At small size the face, the number and one word must still read.
   - **Facts:** every word must be factual. "Fraud" only after a conviction or plea, otherwise "CHARGED" / "FEDS ALLEGE". A question mark does not excuse a false implication.
   - **References:** `episodes/015-little-tiger/thumb3.json`, `episodes/016-rozier/thumb3.json`, `episodes/017-belfort/thumb3.json`.
4. **Titles:** Name + $amount + scheme + CAPS verb + years/twist, under 70 characters, every word sourced. Example: "Elizabeth Holmes: The $9B Blood Test That NEVER Worked — 11 Years".
5. **Shorts v2 (20–40 s; 4 candidates per LONG run, only the best 1–2/day go to YouTube — see "Shorts: cadence + hook rules"):**
   - frame 0 = face/document + giant number + tag;
   - narration starts at 0.05 s with the verdict, speed 1.15;
   - big centered word-level captions;
   - punch-zoom and flash on numbers;
   - no slow intro.
6. **Long videos 12–18 min:**
   - published within 24–48 h of the news;
   - a re-hook every ~2 min;
   - the hero's name at the start of the title.
7. **Engagement:**
   - the description and the first comment ask one question ("Was 11 years enough?");
   - end screen added in Studio by the owner;
   - Shorts "Related video" field points to the long video (Studio, manual).

## 0. Context
- Channel bible: Projects doc `claude/sworn-bible.md` (project "AI YOUTUBE"). Brand book: Design System artifact "SWORN".
- YouTube channel: SWORN (UCNoMjeEPiut8OgSGl0Y-WJg). Metricool brand **SWORN, blogId 7806713**. Publish timezone **America/New_York**.
- Schedule per US day (ET): Shorts **10:00 and 18:00** (best 1–2 per day of s1–s4 by the scorecard; on the long day 18:00 = trailer for the long); long episode **12:00 every 2nd day** ("Long-video cadence") (owner decision 2026-11-23; was 3 Shorts at 10:00, 14:00, 18:00, before that 6).
- Owner decisions: voice = **Chatterbox via TTS relay** (section "Voice = Chatterbox via TTS relay"); fallback only: voice **B** = Kokoro `am_michael` + SWORN processing (built into `pipeline/tts.py`; long speed 0.98, Shorts 1.05). Do NOT set isAiGeneratedContent (graphics + real documents + synthetic narrator; the description says "Narration uses a synthetic voice").

## 1. Setup (fresh container)
```bash
git clone --depth 1 https://github.com/ituraev97/sworn_media /home/claude/sworn_media   # after add_repo(access=push)
pip install --break-system-packages -q kokoro-onnx soundfile scipy
mkdir -p /home/claude/tts && cd /home/claude/tts && \
  curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx && \
  curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
```
Playwright + Chromium (`require('playwright')` with `NODE_PATH=$(npm root -g)`), ffmpeg, pdftoppm/pdftotext are preinstalled. Fonts and the seal are in `pipeline/fonts`, `pipeline/brand`.

## 2. Target date and case
- Target date = T from "Long-video cadence" (step 0 already read Metricool; OFF runs never get here).
- Case = first `todo` row of `backlog.md`. Mark it `in progress` immediately (commit+push to main) so parallel runs don't take it.
- Only cases with a verdict/sentence (or a decided Supreme Court case). Focus: fraud, financial crime, white-collar, scams, landmark Supreme Court decisions. Never: crimes against children, sexual crimes, gore. Pardons, reversals, reduced sentences must be told.
- Rotate formats: THE VERDICT (one case, crime → sentence), THE PAPER TRAIL (how a fraud was uncovered), THE ARGUMENT (Supreme Court case; real argument audio only if a public-domain source is reachable).

## 3. Sources and research (facts decide everything)
- Primary first: justice.gov press releases and charging documents (PDFs download fine with curl from the shell: `/archive/usao/<district>/pressreleases/...` and `/usao-<district>/pr/...`), court opinions, SEC/FTC/FBI releases and complaints, supremecourt.gov. Then AP/Reuters/major outlets. WebFetch for pages the shell can't reach (sec.gov from shell is blocked; WebFetch works).
- Every number, date, name and quote must come from a page you opened → `episodes/NNN-slug/sources.md` (claim → URL).
- **Footage:** relay clips (see "Real footage via relay") alongside the documents, Wikimedia Commons, DVIDS and government photos below.
- **Images = only U.S. government documents** (rasterize the PDF with `pdftoppm -r 220`, crop with PIL, save JPG in `episodes/NNN-slug/img/`). Crop OUT agency seals and logos. No photos of people unless public domain AND clearly licensed. Never: Court TV / Law&Crime / TV footage, AI images of real people, mugshots of acquitted people.
- Quotes on screen (`quote` scenes, `q`) must be verbatim (ellipsis allowed). If it's a reporter's or prosecutors' quotation, the cite says so ("As quoted in …").
- Charged-but-not-convicted people: "charged", "alleged", "prosecutors say". Private victims: no names.

## 4. Script → `episodes/NNN-slug/make_spec.py` → `episode.json`
- Copy the structure of 001. Each line = `{"say": spoken text (numbers as words), "show": subtitle text (digits), "scene": {...}}`; a line without `scene` continues the previous scene.
- 1,600–2,000 words → 12–15 min (Chatterbox, see the voice section). Cold open (≤45 s, the strongest verified moment) → `title` → 5–6 `chapter`s → closing line → `end`.
- Scene types (see `pipeline/stage.html`): `title{kicker,title,sub}`, `chapter{n,title}`, `doc{img,pan:[from,to],hl:[x,y,w,h],kicker,title,note,src}` (real document scan; hl = gold highlight box in image fractions), `quote{q,case,doc,cite,size,recreated}`, `big{kicker,lines:[...], src}` ("|" = line break; the last line turns gold and appears on the next spoken line), `stat{kicker,value,label,src}`, `bars{kicker,title,items:[{label,value,display}],src}`, `list{kicker,items:[[n,label]],src}`, `timeline{kicker,events:[{date,text}],at,src}`, `verdict{kicker,stamp,big,sub,neutral}` (the ONLY place for red; `neutral:true` for NOT GUILTY / dismissed), `end{}`.
- Real footage: `clip{file:"footage/<name>.mp4",from,label,audio}`. `file` is relative to the workdir (Shorts also look in the parent workdir). `from` = start second inside the clip, and the clip runs for the scene's duration (more lines without `scene` = longer). Keep each clip shot ≤ ~12 s, then cut back to graphics/documents; to stay on the same footage, start a new `clip` scene with a later `from`. The `label` is ALWAYS set ("SOURCE: DOJ PRESS CONFERENCE · NOV 20, 2026"), and every source goes in the description. Clips are muted under narration by default. `audio:true` plays the original audio and ducks narration and music: use it only for a short named quote (≤ 15 s, speaker named in the label, a `pause` on the line to make room). How it works: stage.html draws a green key frame plus the label, and `pipeline/clips.py` (run by make.sh after render.js) keys in the real clip (long = fill-crop; Shorts = blurred fill + 16:9 band). A missing file logs `WARNING clip missing` and leaves a dark frame with the label, so check the log and the contact sheet.
- Variety: no more than 3 `quote` scenes in a row; every chapter needs at least one real document (`doc`).
- Shorts → `make_shorts.py` → `short1.json … short4.json` (4 candidates, 2 days): each `{title, hook: "two|lines", lines:[...]}`, 55–90 words (20–40 s), 6–8 lines, one angle each (the confession, the warnings, where the money went, the sentence math, the victims, the aftermath…), last line = `end`. Shorts title ≤ 60 chars + #shorts (hook rules above).
- `meta.json` (title ≤ 100 chars, summary, tags, sources) and `thumb2.json` (v3 formats A/B/C, v2 rule 3; make.sh uses it when present). Legacy `thumb.json` (A + C: 1–2 words, one gold accent word, hook plate ≤ 5 words, document crop; bottom-right corner empty) only as a fallback.

## 5. MANDATORY independent fact-check
Launch a separate agent (did not write the script) to verify every spoken line, subtitle and on-screen text of episode.json AND all short*.json against sources (it writes `factcheck.md`). Apply every FIX before the final build. 001's check is the model.

## 6. Build
Every `make.sh` build (this one, voice step 1, any re-encode or Shorts-only rebuild) takes ~45–60 min on 2 cores. Start it in the background with a log and a pid file, then wait ONLY with `tools/waitfor.sh` (one call blocks up to 9 min and prints just DONE/EXITED/WAITING + the last 3 log lines):
```bash
cd /home/claude/sworn_media/pipeline && W=/home/claude/work/NNN && mkdir -p $W && \
  nohup bash -c "LONG_MAX_MB=450 LONG_CRF=18 ./make.sh ../episodes/NNN-slug $W all; echo EXIT \$?" > $W/build.log 2>&1 & echo $! > $W/build.pid
bash /home/claude/sworn_media/tools/waitfor.sh $W/build.log "^EXIT [0-9]+|Traceback|Error:" 540 $(cat $W/build.pid)   # repeat while it prints WAITING
grep -E "^EXIT|mp4 [0-9.]+s|I:|Traceback|Error" $W/build.log | tail -n 20   # summary only
```
`EXIT 0` = success (make.sh prints one `<file>.mp4 <sec>s <MB>MB` line + the loudness `I:` line per video at the end). `EXIT` ≠ 0, `Traceback` or `Error:` = failure → read only the relevant part (`grep -n -B3 -A10 Traceback $W/build.log | head -40`). Never `cat`/`tail -f` the full log, never poll it with sleep loops, and print only summaries.
For quick looks: `node render.js <workdir> <episode_dir> <prefix> 1 t1,t2,...` renders single frames.
QA (do not skip): open `out/contact_long.jpg` and every `contact_sN.jpg` — nothing cut off or overlapping, highlights on the right lines, no seals, no empty cards; loudness ≈ −14 LUFS (make.sh prints it); long ≥ 10:00 and ≤ 450 MB; Shorts 20–40 s (hard cap 50 s). Thumbnails: check at 168×94 that the big word reads.

## 7. Host (public URLs for Metricool)
**Long video → Google Drive (owner 2026-11-23; no more squeezing to 95 MB).** Metricool's YouTube limit is 500 MB, so the long encodes to ≤ 450 MB (§6):
```bash
python3 /home/claude/sworn_media/tools/drive_upload.py $W/out/long.mp4 --folder "SWORN" --creds /tmp/drive_creds.json   # prints {"id","link","direct",...}
```
Use `direct` as the long video's Metricool media. If Metricool rejects it as too big: re-encode to ≤ 300 MB (`LONG_MAX_MB=300 ./make.sh … long`, or rerun only the capped ffmpeg pass), upload again; still rejected → ≤ 95 MB and host it on the drop branch as before.
**Shorts and thumbnails → GitHub drop branch (unchanged):**
Branch = weekday of the ET date the files publish on (`drop-mon` … `drop-sun`). A LONG run makes two drops: drop-<T> = thumb_A, thumb_C + T's Shorts; drop-<T+1> = T+1's Shorts only. Commit main changes first (the `checkout -qf main` below discards uncommitted edits). Orphan commit with ONLY that day's files, force-push (FILES = that day's files, e.g. `thumb_A.jpg thumb_C.jpg s1.mp4 s3.mp4`):
```bash
cd /home/claude/sworn_media && git checkout -q --orphan up && git rm -rqf . && for f in $FILES; do cp $W/out/$f .; done && \
git add $FILES && git -c user.name="SWORN bot" -c user.email="ituraev97@users.noreply.github.com" commit -qm "drop NNN" && \
git push -qf origin up:drop-XXX && git checkout -qf main && git branch -D up
```
Check every `https://raw.githubusercontent.com/ituraev97/sworn_media/drop-XXX/<file>` with `curl -sI` → 200. Never put video on main.

## 8. Schedule in Metricool (createScheduledPost, blogId 7806713, autoPublish true, providers [{"network":"youtube"}], publicationDate timezone America/New_York)
- Long 12:00 on T: text = `out/youtube_description.txt` (must be < 5,000 characters, `wc -m`; trim the source list first); youtubeData {title, type "video", privacy "public", madeForKids false, category "EDUCATION", tags}; media [Drive `direct` URL of long.mp4]; videoThumbnailUrl = thumb_A URL (if rejected, retry once without it).
- Shorts: only candidates that passed the scorecard, ≤ 2 per day for T and T+1 ("Long-video cadence"): T 10:00 = best non-trailer, T 18:00 = trailer for the long, T+1 10:00/18:00 = next best (the rest are not scheduled): type "short", title from the short json, text = 1–2 lines + "Full case on the channel." + "#truecrime #courtcase #shorts", madeForKids false, category EDUCATION.

## 9. Close
- After scheduling: `python3 /home/claude/sworn_media/tools/drive_upload.py --cleanup-days 7 --folder "SWORN" --creds /tmp/drive_creds.json` (deletes our Drive uploads older than 7 days).
- Commit to main: episode folder (spec scripts, json, img/, sources.md, factcheck.md — no video), `backlog.md` row → `done YYYY-MM-DD`. fetch/rebase before push.
- Report to the owner in Russian (SendUserMessage): case + title, publish date and times (ET and Tashkent = ET+10 in winter / +9 in summer), Metricool plannerUrls, fact-check result (how many fixes), Shorts scorecard (each candidate's score, which were scheduled for which day and why), anything skipped; SendUserFile thumb_A.

## Proven format — owner decision 2026-11-23 (best SWORN video so far)
"Backward Hat Capital: 2 Founders…" (thumbnail "WHERE DID $600M GO?" + court-document excerpt, 13:54): CTR 8.7 % (channel norm ~2–4 %), average view 6:03 = 43 %, but only 578 impressions — mostly search traffic, because the channel's other long videos earn too few views for YouTube to widen browse impressions. So:
- Prefer fresh money cases that support a money question: thumbnail format B ("WHERE DID $X GO?" / "WHO TOOK $X?") + a real document excerpt with the dollar figure highlighted; the title opens with the names + the amount.
- Keep 12–15 min with a re-hook every ~2 min; open on the money question, answer it in the last chapter.
- Every Short of an episode ends with "Full case on the channel" and the run report reminds the owner to set the Short's "Related video" to the long (Studio only).
- Never publish a weak long video just to fill a day — one strong long every 2 days beats daily filler.

## Performance rules
Weekly review (Mondays, Asia/Tashkent). Each rule is backed by ≥ 3 of our own videos (Metricool YTVP, last 28 days). Owner content rules, schedule and AI-label settings are NOT changed here — only recommended in the report.
1. **Fresh cases beat history recaps.** Shorts on v2 fresh-case days (Nov 14–20, 21 Shorts) median 16 views vs 4 for old-case Shorts (Nov 2–13, 45 Shorts); long videos median 12 (6) vs 7 (11). Fresh first; backlog only as fallback.
2. **Convicted / pleaded beats charged-only.** Shorts on verdict/plea/sentence days (Milton, Link, Chen, Belfort, Earl Thomas; 15 Shorts) median 44 views vs charged-only days (Rozier, Backward Hat; 6 Shorts) median 9. Prefer a case with a court finding; a charged-only case needs a famous name to compete.
3. **A recognisable name + a dollar figure wins Shorts.** Top 4 Shorts of the month: "$12.8M of $110M … The Wolf's Restitution" 537, "$1.5M–$3M Stolen From Earl Thomas" 414, "3,716 Grams and $228,000 Cash: … Earl Thomas" 185, "$240 Million Cattle Scheme. FBI Fugitive Caught at LAX." 123.
4. **Number-first Shorts openers.** Titles/hooks opening with "$" or a digit: median 10.5 views (22 Shorts) vs a verbatim quote 8 (21) vs anything else 5 (23).
5. **Long titles ≤ 66 characters.** Long videos with titles ≤ 66 chars: median 12 views (10 videos, e.g. Chen 42, Backward Hat 34, Ponzi ranking 45); > 66 chars: median 3 (7 videos, e.g. Fyre 1, Madoff 2, SBF 2). Keep "Name + what happened" short.
6. **Fresh documented cases hold long-video viewers 3–4 minutes.** Average view duration: Link 263 s, Earl Thomas 256 s, Backward Hat 231 s, Milton 177 s vs old recaps Madoff 4 s, SBF 11 s, Fyre 29 s, Holmes 18 s. Keep the document-led, fresh-news format.
7. **10:00 ET is the strongest Shorts slot in v2 (supports the 2026-11-23 schedule).** Nov 14–20: 10:00 ET median 66 views (7 Shorts: 537, 414, 123, 66 …) vs 14:00 ET 23 (7) vs 18:00 ET 12 (7). Put the highest-scoring Short at 10:00.
8. **Thumbnails: no data yet.** Custom thumbnails still fail to upload (channel not phone-verified), so A/B/C formats cannot be compared from Metricool; ask the owner for the YouTube Studio Test & Compare result.

Changelog:
- 2026-11-09: section created (first weekly review; 10 Shorts with data, 0 long videos with data).
- 2026-11-16: rewritten (9 long videos + 44 Shorts with data, Nov 2–11). Old rule "quote/number openers win" dropped (no longer supported: median 3 vs 4); added name-first case choice, ≤ 60-char long titles, "Explained"/ranking framing, slot observation.
- 2026-11-23: rewritten (17 long videos + 66 Shorts with data, Oct 26 – Nov 20; Metricool rows end Nov 20). Added fresh-vs-history, convicted-vs-charged, number-first openers (now supported: 10.5 vs 8 vs 5), long-video watch time, 10:00 ET slot; title limit set to ≤ 66 chars from data; "Explained" framing dropped (only 2 videos since); thumbnails still unmeasurable.


## Lessons from past runs (distilled 2026-11-23)
Distilled from the run notes of runs 002–023 (full text: RUNBOOK_NOTES.md). Each still applies to every run.
- justice.gov from the shell: `/archive/...` pages and PDFs, `/usao-<d>/media/<id>/dl?inline`, `/usao-<d>/page/file/<n>/dl` and `/sites/default/files/...` download; `/usao-*/pr/` and `/archives/opa/pr/` return a bot challenge — never bypass it; read listings and release pages with Playwright (`/news?page=0`, `/usao-<d>/news`, single releases) or WebFetch (`/news/press-releases` page 1).
- Blocked from the shell: sec.gov, govinfo, courtlistener (incl. storage), findlaw, loc.gov, fbi.gov (Cloudflare — never bypass), ic3.gov, wikipedia.org, some local outlets → use WebFetch or a web-fetch agent. WebFetch calls that need approval time out unattended (bop.gov, yahoo, some justice.gov) → use Playwright or try them early.
- Court filings: RECAP mirror on archive.org — `advancedsearch.php?q=<name>+AND+collection%3Ausfederalcourts&fl[]=identifier&output=json` → `archive.org/metadata/<id>` → `archive.org/download/<id>/<id>.<entry>.0.pdf`; the docket JSON often stops early, so list PDFs from metadata; download in parallel (`xargs -P 8 curl`); on HTTP 500 retry the redirected `dnNNN.ca.archive.org/0/items/...` URL.
- Supreme Court: case files `micro_IA…` (`q=<name>+AND+mediatype:texts`) and DocumentCloud mirrors of SG briefs / joint appendix (`q=<docket no.>`); U.S. Reports pages via `<id>_jp2.zip/<id>_jp2%2F<id>_0NNN.jp2`; opinions from supreme.justia.com; supremecourt.gov PDFs only via WebFetch "quote exactly the sentence containing X".
- Old cases thin on RECAP: try appellate briefs (`gov.uscourts.ca5.<no>` etc.), post-judgment collection dockets, cert-stage items and DOJ Corporate Fraud Task Force reports (justice.gov/archive/dag/cftf/).
- Show as document images only government/court-authored pages (DOJ filings, opinions, orders, judgments, SG briefs, court-authored JA pages, CRS sidebars); quote — never show — reporter transcripts, defense filings/petitions, private-party exhibits (e-mails, texts, letters, victim statements, contracts), juror materials, press clippings.
- Black out private names (victims, investors, uncharged relatives) and personal contact data on every document image and thumbnail; crop out uncharged abuse allegations and never narrate them.
- Seals/logos: DOJ letterhead seal top-left → start the crop at 11.5–15% of page height (or paint it white); CRS/LoC logo → ≥ 20%; paint the FBI seal out of wanted posters.
- Web releases as documents: re-typeset the text as a text-only page/PDF (009 `shot.py`, 015 `make_img.py`); never print the live justice.gov DOM to PDF (clips the body) or render it with its external CSS (hangs).
- Highlight boxes: from `pdftotext -bbox` (text layer) or tesseract TSV (scans) — start from the latest `episodes/0NN/make_img.py` (handles OCR splits, pleading-paper margin numbers, ECF headers); check that each line's `hl` points at that line's paragraph and stays inside the frame (003 `panfix.py`).
- Lawful images hide inside DOJ/court PDFs (wanted posters, sentencing slides, FBI photos in indictments, trial exhibits): extract with `pdfimages -j`, inspect every image by eye, caption only what the document says and name no one the paragraph doesn't.
- Never enlarge a face < 500 px (use it at native size or go without a face). Wikimedia: fetch the face early; on upload.wikimedia.org 429 request the 1280px `/thumb/.../1280px-<name>` rendition.
- No lawful face → thumbnails = question panel + re-typeset verbatim excerpt cards (zoomcard.js) labelled "RE-TYPESET FROM <source>", amounts labelled as the source labels them, trailing ellipses on cut excerpts, no stamps on text cards.
- Scene limits: `big` ≤ 3 rendered lines (Shorts ≤ ~14 characters per line); `verdict.big` ≤ ~22 characters; a `quote` line needs ≥ ~2 s of speech. Verify with single-frame renders (render each test time twice, use the second).
- Shorts hook with a small/portrait face: build a 1080×1920 hook image (eyes at y ≈ 430, blurred fill; 016 `make_hookimg.py`), zoom 1.3334, pos "50% 0%"; the hook scene is copied into timeline.json — patch it there or rerun timeline.py before a re-render.
- Shorts length: 65–80 words ≈ 28–33 s at 1.15; ≥ 84 words risks > 35 s — check durations in the make.sh summary.
- Fix one bad block by rendering that segment and overlaying it (`overlay=enable='between(t,a,b)'`), then re-encode at a capped bitrate (an uncapped CRF overlay pass bloats the file).
- If the long ever falls back to a drop branch, push Shorts/thumbs first and the long in a second push (one ~130 MB push → HTTP 500).
- Custody status: BOP locator via WebFetch (`bop.gov/PublicInfo/execute/inmateloc?todo=query&output=json&inmateNum=<reg>`); an "actual release date" alone can mean death in custody — need a second source before saying "released".
- Research quota: the YouTube Data API key is shared and can hit 429 early → fall back to WebSearch; `api.fbi.gov/wanted/v1/list?field_offices=<office>` gives wanted-poster metadata.
- Fact-check pattern: allegations (complaints, indictments, SEC/DOJ claims, defense claims) carry "alleged / prosecutors say / the indictment says" on every line incl. titles, thumbnails, tags and Shorts; facts stipulated in a plea or factual resume may be stated as fact.
- Fact-check pattern: quotes are verbatim with every omission marked, never cut so the meaning changes, attributed to the right speaker, hearing and date, and quotes-within-quotes say so ("as quoted in", "according to the government").
- Fact-check pattern: spoken numbers match subtitles; job titles match the date; places come from an official record; counts of conviction named by number; co-defendant status "as of <date>"; contested facts attributed everywhere; no narrator verdicts or unsourced superlatives.
- Re-run the fact-check after inserting or moving lines (back-references break).

## Thumbnails v5 — illustrated cut-out from REAL images (owner decision 2026-11-23)
Owner: "bright and illustrated-looking, like the top drama channels — but faces must not be distorted". This section overrides the **thumb_A** part of the earlier thumbnail rules; thumb_B and thumb_C keep the current generator, so YouTube Studio → Test & Compare measures the new style against the old one. All earlier content rules stay in force: lawful image sources, every word true and sourced, fact-check of the thumbnail text, no gore, no victims' faces under crime words, bottom-right corner empty.

- Tool: `tools/thumbkit/thumbkit.py` (header = full spec). Setup once per run: `pip install -q pillow numpy opencv-python-headless "rembg[cpu]"` (downloads a 176 MB cut-out model on first use; if that fails the tool still works with a soft oval mask — say so in the report).
- It cuts the subject out of a real photo or video frame, adds a white sticker outline, a coloured glow and a rim light, washes the background in colour and sets 2–3 huge Anton words + an optional yellow sticker. Only pixel filters — no AI redraw, faces stay exactly as photographed. NEVER feed it an AI-generated image of a real person.
- Spec (`<ep>/thumbkit.json`, a list → thumb.jpg, thumb_B.jpg… — for this channel set "out":"thumb_A.jpg"):
  `[{"out":"thumb_A.jpg","layout":"solo","people":[{"src":"photo_or_clip","t":12.4,"crop":[x,y,w,h],"tint":"warm","kind":"person"}],"line1":"$250M","line2":"VANISHED","sticker":"SMALL FACT","brand":{"accent":"<channel colour>","sticker":"#FFD400","border":false}}]`
  - `layout`: "solo" (subject right, words left) or "versus" (two REAL sides of the same dispute, words centre — never pair people who are not part of the same story).
  - `kind`: "person" or "object" (boat, drug bundle, document, product, building, aircraft…).
  - `crop`: generous box around head + shoulders (face ≈ 35–50 % of its height) in source pixels; the subject must be ≥ 360 px tall in the source (the tool warns otherwise — find a bigger image).
  - `tint`: warm | cold | toxic | gold. `brand.accent` = the channel's main colour from the current generator.
- After rendering, LOOK at thumb_A at 320 px wide: words readable, face not covered, outline clean (no chunks of background). If the cut-out is bad (busy background, hands lost), use the current generator for A and say so in the report.

## Thumbnails v6 — YouTube-AI style: AI picture + real text/documents (owner decision 2026-11-23)
Owner: "make them like the thumbnails YouTube Studio's AI draws — bright, illustrated, with brands". This section overrides the **thumb_A and thumb_B** parts of the earlier thumbnail rules; thumb_C keeps the current generator, so YouTube Studio → Test & Compare measures the new style. Earlier content rules stay: lawful image sources, every word true and sourced, fact-check of thumbnail text, no gore, no victims' faces under crime words, bottom-right corner empty.

0. **EMOTION FIRST (owner 2026-11-24):** every thumbnail must show a strong emotion at first glance (rage, shock, fear, disbelief) — never a calm or smiling face. Pick the PEAK real frame/photo, let the AI dramatize light/smoke/contrast while keeping the exact face and expression; if no emotional real frame exists, put the emotion into the scene (fire, sirens, red stamp). Details: STYLE.md "EMOTION FIRST".
1. Read `tools/thumbkit/STYLE.md` — templates learned from YouTube's own AI thumbnails: doc (documentary split), evidence/fraud (object + real document + stamp), ntsb (full-bleed reconstruction + telemetry HUD + red circle), mugshot (real face + seized items, soft seam), versus, solo. Pick the template that fits this channel's examples.
2. AI pictures (free, FLUX.2 klein on the owner's office PC) via Drive "IMG RELAY" — request EARLY in the run (≈ 12 min per picture, longer while the PC voices — at most 3 pictures per run):
   `python3 tools/img_client.py request <ID> plates.json --creds /tmp/drive_creds.json` then later `python3 tools/img_client.py wait <ID> <ep>/plates --creds /tmp/drive_creds.json --timeout 2400`.
   plates.json = `[{"name":"plate_A.png","prompt":"cinematic photo of ..., dramatic side light, dark background, high detail","w":1280,"h":720,"seed":1}, ...]` (max 6). The AI paints ONLY pictures — NEVER ask it for text, documents, logos-as-evidence. Real people: send their REAL lawful photo as `"ref"` (edit mode: "same person, same expression, re-lit with red and blue police lights, sharp, cinematic") — never generate a real person from text.
   No answer in time → build A/B with real frames (thumbkit solo/versus) and say so in the report.
3. Compose with `tools/thumbkit/thumbkit.py <ep>/thumbkit.json` (setup: `pip install -q pillow numpy opencv-python-headless "rembg[cpu]"`; header lists every layout and overlay: tag, ribbon, hud, circle, path, stamp, bignum, pill, label, band). Text, numbers, stamps and the REAL document crop are drawn by thumbkit — documents come only from the real source (PDF page → `doc`, `highlights` boxes in its pixels).
4. LOOK at every thumb at full size and at 320 px: AI picture has no garbage text/extra fingers/melted objects, faces unchanged, words readable. Bad picture → new seed/prompt (one retry), otherwise fall back to the real-frame layout.
