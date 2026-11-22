# SWORN — daily production runbook

One run = one long episode (10–13 min, ≥ 10:00, 1920×1080) + **3** vertical Shorts (25–40 s, 1080×1920; owner rule 2026-11-06), all about ONE court case, hosted here and scheduled in Metricool for ONE US day.
Reference episode: `episodes/001-madoff/` (make_spec.py → episode.json, make_shorts.py → short1–6.json, meta.json, thumb.json, factcheck.md). Read it before writing anything.

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

## ⚡ v2 rules (owner-approved 2026-11-14). These override older sections where they conflict
Why: channel analytics showed Shorts lose viewers in 1–2 s and long videos have no thumbnails. YouTube Studio "Inspiration" for our niche (court/true-crime news) shows that winning videos have a **big emotional face**, few words, a fresh news peg, and a title built as "name + what happened". Holmes/Balwani/Theranos items are in that feed.

**Blocker:** custom thumbnails fail ("Could not upload video thumbnail") until the owner's sister phone-verifies the channel at youtube.com/verify. Keep generating thumbnails anyway and report the blocker in every run summary until uploads succeed.

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
5. **Shorts v2 (20–35 s, 3/day):**
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
- Schedule per US day (ET): Shorts **10:00, 14:00, 18:00** (s1–s3); long episode **12:00** (owner rule 2026-11-06; was 6 Shorts).
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
- **Footage:** relay clips (see "Real footage via relay") alongside the documents, Wikimedia Commons, DVIDS and government photos below.
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
cd /home/claude/sworn_media/pipeline && LONG_MAX_MB=450 LONG_CRF=18 ./make.sh ../episodes/NNN-slug /home/claude/work/NNN all   # ~45–60 min on 2 cores; run with nohup and poll
```
For quick looks: `node render.js <workdir> <episode_dir> <prefix> 1 t1,t2,...` renders single frames.
QA (do not skip): open `out/contact_long.jpg` and every `contact_sN.jpg` — nothing cut off or overlapping, highlights on the right lines, no seals, no empty cards; loudness ≈ −14 LUFS (make.sh prints it); long ≥ 10:00 and ≤ 450 MB; Shorts 30–60 s. Thumbnails: check at 168×94 that the big word reads.

## 7. Host (public URLs for Metricool)
**Long video → Google Drive (owner 2026-11-23; no more squeezing to 95 MB).** Metricool's YouTube limit is 500 MB, so the long encodes to ≤ 450 MB (§6):
```bash
python3 /home/claude/sworn_media/tools/drive_upload.py $W/out/long.mp4 --folder "SWORN" --creds /tmp/drive_creds.json   # prints {"id","link","direct",...}
```
Use `direct` as the long video's Metricool media. If Metricool rejects it as too big: re-encode to ≤ 300 MB (`LONG_MAX_MB=300 ./make.sh … long`, or rerun only the capped ffmpeg pass), upload again; still rejected → ≤ 95 MB and host it on the drop branch as before.
**Shorts and thumbnails → GitHub drop branch (unchanged):**
Branch = weekday of the ET target date (`drop-mon` … `drop-sun`). Orphan commit with ONLY that day's files, force-push:
```bash
cd /home/claude/sworn_media && git checkout -q --orphan up && git rm -rqf . && cp $W/out/thumb_A.jpg $W/out/thumb_C.jpg $W/out/s[1-3].mp4 . && \
git add thumb_A.jpg thumb_C.jpg s*.mp4 && git -c user.name="SWORN bot" -c user.email="ituraev97@users.noreply.github.com" commit -qm "drop NNN" && \
git push -qf origin up:drop-XXX && git checkout -qf main && git branch -D up
```
Check every `https://raw.githubusercontent.com/ituraev97/sworn_media/drop-XXX/<file>` with `curl -sI` → 200. Never put video on main.

## 8. Schedule in Metricool (createScheduledPost, blogId 7806713, autoPublish true, providers [{"network":"youtube"}], publicationDate timezone America/New_York)
- Long 12:00: text = `out/youtube_description.txt`; youtubeData {title, type "video", privacy "public", madeForKids false, category "EDUCATION", tags}; media [Drive `direct` URL of long.mp4]; videoThumbnailUrl = thumb_A URL (if rejected, retry once without it).
- Shorts 10:00, 14:00, 18:00 (s1…s3 in that order): type "short", title from the short json, text = 1–2 lines + "Full case on the channel." + "#truecrime #courtcase #shorts", madeForKids false, category EDUCATION.

## 9. Close
- After scheduling: `python3 /home/claude/sworn_media/tools/drive_upload.py --cleanup-days 7 --folder "SWORN" --creds /tmp/drive_creds.json` (deletes our Drive uploads older than 7 days).
- Commit to main: episode folder (spec scripts, json, img/, sources.md, factcheck.md — no video), `backlog.md` row → `done YYYY-MM-DD`. fetch/rebase before push.
- Report to the owner in Russian (SendUserMessage): case + title, publish date and times (ET and Tashkent = ET+10 in winter / +9 in summer), Metricool plannerUrls, fact-check result (how many fixes), anything skipped; SendUserFile thumb_A.

