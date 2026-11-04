# Fact-check — SWORN Case 004: United States v. Robert Allen Stanford

Date checked: 2026-11-04
Checker: independent (did not write the script)
Scope: `episode.json`, `short1.json` … `short6.json` (say, show, every on-screen scene field, every `doc` image and highlight band). `meta.json`/`thumb.json` were looked at only for consistency (see notes at the end).

Line numbers are 0-based indexes into `lines`. Brief page numbers are **PDF pages** (the brief's own printed page number is in brackets).

## Sources actually opened

1. **[BR]** Brief of the United States, *U.S. v. Stanford*, 5th Cir. No. 12-20411, filed Mar 3, 2015 (`gov.uscourts.ca5.12-20411.00502955799.0.pdf`): PDF pp. 1, 22–54 read in full with `pdftotext -layout`.
2. **[CMP]** SEC First Amended Complaint, N.D. Tex. 3:09-cv-298, Dkt. 48 (`amcomp.txt` + PDF pp. 1, 8, 9): ¶¶1–5, 12–13, 35–43.
3. **[RCV]** Order Appointing Receiver, Dkt. 10 (scanned; checked through `img/rcv.jpg`): N.D. Tex. Dallas Division, "on the motion of Plaintiff Securities and Exchange Commission", clerk's FILED stamp Feb 17, 2009.
4. **[DOCKET]** N.D. Tex. docket 3:09-cv-298 (`txnd_docket.html`): case filed 2009-02-17; Dkt. 8 (TRO) and Dkt. 10 (receiver) "Ordered by Judge Reed C O'Connor on 02/16/09", entered 02/17/2009.
5. **[PRC]** U.S. Attorney S.D. Tex. release, Mar 6, 2012, with Mar 8 update (`pr_conv.txt`, `img/pr_conv.jpg`).
6. **[PRS]** U.S. Attorney S.D. Tex. release, Jun 14, 2012 (`pr_sent.txt`, `img/pr_sent.jpg`, `img/pr_judge.jpg`).
7. **[OIG]** SEC OIG, *Investigation of the SEC's Response to Concerns Regarding Robert Allen Stanford's Alleged Ponzi Scheme*, Report No. OIG-526, Mar 31, 2010 (WebFetch, sec.gov). Executive Summary pp. 16–18, Results p. 30.
8. **[CA5]** *U.S. v. Stanford*, 5th Cir. No. 12-20411, opinion filed Oct 29, 2015 (WebFetch, ca5.uscourts.gov). Panel: Benavides, Clement, Higginson; opinion by Clement.
9. **[DAVIS]** DOJ release, Jan 22, 2013, on the Davis sentencing (WebFetch).
10. **[HLK]** DOJ Fraud Section case page, *U.S. v. Holt, Lopez, Kuhrt* (WebFetch).
11. **[KING]** DOJ release, Feb 24, 2021, on the King sentencing (WebFetch). The page's "Updated February 5, 2025" stamp is a routine page update with no new content.
12. **[SEC25]** SEC Litigation Release No. 26255, Feb 24, 2025 (WebFetch).
13. **[IJ]** Insurance Journal (Reuters), Nov 29, 2016 (WebFetch).
14. **[BLC]** Bloomberg Law, Sept 1, 2023: compassionate release denied again (WebFetch).
15. **[BLK]** Bloomberg Law, Sept 19, 2025: SEC drops its Kuhrt case after the Biden reprieve (WebFetch).
16. **[CNN]** CNN via ABC17, Feb 27, 2023: TD Bank settlement (WebFetch).
17. **[FH]** Fishman Haygood, Aug 15, 2023: court approves the bank settlements (WebFetch).
18. **[DOJ-CLEM]** DOJ Office of the Pardon Attorney, "December 12, 2024 Commutation Recipients" (WebFetch). Only surnames A–D were readable through the tool, so K/L/S entries could **not** be checked. The shell fetch was blocked and I did not try to get around it.
19. **[WIKI]** Wikipedia, "Gilbert Lopez" and "Allen Stanford" (WebFetch). Used only as leads, never as support.
20. WebSearch, Nov 2026, for any pardon, commutation, release or reversal for Stanford, Lopez, Kuhrt, Davis, Pendergest-Holt or King. I found none for Stanford. Kuhrt's clemency is reported in [BLK]. Search results also confirm the ~1,500-commutation action was dated Dec 12, 2024. For Lopez, see the NOTE at short6 / episode 50.

**On the $541M vs. $741M discrepancy:** [CMP] ¶¶40–42 and [BR] p.49 [30] both give **$541 million**. [PRS] says $741 million. The script uses $541M and shows it on the SEC complaint (episode 34–35, short4 1–2), which is the right choice. It never states $741M. **OK**, with one optional attribution NOTE (episode 34).

---

## episode.json

| file | line# | field | claim | verdict | source (doc + page) | fix text |
|---|---|---|---|---|---|---|
| episode | 0 | say/show, scene | 1997, SEC Fort Worth examiners finish a look at a Houston brokerage that sells CDs from a Caribbean bank | OK | OIG p.16–18 (1997 FWDO exam of SGC, incl. SGC's referral fees for SIB CD sales); CMP ¶13 / BR p.24 (SGC is Houston-based) | — |
| episode | 1 | say, scene.q/doc/cite | Conclusion recorded in the tracking system: "Possible misrepresentations. Possible Ponzi scheme." | OK | OIG p.18 (verbatim; "the SEC's internal tracking system") | — |
| episode | 2 | say/show | Bank kept selling almost 12 more years; Feb 2009 SEC went to court; judge appointed a receiver | OK | DOCKET; RCV; BR p.52 [33] | — |
| episode | 2 | scene (doc rcv) | Image = Order Appointing Receiver; band on the title | OK | RCV p.1 | (NOTE: the kicker says FEBRUARY 16 while the image's stamp reads FEB 17 2009. Both are correct: signed 2/16, entered 2/17. Optional kicker "SIGNED FEBRUARY 16, 2009".) |
| episode | 3 | say/show, scene | Convicted; 110 years | OK | PRS; BR p.23 [4] | — |
| episode | 4 | scene | Title card, S.D. Tex., 2009–2025 | OK | — | (NOTE: the 2025 judgment is in the N.D. Tex. SEC case. That is acceptable for a series sub-line.) |
| episode | 5 | — | Chapter card | OK | — | — |
| episode | 6 | say/show | Per DOJ: bank began in 1985 on Montserrat as Guardian International Bank | OK | PRS | — |
| episode | 6 | scene.events | 1990 move to Antigua; 1994 renamed SIB (per DOJ) | NOTE | PRS says 1990; BR p.32 [13] says "In 1991, Guardian relocated from Montserrat to Antigua" | Optional: change the event date to "1990–91" or keep it as DOJ-attributed (the kicker already says PER THE JUSTICE DEPARTMENT). |
| episode | 7 | say/show, scene | Nov (28) 1990, Montserrat finance ministry faxed notice of intent to revoke the license | OK | BR p.31 [12]; image brief_montserrat, band covers the sentence | — |
| episode | 8 | say/show, scene | Moved to Antigua; 1994 became SIB; Antigua knighted him; "Sir Allen Stanford" was good marketing | OK | PRS (1994); BR p.32 [13] ("knighted him 'Sir Allen Stanford,' which Stanford asserted was a good marketing device") | — |
| episode | 9 | say | CDs paid more than U.S. bank CDs; SGC advisers in Houston sold them to U.S. investors | OK | BR p.24 [5]; PRS ("typically paid a premium") | — |
| episode | 9 | scene.hl | Band should cover the SGC/Houston passage | **FIX** | BR p.24 [5]. The current band covers "From roughly 1990 through 2009 … fraudulent investment scheme", which is not what the line says. The SGC paragraph sits at the top of the crop | scene.hl: `[0.0, 0.0935, 1.0, 0.37]` (covers "SGC, headquartered in Houston, Texas … The SEC regulated SGC."). If regenerating with make_img.py, use phrase `('SGC, headquartered', 'regulated')`. |
| episode | 10 | say/show, scene | No FDIC insurance; per prosecutors, Stanford joked people were greedy … extra 2% | OK | BR p.28 [9], p.37 [18] | — |
| episode | 11 | say/show | Per SEC: about $8B of CDs sold by year-end 2008; claimed 50,000 clients in 100+ countries | OK | CMP ¶3, ¶12 | — |
| episode | 11 | scene (doc cmp_cover) | The band is on ¶1 ("massive Ponzi scheme"), but the narration's figures are not on this page, so image and narration don't match | **FIX** | CMP p.1 ¶1 | say: "By the end of two thousand eight, according to the S.E.C., the bank had sold about eight billion dollars of these CDs, and claimed fifty thousand clients in more than one hundred countries. The S.E.C. called it a massive Ponzi scheme." / show: "By the end of 2008, according to the SEC, the bank had sold about $8 billion of these CDs, and claimed 50,000 clients in more than 100 countries. The SEC called it a massive Ponzi scheme." (scene unchanged) |
| episode | 12 | — | Chapter card | OK | — | — |
| episode | 13 | say/show, scene | Annual reports always showed a profit; per Davis, no profitable year after 1986; each year the two made up the numbers; title "fake profit numbers" | OK | BR p.30 [11] (band covers it; title verbatim) | — |
| episode | 14 | say, scene | SEC: monthly predetermined return; accountants reverse-engineered the statements | OK | CMP ¶5 ("Each month"), ¶37 (shown, band on ¶37) | — |
| episode | 15 | say, scene | Told: safe, liquid, overseen by managers/analysts; tiers 10/15/75 per prosecutors | OK | BR p.33 [14], p.40–42 [21–23] | — |
| episode | 16 | say/show, scene | Tier 1 cash 10%; Tier 2 analysts 15%; Tier 3 75% to companies, real estate, lifestyle; title "the remaining 75%" | OK | BR p.41–42 [22–23] (band and title verbatim) | — |
| episode | 17 | say/show, scene | By end-2008 >$2B to 50+ businesses: restaurants, two airlines, newspaper, cricket tournament with $20M prize, 112-ft yacht | OK | BR p.33 [14] (band and title "over $2 billion in CD monies" verbatim) | — |
| episode | 18 | say/show, scene | By 2008 ~$1M a day to keep businesses afloat (per government) | OK | BR p.34 [15], p.47 [28] | — |
| episode | 19 | say/show | One-man Antigua auditor; in 16 years never got the documents; signed off every year | OK | BR p.44 [25] | — |
| episode | 19 | scene.hl | The band stops at "In 16 years," and leaves out the passage being narrated | **FIX** | BR p.44 [25] | scene.hl: `[0.0, 0.0648, 1.0, 0.5502]` (from "Beginning on Montserrat" through "accuracy of the assets (USCA5 Supp. 6 7141; GX 100-120)."). make_img phrase: `('Beginning on Montserrat,', 'GX 100-120).')`. |
| episode | 20 | say/show, scene | Prosecutors: >$3.3M from Swiss account on top of fees; "God led me to Hewlett" | OK | BR p.44 [25] (band on the $3.3M paragraph) | — |
| episode | 21 | — | Chapter card | OK | — | — |
| episode | 22 | say/show | "In 2010, the SEC's own inspector general investigated …" | NOTE | OIG (report dated Mar 31, 2010; the investigation itself began in 2009) | Optional: "In two thousand ten, the S.E.C.'s own inspector general reported on how the agency had handled Stanford." / show "In 2010, the SEC's own inspector general reported on how the agency had handled Stanford." |
| episode | 22 | scene.q | "the SEC's Fort Worth office was aware since 1997 that Robert Allen Stanford was likely operating a Ponzi scheme" | OK | OIG p.16 (verbatim) | — |
| episode | 23 | say/show, scene | Four exams 1997/98/2002/2004; a branch chief called the CD returns "absolutely ludicrous" | OK | OIG p.16 (exams); p.17 (the former FWDO broker-dealer exam branch chief said SIB CDs' purported above-market returns were "absolutely ludicrous"; identified on p.30 as Julie Preuitt) | — |
| episode | 24 | say/show, scene | Enforcement opened an inquiry May 1998, closed three months later (Aug); reasons related to lack of U.S. investors | OK | OIG p.18 | — |
| episode | 25 | say/show | Preference for "quick hit" cases; no meaningful effort until late 2005 | OK | OIG p.16 ("no meaningful effort was made by Enforcement … until late 2005"), p.18 | — |
| episode | 25 | scene.q | "the preference for "quick hit" cases as a result of internal SEC pressure" | OK | OIG p.18 (verbatim) | — |
| episode | 26 | say/show, scene | 2005 confidential request to Leroy King, head of Antigua's FSRC; kicker "PRIVILEGED AND CONFIDENTIAL" | OK | BR p.46 [27]; KING ("administrator and CEO") | (NOTE: the band covers only the first sentence. Optional: extend it to cover the "Privileged and Confidential" line, `[0.0, 0.186, 1.0, 0.18]`.) |
| episode | 27 | say, scene | King immediately shared it; Stanford helped draft the reply | OK | BR p.46 [27] | (NOTE: the band covers only the sharing sentence. Optional `[0.0, 0.4289, 1.0, 0.565]` would also cover "Stanford worked with SIB's general counsel and drafted a response, purporting to come from King".) |
| episode | 28 | say/show, scene | King admitted Stanford's cash payments ≈ $520,963.87, plus Super Bowl tickets and private-jet flights | OK | KING | — |
| episode | 29 | say, scene | Per the government's account of trial testimony, blood-oath ceremony | OK | BR p.45 [26] (band verbatim) | — |
| episode | 30 | — | Chapter card | OK | — | — |
| episode | 31 | say/show, scene | 2008 crisis: redemptions jumped, new sales flatlined | OK | BR p.47 [28] | — |
| episode | 32 | say/show, scene | Oct 2008, told global executive team the bank was "$5 billion more liquid than it should be" (per prosecutors) | OK | BR p.47–48 [28–29] (band and title verbatim) | — |
| episode | 33 | say | Manager suggested asking wealthy friends; Stanford: "I'll go to the Libyans. They love me"; "the trip did not work" | **FIX** | BR p.48 [29] (Green's suggestion; quote cited to trial transcript; "Stanford's trip to Libya proved unsuccessful"). Needs an attribution, and "the trip" was never set up | say: "When a manager suggested he ask wealthy friends for money, according to trial testimony, Stanford answered: I'll go to the Libyans. They love me. His trip to Libya was unsuccessful." |
| episode | 33 | scene.q | "I'll go to the Libyans. They love me" | OK | BR p.48 [29] (verbatim) | — |
| episode | 33 | scene.doc / scene.cite | The card does not say who said it | **FIX** | BR p.48 [29] | scene.doc: "STANFORD · NOVEMBER 2008 · PER TRIAL TESTIMONY"; scene.cite: "As quoted in the Brief of the United States, 5th Cir. No. 12-20411, Mar 3, 2015" |
| episode | 34 | say/show, scene | Dec 2008 report told investors of a $541M capital infusion; title verbatim | OK | CMP ¶40 (band covers it); BR p.49 [30] | (NOTE: because DOJ's release says $741M, optionally attribute in narration: "…according to the S.E.C., the bank told investors…".) |
| episode | 35 | say/show | SEC said false; Stanford contributed interests in two properties the bank already owned, about $88.5M; per Davis, merely a bookkeeping entry | OK | CMP ¶41 ("valued at approximately $88.5 million when acquired"); BR p.49 [30] | (NOTE: "acquired for about" ≈ "valued … when acquired". Acceptable.) |
| episode | 35 | scene.kicker | "THE SEC'S FINDING". A complaint contains allegations, not findings | **FIX** | CMP ("Plaintiff Securities and Exchange Commission alleges") | scene.kicker: "PER THE SEC'S COMPLAINT" |
| episode | 36 | say/show, scene | Per DOJ: accountants marked up land bought for $63.5M by 5,000% to >$3B ($3.1B); bought 2008 | OK | PRS ("inflated on paper … $63.5 million earlier in 2008 by 5,000 percent to $3.1 billion") | (NOTE: BR p.49–50 [30–31] gives $3.2B and says "SIB collapsed before the sham transaction could be executed". Optional: "…to more than three billion, on paper." The DOJ attribution makes the line acceptable.) |
| episode | 37 | say/show, scene | As SEC investigation surged, St. Croix estate manager testified to filling barrels with bank records and burning them | OK | BR p.47 [28] | (NOTE: the image `brief_burn` shows the manager's full name, "Kelly Taylor". She is a witness, not a victim, so no rule is broken, but sources.md says she is not named. Optional: mask the name in the crop.) |
| episode | 38 | say/show | "…appointed a receiver… The next day, the receiver took over, and the S.E.C. filed suit." | **FIX** | DOCKET (docketed 2/17); SEC25 ("filed Feb. 16, 2009"); RCV (order on the SEC's motion). Saying the SEC sued the day *after* the receiver was appointed is contradicted by the SEC and makes no sense procedurally | say: "On February sixteenth, two thousand nine, on the S.E.C.'s motion, a federal judge in Dallas appointed a receiver for the Stanford companies. The next day, the receiver took over." / show: "On February 16, 2009, on the SEC's motion, a federal judge in Dallas appointed a receiver for the Stanford companies. The next day, the receiver took over." |
| episode | 38 | scene | Order Appointing Receiver, Dallas Division | OK | RCV | — |
| episode | 39 | say/show, scene | FBI agent traced $2B in loans; $8.59B reported; $5B "hole" (per government) | OK | BR p.53 [34] (band and title verbatim) | (NOTE: "That left" sounds like simple subtraction, but 8.59 − 2 ≠ 5. The brief says $5B "in untraceable funds". Optional: "…That left, the government said, a five billion dollar hole in untraceable funds.") |
| episode | 40 | — | Chapter card | OK | — | — |
| episode | 41 | say/show, scene | 14-count superseding indictment: conspiracy, wire, mail, obstruction, money-laundering conspiracy | OK | BR p.22 [3] (band) | — |
| episode | 42 | say/show, scene | Per government: did not dispute moving >$2B; defenses: Davis, receiver, legitimate investments | OK | BR p.53 [34] | — |
| episode | 43 | say/show, scene | Mar 6, 2012; six-week trial; ~3 days' deliberation; guilty 13 of 14 | OK | PRC (band verbatim) | (BR says "30-day trial", which is consistent.) |
| episode | 44 | say/show, scene | Acquittal = wire count over $9,000 Super Bowl tickets for King; two days later, 29 accounts ≈ $330M found to be proceeds | OK | BR p.53 [34]; PRC Mar 8 update | — |
| episode | 45 | say/show, scene | Jun 14, 2012; >350 victim impact letters; quote from the coalition founder (unnamed) | OK | PRS (quote verbatim, Angie Shaw, Director and Founder, Stanford Victims Coalition) | — |
| episode | 46 | say, scene | Hittner: "one of the most egregious frauds ever presented to a trial jury in federal court" | OK | PRS (band verbatim) | — |
| episode | 47 | say/show, scene | 20 + 4×20 + 5 + 5, consecutive | OK | PRS | (NOTE: mail fraud and laundering terms ran concurrently. Optional add: "The other counts ran at the same time.") |
| episode | 48 | say/show, scene | 110 years; max 230; $5.9B money judgment | OK | BR p.23 [4], p.53 [34]; PRS | — |
| episode | 49 | — | Chapter card | OK | — | — |
| episode | 50 | say/show, scene | Davis cooperated, testified, 5 yrs; Pendergest-Holt (CIO) pleaded to obstruction, 3 yrs; Kuhrt (controller) and Lopez (CAO) convicted at trial, 20 yrs each | OK | DAVIS; HLK (Kuhrt = "global controller") | **NOTE, high priority, verify before publish:** Wikipedia says Lopez was released on Dec 20, 2024, eight days after Biden's Dec 12, 2024 mass commutation, though a 20-year term imposed in 2013 would normally run to ~2029. I could not confirm whether Lopez got clemency: [DOJ-CLEM] was readable only for surnames A–D. If DOJ lists Lopez, the channel rule requires a mention. Suggested replacement for episode 51 in that case: say "In December two thousand twenty-four, President Biden shortened the prison terms of both Kuhrt and Lopez." (and update short6 2 the same way). |
| episode | 51 | say/show, scene | Per Bloomberg Law, Biden shortened Kuhrt's prison term in a clemency action, Dec 2024 | OK | BLK ("cut short his prison term"; "clemency action for some 1,500 convicted criminals"); that action was Dec 12, 2024 (search results; DOJ-CLEM page) | (NOTE: the BLK text itself gives no month. Dec 2024 comes from matching it to the ~1,500 action.) |
| episode | 52 | say/show, scene | King awaiting extradition at trial; extradited Nov 2019; pleaded guilty (Jan 30, 2020) to obstruction; Feb 2021, 10 yrs | OK | BR p.52 [33]; KING (conspiracy to obstruct and obstruction) | — |
| episode | 53 | say/show, scene | Oct 2015 Fifth Circuit affirmed; quote "Stanford sat atop a massive Ponzi scheme" | OK | CA5 ("In fact, Stanford sat atop a massive Ponzi scheme…"; "we AFFIRM"; filed Oct 29, 2015) | — |
| episode | 54 | say/show | Nov 2016 Supreme Court declined; 2023 Hittner again denied compassionate release | OK | IJ; BLC | — |
| episode | 54 | scene (doc brief_cover) | Shows the 2015 government brief cover while the narration covers the 2016 Supreme Court denial and the 2023 ruling, so image and narration don't match | **FIX** | — | Replace the whole scene with: `{"type": "timeline", "kicker": "AFTER THE APPEAL", "events": [{"date": "OCT 2015", "text": "Fifth Circuit affirms"}, {"date": "NOV 2016", "text": "Supreme Court declines to hear it"}, {"date": "2023", "text": "Compassionate release denied again"}], "at": 2, "src": "U.S. Court of Appeals, 5th Cir., Oct 29, 2015 · Insurance Journal, Nov 29, 2016 · Bloomberg Law, Sept 1, 2023"}` |
| episode | 55 | say/show, scene | Receiver went after banks; by 2023 five-bank settlements incl. $1.2B TD topped $1.6B | OK | CNN; FH (TD $1.205B; Trustmark $100M; SocGen $157M; Independent $100M; HSBC $40M; >$1.6B) | (NOTE: the claims were brought by the Receiver together with the Official Stanford Investors Committee. Acceptable.) |
| episode | 56 | say/show, scene | Jan (29) 2025 final judgment, 16 years after suit; $5.9B civil penalty | OK | SEC25 | — |
| episode | 57 | say, scene | 1997: "Possible Ponzi scheme." | OK | OIG p.18 | — |
| episode | 58 | say, scene | Four exams; regulator taking cash; profit every year; "decided on the paper trail" | OK | OIG; KING; BR p.30 [11] | (NOTE: "decided on the paper trail" is rhetoric. The verdict also rested heavily on Davis's testimony. Optional: "In the end, the paper trail caught up with him.") |
| episode | 59 | — | End card | OK | — | — |

## short1.json

| file | line# | field | claim | verdict | source (doc + page) | fix text |
|---|---|---|---|---|---|---|
| short1 | meta | title/hook | "Possible Ponzi Scheme" in 1997; ran 12 more years | OK | OIG p.18; RCV (1997 → Feb 2009 ≈ 11–12 yrs) | — |
| short1 | 0 | say/show | 1997 SEC examiners in Fort Worth review a Houston firm selling CDs from Stanford's offshore bank | OK | OIG p.16–18; CMP ¶13 | — |
| short1 | 0 | scene.lines | "look at Stanford." is 17 characters | **FIX** | big-line rule (≤ ~14) | scene.lines: `["SEC examiners", "look at|Stanford."]` |
| short1 | 1 | say, scene.q | Conclusion as quoted by the IG | OK | OIG p.18 (verbatim) | (NOTE: optional scene.doc "SEC EXAMINERS, 1997 · AS QUOTED BY THE INSPECTOR GENERAL", to match the episode.) |
| short1 | 2 | say/show, scene | Exams again 1998, 2002, 2004 | OK | OIG p.16 | — |
| short1 | 3 | say/show | Inquiry opened 1998, closed after three months; no meaningful effort until late 2005 | OK | OIG p.16, p.18 | — |
| short1 | 3 | scene.lines | "Inquiry closed." is 15 characters | NOTE | big-line rule | Optional: `["Inquiry|closed.", "Until late|2005."]` |
| short1 | 4 | say/show, scene | Kept selling until Feb 2009; receiver | OK | RCV; DOCKET (band on the title) | — |
| short1 | 5 | say/show, scene | Convicted; 110 years; Jun 14, 2012 | OK | PRS | — |
| short1 | 6 | — | End | OK | — | — |

## short2.json

| file | line# | field | claim | verdict | source (doc + page) | fix text |
|---|---|---|---|---|---|---|
| short2 | meta | hook | "Where the money" is 15 characters | NOTE | big-line rule | Optional: "Where the|money went." |
| short2 | 0 | say, scene | SIB told investors: safe, liquid, globally diversified | OK | PRS; BR p.33 [14] | — |
| short2 | 1 | say/show, scene | Tiers 10% / 15% (per prosecutors) | OK | BR p.41 [22] | — |
| short2 | 2 | say/show, scene | Tier 3, 75%, to companies, real estate, lifestyle | OK | BR p.42 [23] (band correct) | — |
| short2 | 3 | say/show, scene | >$2B to 50+ businesses; list | OK | BR p.33 [14] (band correct) | — |
| short2 | 4 | say/show, scene | ~$1M/day by 2008 (per prosecutors) | OK | BR p.34 [15] | — |
| short2 | 5 | say/show, scene | Convicted on 13 of 14 | OK | PRC (band correct) | — |
| short2 | 6 | — | End | OK | — | — |

## short3.json

| file | line# | field | claim | verdict | source (doc + page) | fix text |
|---|---|---|---|---|---|---|
| short3 | 0 | say, scene | Audited reports every year; one-man Antigua firm C.A.S. Hewlett | OK | BR p.28 [9] ("purportedly audited"), p.44 [25] (band on the one-man auditor sentence) | (NOTE: optional "published reports it said were audited".) |
| short3 | 1 | say/show, scene | Prosecutors: 16 years without documents, signed every year | OK | BR p.44 [25] | — |
| short3 | 2 | say/show | "Stanford paid him more than $3.3 million from a Swiss account" is stated as fact with no attribution; the "God led me…" line needs a source | **FIX** | BR p.44 [25] (bribe payments are the government's account; the quote is cited to Davis's testimony, Supp. 6 7139) | say: "Prosecutors said Stanford paid him more than three point three million dollars from a Swiss account. According to his finance chief, Stanford told him: God led me to Hewlett." / show: "Prosecutors said Stanford paid him more than $3.3 million from a Swiss account. According to his finance chief, Stanford told him: \"God led me to Hewlett.\"" |
| short3 | 2 | scene.q | "God led me to Hewlett" | OK | BR p.44 [25] (verbatim) | — |
| short3 | 2 | scene.doc / scene.cite | The card does not say who said it | **FIX** | BR p.44 [25] | scene.doc: "STANFORD TO DAVIS · PER TRIAL TESTIMONY"; scene.cite: "As quoted in the gov't brief, 5th Cir. No. 12-20411, 2015" |
| short3 | 3 | say/show | King, head of Antigua's watchdog, admitted ≈ $521,000 cash from Stanford | OK | KING | — |
| short3 | 3 | scene.value | "$520,963" truncates $520,963.87 (it would round to $520,964) and differs from the episode | **FIX** | KING | scene.value: "$520,963.87" |
| short3 | 4 | say/show, scene | 2005 confidential SEC request; prosecutors said he passed it to Stanford | OK | BR p.46 [27] (band correct) | — |
| short3 | 5 | say/show, scene | King 10 yrs; Stanford 110 | OK | KING; PRS | — |
| short3 | 6 | — | End | OK | — | — |

## short4.json

| file | line# | field | claim | verdict | source (doc + page) | fix text |
|---|---|---|---|---|---|---|
| short4 | meta | title/hook | "$541 Million That Never Arrived" | OK | CMP ¶41; BR p.49 [30] | — |
| short4 | 0 | say/show | Late 2008 investors pulling money | OK | BR p.47 [28] | — |
| short4 | 0 | scene.lines | "Withdrawals up." is 15 characters | NOTE | big-line rule | Optional: `["Withdrawals|up.", "Sales flat."]` |
| short4 | 1 | say/show, scene | December report: $541M capital infusion | OK | CMP ¶40 (band correct) | — |
| short4 | 2 | say/show | SEC said it was real estate the bank already owned, ≈ $88.5M when acquired | OK | CMP ¶41 | — |
| short4 | 2 | scene.kicker | "THE SEC'S FINDING". The complaint makes allegations, not findings | **FIX** | CMP | scene.kicker: "PER THE SEC'S COMPLAINT" |
| short4 | 3 | say/show, scene | Prosecutors: land bought for $63.5M marked up 5,000% to $3.1B | OK | PRS | (NOTE: as at episode 36, BR says the flip was never executed. Optional "on paper".) |
| short4 | 4 | say/show, scene | St. Croix employee testified records were burned in barrels | OK | BR p.47 [28] | (NOTE: the image names the witness. See episode 37.) |
| short4 | 5 | say/show, scene | Feb 2009 receiver; 110 years | OK | BR p.52 [33]; PRS | — |
| short4 | 6 | — | End | OK | — | — |

## short5.json

| file | line# | field | claim | verdict | source (doc + page) | fix text |
|---|---|---|---|---|---|---|
| short5 | 0 | say/show, scene | Mar 6, 2012; Houston jury; 13 of 14 | OK | PRC | — |
| short5 | 1 | say/show, scene | The one acquittal: $9,000 Super Bowl tickets for an Antiguan regulator | OK | BR p.53 [34] | (NOTE: shortened wording. Optional: "The one acquittal: a count over nine thousand dollars in Super Bowl tickets for an Antiguan regulator." / show "…a count over $9,000 in Super Bowl tickets…") |
| short5 | 2 | say, scene | Hittner quote | OK | PRS (band correct) | — |
| short5 | 3 | say/show, scene | 20 + 4×20 + 5 + 5, consecutive; list 20/80/10 | OK | PRS | — |
| short5 | 4 | say/show, scene | 110 of possible 230; $5.9B | OK | BR p.53 [34]; PRS | — |
| short5 | 5 | say/show, scene | Fifth Circuit affirmed; quote | OK | CA5 | — |
| short5 | 6 | — | End | OK | — | — |

## short6.json

| file | line# | field | claim | verdict | source (doc + page) | fix text |
|---|---|---|---|---|---|---|
| short6 | 0 | say/show, scene | Stanford 110 yrs; inner circle to prison | OK | PRS; DAVIS; HLK; KING | — |
| short6 | 1 | say/show, scene | Davis cooperated/testified, 5 yrs; Pendergest-Holt obstruction plea, 3 yrs; bars | OK | DAVIS; HLK | — |
| short6 | 2 | say/show, scene | Lopez and Kuhrt convicted at trial, 20 yrs each; Bloomberg: Biden shortened Kuhrt's term Dec 2024 | OK | HLK; BLK | **NOTE, high priority:** Lopez clemency status is unverified (see episode 50). If confirmed, say: "…Bloomberg Law reports President Biden shortened Kuhrt's term in December two thousand twenty-four." becomes "In December two thousand twenty-four, President Biden shortened the terms of both men." (and attribute to the DOJ list). |
| short6 | 3 | say/show, scene | King extradited 2019; 10 years (2021) | OK | KING | — |
| short6 | 4 | say/show, scene | Jan (29) 2025 SEC final judgment against Stanford; $5.9B penalty | OK | SEC25 | — |
| short6 | 5 | — | End | OK | — | — |

## Other checks

- **Private victims:** none named in narration, subtitles or on-screen text. The brief pages that name victim-depositors (PDF pp. 28, 31, 50) are not shown. The top line of `brief_montserrat` begins after "victim-depositor Larson," so the name is cropped out. The `brief_burn` crop names a witness (estate manager), not a victim (NOTE above).
- **Invented dialogue:** none. Every quoted utterance is in a source (OIG, BR, PRS, CA5).
- **Pardons/commutations/reversals:** Stanford: no pardon, commutation, release or reversal found as of 2026-11-04. The conviction was affirmed (CA5), cert was denied (IJ), and compassionate release was denied (BLC). Kuhrt's clemency is mentioned (BLK). Lopez is unverified: possible clemency, see NOTE. Davis, Pendergest-Holt and King: no clemency found.
- **meta.json / thumb.json (out of scope, for information):** consistent with the sources. Thumb "$7 BILLION FRAUD" matches DOJ's headline figure (PRC/PRS).

## Summary

- **FIX: 13 field-level items across 10 lines**
  - episode 9 (hl), 11 (say/show), 19 (hl), 33 (say; doc/cite), 35 (kicker), 38 (say/show), 54 (scene)
  - short1 0 (lines)
  - short3 2 (say/show; doc/cite), 3 (value)
  - short4 2 (kicker)
- **NOTE: 27 items.** One is high priority: verify whether Gilbert Lopez received clemency (episode 50/51, short6 2) before publishing.
- **Overall verdict:** the script is substantially accurate and well attributed. Every number, date and verbatim quote checked out against primary sources, and the $541M figure is correctly taken from the SEC complaint and the brief, not from DOJ's $741M. Required changes:
  - two highlight bands that sit on the wrong passage
  - one image that doesn't match its narration (episode 54)
  - one sequencing error about when the SEC sued (episode 38)
  - "finding" labels on SEC allegations
  - two quote cards that don't name the speaker, with their narration attribution
  - one over-length Shorts line
  - one truncated figure

  **Publishable after the FIX items are applied and the Lopez clemency question is resolved.**

## Resolution (applied by the producer, 2026-11-04)
- All 13 FIX items applied in make_img.py / make_spec.py / make_shorts.py; episode.json and short*.json regenerated.
- Lopez question: Federal Bureau of Prisons inmate locator (register 99141-179, checked via WebFetch 2026-11-04) lists GILBERT T LOPEZ JR as released 12/20/2024. The cause (clemency or otherwise) could not be confirmed from a primary source, so the script states only the BOP fact ("The Bureau of Prisons lists Lopez as released that same month") next to Bloomberg Law's report of Kuhrt's clemency.
- Added: BOP locator lists Robert Allen Stanford (35017-183) at USP Coleman II with a projected release date of 03/13/2103 (episode line 54).
- NOTEs applied: "on paper" for the land mark-up (episode 36, short4 3); "according to the SEC" on the $541M claim (episode 34); Shorts big lines shortened to ≤14 characters. The Antigua move stays at 1990, attributed to the Justice Department release. The brief_burn crop shows the estate manager's name in the brief's text; she is a witness (not a victim) and is not named in narration.
