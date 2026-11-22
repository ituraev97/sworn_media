# Fact-check — SWORN 022 "Juror 52" (independent review, 2026-11-22)

Sources are cited by short name:
- **277**: gov't sentencing memo for Ali (24-cr-173 Dkt. 277)
- **216**: memo for Abdiaziz (Dkt. 216)
- **251**: memo for Said (Dkt. 251)
- **243**: memo for Nur (Dkt. 243)
- **203**: memo for Abdulkarim (Dkt. 203)
- **207**: minutes for Abdulkarim (Dkt. 207)
- **155**: Abdulkarim plea agreement (Dkt. 155). It was signed by all parties and filed 4-2-2025.
- **230 / 231**: minutes (Dkt. 230) and judgment (Dkt. 231) for Abdiaziz
- **579**: Said's judgment of acquittal (22-cr-124 Dkt. 579)
- **929**: Nur's fraud-case memo (22-cr-124 Dkt. 929)
- **PR24 / PRNUR / PRALI**: USAO releases of Jun 26, 2024, Jul 23, 2024 and Sep 5, 2024
- **MPR-1120**: MPR News, Nov 20, 2026. I fetched it live; its quotes match the notes. It also says Nur got five years "consecutive to his 10-year term for fraud" and calls the case the "first Feeding Our Future fraud trial".
- **CBS-1119**: CBS Minnesota, Nov 19, 2026. I fetched it live; it does not say whether Nur's term is consecutive.
- **AP-PBS**: AP via PBS, Jun 4, 2024. I fetched it live. It calls Feeding Our Future a "Minnesota nonprofit" and says defendants "allegedly produced invoices for meals that were never served". It says Thompson made the quote "in court on Monday, according to the Star Tribune". Prosecutors called it "one of the largest COVID-19-related fraud cases in the country".
- **AP-ABC**: AP via ABC, Jun 2024
- **MPR-0722 / KSTP-0722**: MPR News and KSTP, Jul 22, 2026
- **MPR-0521**: MPR News, May 21, 2026. I fetched it live; it says "Feeding Our Future founder Aimee Bock".

Verdicts: **OK** means accurate and sourced. **FIX** gives the exact replacement. Lines not mentioned under a FIX are unchanged.

---

## episode.json (indices 0–68)

