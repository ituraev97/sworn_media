# Fact-check — SWORN 011: U.S. v. Ramesh "Sunny" Balwani

Checked 2026-11-11 by an independent fact-checker (did not write the script).
Sources: local text copies in /home/claude/docs (ca9 = 9th Cir. Order & Amended Opinion, Dec 22, 2025, page = opinion page; sec = SEC complaint, allegations; tsi = Third Superseding Indictment; ind = 2018 indictment; memo = U.S. sentencing memo re Holmes, ECF page; fix = ECF 1811; ord = ECF 1816).
Web sources: all four fetched successfully on 2026-11-11 and are marked **WEB-OK**: DOJ release Dec 7, 2022; AP via katv.com; Supreme Court docket 25-1330; InvestmentNews Mar 31, 2026.
Highlight boxes: every distinct doc image and `hl` box was cropped and viewed.

Verdicts: **OK** = matches the source. **FIX** = must change; the exact replacement is given. **NOTE** = acceptable, with an optional improvement.

## episode.json

| # | Verdict | Source | Finding / replacement |
|---|---|---|---|
| 0 | NOTE | ca9 p.9, 16–17 | "Same fraud" is loose, because Holmes was acquitted of the patient fraud (which the episode itself stresses). They were charged with the same indictment and the same range. Optional: "Same company. Same indictment. Same judge." |
| 1 | **FIX** | ca9 p.9, 16–17; DOJ (WEB-OK) | Numbers and range are OK. Balwani was the *former* president/COO at sentencing (employed Sept 2009–July 2016). **say:** "Holmes got one hundred thirty-five months. Balwani, Theranos's former president and chief operating officer, got one hundred fifty-five." **show:** "Holmes got 135 months. Balwani, Theranos's former president and chief operating officer, got 155." |
| 2 | OK | ca9 p.16 | Holmes acquitted on Counts 2, 10–12; Balwani convicted of all counts (1–12). The `hl` box covers "The jury convicted Balwani of all counts…" (verified). |
| 3 | OK | SCOTUS docket 25-1330 (WEB-OK) | Petition denied Oct 5, 2026. Sub "San Jose · 2022" OK (ind cover: San Jose Division). |
| 4 | OK | — | Chapter card. |
| 5 | NOTE | ca9 p.8 | Quote OK; `hl` covers it. The opinion has "[O]ne"; the show line capitalizes "One" without the bracket. Acceptable at sentence start. |
| 6 | OK | ca9 p.8–9 | 2003 founding; "fast, accurate, and affordable tests with just a drop of blood drawn from the prick of a finger". Title "nothing more than a mirage" is verbatim and inside the `hl` box. |
| 7 | OK | sec ¶17 p.4 | Attributed to the SEC; kicker says AS ALLEGED. The line text is verbatim in substance and the `hl` box covers ¶17. (The 9th Cir. p.9 says "later appointed" president/COO; the SEC framing is attributed, so OK.) |
| 8 | OK | ca9 p.9–10 | 2004–2016, "evidence offered at both showed", oversaw operations in the patient-testing lab, "primary contact" for Safeway and Walgreens. Title verbatim; `hl` OK. |
| 9 | OK | DOJ release (WEB-OK) | "nearly 30 million shares of Theranos – over 6% of the company". Kicker 2009–2016 matches Sept 2009–July 2016. |
| 10 | OK | — | Chapter card. |
| 11 | **FIX (hl)** | ca9 p.13 | Text is OK (controller testimony: no revenue 2012/2013, $57M and $92M net losses). The `hl` box [0,0.3885,1,0.0825] starts at "respectively…" and **misses the $57M/$92M line**. **Replace hl with** `[0.0, 0.3495, 1.0, 0.0390]` (covers "did not have any revenue in 2012 and 2013 … suffered $57 million and $92 million in net losses"). say/show unchanged. |
| 12 | OK | ca9 p.13 | "In November 2013, Balwani told Holmes that Theranos was down to $15 million in cash, but the company was spending up to $2 million weekly." Title verbatim; `hl` covers it. |
| 13 | **FIX** | sec ¶2, ¶47, ¶77 | "$700M, late 2013 to 2015" is OK and attributed. "Investors typically got a binder" is stated as fact but comes only from the SEC complaint (¶47). **say:** "From late twenty thirteen to twenty fifteen, the S.E.C. said, Theranos raised more than seven hundred million dollars from investors. Investors typically got a binder, the complaint says. And the SEC alleged that Balwani drafted the financial information inside it." **show:** "From late 2013 to 2015, the SEC said, Theranos raised more than $700 million from investors. Investors typically got a binder, the complaint says. And the SEC alleged that Balwani drafted the financial information inside it." Title verbatim (¶77); `hl` OK. |
| 14 | OK | sec ¶77, ¶80 | >$100M revenue for 2014, ~$1B for 2015; "little more than $100,000" recorded. Bars are labeled AS ALLEGED BY THE SEC. |
| 15 | **FIX** | sec ¶80–81 p.18 | The second sentence (insurers, $120–140M) reads as established fact but is an SEC allegation. "year-end figures" should say these were revenue projections. **say:** "The S.E.C. alleged that Theranos actually recorded little more than one hundred thousand dollars in revenue in twenty fourteen. And it alleged that in October of that year, the same month he gave investors year-end revenue projections of one hundred twenty to one hundred forty million dollars, Balwani told potential insurers the company was losing eight to nine million dollars a month." **show:** "The SEC alleged that Theranos actually recorded little more than $100,000 in revenue in 2014. And it alleged that in October of that year, the same month he gave investors year-end revenue projections of $120 to $140 million, Balwani told potential insurers the company was losing $8 to $9 million a month." Title verbatim; `hl` OK. |
| 16 | OK | ca9 p.38–40 | SEC deposition; "financial model" vs. "financial projections"; "expressly disclaiming responsibility for the financial projections". Kicker PAGE 40 is correct; `hl` covers the passage. |
| 17 | **FIX** | AP (WEB-OK) | AP says Davila "said the numbers Balwani drew up were false" and called them lies. AP does not say he was responding to the model/projections distinction, so "addressed exactly that" overstates the link. **say:** "At his sentencing, Judge Edward Davila spoke about the projections Balwani drew up, the Associated Press reported. The projections, he said:" (no show needed). |
| 18 | OK | AP (WEB-OK) | "weren't just projections, they were lies" is verbatim. The quote card says "As quoted by Associated Press"; the ellipsis is used correctly in the show line. |
| 19 | OK | — | Chapter card. |
| 20 | **FIX** | sec ¶5 p.2–3; ca9 p.12 | 12 of 200+ tests is OK as an SEC allegation. "Investors were told…" is stated as fact. The source (ca9 p.12) is investors' testimony that they were misled into believing this. "bought from other companies" is not in the source, which says "third-party commercially available analyzers". **say:** "Investors testified they were led to believe Theranos ran its tests on its own machines. The S.E.C. alleged that in its clinical lab, the proprietary analyzer ran only about twelve of the more than two hundred tests on the menu. The rest ran on commercially available analyzers made by other companies, some modified for fingerstick samples." **show:** "Investors testified they were led to believe Theranos ran its tests on its own machines. The SEC alleged that in its clinical lab, the proprietary analyzer ran only about 12 of the more than 200 tests on the menu. The rest ran on commercially available analyzers made by other companies, some modified for fingerstick samples." |
| 21 | OK | ca9 p.12–13 | VIP guests "including investors"; the device was running a "null protocol"; samples were "surreptitiously" run on third-party devices. Title verbatim; `hl` OK. |
| 22 | OK | ca9 p.15; ca9 p.8 | Logos (Pfizer etc.), Holmes's admission, no validation or authorization; reports were shared with investors. Title "half-truths and outright lies" is verbatim (p.8) and inside the `hl` box. |
| 23 | OK | sec ¶63 p.14 | Attributed as an allegation; "75 percent" verbatim; `hl` OK. |
| 24 | OK | sec ¶64; ca9 p.13–14 | ~$300,000 from three DOD contracts (attributed to the complaint). The Mattis testimony matches ca9. Title verbatim; `hl` OK. |
| 25 | OK | ca9 p.10, 14 | "primary contact"; Walgreens rep testified the partnership was "actually contracting". |
| 26 | OK | — | Chapter card. |
| 27 | NOTE | ca9 p.10–12; memo p.28–29 | "ran the operations of the lab" ≈ "oversaw operations". Optional: "He oversaw the lab's operations." "Here is what set Balwani's case apart" is editorial framing, not a court finding. |
| 28 | OK | memo ECF p.28 | Late May 2014, Rosendorff halted hCG on the Theranos analyzer "in light of inaccurate results"; Balwani "immediately passed along that news". `hl` OK. (Optional: "the government's sentencing memo for Holmes".) |
| 29 | OK | memo ECF p.28–29 | Bicarbonate "lost all diagnostic value"; forwarded to Holmes; the PT/INR low-readings study. `hl` OK. |
| 30 | OK | memo ECF p.29 | "Always another study after the fact." is verbatim and labeled "As quoted in"; dated 2014 ("around that same time" as August 2014). |
| 31 | OK | memo ECF p.29 | Late Nov 2014 text; the "Normandy lab (where Theranos conducted its proprietary testing)"; "disaster zone" verbatim (the original reads "f___ing disaster zone"). `hl` OK. |
| 32 | **FIX** | ca9 p.28 | (a) The quote is cut before "that we do on this . . . system", which removes the qualifier and makes it sound like one in four of *all* tests failed. (b) The `hl` box [0,0.7452,1,0.0825] covers "if you just extrapolate…there's" and **misses the quoted words**. **say:** "A lab associate, Erika Cheung, testified that there was something still going on that is causing one out of four failures of every single test that we do on this system." **show:** "A lab associate, Erika Cheung, testified there was \"something still going on that is causing one out of four failures of every single test that we do on this . . . system.\"" **hl:** `[0.0, 0.8140, 1.0, 0.0560]`. |
| 33 | **FIX** | tsi ¶16 p.6–7 | The indictment *alleges* that the defendants knew Theranos was "not capable of consistently producing accurate and reliable results" for these tests. The line states it as fact. **say:** "The indictment lists tests it alleged Theranos could not consistently get right, from cholesterol and glucose to H.I.V., P.S.A. and h.C.G." **show:** "The indictment lists tests it alleged Theranos could not consistently get right, from cholesterol and glucose to HIV, PSA and hCG." `hl` covers the list (OK). |
| 34 | NOTE | ca9 p.15 | Accurate. The source says "incorrect results from a Theranos blood test about her pregnancy"; "a pregnancy test" is acceptable. No patients are named. Title verbatim; `hl` OK. |
| 35 | **FIX** | tsi p.10 (Count 12) | "one of those ad buys" ties Count 12 to the *Arizona* ads in line 34. Count 12 is an EFT to Horizon Media (New York) "to purchase advertisements for Theranos Wellness Centers" and names no state. **say:** "Count twelve of the indictment is an ad buy: on August third, twenty fifteen, one million, one hundred twenty-six thousand, six hundred sixty-one dollars wired to buy advertising for Theranos Wellness Centers." **show:** "Count 12 of the indictment is an ad buy: on August 3, 2015, $1,126,661 wired to buy advertising for Theranos Wellness Centers." `hl` OK. |
| 36 | OK | memo ECF p.29; ca9 p.4, 12 | "void every single Edison test following extremely negative CMS findings" is verbatim in the title; `hl` OK. |
| 37 | OK | — | Chapter card. |
| 38 | OK | ind p.1 (Jun 14, 2018); DOJ (WEB-OK); ca9 p.9 | Grand jury true bill, June 2018. TSI: 2 conspiracies + 10 wire fraud counts (memo ECF p.20). |
| 39 | OK | DOJ (WEB-OK) | "investigation by the FBI, USPIS, and the FDA Office of Criminal Investigations". |
| 40 | **FIX (hl)** | memo ECF p.20; fix p.3; ord p.1; ca9 p.16 | Text OK: Jan 3, 2022; 4 investor counts; acquitted on patient counts; hung on 3 (Counts 3–5). The `hl` box [0,0.6366,1,0.2054] highlights **Balwani's** conviction, but the title says "Holmes: guilty on 4". **Replace hl with** `[0.0, 0.0, 1.0, 0.155]` (top of ca9_all: "…investor-related conspiracy (Count 1), and wire fraud relating to three investor-victims (Counts 6–8). The jury hung … (Counts 3–5)."). Optional: add the memo (ECF 1643) to src for the Jan 3 date. |
| 41 | NOTE | memo ECF p.20; ca9 p.16; AP (WEB-OK) | Began March 2022, same twelve counts, nearly four months; AP: "he chose not to testify". Kicker "ONE COURTROOM" is unsourced (same court and judge is sourced). Optional kicker: "TWO TRIALS · ONE JUDGE". |
| 42 | OK | fix p.3 | "On July 7, 2022, a jury found Defendant Ramesh Balwani guilty of all counts alleged in the Third Superseding Indictment." `hl` OK. |
| 43 | OK | ca9 p.9, 16 | Investor counts 1, 3–8 = 7; patient counts 2, 9–12 = 5; 12 of 12. Holmes was acquitted of the patient counts. |
| 44 | OK | — | Chapter card. |
| 45 | OK | AP (WEB-OK) | 15 years sought; "four to 10 months recommended by his lawyers"; "never sought the fame…"; "is not Ms. Holmes" (Coopersmith); "declined Davila's invitation to make a statement". |
| 46 | OK | AP (WEB-OK) | Schenk quote verbatim, "As quoted by AP". (AP refers to Schenk as the prosecutor; the AUSA title is correct for Dec 2022.) |
| 47 | OK | ca9 p.16–17; fix p.3 | Same victims/loss findings; 135–168; Holmes 135; Balwani 155; $25,000 fine. Title verbatim; `hl` OK. |
| 48 | OK | DOJ (WEB-OK) | Quote verbatim; Stephanie M. Hinds was U.S. Attorney in Dec 2022. |
| 49 | **FIX** | ca9 p.17 | The source says "jointly and severally liable". "owed jointly" misstates the liability (it implies each owes only a share). **say:** "In May twenty twenty-three, the court ordered restitution: four hundred fifty-two million dollars, with Holmes and Balwani each liable for the full amount, to investors and to Safeway and Walgreens." **show:** "In May 2023, the court ordered restitution: $452 million, with Holmes and Balwani jointly and severally liable, to investors and to Safeway and Walgreens." `hl` OK. |
| 50 | OK | — | Chapter card. |
| 51 | OK | ca9 p.3, 5, 17–18 | Lay witnesses gave improper expert opinions; constructive amendment (paraphrased fairly). The `hl` box covers the filed/amended dates (title "Holmes · Balwani" is generic; acceptable). |
| 52 | NOTE | ca9 p.3, 5, 27, 44 | "veered into expert territory" and "plainly gave" are verbatim (amended opinion). The quotes come from the Dec 2025 amended text and are attributed to Feb 2025. The holding is unchanged, but optional: "In February twenty twenty-five, the Ninth Circuit affirmed. In its opinion, it agreed…" Verdict card dates are OK. |
| 53 | OK | ca9 p.7 (Order); SCOTUS docket (WEB-OK) | Rehearing denied Dec 22, 2025; petition May 21, 2026; waiver Jun 9, 2026; denied Oct 5, 2026; Thomas took no part. |
| 54 | OK | ord p.1, 9–10; InvestmentNews (WEB-OK) | Mar 26, 2026; Amendment 821; 135 → 123. |
| 55 | **FIX** | ca9 p.16; sec ¶77; ca9 p.9–10 | In the conclusion, "He drafted the numbers investors saw, according to the S.E.C." reads as fact. It is an SEC allegation, so it should be framed as one. **say:** "So why more time for Balwani? The record gives the pieces. Every count against him ended in a guilty verdict, including defrauding patients. The S.E.C. alleged he drafted the numbers investors saw. And he oversaw the lab the warnings came from." **show:** "So why more time for Balwani? The record gives the pieces. Every count against him ended in a guilty verdict, including defrauding patients. The SEC alleged he drafted the numbers investors saw. And he oversaw the lab the warnings came from." |
| 56 | OK | ca9 p.8, 16 | Callback. |
| 57 | OK | — | Outro. |