## Performance rules
Weekly review (Mondays, Asia/Tashkent). Each rule is backed by ≥ 3 of our own videos (Metricool YTVP, last 28 days). Owner content rules, schedule and AI-label settings are NOT changed here — only recommended in the report.
1. **A household name beats everything else.** Shorts median views by case-day: Holmes 18 (5 Shorts), SBF/FTX 7.5 (6), Madoff 4.5 (6), Stanford 4.5 (6), WorldCom 4 (6), Fyre 2 (6). The 3 best Shorts of the month (197, 97, 22 views) were all on SBF/Stanford/Holmes days. Pick the case with the most recognisable face/name first.
2. **Long titles ≤ 60 characters.** Long videos with titles ≤ 60 chars: 30, 21, 4 views (median 21; Enron "Explained", Ponzi ranking, Gideon "Explained"). Titles > 70 chars: 6, 4, 2, 1, 1, 1 (median 1.5; Holmes, Stanford, WorldCom, Fyre, SBF, Madoff). Keep the owner's "Name + what happened" formula but cut it to ≤ 60.
3. **"Explained" / ranking framing held viewers longest on long videos:** average view duration 210 s (ranking), 87 s (Enron Explained), 52 s (Gideon Explained) vs 2–49 s for the six "Name: … — the paper trail/verdict" titles. Use "… Explained" or a number-led promise when it fits the facts.
4. **Shorts are lost in the first seconds:** median average view duration 4 s across 44 Shorts (Nov 2–11). Frame 0 must already carry face/document + number, narration from 0.05 s (v2 hook) — no context sentence first.
5. **Opening word alone does not save a Short:** quote/number openers median 3 views (17 Shorts) vs other openers 4 (27). Where/How/Did/The openers 17 Shorts, median 4. Hook + name matter more than the first word; still never repeat an opening word on one day.
6. **Slot (recommendation only, schedule unchanged):** Shorts at 13:00 UTC (8:00 ET, old schedule) median 13.5 views (6) vs 15:00 UTC (10:00 ET) median 2.5 (10), 21:00 UTC 9.5 (6), 23:00 UTC 3 (9). Owner may consider moving the first Short earlier.
7. **No data yet for v2:** Metricool returned no rows for any video published after 2026-11-11 (all v2 episodes 014–015 and their Shorts). Re-check next Monday before changing v2 packaging.

Changelog:
- 2026-11-09: section created (first weekly review; 10 Shorts with data, 0 long videos with data).
- 2026-11-16: rewritten (9 long videos + 44 Shorts with data, Nov 2–11). Old rule "quote/number openers win" dropped (no longer supported: median 3 vs 4); added name-first case choice, ≤ 60-char long titles, "Explained"/ranking framing, slot observation.