| # | Verdict | Notes / replacement | Source |
|---|---|---|---|
| 0 | OK | 8:50 PM, rang bell, Hallmark gift bag; title "Two Hallmark gift bags" | 277 p3; PRALI |
| 1 | OK | "present" for Juror 52, more if she voted not guilty; stepfather | 216 p3; 277 p3 |
| 2 | **FIX** | "biggest pandemic fraud trial in Minnesota" is not supported by any source. **say:** "His stepdaughter is Juror fifty-two, in the first Feeding Our Future fraud trial. Inside the bag: one hundred twenty thousand dollars in cash." **show:** "His stepdaughter is Juror 52, in the first Feeding Our Future fraud trial. Inside the bag: $120,000 in cash." | MPR-1120 ("first Feeding Our Future fraud trial"); KSTP-0722; PRALI |
| 3 | OK | $200,000 / $80,000 kept | PRALI; 277 p3 |
| 4 | OK | Juror called police | 216 p3; AP-PBS |
| 5 | OK | Nov 20, 2026; last of five; all pleaded guilty; 4 years. Kicker "ST. PAUL" is not firmly verified (see the list below). | MPR-1120; CBS Nov 20 |
| 6 | **FIX** | The scene sub "sentenced Nov 18–20, 2026" is wrong: the sentences ran from Mar 4 to Nov 20, 2026. **sub:** "United States v. Farah et al. · D. Minn. 24-cr-173 · sentenced Mar 4 – Nov 20, 2026" | 207; 230; MPR-1120 |
| 7 | OK | — | — |
| 8 | OK | "Minnesota nonprofit"; federal child-nutrition program | AP-PBS; 929 p2 |
| 9 | OK | "prosecutors say" meals never served; >$250M per AP; "the largest Covid-19 fraud scheme in the United States" is verbatim | AP-PBS; AP-ABC; 929 p1 |
| 10 | **FIX** | Empire Cuisine was not "one of the sites" of Feeding Our Future's network. 929 says the scheme "originated out of" it, and its sponsor was Partners In Nutrition (929 p5). **say:** "This trial's scheme, prosecutors say, started at a small halal market in Shakopee, called Empire Cuisine and Market. It enrolled in the program in April twenty twenty." **show:** "This trial's scheme, prosecutors say, started at a small halal market in Shakopee, called Empire Cuisine & Market. It enrolled in the program in April 2020." | 929 p2, p5 |
| 11 | **FIX** | The source says "Nur and his co-defendants claimed", not "Empire Cuisine and its partners". **say:** "According to prosecutors, at the peak, Nur and his co-defendants claimed to serve two point seven million meals to children, in the month of March twenty twenty-one alone. Many of the sites, prosecutors wrote, were nothing more than parking lots or vacant commercial spaces." **show:** "According to prosecutors, at the peak, Nur and his co-defendants claimed to serve 2.7 million meals to children, in the month of March 2021 alone. Many of the sites, prosecutors wrote, were \"nothing more than parking lots or vacant commercial spaces.\"" | 929 p3 |
| 12 | **FIX (src only)** | The text is OK: 79 charged per MPR; Apr 22, 2024; seven defendants; Judge Brasel. The "first seven went on trial … before Brasel" claim comes from PR24, not 277. **src:** append "; U.S. Attorney's Office, D. Minn., press release (Jun 26, 2024)" | MPR-0521; PR24; 277 p1 |
| 13 | **FIX** | The narration is OK (929 p3). The **image is wrong**: `img/ex_texts.jpg` (from i929/x-007.png) is an email from Nur to his sister dated June 21, 2021. It is not Exhibit H-51b and not a message between Abdiaziz and Nur. It also shows a private person's personal Gmail address. **Fix:** rebuild `ex_texts.jpg` from `/home/claude/work/fof/dl/r2/i929/x-001.png`. That is the WhatsApp exhibit labelled "GOVERNMENT EXHIBIT H-51b", with headers "Abdimajid bro (Abdimajid Nur)" and "Abdiaziz Farah" and no photos of people. Keep caption "GOV'T TRIAL EXHIBIT H-51b · MESSAGES BETWEEN ABDIAZIZ FARAH AND ABDIMAJID NUR". Do **not** use x-008 or x-009, which contain photos of the defendants. | 929 exhibits |
| 14 | OK | >$900,000 (chart $913,613.04); caption "APR 2021 – JAN 2022" matches the chart (4/5/2021–1/31/2022); $12,000 to take courses | 929 p9, p11 |
| 15 | **FIX** | The jury size is unsourced, and AP says alternates replaced two jurors. Change the big lines to `["Six weeks.", "One jury.", "One target."]`. The say is OK: six-week trial; "Soon after the jury was selected". | 929 p11; 277 p1 |
| 16 | OK | — | — |
| 17 | OK | Quote is verbatim: "the youngest and only person of color on the jury" | 216 p1 |
| 18 | OK | Quote is verbatim with the source's own ellipses | 216 p2 |
| 19 | OK | Online research, home address, Abdulkarim surveillance; also admitted in the 155 plea | 216 p2; 277 p2; 155 |
| 20 | OK | $150,000. The "plea records" wording is supported: the plea-day release says "According to court documents". Optionally add PRALI/PRNUR to src. | PRALI; PRNUR; 277 p2 |
| 21 | **FIX** | The plea-stage releases say Ali "**attempted** to follow Juror 52 home as she left a downtown Minneapolis parking ramp". Only the 2026 gov't memos say she followed her home. Attribute the stronger claim. **say:** "On May thirtieth, she flew to Minneapolis. The next day, the first day of closing arguments, she followed Juror fifty-two from a downtown parking ramp, prosecutors say, all the way home." **show:** "On May 30, she flew to Minneapolis. The next day, the first day of closing arguments, she followed Juror 52 from a downtown parking ramp, prosecutors say, all the way home." | PRALI; PRNUR; 277 p2 |
| 22 | OK | Magnetic GPS tracker, attributed | 216 p2 |
| 23 | **FIX** | This is the indictment-stage account in PR24 and needs attribution. The quotes are verbatim. **say:** "And, prosecutors say, they wrote her a script. A list of instructions, telling her to vote not guilty on all counts for all defendants. And to convince the other jurors to do the same." **show:** "And, prosecutors say, they wrote her a script. A list of instructions, telling her to vote \"NOT GUILTY ON ALL COUNTS FOR ALL DEFENDANTS.\" And to \"convince all the remaining jurors\" to do the same." | PR24 |
| 24 | OK | — | 277 |
| 25 | OK | — | — |
| 26 | OK | Bar story, $500,000, delivery next day. Ali admitted this ("falsely") per the plea release. | 277 p2; PRALI |
| 27 | OK | Quote verbatim | 277 p2 |
| 28 | OK | Morning of June 2; "have the money ready" by 10:00 | 251 p2; 216 p2 |
| 29 | OK | $200,000 from multiple individuals and a hawala at Karmel Mall, Minneapolis (the hawala gloss is explanatory) | 251 p2 |
| 30 | OK | Cardboard box at Bushra; Bloomington lot; Hallmark bag | PRNUR; PRALI |
| 31 | OK | Did not trust her; drive and record | 277 p3; 216 p3 |
| 32 | OK | Stole $80,000 on the way; "insisted that he drive … prevented Ali from stealing all" | 277 p3; PRALI |
| 33 | OK | Target, screwdriver, license plate off the rental car | 216 p3; PRALI |
| 34 | OK | 8:50 PM; filmed from the car; stepfather; "present" | 277 p3; 216 p3 |
| 35 | OK | "It's done babe." verbatim | 243 p3 |
| 36 | **FIX** | Cutting "[Juror 52] will come through" changes what the "good feeling" was about, and the em-dash join hides the omission. **say:** "The video went out over Signal. Abdiaziz Farah forwarded it to his brother Said, with three words: watch and delete. And he texted another co-conspirator that he had a good feeling Juror fifty-two would come through, and that's a lot of money for her family." **show:** "The video went out over Signal. Abdiaziz Farah forwarded it to his brother Said, with three words: \"watch and delete.\" And he texted another co-conspirator that he had \"a good feeling [Juror 52] will come through and that's a lot of money for her family.\"" | 216 p3 |
| 37 | OK | Bars 200,000 / 80,000 / 120,000 match PRALI | PRALI; 277 |
| 38 | OK | — | — |
| 39 | OK | Quote verbatim; AP paraphrase accurate | 216 p3; AP-PBS |
| 40 | OK | Next morning before closings resumed; Brasel ordered phones surrendered to the FBI | 277 p3; 216 p3 |
| 41 | **FIX** | The factory reset was charged as obstruction (Count 4), which was **dismissed**. Abdiaziz pleaded only to Count 2 (231). It is the government's account. **say:** "Then, prosecutors say, the race to destroy the evidence began. Abdiaziz Farah did a factory reset of his phone, before agents could take it." **show:** "Then, prosecutors say, the race to destroy the evidence began. Abdiaziz Farah did a factory reset of his phone, before agents could take it." | 216 p4; PR24; 231 |
| 42 | **FIX** | Nur admitted deleting Signal (PRNUR), but the recovered note is only in the gov't memo. **say:** "Nur deleted Signal. But, according to prosecutors, investigators recovered a deleted note from his phone. Thirty talking points, for Ali to give Juror fifty-two, to help her convince the other jurors." **show:** "Nur deleted Signal. But, according to prosecutors, investigators recovered a deleted note from his phone. 30 talking points, for Ali to give Juror 52, to help her \"convince other jurors.\"" | PRNUR; 243 p3 |
| 43 | OK | Warned; flight June 5 moved to June 3 (two days); UPS; attributed | 277 p3–4 |
| 44 | OK | Fingerprints on the gift bag (also reported by MPR); GPS devices in her hotel | 277 p4; MPR-1120 |
| 45 | OK | Dismissed; trial continued; Thompson said it "in court" per the Star Tribune via AP. Nit: drop "KSTP" from the cite, since KSTP is not the source of the quote. | AP-PBS; KSTP-0722 |
| 46 | OK | June 7, four days after June 3; Abdiaziz and Nur convicted | 216 p4; 243 p3 |
| 47 | OK | Acquitted on all counts; "ironically" verbatim. This does not imply the jurors knew of the bribe. | 251 p4 |
| 48 | **FIX** | The judgment is not "one line": it has two sentences (finding plus order of acquittal and discharge). **say:** "The judgment is short. The defendant was found not guilty. But the bribery case was just beginning." **show:** "The judgment is short. \"The Defendant was found not guilty.\" But the bribery case was just beginning." Kicker date June 12, 2024 is the signature date and is OK. | 579 |
| 49 | OK | — | — |
| 50 | **FIX (src only)** | The text is OK: indicted June 25, 2024; "Then-U.S. Attorney" is correct; Luger's quote is from the AP indictment story, not AP Jun 4. **src:** "U.S. Attorney's Office, D. Minn., press release (Jun 26, 2024); AP via ABC News, Jun 2024 — five charged" | 216 p4; 277 p4; PR24; AP-ABC |
| 51 | OK | Plea dates: Nur Jul 23, 2024; Ali Sep 5, 2024; Abdulkarim Apr 2, 2025 (155, signed and filed that day); Abdiaziz Jun 18, 2025; Said Aug 21, 2025. Each pleaded to one count of bribery of a juror. | 243 p4; PRNUR; 277 p4; PRALI; 155; 207; 216 p4; 251 p4 |
| 52 | OK | 336 months, Aug 6, 2025 | 216 p4 |
| 53 | **FIX** | The bars title "Before the bribery sentences" is false: Abdulkarim's bribery sentence (Mar 4, 2026) came before Bock's (May 2026). **title:** "The fraud sentences". The say and show are OK: Nur 120 months Nov 24, 2025; Bock 500 months, "founder", convicted by a jury in 2025 (a different trial from the 2024 trial). | 243 p3; MPR-0521; 207 |
| 54 | OK | Tostrud sentenced Abdulkarim, Abdiaziz, Said and Ali. For Nur, Tostrud is the presiding judge on 243 (ECT), but no hearing record or report names the judge. | 207; 230; MPR-1120; 243 |
| 55 | OK | — | — |
| 56 | **FIX (src only)** | The text is OK: 57 months on Mar 4, 2026; guideline range 46–57; "the high end of his guideline range". **src:** append "; Government's position regarding sentencing, Abdulkarim Shafii Farah (Dkt. 203, Feb 11, 2026); Dkt. 216 at 9" | 207; 203; 216 p9 |
| 57 | OK | July 22; "organizer and leader" attributed to prosecutors; Murphy quote verbatim | 216 p9; 230; MPR-0722 |
| 58 | OK | Verbatim | MPR-0722 |
| 59 | OK | Verbatim, with an ellipsis joining the two quotes | MPR-0722 |
| 60 | OK | 120 months consecutive to the 22-CR-124 term; "heroic" | 231 p2; 230; KSTP-0722 |
| 61 | OK | Oct 30, 6½ years (78 months per 277 p8) | MPR-1120; 277 |
| 62 | **FIX** | WCCO/CBS does not say Nur's term is consecutive; MPR does. **say:** "November eighteenth. Abdimajid Nur. Five years, according to WCCO. M.P.R. News reports it runs on top of the ten he is already serving for the fraud." **show:** "November 18. Abdimajid Nur. Five years, according to WCCO. MPR News reports it runs on top of the 10 he is already serving for the fraud." **kicker:** "NOVEMBER 18, 2026 · PER WCCO / MPR NEWS". The sub can stay. | CBS-1119 (Wednesday = Nov 18); MPR-1120 |
| 63 | OK | Nov 20; $80,000; gov't asked 57 months; title quote verbatim | 277 p1, p8 |
| 64 | OK | Newmark quote verbatim (the say splits it into two sentences, which is fine) | MPR-1120 |
| 65 | OK | Verbatim | MPR-1120 |
| 66 | OK | 4 years; report Jan 19. Kicker "ST. PAUL" is not firmly verified. | MPR-1120 |
| 67 | OK | Bars: 120 / 78 (6½ yrs) / 60 / 57 / 48. Spoken amounts match the show. | 231; 277 p8; MPR-1120; CBS-1119; 207 |
| 68 | **FIX** | "easiest juror to buy" goes beyond the source ("best candidate to bribe"). **say/show:** "They picked her because they thought she was the best candidate to bribe. She was the one who picked up the phone. Was four years enough for the courier who skimmed the bribe? Tell us in the comments." | 216 p1; 277 p1 |

