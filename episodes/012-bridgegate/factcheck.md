# SWORN 012 (Bridgegate): independent fact-check

Checked: episode.json (67 lines), short1/2/3.json (12 lines + titles/hooks), thumb.json (2 variants), meta.json (title + summary). Total of **79 spoken lines** plus the Shorts titles and hooks, the thumbnails and the meta. Every say, show and on-screen field was checked, and every doc-scene highlight was compared with hl.json and with OCR line positions in img/*.jpg.

Sources used:
- USB = Brief for the United States, /home/claude/src/usbrief.txt, page numbers as printed.
- JA = Joint Appendix vol. II, local copy.
- CRS1 = LSB10326. CRS2 = LSB11025.
- OP = Supreme Court slip opinion (WebFetch of supremecourt.gov PDF; direct download was blocked by the proxy).
- DKT = Supreme Court docket.
- DOJ = USAO D.N.J. releases of 11/4/16, 3/29/17, 7/12/17 and 4/24/19 (all fetched).
- AP1 = 6abc, 5/7/20. CNBC = CNBC, 5/7/20. AP2 = fox29, 6/13/20.

Result: **13 FIXes**. 6 are wording, 2 are Shorts packaging and 5 are highlight positions.

## 1. Line table

| Line | Verdict | Source / note |
|---|---|---|
| ep[0] "Why did the Supreme Court throw out…" | **FIX** | OP p.13: "Because the scheme here did not aim to obtain money or property, Baroni and Kelly could not have violated the federal-program fraud or wire fraud laws." The holding covers those two statutes. "Federal fraud law" as a whole is too broad: honest-services fraud (§1346), for example, needs no property. |
| ep[1] "It started with one line…" | OK | JA 917 (GX 145); OP p.3. The quote and the e-mail date are verbatim. |
| ep[2] "Four days of gridlock followed…" | OK | DOJ 11/4/16 (all 7 counts); DKT "opinion for a unanimous Court"; OP has no concurrence or dissent. |
| ep[3] chapter | OK | — |
| ep[4] "The George Washington Bridge connects…" | OK | USB p.3: "250,000 to 300,000", "busiest motor-vehicle bridge in the world". The highlight is band 0, which is correct. |
| ep[5] "It is run by the Port Authority…" | **FIX (hl)** | Text OK (USB p.3). The highlight, band 1, sits on the "create as big a traffic jam" sentence and not on the twelve-lanes and cones sentences. |
| ep[6] "Those three lanes carry…" | **FIX (hl)** | Text OK (USB pp.3–4, "cut through Fort Lee", "roughly 25%"). The highlight again sits on the "traffic jam" sentence. |
| ep[7] "Two officials are at the center…" | OK | USB p.2. The highlight is band 3, which is correct. |
| ep[8] "In 2013, the governor was running…" | OK | OP p.3: "Mayor Sokolich informed Kelly's office that he would not back the Governor's campaign." |
| ep[9] "According to the government, Kelly wanted…" | OK | USB p.4. The title is a verbatim fragment. The highlight is band 0, which is correct. |
| ep[10] "The plan, in the government's words…" | **FIX** | USB p.3 itself puts "create as big a traffic jam as possible" in quotation marks, citing J.A. 269. Per the brief's addendum, J.A. 241–330 is Wildstein's direct testimony. So these are trial-testimony words that the government quotes, not "the government's words". The highlight is band 1, which is correct. |
| ep[11] chapter | OK | — |
| ep[12] "On August 13, 2013, at 7:34…" | OK | JA 917: 7:34 AM, from a yahoo.com personal account. |
| ep[13] "One minute later, Wildstein answered…" | OK | JA 917: 7:35:31, "Got it". |
| ep[14] "There was a problem. As deputy executive director…" | **FIX (hl)** | Text OK (USB p.4, quoting Pet. App. 31a, the Third Circuit). The highlight is band 0, which marks the "Kelly wanted to punish" sentence, not "Baroni lacked the authority". |
| ep[15] "So, the government says, they needed to lie…" | OK | USB p.4. The highlight is band 1, which is correct. |
| ep[16] "The courts called that study a sham…" | **FIX** | The brief's "sham" cites only Pet. App. 28a (the Third Circuit). The Supreme Court did not adopt the word. OP p.11 says only that "By the Government's own account" the study was a "sham". "Courts" (plural) is unsupported. "there was no study" is Executive Director Foye, J.A. 181 (redirect, per the addendum), so that part is OK. The highlight is band 2, which is correct. |
| ep[17] "With only one Fort Lee lane open…" | OK | USB p.6. The highlight is band 0, which is correct. |
| ep[18] "They joked, the brief says…" | OK | USB p.6, verbatim. The highlight is band 1, which is correct. |
| ep[19] chapter | OK | — |
| ep[20] "They picked the date…" | OK | USB p.6: "maximize the impact on Fort Lee", Monday Sept 9, 2013, "the first day of school", no advance knowledge. The highlight is band 2, which is correct. |
| ep[21] "Three local lanes became one…" | OK | USB p.7, J.A. 107. The addendum shows J.A. 102–119 is the direct testimony of Mayor Sokolich, so "a witness" is accurate. The highlight is band 0, which is correct. |
| ep[22] "Fort Lee's chief of police testified…" | OK | USB p.7, verbatim with brackets (J.A. 96 = Chief Bendul). The highlight is band 1, which is correct. |
| ep[23] "First responders were slowed…" | OK | USB p.7. The child is not named. The highlight is band 2, which is correct. |
| ep[24] "The mayor called Baroni…" | OK | USB pp.7–8; JA 918 (Wildstein: "radio silence"). |
| ep[25] "When Wildstein forwarded Kelly a text…" | OK | USB p.8. The highlight is band 0, which is correct. |
| ep[26] "Is it wrong that I'm smiling?" | OK | USB p.8 / J.A. 753 is verbatim. J.A. 753 and 796–797 confirm it was a text message sent 9/10/2013 at 7:04 AM. |
| ep[27] "At trial, Kelly explained…" | OK | JA 916 (sentencing), verbatim; JA 754 (Kelly's testimony). |
| ep[28] "The jams lasted four days…" | OK | USB p.8: "media inquiry". The highlight is band 1, which is correct. |
| ep[29] "He vowed to get to the bottom…" | **FIX (hl)** | Text OK. USB p.8: vowed to "get to the bottom of this abuse of decision [sic]"; "Baroni twice asked…"; "The Executive Director refused." The highlight (band 1) ends at about y 0.635 and so does not reach the vow, the twice-asked or the refused sentences. |
| ep[30] "Two months later, in November 2013…" | OK | DOJ 11/4/16 (Nov 25, 2013, "part of a one-week traffic study"); JA 908, verbatim "was also misled". These were the judge's findings at sentencing. |
| ep[31] chapter | OK | — |
| ep[32] "In 2015, a federal grand jury…" | OK | DOJ 11/4/16 and 3/29/17: "indictment returned May 1, 2015, by a federal grand jury". Wildstein pleaded guilty May 1, 2015 to "two counts of conspiracy". The timeline item "Sept 2016 trial begins" is supported by the USB addendum (government opening Sept 19, 2016). |
| ep[33] "The charges: wire fraud…" | OK | USB p.2 (seven counts listed). The highlight is band 0, which is correct. |
| ep[34] "The trial in Newark lasted six weeks…" | OK | DOJ "six-week trial"; JA 863, verbatim. The highlight is band 0, which is correct. |
| ep[35] "The jury was also told that an honest belief…" | **FIX (hl)** | Text OK (USB p.20: "a complete defense" … jury "roundly rejected" that defense, quoting the Third Circuit). The highlight is band 0, which marks "fourteen … sham work". |
| ep[36] "On November 1, 2016, the jury sent out a question…" | OK | JA 905, verbatim (the note reads "punitive", with a period); date Nov 1, 2016, 12:15. The highlight is band 0, which is correct. |
| ep[37] "Three days later, on November 4…" | OK | Nov 1 → Nov 4 is 3 days. DOJ: "The jury deliberated less than four days"; "convicted on all seven counts". |
| ep[38] "At sentencing, in March 2017…" | OK | JA 914–915, verbatim. |
| ep[39] "People, she said, needlessly suffered…" | OK | JA 915, verbatim. |
| ep[40] "Baroni got 24 months…" | OK | DOJ 3/29/17; USB p.2; DOJ 7/12/17 (Wildstein: three years' probation). That release says "Kelly to 19 months", a typo contradicted by the 3/29/17 release and USB. |
| ep[41] "For Kelly, the judge noted…" | OK | JA 916: "between 37 months and 46 months". 18 months is below that range. |
| ep[42] "On appeal, the Third Circuit threw out…" | OK | USB p.2; DOJ 4/24/19. The highlight is band 2, which is correct. |
| ep[43] chapter | OK | — |
| ep[44] "Baroni had begun serving…" | OK | AP1: "Kelly was weeks from beginning a 13-month sentence … when the Supreme Court agreed to hear the case"; "Baroni had begun serving his 18-month sentence"; DKT granted June 28, 2019. |
| ep[45] "The question was not whether the scheme happened…" | OK | CRS1 p.1: "The federal fraud statutes at issue condemn schemes to obtain money or property." The highlight is correct. |
| ep[46] "The government's answer…" | OK | USB p.21 (Summary of Argument), verbatim title "to hijack Port Authority resources". The highlight is correct. |
| ep[47] "Concretely, the work of fourteen public employees…" | OK | USB p.20, quoting the Third Circuit: "fourteen public employees—eleven toll collectors paid overtime and three professional staff members". The highlight is band 2, which is correct. |
| ep[48] "Payroll records put the toll collectors' extra shifts…" | OK | USB p.18: Pet. App. 47a, "payroll records showed a total cost of $3,696.09", tied to the extra relief toll collectors at overtime. It covers the toll collectors only; the engineers' and other staff's time was separate ($1,828.80). The wording is accurate. |
| ep[49] "Kelly's side answered with a snowplow…" | OK | CRS1 p.3: "a paid public official's decision of which snow-closed streets to plow first … would become a federal crime of fraud if based on unannounced political considerations conflicting with announced reasons." This is a fair paraphrase. The highlight is band 0, which is correct. |
| ep[50] "The appeals court's theory, the petition said…" | OK | CRS1 p.3, verbatim. The highlight is band 1, which is correct. |
| ep[51] "The government replied that this case was different…" | OK | USB pp.21–22 (Summary of Argument). The title "politically motivated" is correctly labeled as the appeals court's words. The highlight is band 1, which is correct. |
| ep[52] "The justices heard the case on January 14, 2020." | OK | DKT. |
| ep[53] chapter | OK | — |
| ep[54] "On May 7, 2020, Justice Elena Kagan…" | OK | DKT "Kagan, J., delivered the opinion for a unanimous Court." |
| ep[55] "The evidence the jury heard…" | OK | OP p.2, verbatim. |
| ep[56] "But the federal fraud statutes at issue…" | OK | OP p.2, verbatim. |
| ep[57] "The lanes, the Court said, were not property taken…" | OK | OP p.8, verbatim q; OP p.9: "nor did they take the lanes from the Government"; p.10: "cannot count as the taking of property". |
| ep[58] "And the employees' time?…" | OK | OP p.12, verbatim. |
| ep[59] "For no reason other than political payback…" | **FIX (show)** | OP pp.12–13. The quoted sentence continues: "…access lanes to the George Washington Bridge—and thereby jeopardized the safety of the town's residents." The show closes the quotation with a period mid-sentence, so it needs an ellipsis. The q card ("But not every corrupt act…", p.13) is verbatim and OK. |
| ep[60] "Federal prosecutors, the Court said…" | OK | OP p.12: "Federal prosecutors may not use property fraud statutes to “set[] standards of disclosure and good government for local and state officials.”" The opinion prints "set[]", so the bracket matches. CRS1 matches too. |
| ep[61] "Judgment reversed." | OK | DKT: "Judgment REVERSED and case REMANDED." |
| ep[62] "In June 2020, a federal judge dismissed the indictments…" | OK | AP2: the judge dismissed the indictments of Baroni and Kelly (Friday, June 12) and vacated Wildstein's conviction. The Wildstein tweet is verbatim. |
| ep[63] "Kelly said the ruling gave me back my name…" | OK | CNBC: the court "gave me back my name and began to reverse…"; "Christie was never charged … has repeatedly denied knowing about the plan." AP1 and AP2 agree. The wording is neutral. |
| ep[64] "The line Kelly drew did not stay in Fort Lee…" | **FIX** | CRS2 p.1: "In Ciminelli and Percoco, the Court reversed two wire-fraud convictions"; it "upheld wire fraud convictions" (plural) in Kousisis. "upheld one" is inaccurate. "The line Kelly drew" can be heard as Bridget Kelly drawing it. The highlight is correct. |
| ep[65] "So the answer to the question is simple…" | **FIX** | "The jury was right about what happened" is the channel's own verdict, and no court said it in those words. The Supreme Court said "The evidence the jury heard no doubt shows wrongdoing". State that finding instead. |
| ep[66] outro | OK | — |
| short1 title / hook | OK | Verbatim (title-cased). |
| short1[0] "Time for some traffic problems…" | OK | JA 917: the e-mail body is exactly that one line; the reply was "Got it". |
| short1[1] "On the first day of school…" | OK | USB p.6; DOJ "from three to one"; four days. The highlight is band 1, which is correct. |
| short1[2] "A jury convicted her on every count…" | OK | DOJ; DKT. |
| short1[3] outro | OK | — |
| short2 title "$3,696.09 in Overtime Decided the Bridgegate Case" | **FIX** | This overstates. The Court held the opposite: the labor cost was an "incidental byproduct" (OP p.12), and the case turned on the scheme's object, not on the $3,696.09. |
| short2 hook "$3,696.09 IN OVERTIME" | OK | USB p.18 (overtime relief toll collectors). |
| short2[0] "$3,696.09. Payroll records…" | OK | USB p.18. |
| short2[1] "Prosecutors said the employees' time was property…" | OK | USB pp.10–11, 20. Framed as the prosecutors' claim. The highlight is band 2, which is correct. |
| short2[2] "The Supreme Court disagreed, 9–0…" | OK | OP p.12, verbatim fragment. |
| short2[3] outro | OK | — |
| short3 title "Guilty on All 7 Counts. Then the Supreme Court Said 9–0." | OK | Literally true. See the note on the hook. |
| short3 hook "ALL 7 COUNTS → REVERSED 9–0" | **FIX** | This says the Supreme Court reversed all 7 counts. It reversed only the 5 remaining fraud and conspiracy counts; the Third Circuit had already vacated the 2 civil-rights counts (USB p.2; DOJ 4/24/19). |
| short3[0] "What the jury found: guilty on all seven counts…" | OK | DOJ. The motive is framed as "prosecutors said". |
| short3[1] "What the Supreme Court found…" | OK | OP p.2, verbatim. |
| short3[2] "But not every corrupt act…" | OK | OP p.13, verbatim. |
| short3[3] outro | OK | — |
| thumb A "THROWN OUT / GUILTY. THEN 9–0." | OK | DOJ; DKT. |
| thumb C "TRAFFIC PROBLEMS / THE BRIDGEGATE CASE / REVERSED" | OK | JA 917; DKT. |
| meta title | OK | — |
| meta summary | OK | OP pp.2, 12–13; DOJ; USB pp.6, 18. "deception, corruption, abuse of power" is verbatim. |

## 2. FIXes (ready to paste)

**F1. episode.json line 0** (say; no show)
- say: `Why did the Supreme Court throw out the Bridgegate convictions? Because, a unanimous Court ruled, the scheme was not aimed at money or property. And the federal fraud laws they were convicted under require that it is.`
- Why: OP p.13 limits the holding to the federal-program fraud (§666) and wire fraud statutes. Not every federal fraud law needs property; honest-services fraud is one example.

**F2. episode.json line 5** (scene)
- `"hl": [0.0, 0.4228, 1.0, 0.1099], "pan": [0.179, 0.239]`
- Why: band 1 (0.358–0.429) marks "create as big a traffic jam…". The twelve-lanes and cones sentences sit at y 0.4228–0.5327 (OCR of usb_bridge.jpg). The pan was recomputed with panfix.py geometry so the band stays in frame.

**F3. episode.json line 6** (scene)
- `"hl": [0.0, 0.5746, 1.0, 0.091], "pan": [0.321, 0.381]`
- Why: the "cut through Fort Lee … roughly 25%" sentences sit at y 0.5746–0.6656. The current band marks the "traffic jam" sentence.

**F4. episode.json line 10** (say + show)
- say: `The plan, according to the government: create as big a traffic jam as possible in Fort Lee.`
- show: `The plan, according to the government: to "create as big a traffic jam as possible" in Fort Lee.`
- Why: in the brief these words are themselves a quotation (J.A. 269, from Wildstein's trial testimony), so they are not "the government's words".

**F5. episode.json line 14** (scene)
- `"hl": [0.0, 0.1958, 1.0, 0.0537], "pan": [0.0, 0.05]`
- Why: "Baroni lacked the authority … unilaterally" is at y 0.1958–0.2495 of usb_lie.jpg. Band 0 (0.5096) marks "Kelly wanted to punish Fort Lee's mayor". The old pan of 0.244 would also scroll the correct band out of view.

**F6. episode.json line 16** (say + show)
- say: `The appeals court called that study a sham. The Port Authority's executive director later testified: there was no study.`
- show: `The appeals court called that study a "sham." The Port Authority's executive director later testified: "there was no study."`
- Why: the only source for "sham" is the Third Circuit (Pet. App. 28a, cited in the brief and in CRS1). The Supreme Court attributed the word to "the Government's own account" (OP p.11).

**F7. episode.json line 29** (scene)
- `"hl": [0.0, 0.6125, 1.0, 0.1099], "pan": [0.369, 0.429]`
- Why: the vow, "Baroni twice asked…" and "The Executive Director refused" sit at y 0.6125–0.7224 of usb_smile.jpg. Band 1 ends at 0.6354.

**F8. episode.json line 35** (scene)
- `"hl": [0.0, 0.1391, 1.0, 0.072]` (pan [0.0, 0.0] can stay)
- Why: "a complete defense … roundly rejected" is at y 0.1391–0.2111 of usb_14.jpg. Band 0 marks "fourteen … sham work".

**F9. episode.json line 59** (show only; say can stay)
- show: `"For no reason other than political payback, Baroni and Kelly used deception to reduce Fort Lee's access lanes . . . ." "But not every corrupt act by state or local officials is a federal crime."`
- Why: the opinion's sentence continues past "access lanes" ("…to the George Washington Bridge—and thereby jeopardized the safety of the town's residents."). A closing period inside the quotation marks implies the sentence ends there, so verbatim rules require an ellipsis.

**F10. episode.json line 64** (say + show)
- say: `The line drawn in Kelly did not stay in Fort Lee. In twenty twenty-three, the Court reversed two more wire-fraud convictions, in Ciminelli and Percoco. In twenty twenty-five, in Kousisis, it upheld wire-fraud convictions.`
- show: `The line drawn in Kelly did not stay in Fort Lee. In 2023, the Court reversed two more wire-fraud convictions, in Ciminelli and Percoco. In 2025, in Kousisis, it upheld wire-fraud convictions.`
- Why: CRS2 p.1 says the Court "upheld wire fraud convictions" (plural) in Kousisis. "The line Kelly drew" reads as if Bridget Kelly drew it.

**F11. episode.json line 65** (say; no show)
- say: `So the answer to the question is simple, and uncomfortable. The Court said the evidence no doubt showed wrongdoing. And it ruled that this still was not federal fraud.`
- Why: "The jury was right about what happened" is the narrator's own judgment. The sourced finding is the Supreme Court's own line (OP p.2), so state that.

**F12. short2.json title**
- title: `$3,696.09 in Overtime: The "Property" in the Bridgegate Case`
- Why: "Decided the Bridgegate Case" overstates and inverts the holding. The Court called the labor cost an "incidental byproduct" (OP p.12). $3,696.09 was the government's property theory (via the Third Circuit's payroll finding), not what decided the case.

**F13. short3.json hook**
- hook: `GUILTY →|REVERSED 9–0`. The title can stay.
- Why: the current hook "ALL 7 COUNTS → REVERSED 9–0" says the Supreme Court reversed seven counts. The Third Circuit had already vacated the two civil-rights counts (USB p.2; DOJ 4/24/19); the Supreme Court reversed the remaining five.

## 3. Notes (no change required)
- The direct download of the opinion PDF was blocked by the proxy. Opinion quotes were verified through WebFetch, with exact-text queries for the bracket "set[]", the "byproduct" sentence (p.12) and the "sham" usage.
- The DOJ release of 7/12/2017 says "Kelly to 19 months". That is an error in the release; the 3/29/2017 release and the SG brief both say 18 months. The script uses 18, which is correct.
- The ep[32] timeline "src" cites only DOJ releases for "Sept 2016, trial begins". The opening date (Sept 19, 2016) comes from the USB addendum, which could be added to src.