## short1.json

| # | Verdict | Source | Finding / replacement |
|---|---|---|---|
| title | **FIX** | AP (WEB-OK) | The AP quote is the fragment "weren't just projections, they were lies". The title adds an unbracketed "They" and splits it into two quoted sentences. **title:** "\"[They] Weren't Just Projections, They Were Lies.\"" |
| hook | OK | AP | "THEY WERE LIES." is a verbatim fragment. |
| 0 | **FIX** | AP (WEB-OK); DOJ | (a) The show line puts the non-verbatim "They weren't… They were lies." inside quotation marks. (b) "Theranos president" is wrong for Dec 2022, when he was former president. **say:** "They weren't just projections. They were lies. A federal judge said that at the sentencing of former Theranos president Sunny Balwani, the A.P. reported." **show:** "\"…weren't just projections, they were lies.\" A federal judge said that at the sentencing of former Theranos president Sunny Balwani, the AP reported." The quote card is OK. |
| 1 | OK | sec ¶77, ¶80 | Attributed ("The SEC alleged… It said"). Optional: "It alleged". `hl` OK. |
| 2 | OK | ca9 p.16–17 | All twelve counts; 155 months. |
| 3 | OK | — | Outro. |

## short2.json

| # | Verdict | Source | Finding / replacement |
|---|---|---|---|
| title/hook | OK | ca9 p.16–17 | 135 vs. 155. |
| 0 | NOTE | ca9 p.16–17 | Numbers OK. "Same fraud" is loose (see episode line 0). |
| 1 | OK | ca9 p.16 | `hl` OK. |
| 2 | OK | ca9 p.15; SCOTUS docket (WEB-OK) | "linked Balwani to the transmission of these inaccurate results"; denied Oct 5, 2026. |
| 3 | OK | — | Outro. |