## short1.json — title "$120,000 in a Gift Bag: The Juror Who Called the Police" — title OK

| # | Verdict | Notes / replacement | Source |
|---|---|---|---|
| 0 | **FIX** | "biggest pandemic fraud trial" is unsupported. **say:** "A hundred and twenty thousand dollars in cash, in a Hallmark gift bag, left at a juror's door in the first Feeding Our Future fraud trial." **show:** "$120,000 in cash, in a Hallmark gift bag, left at a juror's door in the first Feeding Our Future fraud trial." | MPR-1120; PRALI |
| 1 | OK | — | 216 p3 |
| 2 | OK | PR24 says "youngest juror"; the memos say "believing her to be the youngest" | PR24; 216 |
| 3 | OK | "That night": she reported "immediately", and the court was told the next morning. Sentences ran from 48 to 120 months, so "4 to 10 years" is correct; Mar–Nov 2026 is correct. | 216; AP-PBS; 207; 231; MPR-1120 |
| 4 | OK | — | — |

## short2.json — title "\"It's Done Babe\": She Skimmed $80K From a Juror Bribe" — title OK

| # | Verdict | Notes | Source |
|---|---|---|---|
| 0 | OK | $80,000 of $200,000 | PRALI |
| 1 | OK | $500,000; "fabricated this entire interaction" verbatim | 277 p2; PRALI |
| 2 | OK | "It's done babe." | 243 p3 |
| 3 | OK | Kicker "ST. PAUL" not firmly verified | MPR-1120 |
| 4 | OK | — | — |