## Notes from run 002 (2026-11-02)
- justice.gov `/usao-*/pr/` pages and `press-release/file` downloads now return a bot-challenge page from the shell (do NOT try to bypass); `/usao-sdny/file/NNN/download` and `/archive/` PDFs still work. WebFetch reads most justice.gov pages.
- S.D.N.Y./federal court filings (indictments, judgments, orders, gov't memoranda) are reachable from the shell via the RECAP mirror on archive.org: `https://archive.org/advancedsearch.php?q=<name>+AND+collection%3Ausfederalcourts&fl[]=identifier&output=json`, then `https://archive.org/metadata/<id>` and `https://archive.org/download/<id>/<id>.<doc>.0.pdf`. ca2.uscourts.gov, supremecourt.gov, courtlistener, govinfo are blocked from the shell (WebFetch works for ca2/supremecourt).
- Do not show court-reporter transcripts as document images (reporter may be a private contractor); quote them in quote/big cards instead. Show DOJ filings and court orders/judgments.
- `big` scenes: keep to 3 rendered lines max, or the last line collides with the source line.

## Notes from run 003 (2026-11-03)
- N.D. Cal. RECAP docket JSON on archive.org can stop years early; list the item's PDFs from `archive.org/metadata/<id>`, download the high-numbered ones and read page 1 with pdftotext to find verdict forms, judgments, orders.
- `episodes/003-holmes/panfix.py` keeps every `doc` highlight inside the visible frame (adjusts `pan` from image size); reuse it in make_spec/make_shorts.
- `render.js` test mode can show the first frame of a doc before its image loads (pan looks like 0) — render each test time twice and use the second.
- Shorts `big` scenes: keep each line ≤ ~14 characters or it wraps into the next line.
- Check restitution-order payee tables yourself — later orders can miscount victims.

## Notes from run 004 (2026-11-04)
- S.D. Tex. criminal filings are thin on RECAP; the government's 5th Cir. appellate brief (archive.org `gov.uscourts.ca5.<no>`) has a full statement of facts with record cites — a good DOJ document to show. N.D. Tex. SEC case: `gov.uscourts.txnd.184049`.
- Archived USAO releases (`justice.gov/archive/usao/...html`) download from the shell; render them with Playwright with images and nav hidden (see 004 make_img.py / shots) to show as documents without the seal.
- BOP inmate locator works through WebFetch: `https://www.bop.gov/PublicInfo/execute/inmateloc?todo=query&output=json&inmateNum=<reg>` — use it to check current custody/release (found Lopez released Dec 2024).
- A single push of ~130 MB to a drop branch returned HTTP 500; pushing shorts first and the long in a second commit worked.
- `findy.py` (004) computes highlight boxes from pdftotext -bbox phrases; make_img writes hl.json used by make_spec/make_shorts.

## Notes from run 005 (2026-11-05)
- Episode folders are numbered by release order (005 = backlog row 006); backlog row 005 Miranda was skipped (underlying crime is rape — sexual-crime rule). Prefer Supreme Court cases whose facts are non-violent/non-sexual (e.g. Gideon) for THE ARGUMENT.
- S.D.N.Y. criminal dockets on RECAP are rich: the government sentencing memo, sentencing/plea transcripts, judgment, forfeiture and later letters were all on archive.org. Scanned filings have no text layer: `tfind.py` (005) finds highlight boxes with tesseract TSV on the 220-dpi raster.
- DOJ letters on SDNY letterhead carry the seal at the top-left: start the crop at ~15% of the page.
- Do not show exhibits written by private parties (emails, employee letters, victim statements) as images; quote them "as quoted in" the government memo.
- Fact-checker caught: a "the X never began" vs "set to begin" wording, "she wrote" ambiguity right after a lawyer is mentioned, and on-bail vs. after-revocation chronology. Watch these.
- A BOP inmate-locator WebFetch needed approval in this unattended run and timed out; rely on reporting (NPR) for release dates or try it early.

## Notes from run 006 (2026-11-06)
- No S.D.N.Y. criminal docket on RECAP for 2002–05 cases; the Supreme Court cert-stage item on archive.org (`micro_IA...`, "Opposition Brief.pdf" = Solicitor General's brief; the petition's Appendix = court of appeals opinion and district court orders) is a rich source of showable documents with a text layer. Show only the SG brief and the appendix (court opinions), never the defense petition pages.
- USAO compassionate-release pages publish filings as `justice.gov/usao-sdny/page/file/<n>/dl` (download from the shell); the government's opposition letter can carry the old sentencing transcript as an exhibit (quote it, don't show it).
- DOJ Corporate Fraud Task Force reports (justice.gov/archive/dag/cftf/) are good for 2002–2008 corporate cases.
- `stage.html` quote typing now finishes at ~72% of the block (was 86%): short quote lines showed a half-typed quote. Still keep a quote line ≥ ~2 s of speech (Shorts: put a lead-in in the same line).
- Shell egress is narrow (justice.gov, archive.org, github work; sec.gov, govinfo, courtlistener, findlaw do not) — use WebFetch for text from those.
- The 2026-11-05 long video on Metricool reported "Could not upload video thumbnail" — the channel likely needs phone verification for custom thumbnails.

