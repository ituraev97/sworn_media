# SWORN — daily production runbook

One run = one long episode (10–13 min, ≥ 10:00, 1920×1080) + **3** vertical Shorts (25–40 s, 1080×1920; owner rule 2026-11-06), all about ONE court case, hosted here and scheduled in Metricool for ONE US day.
Reference episode: `episodes/001-madoff/` (make_spec.py → episode.json, make_shorts.py → short1–6.json, meta.json, thumb.json, factcheck.md). Read it before writing anything.

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
cd /home/claude/sworn_media && git checkout -q --orphan up && git rm -rqf . && cp $W/out/long.mp4 $W/out/thumb_A.jpg $W/out/thumb_C.jpg $W/out/s[1-3].mp4 . && \
git add long.mp4 thumb_A.jpg thumb_C.jpg s*.mp4 && git -c user.name="SWORN bot" -c user.email="ituraev97@users.noreply.github.com" commit -qm "drop NNN" && \
git push -qf origin up:drop-XXX && git checkout -qf main && git branch -D up
```
Check every `https://raw.githubusercontent.com/ituraev97/sworn_media/drop-XXX/<file>` with `curl -sI` → 200. Never put video on main.

## 8. Schedule in Metricool (createScheduledPost, blogId 7806713, autoPublish true, providers [{"network":"youtube"}], publicationDate timezone America/New_York)
- Long 12:00: text = `out/youtube_description.txt`; youtubeData {title, type "video", privacy "public", madeForKids false, category "EDUCATION", tags}; media [long.mp4 URL]; videoThumbnailUrl = thumb_A URL (if rejected, retry once without it).
- Shorts 10:00, 14:00, 18:00 (s1…s3 in that order): type "short", title from the short json, text = 1–2 lines + "Full case on the channel." + "#truecrime #courtcase #shorts", madeForKids false, category EDUCATION.

## 9. Close
- Commit to main: episode folder (spec scripts, json, img/, sources.md, factcheck.md — no video), `backlog.md` row → `done YYYY-MM-DD`. fetch/rebase before push.
- Report to the owner in Russian (SendUserMessage): case + title, publish date and times (ET and Tashkent = ET+10 in winter / +9 in summer), Metricool plannerUrls, fact-check result (how many fixes), anything skipped; SendUserFile thumb_A.

## Performance rules
Weekly review (Mondays, Asia/Tashkent). Each rule is backed by ≥ 3 of our own videos (Metricool YTVP, last 28 days). Owner content rules, schedule and AI-label settings are NOT changed here — only recommended in the report.
1. Shorts titles open with a verbatim quote or a short declarative statement/number ("FTX Is Fine. Assets Are Fine." 200, "He Confessed. Then the Judge Spoke." 20, "It's All Just One Big Lie" 18, "Six Warnings…" 5, "The Coin Flip…" 4 → median 18). Never open a Short with Where/How/Did or "The Hidden…" explainer phrasing (5 Shorts: 3, 3, 1, 1, 1 → median 1).
2. Average view duration was ≤ 33 s on all 10 measured Shorts (7 of 10 at ≤ 9 s): the quote or the number must be on screen from frame 0 and the first spoken line must already be the payoff-setup — no titles, no context sentence first.
3. Do not draw conclusions from videos younger than ~7 days: Metricool returned null views for every video published after 2026-11-04 (15+ videos, including all long episodes) at review time. Re-check long-video performance next Monday.

Changelog:
- 2026-11-09: section created (first weekly review; 10 Shorts with data, 0 long videos with data).

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