## short3.json — title "Acquitted on All Counts, Then Guilty of Bribing a Juror" — title OK (the plea came after the acquittal)

| # | Verdict | Notes / replacement | Source |
|---|---|---|---|
| 0 | **FIX** | "to bribe that jury" alongside "acquitted" can read as if the bribe reached or swayed the jury that acquitted him. The bribe targeted one juror, who reported it and was removed. **say:** "Acquitted on all counts. And the government says he was the one who collected two hundred thousand dollars in cash to bribe one of its jurors." **show:** "Acquitted on all counts. And the government says he was the one who collected $200,000 in cash to bribe one of its jurors." | 251 p2–4; KSTP-0722 |
| 1 | OK | — | 251; 216 |
| 2 | OK | "remaining jurors" (Juror 52 had been removed); "ironically" verbatim | 251 p4; AP-PBS |
| 3 | OK | Pleaded guilty Aug 21, 2025; 6½ years Oct 30 | 251; MPR-1120 |
| 4 | OK | — | — |

## thumb2.json

| Field | Verdict | Notes |
|---|---|---|
| A q "$200K / TO BUY / A JUROR?" | OK | $200,000 in cash "to bribe Juror 52" (PRNUR) |
| A tag "BREAKING" | OK | Final sentencing was Nov 20, 2026 |
| B line1 "$120K BRIBE FOR JUROR 52" | OK | PR24 / PRALI |
| B line2 "SHE CALLED THE POLICE" | OK | 216; AP-PBS |
| B/C tag "SENTENCED" | OK | — |
| C line1 "$80K SKIMMED FROM THE BRIBE" | OK | PRALI; 277 |
| C line2 "ALL 5 SENTENCED" | OK | 207; 231; MPR-1120; CBS-1119 |