## short3.json

| # | Verdict | Source | Finding / replacement |
|---|---|---|---|
| title/hook | OK | tsi p.10; memo ECF p.29 | $1,126,661; "disaster zone" is his text as quoted in the government's memo. |
| 0 | OK | tsi p.10 | 8/3/2015 EFT to buy ads for Theranos Wellness Centers. `hl` OK. |
| 1 | OK | memo ECF p.29 | Nov 2014 is about 8 months before Aug 2015, so "months earlier" is right. He was president in 2014, so the title is correct for that date. `hl` OK. |
| 2 | OK | tsi; fix p.3; ca9 p.17 | Count 12 → convicted on all → 155 months. |
| 3 | OK | — | Outro. |

## meta.json / thumb.json

| Field | Verdict | Source | Finding / replacement |
|---|---|---|---|
| meta.title | OK | ca9 p.16–17 | |
| meta.summary | **FIX** | DOJ (WEB-OK) | "Theranos's president and COO" is wrong for the 2022 sentencing. Replace with "Theranos's former president and COO". The rest is OK: SEC items are labeled "as alleged"; $1,126,661; July 7, 2022; 155 months; $452M; Oct 5, 2026. Optional: "declined to hear his appeal" → "declined to hear his case" (it was a cert petition). |
| meta.docs_note / sources | OK | — | ECF numbers and dates match sources.md and the documents. |
| thumb A | OK | ca9 p.16 | "ALL 12 COUNTS", "THE OTHER THERANOS VERDICT". |
| thumb C | OK | ca9 p.16–17 | "135 vs. 155", "WHY HE GOT MORE TIME", stamp GUILTY. |

## Checks with no problems

- No private investors or patients are named (the opinion's investor names were not used).
- No abuse allegations are mentioned (the opinion's severance reason was correctly left out).
- "Jury" vs. "court" is correct throughout: the court ordered severance and restitution, and the juries returned the verdicts.
- Count arithmetic is correct: 7 investor counts + 5 patient counts = 12.

## FIX count: 15

episode.json lines 1, 11 (hl), 13, 15, 17, 20, 32 (text + hl), 33, 35, 40 (hl), 49, 55 = 12 · short1 title, short1 line 0 = 2 · meta.summary = 1 → **15 FIXes**.

## Applied (2026-11-11)
All 15 FIXes applied in make_spec.py (setline block), make_shorts.py and meta.json; also applied NOTEs: "Same indictment" instead of "Same fraud" (episode line 0, short2), kicker "TWO TRIALS · ONE JUDGE", "oversaw" (line 27), "It alleged" (short1). Final build from the fixed json.
