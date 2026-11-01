# SWORN — daily production runbook

One run = one long episode (10–13 min, 1920×1080) + **6** vertical Shorts (35–60 s, 1080×1920), all about ONE court case, hosted here and scheduled in Metricool for ONE US day.
Reference episode: `episodes/001-madoff/` (make_spec.py → episode.json, make_shorts.py → short1–6.json, meta.json, thumb.json, factcheck.md). Read it before writing anything.

## 0. Context
- Channel bible: Projects doc `claude/sworn-bible.md` (project "AI YOUTUBE"). Brand book: Design System artifact "SWORN".
- YouTube channel: SWORN (UCNoMjeEPiut8OgSGl0Y-WJg). Metricool brand **SWORN, blogId 7806713**. Publish timezone **America/New_York**.
- Schedule per US day (ET): Shorts **08:00, 10:00, 14:00, 16:00, 18:00, 20:00**; long episode **12:00**.
- Owner decisions: voice **B** = Kokoro `am_michael` + SWORN processing (built into `pipeline/tts.py`; long speed 0.98, Shorts 1.05). Do NOT set isAiGeneratedContent (graphics + real documents + synthetic narrator; the description says "Narration uses a synthetic voice").

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
- Call Metricool getScheduledPosts (blogId 7806713, timezone America/New_York) for the next 3 days. Target = the EARLIEST ET date that is at least tomorrow and has no YouTube long video (type video). If tomorrow and the day after are both taken, stop and report.
- Case = first `todo` row of `backlog.md`. Mark it `in progress` immediately (commit+push to main) so parallel runs don't take it.
- Only cases with a verdict/sentence (or a decided Supreme Court case). Focus: fraud, financial crime, white-collar, scams, landmark Supreme Court decisions. Never: crimes against children, sexual crimes, gore. Pardons, reversals, reduced sentences must be told.
- Rotate formats: THE VERDICT (one case, crime → sentence), THE PAPER TRAIL (how a fraud was uncovered), THE ARGUMENT (Supreme Court case; real argument audio only if a public-domain source is reachable).

## 3. Sources and research (facts decide everything)
- Primary first: justice.gov press releases and charging documents (PDFs download fine with curl from the shell: `/archive/usao/<district>/pressreleases/...` and `/usao-<district>/pr/...`), court opinions, SEC/FTC/FBI releases and complaints, supremecourt.gov. Then AP/Reuters/major outlets. WebFetch for pages the shell can't reach (sec.gov from shell is blocked; WebFetch works).
- Every number, date, name and quote must come from a page you opened → `episodes/NNN-slug/sources.md` (claim → URL).
- **Images = only U.S. government documents** (rasterize the PDF with `pdftoppm -r 220`, crop with PIL, save JPG in `episodes/NNN-slug/img/`). Crop OUT agency seals and logos. No photos of people unless public domain AND clearly licensed. Never: Court TV / Law&Crime / TV footage, AI images of real people, mugshots of acquitted people.
- Quotes on screen (`quote` scenes, `q`) must be verbatim (ellipsis allowed). If it's a reporter's or prosecutors' quotation, the cite says so ("As quoted in …").
- Charged-but-not-convicted people: "charged", "alleged", "prosecutors say". Private victims: no names.