## zoomcard.js (excerpt cards)

| Card | Verdict | Notes |
|---|---|---|
| BAG / h_bag | OK (text) | Verbatim from PRALI; the ellipsis covers the omitted "and explained … But" |
| CALL / t_call | OK | Verbatim from 216 p3 |
| STOLE / h_stole / t_stole | OK | Verbatim from 277 p3 ("briber [sic]") |
| IRONIC | OK | Verbatim from 251 p4 |
| NOTE / t_note | OK | Verbatim from PR24 |
| t_bag | OK (text) | PRALI: "handed it to a relative of Juror 52 . . . delivered $120,000 . . . and kept the remaining $80,000 cash for herself." Omissions are marked. |
| t_bag120 | OK (text) | PRALI |
| t_note2 | OK (text) | PR24, with an internal ellipsis |
| h_ironic | OK | "[Said Farah]" replaces "The defendant" in 251 p2; ellipsis; then 251 p4 |
| **HEAD on USAO cards** | **FIX** | Cards quoting press releases (t_bag, t_note, t_bag120, t_note2, h_bag) carry the case-caption header "U.S. v. FARAH ET AL. · D. MINN.", which presents a press release as a court filing. In the render loop, use `const head = /^USAO/.test(sub) ? "U.S. ATTORNEY'S OFFICE · D. MINN." : HEAD;` and print `${head} · ${sub}`. |