## Notes from run 007 (2026-11-07)
- Supreme Court cases: archive.org `micro_IA4038…` items carry the printed **Transcript of Record** (state charging paper, minute book, verdict, sentence, state supreme court order, the Court's cert order) and the briefs; United States Reports volumes are on archive.org as `sim_united-states-supreme-court-cases-adjudged_…_<vol>` — the .pdf download returns HTTP 500, but single pages come from `<id>_jp2.zip/<id>_jp2%2F<id>_0NNN.jp2` (leaf from `_page_numbers.json`). loc.gov / tile.loc.gov are blocked from the shell.
- `make_img.py` (007) finds highlight boxes with tesseract on both PDF rasters and jp2 pages; prefix a start phrase with `2:` for its second occurrence.
- Florida state records and Florida AG briefs are public domain (bible); the trial reporter's transcript and the defendant's own petition were quoted, not shown.
- `describe.py` now takes optional `docs_note` and `hashtags` from meta.json (non-federal documents, non-fraud cases).
- 3 Shorts, 70–80 words each at 1.05 ≈ 28–35 s. Templates used: verbatim quote / number reveal / before→after.
- WebFetch of some sites (uscourts.gov podcast page) needs approval and times out unattended; other uscourts.gov, Iowa Law Review and encyclopedia.com pages worked.

## Notes from run 008 (2026-11-08)
- The Supreme Court case file on archive.org (`micro_IA43085015_0478` for Skilling; search `advancedsearch.php?q=<name>+AND+mediatype:texts`) is a full PDF (480 MB, ~1 min download) with a text layer: Fifth Circuit opinion (Pet. App.), Joint Appendix (trial docket with the verdict entry, superseding indictment), and the Solicitor General's merits brief — all showable. `pdftotext -layout` once, split on \f to find pages. Never show the defense petition/briefs, juror materials or press clippings in the same file.
- supremecourt.gov PDFs fail even in WebFetch; supreme.justia.com works (use offset for long opinions). justice.gov `/archives/opa/pr/...` gives a bot challenge from the shell (WebFetch works); `/archive/opa/pr/2006/...html` downloads from the shell.
- Rendering a local justice.gov HTML with Playwright hung (external CSS); skipped the press-release image and used stat/quote cards with the DOJ cite.
- Fact-check caught: a title calling Skilling "CEO" for Jan 2001 (he was President/COO until Feb 2001); "peak" claims not in the source; an unhedged government accounting claim; a Short title implying the Supreme Court cut the sentence. Check job titles against dates.
- Pushing the drop branch: shorts+thumbs first, then the long in a second push, worked (75 MB long).

## Notes from run 009 (2026-11-09)
- First weekly ranking episode ("5 Ponzi Schemes That Ended in 50+ Years in Prison"): reused verified images/sources from 001 and 004 and added three new cases; 1,443 words → 10:31 at 0.98 (1,360 words was only 9:55 — aim ≥ 1,430 words for a 10:00 floor).
- RECAP items: Petters D. Minn. 0:08-cr-00364 = `gov.uscourts.mnd.103973` (FBI affidavit Dkt 26, verdict 361, gov't sentencing 388, judgment 400); Okun E.D. Va. 3:08-cr-132 = `gov.uscourts.vaed.227739` (opinions 155/254/302/324). Rothstein's S.D. Fla. criminal docket is not on RECAP; the archived USAO releases download from the shell.
- `episodes/009-ponzi-50/shot.py` re-renders an archived justice.gov release as plain text (no network, no images/seal, forced 24px Georgia) — readable on screen; the earlier full-page render had tiny text.
- BOP inmate-locator WebFetch timed out once (approval) and worked once in the same run. A record with only an "actual release date" may mean death in custody — do not say "released" without a second source.
- Fact-checker caught: an ambiguous "settled their lawsuit against them" (the firm settled its own clients' suit in the other side's favor), an affidavit phrase that was the cooperating witness's words not the agent's, a thumbnail plate ("THE #1 PONZI SENTENCE") implying an all-time superlative, and back-references broken after inserting lines ("That employee", "He estimated"). Re-run the check after any insertion.

## Notes from run 010 (2026-11-10)
- YouTube Data API returned HTTP 429 "Search Queries per day" on the first call (shared key used up by other channel runs before 07:00 UTC) — fell back to WebSearch; consider running research earlier or giving SWORN its own key.
- E.D.N.Y. criminal docket for Shkreli is on archive.org (`gov.uscourts.nyed.379142`; the docket JSON lists entry numbers; PDFs are `<id>.<entry>.0.pdf`). The judge's Rule 29 order (denial of acquittal) is the best showable summary of trial evidence. FTC v. Vyera (`gov.uscourts.nysd.530855`) docket JSON stops in 2020 but the PDFs go to 2023 (opinion = 865).
- Court opinions name private investors and witnesses: `episodes/010-shkreli/make_img.py` now draws black bars over a list of private names (tesseract TSV) on every document image and the thumbnail. Do this whenever a doc page names victims/investors.
- Fact-checker caught: "the court found" for a Rule 29 summary (use "the judge wrote"), a U.S. Attorney quote that dropped "As alleged", an unsourced "well-known auditor", a witness described as "a physician" who was the company's own R&D head, a bar-chart title that mislabeled total invested money as AUM, and a date mismatch inside an indictment paragraph.
- 1,679 words at 0.98 = 12:33. Short 2 at 90 words was 42.5 s → cut to 80 words (37.9 s). Keep Shorts ≤ 80 words.
- Shorts 0.5 s check: put the quote itself in the hook plate (s3 had "WHAT HE SAID VS. THE RECORD" → changed to the quote).

## Notes from run 011 (2026-11-11)
- Picked a second Theranos episode (Balwani, new backlog row 024) over the rotation's THE ARGUMENT because Mapp v. Ohio measured Low demand and Theranos had the best own case-day (Shorts 22/18/16) plus a fresh peg (cert denied Oct 5, 2026). THE ARGUMENT is due next run.
- RECAP item gov.uscourts.cand.327949 has no Balwani-only filings after his severance (no verdict form, judgment or his sentencing memo). Usable instead: 9th Cir. amended opinion filed as ECF 1802 (page = opinion page), U.S. admin. motion ECF 1811 (verdict/sentence dates, fine), Holmes memo ECF 1643 (lab emails/texts), TSI ECF 469, SEC v. Balwani complaint gov.uscourts.cand.323856 Dkt 1 (allegations — always say "the SEC alleged").
- supremecourt.gov docket HTML (docketfiles/html/public/<no>.html) worked via WebFetch; yahoo and bop.gov needed approval and timed out unattended.
- Court opinions can mention uncharged abuse allegations between co-defendants (ca9 p.16): crop them out of doc images; never narrate them.
- Long video 1,513 words = 11:37; first encode exceeded 95 MB → make.sh re-encode at 855k took ~15 min (static docs look fine). Shorts at 70 words = 34–35 s.
- Fact-checker caught: "former" job titles at sentencing, SEC complaint facts stated without "alleged" (incl. "investors got a binder"), a quote cut so it changed meaning ("one out of four failures of every single test" → "…that we do on this . . . system"), "owed jointly" vs "jointly and severally", linking Count 12 to Arizona ads, an AP quote framed as answering a point AP never connected, and two highlight boxes on the wrong paragraph.

## Notes from run 012 (2026-11-12)
- THE ARGUMENT via a fraud-statute Supreme Court case (Kelly v. United States, "Bridgegate"). Supreme Court merits-stage filings are on archive.org as DocumentCloud mirrors: search `advancedsearch.php?q=<docket no. e.g. 18-1059>` → items like `6562201-Brief-of-respondent-United-States-filed` (SG brief, text layer) and `6433896-Joint-appendix-filed-…` (JA; this one is vol. II only). The archive.org download may 500 on the first try; the redirected `dnNNN.ca.archive.org/0/items/...` URL works.
- supremecourt.gov opinion PDFs: WebFetch refuses full verbatim text but answers "quote exactly the sentence containing X" (≤125 chars each) — enough for verbatim quote cards; give the fact-checker the same method.
- Showable docs here: SG brief (DOJ), court-authored JA pages (jury instructions, jury-communication form with the judge's answer), CRS Legal Sidebars (crop the CRS/LoC logo: start the page-1 crop at ≥ 20% of page height). Exhibits (personal e-mails/texts) and transcripts quoted only.
- Fact-checker caught: words in a government brief that were themselves trial testimony ("create as big a traffic jam as possible" → "according to the government"), "the courts called it a sham" (only the appeals court), "upheld one" vs "upheld convictions", narrator verdict "the jury was right", a Shorts hook implying the Supreme Court reversed all 7 counts (2 were already vacated), a title overstating a figure ("decided the case"), a missing ellipsis where the opinion's sentence continues, and 5 highlight boxes on the wrong paragraph (make_img phrase index ≠ the line's point — check hl index per line).
- 1,472 words at 0.98 = 10:33 (79 MB at CRF 21). Shorts 63–78 words = 29.9–31.4 s.

## Notes from run 013 (2026-11-13)
- Picked Trevor Milton (Nikola, backlog 023) as THE VERDICT: the first three todo rows (Petters, Rajaratnam, Rothstein) measured Low again; the Milton query showed a 69.5k-view outlier Short ("rolling a truck down a hill") and ~15 small, often #ad pro-Milton clip channels but no sourced long documentary.
- RECAP is rich for S.D.N.Y. 21-cr-478: `gov.uscourts.nysd.564175` (278 PDFs incl. the government sentencing memo 315 with a full fact summary, opinions 286/334, judgment 327 (scanned → OCR), restitution letter 361, the pardon itself as Exhibit A to 362, bail order 365) and SEC v. Milton `gov.uscourts.nysd.564121` (complaint, 2025 dismissal). `xargs -P 8 curl` downloaded all 278 in ~1 min.
- Presidential pardon warrants filed as exhibits are federal executive documents — shown (no seal on the page). The USAO letter (361) has the DOJ seal top-left: crop from 11.5% of page height.
- Fact-checker caught (22 fixes): "had written"/"E-MAIL" for an exhibit the memo only introduces as "According to Milton"; SEC allegations narrated as fact; a paraphrase that changed meaning (irate that the commercial didn't make the truck *appear* to drive); "four big categories" was the judge quoting the defense brief; "not guilty on the fourth" (it was Count Two); spoken numbers rounded differently from the subtitle; chronology of the judge's remarks vs. victim letters; "never incarcerated" vs AP "not incarcerated pending appeal"; a Shorts title implying restitution was ordered (only requested); memo page numbers = printed page, not PDF page; 7 highlight bands.
- make.sh output: long 10:58 (1,493 words at 0.98), 78 MB at CRF 21; Shorts 70–83 words = 33.2–34.6 s.
- Checking out main with `git checkout -f` after the orphan drop push discards uncommitted main edits (backlog row) — commit main changes before the drop step, or re-apply.

## Notes from run 014 (2026-11-14)
- First v2 fresh-news run: Agridime cattle fraud (jury verdict Nov 10, 2026, N.D. Tex.). justice.gov `/news` is "Access Denied" in Playwright and robots-blocked for WebFetch page 2; WebFetch of `justice.gov/news/press-releases` (page 1) and `/usao-<district>/pr` works; Playwright works on single USAO release pages and lists attachments (`/usao-ndtx/media/<id>/dl?inline` PDFs download from the shell).
- Lawful face: the FBI wanted-poster PDF attached to a DOJ release contains the photo as an embedded JPEG (`pdfimages -j`). fbi.gov is Cloudflare-blocked from the shell/Playwright (do not bypass); `api.fbi.gov/wanted/v1/list?field_offices=<office>` works for poster metadata (publication date, status). Paint the FBI seal out of the poster (make_img.py does it).
- DOJ verdict releases now carry factual resumes (stipulated facts — quotable without "alleged") and exhibit images (chart/table/photo) — usable as `photo` scenes; caption tables as "released by the U.S. Attorney" unless they carry an exhibit sticker.
- Shorts hook with a portrait (driver-license style) face photo: `zoom 0.85, pos "50% 0%"` keeps the eyes above the giant number; zoom 1.0 hid the eyes behind it. The hook scene is copied into timeline.json — patch it there (or rerun timeline.py) before a re-render.
- Fact-checker caught (16 fixes): "their company" for a brother who did not own it; product description not in the source; SEC "traced" → "alleged"; untagged release tables called "gov't exhibit"; state cease-and-desist scope; an unmarked omission in an e-mail quote; wanted-list duration (FBI record: 27 days, not "more than a month"); "net" purchased vs "bought"; spoken vs subtitle number mismatch; 4 highlight boxes; a tag implying a sentence.
- 1,816 words at 0.98 = 13:15 (77 MB). Shorts 72–81 words at 1.15 = 29–32 s.

## Notes from run 015 (2026-11-15)
- Fresh case with no court PDFs on RECAP (S.D. Cal. 24-cr-1317): the seven USAO S.D. Cal. releases were the documents. Saving innerText with Playwright and re-typesetting it as a text-only PDF (`/home/claude/txt2pdf.js` pattern in episodes/015 make_img.py docstring: no seal/logo/third-party images) → pdftoppm → highlight boxes from `pdftotext -bbox` (exact, no OCR). Printing the live justice.gov DOM to PDF clipped the body at ~2,100 pt — don't.
- In-body release images are listed by `img.currentSrc` after scrolling; `/sites/default/files/2026-11/<name>.png` downloads from the shell. DOJ "Package Videos" sentencing slides carried an ID-style photo of the defendant → usable face (enlarged 9× Lanczos; for thumbnails build a 720×720 panel with the face in the top 540 px and a blurred fill, so the caption doesn't cover the mouth). Trilogy Media screen grabs in the same release are third-party: not used.
- ic3.gov and courtlistener storage are blocked from the shell.
- Fact-checker caught (36 fixes): quote cards labelled with the wrong case (Wang's hearing, the separate $65M ring), "upwards of 18%" shown as "18%", "local police" vs "local law enforcement", a quote's speaker (then-U.S. Attorney Tara McGrath, 2024), "thanked" vs "named", co-defendant sentences in a related case stated as current (add "as of <release date>"), a title implying the courier handled the whole $27M, a line implying seized videos showed the defendant, 7 highlight boxes.
- 1,797 words at 0.98 = 13:24 (83 MB). Shorts 78–82 words at 1.15 = 31.8–33.3 s; 84 words was 35.1 s (over the 35 s cap).

## Notes from run 016 (2026-11-16)
- First CHARGED-only fresh case (Terry Rozier, E.D.N.Y. 25-cr-323): every line attributed ("prosecutors say / the indictment alleges"), the defense's case given its own chapter, tag CHARGED (BREAKING on thumb A only). RECAP items gov.uscourts.nyed.537695 + 537701 (per-defendant copies of the same docket): indictment 17 (text layer), superseding 101 (scanned → tesseract TSV in make_img.py), gov't 144/166, defense 124/128/169 (quoted only), arraignment minute entry 69, M.D. Fla. arrest docket 26.
- Wikimedia upload.wikimedia.org returns 429 quickly from this IP; one 1280px thumbnail (`/thumb/.../1280px-<name>`) worked, originals and 1920px kept failing for 10+ min. Get the face early; make_img.py takes any resolution (face box in fractions).
- Shorts hook with a small/portrait face: build a 1080×1920 hook image (face scaled to full width, eyes at ~y 430, blurred fill; make_hookimg.py) and use zoom 1.3334, pos "50% 0%" — otherwise the giant number covers the face.
- Fact-checker caught (20 fixes): **the game was in New Orleans, not Charlotte** (indictment says only "game against the Pelicans" — always check location in an official box score), the original vs superseding indictment describe the $100K differently (payment for the tip vs. bribe), "nothing happened in public" (NBA's Jan 2025 statement, per the defense filing), a news outlet's narration put in quotation marks, "they admit it / he doesn't" contrast implying guilt, joint (not Rozier-only) severance motion, Count Four's exact name, untagged allegation summary card.
- Long 1,867 words at 0.98 = 13:18; first encode 144 MB → auto re-encode 73 MB (~10 min). Shorts 72–80 words = 28–32 s.

## Notes from run 017 (2026-11-17)
- Thin fresh week (Nov 10–17): no fresh case combined a recognisable name + a confirmed court event + showable documents (Earl Thomas's wife: plea only reported by TMZ, no RECAP, already 10+ YouTube videos; Chad Monroe $42M: release only). Fallback = backlog 021 Belfort, pegged to fresh news (Tone AI startup launch Nov 16, 2026) and the July 2026 restitution-expiry report. Watch for future runs: Emmanuel Clase/Luis Ortiz pitch-rigging trial verdict (E.D.N.Y., started Nov 2), Chokwe Antar Lumumba sentencing (S.D. Miss., Nov 20), SBF cert petition 26-349 (response due Dec 16).
- Old cases have little RECAP for the criminal docket, but post-judgment collection fights do: E.D.N.Y. 18-cv-3016 (`gov.uscourts.nyed.417522`, scanned 151-page motion → tesseract), 18-mc-1033 (`nyed.415574`), D. Nev. `nvd.129776` (forensic accountant's declaration, text layer). `make_img.py` (017) blacks out private names from a word list and paints the DOJ letterhead seal white; `find()` now matches on the joined token stream (robust to OCR splits).
- Contested facts across outlets (sentence 4 yrs vs 3½; release 2006 vs 2008) → never assert; attribute the expiry date to "TMZ's sources" everywhere incl. title/thumbnail/first comment (fact-checker caught it on the title).
- Fact-checker caught (26 fixes): a Bloomberg lead sentence presented as a prosecutors' quote; DOJ 1MDB allegations stated as fact (and "according to the allegations in the complaint" cut from a quote); "Dismissed." when the letter only asked for dismissal; "testify against other defendants" not in sources; GUILTY tag on a civil collection-motion Short; missing digit "show" fields on 8 lines.
- 1,774 words at 0.98 = 12:38 (76 MB, no re-encode). Shorts 79–84 words = 29.7–33.1 s.

## Notes from run 019 (2026-11-19)
- **YouTube rejects descriptions over 5,000 characters**: the Nov 18 Belfort long (017) failed in Metricool with "The request metadata specifies an invalid video description" — its description was 5,737 chars. Check `wc -m out/youtube_description.txt` < 5,000 before scheduling; trim the source list first.
- Fresh case with NO lawful face (Backward Hat Capital, S.D.N.Y. complaint unsealed Nov 18, 2026): thumbnails built from re-typeset complaint excerpts (`zoomcard.js` t_* cards: text in the top 380 px, because the bottom 330 px is covered by the caption shade) + number/question panels. Shorts hooks = 1080×1920 excerpt cards (h_*) with zoom 1.3334.
- justice.gov `/news?page=0` renders in Playwright (page 1 = Access Denied); `/usao-<d>/news` pages list releases for some districts (SDNY, MDFL, EDPA, SDTX), others return nothing to the simple scraper. WebFetch of justice.gov needed approval and timed out unattended — use Playwright.
- `make_img.py` (019) searches every complaint page for each phrase and writes hl.json as [img, y0, y1]; page 9 is cropped above the signature block.
- Fact-checker caught (43 fixes): "both founders"/"founders charged" when only 2 of 3 co-founders were charged (title, thumbnail, Shorts); an audit's 6.3% average stated as "a month"; "three years" vs. July 2022–Nov 2026; "a second fund" (there were 12+); "investors started asking for money back" although ~$200M had already been paid out; "six to seven percent" vs 6.01–7.21%; a draft email presented as sent to investors; "WHERE'S THE $600M?" implying all of it missing (→ "WHERE DID $600M GO?"); the auditor "had his own stake" overstated; Minkow's report "with regulators" not in his post; a text exchange quoted without marking the omitted lines.

## Notes from run 020 (2026-11-20)
- Fresh case without any lawful face (Brinks $100M jewelry heist plea, C.D. Cal. 5:25-cr-198): RECAP had a 22-page plea agreement with a rich factual basis (texts, searches, "robo grande") — the best showable document. Thumbnails = question panel ("$100M OR UNDER $10M?") + re-typeset plea excerpts + a Wikimedia file photo of the place of arrest (Tocumen airport, CC BY-SA 4.0, branding blurred).
- C.D. Cal. pleading paper: `pdftotext -bbox` puts the left-margin line numbers inside phrases and moves indented first words to the end of the paragraph — `make_img.py` (020) drops margin digits and sorts words by line (y) before matching.
- Long `verdict` scene: a `big` longer than ~22 characters wraps and overlaps `sub` (long and Shorts). Keep `big` short (surname / "Max 20 Years"); checked by single-frame renders. A one-block fix can be re-rendered with a segment script and overlaid (`overlay=enable='between(t,a,b)'`), but re-encode afterwards at a capped bitrate (the overlay pass at CRF 21 came out 267 MB).
- Fact-checker caught (37 fixes): the count of conviction (count three = the AirTags robbery, not the heist) must be explicit in summary/description; "the owners declared under $10M" → "certain victims declared a total of less than $10M" (his contention, disputed); "HE RAN" right after the heist → "INDICTED, HE RAN" (he left in June 2025); co-defendants' overt acts framed as allegations; "guards" → "drivers"; spoken rounded numbers vs exact subtitles; LA Times attribution ("two people involved with the case"); excerpt cards need trailing ellipses.
- 1,836 words at 0.98 = 12:57 (85 MB after the capped re-encode). Shorts 79–83 words at 1.15 = 30.3–32.9 s.

## Notes from run 021 (2026-11-21)
- Fresh politician case (ex-Jackson mayor Chokwe Antar Lumumba, sentenced Nov 20, 2026; S.D. Miss. 3:24-cr-103). No RECAP on archive.org; the indictment PDF is attached to the USAO S.D. Miss. release (`/usao-sdms/media/<id>/dl?inline`, downloads from the shell). It is a scan: `make_img.py` (021) runs tesseract TSV on the 220-dpi pages, drops the ECF header and the OCR noise inside printed photos, and finds highlight bands.
- **Indictments can carry FBI photos** (recording stills, search photos with evidence markers) — lawful evidence images for thumbnails/Shorts hooks. Caption them only with what the indictment says ("¶ 56 · FBI recording"); do not name people in a still unless the paragraph does.
- Mississippi Free Press / CourtListener storage are blocked from the shell; Mississippi Today pages sometimes fail in WebFetch (use WLBT/Magnolia/SuperTalk). Wikimedia originals kept returning 429 for 1 h+; the 1280px rendition (`/thumb/.../1280px-<name>`) arrived on the first retry loop.
- Fact-checker caught (16 fixes): "the FBI's jet" (it was a private jet paid for by the FBI); "everything was recorded" (only the yacht meeting is described as recorded); a quote attributed to the wrong hearing (Fulcher spoke at Lumumba's presentence hearing on Nov 5, not Owens's); event order (Feb 28 exchange told after Mar 27); a house visit known only from Owens's own account; "more serious" vs "more substantive" charges; "approximately $20,000"; narrator conclusions ("the official act that was for sale") → attribute to the indictment.

## Notes from run 022 (2026-11-22)
- Thin fresh week again; picked the Feeding Our Future juror-bribery plot (last two sentencings Nov 18/20, 2026). D. Minn. RECAP is rich even for 2026: the government's sentencing positions for all five bribery defendants (24-cr-173, `gov.uscourts.mnd.216389`–`216393`, text layer) each carry a full offense narrative, plus judgment/minutes; 22-cr-124 (`gov.uscourts.mnd.203008`–`203014`) has the acquittal judgment (579) and the Nur fraud memo (929) with embedded government trial exhibits (`pdfimages`).
- No lawful face for any defendant (no federal/booking/Commons photo; tiny headshots inside government exhibit charts are < 500 px). Thumbnails = question panel + re-typeset verbatim excerpts (zoomcard.js; cards quoting USAO releases carry "U.S. ATTORNEY'S OFFICE" not the case caption). Stamps on text cards cover the words — leave them off.
- `make_img.py` (022) works on text-layer PDFs only: pdftotext -bbox per page, phrase search on every page, ECF header dropped. Check pdfimages output by eye: an exhibit index can point at a different image (x-007 was an e-mail showing a private Gmail address, not the WhatsApp exhibit).
- commons.wikimedia.org API returned "too many requests" all run; wikipedia.org and mprnews.org are blocked from the shell/Playwright (web-fetch agent read MPR/CBS/KSTP fine).
- Fact-checker caught (23 fixes): "biggest pandemic fraud trial in Minnesota" unsupported; Empire Cuisine called a FOF "site" (the scheme "originated" there); "attempted to follow" (plea releases) vs "followed home" (2026 memos) → attribute; a cut quote dropping what the "good feeling" was about; factory reset is an allegation (obstruction count dismissed); chart title "Before the bribery sentences" false (one bribery sentence came earlier); WCCO didn't say "on top of" (MPR did); "easiest juror to buy" → "best candidate to bribe"; unverified courthouse city on verdict cards → "D. MINN."
- 1,764 words at 0.98 = 12:30 (78 MB). Shorts 68–80 words at 1.15 = 27–28 s.