## 4. Script → `episodes/NNN-slug/make_spec.py` → `episode.json`
- Copy the structure of 001. Each line = `{"say": spoken text (numbers as words), "show": subtitle text (digits), "scene": {...}}`; a line without `scene` continues the previous scene.
- 1,350–1,500 words → 10–11 min at speed 0.98. Cold open (≤45 s, the strongest verified moment) → `title` → 5–6 `chapter`s → closing line → `end`.
- Scene types (see `pipeline/stage.html`): `title{kicker,title,sub}`, `chapter{n,title}`, `doc{img,pan:[from,to],hl:[x,y,w,h],kicker,title,note,src}` (real document scan; hl = gold highlight box in image fractions), `quote{q,case,doc,cite,size,recreated}`, `big{kicker,lines:[...], src}` ("|" = line break; the last line turns gold and appears on the next spoken line), `stat{kicker,value,label,src}`, `bars{kicker,title,items:[{label,value,display}],src}`, `list{kicker,items:[[n,label]],src}`, `timeline{kicker,events:[{date,text}],at,src}`, `verdict{kicker,stamp,big,sub,neutral}` (the ONLY place for red; `neutral:true` for NOT GUILTY / dismissed), `end{}`.
- Variety: no more than 3 `quote` scenes in a row; every chapter needs at least one real document (`doc`).
- Shorts → `make_shorts.py` → `short1.json … short6.json`: each `{title, hook: "two|lines", lines:[...]}`, 80–110 words, 6–8 lines, one angle each (the confession, the warnings, where the money went, the sentence math, the victims, the aftermath…), last line = `end`. Shorts title ≤ 90 chars.
- `meta.json` (title ≤ 100 chars, summary, tags, sources) and `thumb.json` (A + C: 1–2 words, one gold accent word, hook plate ≤ 5 words, document crop; C may carry a stamp; bottom-right corner stays empty).

## 5. MANDATORY independent fact-check
Launch a separate agent (did not write the script) to verify every spoken line, subtitle and on-screen text of episode.json AND all short*.json against sources (it writes `factcheck.md`). Apply every FIX before the final build. 001's check is the model.

## 6. Build
```bash
cd /home/claude/sworn_media/pipeline && ./make.sh ../episodes/NNN-slug /home/claude/work/NNN all   # ~45–60 min on 2 cores; run with nohup and poll
```
For quick looks: `node render.js <workdir> <episode_dir> <prefix> 1 t1,t2,...` renders single frames.
QA (do not skip): open `out/contact_long.jpg` and every `contact_sN.jpg` — nothing cut off or overlapping, highlights on the right lines, no seals, no empty cards; loudness ≈ −14 LUFS (make.sh prints it); long ≥ 10:00 and < 95 MB; Shorts 30–60 s. Thumbnails: check at 168×94 that the big word reads.

## 7. Host on GitHub (public raw URLs for Metricool)
Branch = weekday of the ET target date (`drop-mon` … `drop-sun`). Orphan commit with ONLY that day's files, force-push:
```bash
cd /home/claude/sworn_media && git checkout -q --orphan up && git rm -rqf . && cp $W/out/long.mp4 $W/out/thumb_A.jpg $W/out/thumb_C.jpg $W/out/s[1-6].mp4 . && \
git add long.mp4 thumb_A.jpg thumb_C.jpg s*.mp4 && git -c user.name="SWORN bot" -c user.email="ituraev97@users.noreply.github.com" commit -qm "drop NNN" && \
git push -qf origin up:drop-XXX && git checkout -qf main && git branch -D up
```
Check every `https://raw.githubusercontent.com/ituraev97/sworn_media/drop-XXX/<file>` with `curl -sI` → 200. Never put video on main.

## 8. Schedule in Metricool (createScheduledPost, blogId 7806713, autoPublish true, providers [{"network":"youtube"}], publicationDate timezone America/New_York)
- Long 12:00: text = `out/youtube_description.txt`; youtubeData {title, type "video", privacy "public", madeForKids false, category "EDUCATION", tags}; media [long.mp4 URL]; videoThumbnailUrl = thumb_A URL (if rejected, retry once without it).
- Shorts 08:00, 10:00, 14:00, 16:00, 18:00, 20:00 (s1…s6 in that order): type "short", title from the short json, text = 1–2 lines + "Full case on the channel." + "#truecrime #courtcase #shorts", madeForKids false, category EDUCATION.

## 9. Close
- Commit to main: episode folder (spec scripts, json, img/, sources.md, factcheck.md — no video), `backlog.md` row → `done YYYY-MM-DD`. fetch/rebase before push.
- Report to the owner in Russian (SendUserMessage): case + title, publish date and times (ET and Tashkent = ET+10 in winter / +9 in summer), Metricool plannerUrls, fact-check result (how many fixes), anything skipped; SendUserFile thumb_A.