## meta.json

| Field | Verdict | Notes / replacement |
|---|---|---|
| title | OK | $120,000 delivered (PRALI). "BACKFIRED" is fair: the juror reported it, and all five pleaded guilty and were sentenced. |
| summary | OK | Every fact checks out. The Nur "on top of 10" is supported by MPR-1120 ("consecutive"). "first Feeding Our Future fraud trial" is supported by MPR and KSTP. |
| question | **FIX** | "the organizer" is the prosecutors' characterization. → "Juror 52 called the police. The courier who skimmed $80,000 got 4 years; the man prosecutors called the organizer got 10 on top of 28. Was 4 years enough? Tell us in the comments." |
| first_comment | **FIX** | Same attribution issue. → "The courier kept $80,000 of the bribe for herself and got 4 years. The man prosecutors called the organizer got 10 more years on top of 28. Who deserved the most time?" |

---

## Could not verify

1. **"ST. PAUL, MINN."** in the Ali verdict kickers (episode 5 and 66, short2 3). MPR-1120 carries a St. Paul dateline but does not name the courthouse. Tostrud's other hearings (207, 230) were in St. Paul, so it is likely. If you want certainty, use "NOVEMBER 20, 2026 · D. MINN."
2. **Which judge sentenced Nur** on Nov 18. Tostrud is the presiding judge on 243 (ECT), but CBS-1119 does not name the judge. Line 54 ("each of them would stand in front of … Eric Tostrud") relies on this.
3. Whether Newmark spoke **"to the judge"** (line 64). MPR says only "in court".
4. **Abdulkarim's change-of-plea hearing date.** Plea agreement 155 was signed by all parties and filed 4-2-2025, which strongly supports Apr 2, 2025, but I had no minutes for the plea hearing.
5. Exhibit number for the replacement image x-001 (H-51b) was read from the exhibit sticker in the image, not from the memo text.
