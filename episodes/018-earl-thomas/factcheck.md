# SWORN 018 (Earl Thomas): independent fact-check

Checked on Nov 18, 2026 against:
- **P**: the DOJ plea release of Nov 17, 2026 (/home/claude/work/018/plea.txt)
- **I**: the DOJ release on the superseding indictment, Dec 23, 2024 (/home/claude/work/018/ind.txt)
- the live news sources: Fox News, Nov 8, 2023 (it does say "June 9" and "blue Rolls-Royce Cullinan SUV"); CBS Sports, Nov 8, 2023; Longhorns On SI, Nov 9, 2023; TMZ, Dec 21, 2024; TMZ, Nov 13, 2026; TMZ, Nov 16, 2026; Wikipedia, "Earl Thomas"
- PFT/NBC Sports, used as a cross-check

**What was checked**
- episode.json: 77 lines
- short1, short2 and short3: 6 lines plus a title each (21 items)
- thumb2.json, all three rendered thumbnails, and both zoom cards
- meta.json: title, summary, docs_note, first_comment and question
- 37 doc-scene highlight boxes, each cropped and read
- the guardianship redaction in img/plea.jpg

That is about 110 items. **27 need a FIX.**

The two zoom cards, `img/zoom_total.jpg` and `img/zoom_rolls.jpg`, quote P word for word, including "THOMSPON". The zoom_rolls card uses "…" to stand for the omitted clause "who was scheduled to visit the credit union", which is acceptable. The guardianship clause is fully blacked out in img/plea.jpg. No guardianship or mental-capacity wording appears in any say, show, title or metadata field. Every quotation in quote marks matches P or I exactly.

---

## FIX items

### A. Accuracy and overstatement

**1. episode.json line 63, scene `big.lines`**
- Current: `["One count each.", "Not aggravated|identity theft."]`
- Problem: This is wrong for Thompson. He pleaded guilty to two counts: the wire-fraud conspiracy and the cocaine count. Line 62 says so one line earlier.
- Source: P: "THOMPSON also pled guilty to possession with intent to distribute five hundred grams or more of cocaine."
- Replace with: `["One conspiracy count each.", "Not aggravated|identity theft."]`

**2. episode.json line 70, say**
- Current: "Judge Long will decide how much prison time, if any, comes with these pleas."
- Problem: "If any" is not true for Thompson. His drug count carries a mandatory minimum of five years.
- Source: P: "THOMPSON faces a minimum term of imprisonment of five (5) years".
- Replace the say with: "No sentencing date was given in the release. Judge Long will decide the sentences."

**3. episode.json line 59, say**
- Current: "For almost two years, the case moved slowly. Then, this month, it ended without a trial."
- Problem: The case has not ended, because sentencing is still pending. "Moved slowly" is also an unsourced characterization, and it repeats line 56.
- Replace the say with: "For almost two years, there was no trial. Then, this month, both defendants pleaded guilty."

**4. episode.json line 38 (and the fallout in lines 5 and 72)**
- Line 38 current say: "It went on for about two years. And it might have gone on longer, if not for one line on one form." Kicker: "2022 → 2023".
- Problem 1: This contradicts line 23. There, the indictment's period runs from Sept 6, 2021 to Dec 13, 2024, "more than three years".
- Problem 2: The causation is overstated. P says the credit union had already contacted JPSO about an identity takeover *before* officials reviewed the form. The form tied the account to Thompson. It did not uncover the fraud.
- Replace the line 38 say with: "The plea release describes this activity across twenty twenty-two and twenty twenty-three. Then a credit union noticed."
- Replace the line 38 lines with: `["Then a credit union", "noticed."]` (the kicker "2022 → 2023" can stay)

**5. episode.json line 72, say and `big.lines`**
- Current say: "…It did not stop the transfers. A credit union, reading one form, did."
- Current lines: `["The order didn't", "stop it.|One form did."]`
- Problem: Same overstatement as item 4. The indictment alleges the conduct ran "to on or about December 13, 2024", well after the June 2023 arrest. The script cannot say the form "stopped" it.
- Replace the say with: "And notice what did not stop this. A court order told both spouses not to move each other's money. It did not stop the transfers. What exposed it was a credit union that noticed, and a phone number on a form."
- Replace the lines with: `["The order didn't", "stop it.|A credit union noticed."]`

**6. episode.json line 5, say**
- Current: "This is how it worked. Fake signatures, accounts in his name, his paychecks rerouted, his cars sold. And how a phone number on a form brought it all down."
- Problem 1: Thomas was retired, so these were not paychecks. P says "all payments for the victim" from his "labor union association".
- Problem 2: "Brought it all down" is overstated (see items 4 and 5).
- Problem 3: "Fake signatures" goes further than P, which says only that Thompson "practiced signing the victim's name".
- Replace the say with: "This is how it worked. A practiced signature, accounts in his name, his union payments rerouted, his cars sold. And how a phone number on a form led to an arrest."

**7. episode.json line 42, say and show**
- Current: "Reports at the time, citing the sheriff's office, described it as a blue Rolls-Royce Cullinan SUV. The date was June ninth."
- Problem: The reports were not "at the time". They came out in November 2023, five months after the June 9 arrest. The date itself, June 9, is confirmed: Fox News has "Thompson was arrested on June 9 when he drove a blue Rolls-Royce Cullinan SUV to the bank".
- Replace the say with: "Reports in November twenty twenty-three, citing the sheriff's office, described it as a blue Rolls-Royce Cullinan SUV. The date was June ninth."
- Replace the show with: "Reports in November 2023, citing the sheriff's office, described it as a blue Rolls-Royce Cullinan SUV. The date was June 9."

**8. episode.json line 67, say, show and stat label**
- Problem 1: TMZ cites a "federal court document, obtained by TMZ". It does not cite "the plea documents".
- Problem 2: TMZ says the judge "ordered" joint responsibility for restitution. Its own text, however, says Nina "will plead". The script's neutral "reported a figure" is the safe choice; it only needs to say what TMZ actually said.
- Problem 3: The spoken figure drops the 64 cents that the subtitle shows.
- Replace the say with: "TMZ, citing a federal court document, reported a restitution figure of three million, four hundred ninety-seven thousand, four hundred forty-four dollars and sixty-four cents, which it said the two of them would be jointly responsible for paying."
- Replace the show with: "TMZ, citing a federal court document, reported a restitution figure of $3,497,444.64, which it said the two of them would be jointly responsible for paying."
- Replace the label with: "jointly, TMZ reported"
- Optional: add a clause saying the figure is higher than the DOJ's $1.5M–$3M theft range. Viewers will notice the gap.

**9. episode.json line 68, say and show**
- Current: "And TMZ listed what prosecutors want forfeited. …"
- Problem: TMZ (Nov 16) presents this as property Nina Thomas "must forfeit" as part of her plea deal. It is not a prosecutors' wish list. The items themselves check out:
  - 2020 Rolls-Royce Cullinan
  - 2020 Aston Martin Vantage (TMZ: "Vantage Coupe")
  - 2018 Porsche Panamera
  - Birkin bag
  - Chanel (earrings and a belt bag)
  - gold chains
  - designer clothes
  - $228,860 in cash
- Replace the opening of the say and show with: "And TMZ listed the property Nina Thomas must forfeit under her plea deal." The rest of the sentence stays as it is.

**10. episode.json line 73, say and show mismatch**
- Current say: "One check for eight hundred eighty-five thousand dollars." Current show: "One check for $885,419."
- Problem: The spoken figure does not match the subtitle.
- Replace the say with: "…One check for eight hundred eighty-five thousand, four hundred nineteen dollars. …" The show stays as it is.

**11. episode.json line 26, say and show**
- Current: "…open several bank accounts, with Thompson's address, or his telephone number."
- Problem: This drops part of the source. I says "using that email account and Victim 1 or THOMPSON's address, or THOMPSON's address and/or telephone number." Not every account carried Thompson's details.
- Replace the say and show with: "The indictment says they created an email account in the victim's name. Then they used it to open several bank accounts, using the victim's or Thompson's address, and in some cases Thompson's phone number."

**12. episode.json line 55, scene `src`**
- Problem: "Both were taken into custody on December 16" is supported only by TMZ, Nov 13, 2026: "Nina and Kevin were eventually arrested and taken into custody on December 16, 2024." The Dec 21, 2024 TMZ article mentions only Nina, because the co-defendant's name was redacted.
- Replace the src with: "TMZ (Dec 21, 2024), citing court documents · TMZ (Nov 13, 2026)"

**13. episode.json line 5, scene `sub`: "… · 2:24-cr-00058"** (also used in meta.summary and meta.hashtags)
- Problem: Neither DOJ release, nor any listed news article, gives a docket number, and sources.md cites no source for it. I could not verify it.
- Fix: Cite a docket source in sources.md (PACER or CourtListener). If none is available, drop the number: sub "United States v. Thompson & Thomas · E.D. La."; summary "(E.D. La.)"; hashtags "United States v. Kevin J. Thompson and Nina Thomas (E.D. La.)".

### B. Highlight boxes

**14. episode.json line 17, `hl`**
- Current: `[0.0, 0.2671, 1.0, 0.0353]`
- Problem: The box covers the court-order sentence, which is what line 19 is about. It misses the divorce-petition sentence that line 17 is speaking. By pixel scan, the divorce sentence and the redacted line sit at about 0.2417–0.2680.
- Replace with: `[0.0, 0.2374, 1.0, 0.0353]`

**15. episode.json line 57, `hl`**
- Current: `[0.0, 0.6133, 1.0, 0.034]`
- Problem: The box covers only the 30-year wire-fraud sentence. The scene title "Up to 30 years · 2 years mandatory" and the say also cover the aggravated identity theft sentence, which is the next box down (0.6433–0.6773).
- Replace with: `[0.0, 0.6133, 1.0, 0.064]`

### C. Shorts: identification of the victim, and the victim's photo next to guilt or drug words

**16. short1.json line 0, say and show**
- Problem: Nowhere in short1 is the victim's identity attributed to news reports. Line 3 runs over the DOJ doc, which implies that the DOJ figure names Earl Thomas.
- Replace the say with: "Up to three million dollars stolen, prosecutors say, from the man news reports identify as Super Bowl champion Earl Thomas. His estranged wife and her boyfriend just pleaded guilty."
- Replace the show with: "Up to $3 million stolen, prosecutors say, from the man news reports identify as Super Bowl champion Earl Thomas. His estranged wife and her boyfriend just pleaded guilty."

**17. short1.json line 2, say and show**
- Current say: "His union paychecks were redirected. One check: eight hundred eighty-five thousand dollars." Current show: "… $885,419."
- Problem 1: The spoken figure does not match the subtitle.
- Problem 2: These were payments from the union, not paychecks (P).
- Replace the say with: "His union payments were redirected. One check: eight hundred eighty-five thousand, four hundred nineteen dollars."
- Replace the show with: "His union payments were redirected. One check: $885,419."

**18. short2.json title**
- Current: `"Driving a Rolls Royce": How Earl Thomas's Thief Got Caught`
- Problem: "Thief", in the singular, pins the theft on one person. Both defendants admitted the scheme, and the plea was to wire-fraud conspiracy, not theft or identity theft. The channel rule bars "thief" and "impostor" in titles.
- Replace with: `"Driving a Rolls Royce": How the Man Using Earl Thomas's Name Got Caught`

**19. short2.json line 0, say and show, plus hook `number`**
- Current say: "Seven hundred thousand dollars, withdrawn in Earl Thomas's name." Current show: "$700,000, …". Hook: "$700K+".
- Problem 1: P says "more than $700,000.00", and the hook already shows "+". The say and show leave out "more than".
- Problem 2: The connection to Thomas is not attributed. CBS reports "at least $700,000 from Thomas' accounts".
- Replace the say with: "More than seven hundred thousand dollars, withdrawn in Earl Thomas's name, reports say. Then the man behind it drove a Rolls-Royce to the credit union."
- Replace the show with: "More than $700,000, withdrawn in Earl Thomas's name, reports say. Then the man behind it drove a Rolls-Royce to the credit union."

**20. short2.json line 2, say**
- Current: "The account was in Thomas's name. The phone number was Thompson's."
- Problem: This plays over the DOJ document, which says "the victim's name". It implies that the DOJ named Thomas.
- Replace with: "The account was in the victim's name. The phone number was Thompson's."

**21. short2.json and short3.json line 0, hook `tag`**
- Current: `"GUILTY"`
- Problem: The tag sits on img/earl_hook.jpg, a photo of the victim. Viewers can read it as "Earl Thomas: GUILTY".
- Replace with: `"BREAKING"` in both files, which matches short1.

**22. short3.json line 0, hook `label`, say and show**
- Current label: "COCAINE SEIZED|IN THE EARL THOMAS CASE", shown over Earl Thomas's photo.
- Problem 1: Over his face, this associates the victim with the cocaine. P says the drugs were seized from "THOMPSON's residence".
- Problem 2: The say, "the man who used Earl Thomas's identity", has no attribution anywhere in the short.
- Replace the label with: "SEIZED FROM THE HOME OF|THE MAN WHO USED HIS NAME"
- Leave the line 0 say and show as they are. Instead, change the line 2 say to: "Kevin Thompson had been arrested at a credit union, with ID cards in the victim's name. News reports identify that victim as Earl Thomas."

**23. short3.json title**
- Current: `3,716 Grams and $228,000 Cash: The Earl Thomas Fraud Search`
- Problem: "The Earl Thomas … Search" can be read as a search of Earl Thomas.
- Replace with: `3,716 Grams and $228,000 Cash: What Police Found in the Earl Thomas Fraud Case`

### D. Thumbnails and metadata

**24. thumb2.json C: `line2`, and `line1` for context**
- Current: line1 "HIS ROLLS-ROYCE, HIS NAME", line2 "BOTH PLEAD GUILTY", next to Earl Thomas's face.
- Problem: "Both" has no antecedent. The only person pictured is the victim, so a viewer can read it as Earl Thomas pleading guilty. "His Rolls-Royce" itself is supported: CBS says "a blue Rolls-Royce SUV owned by Thomas", and P says "fraudulently obtained from the victim".
- Replace line2 with: "WIFE & BOYFRIEND PLEAD GUILTY" (reduce size2 to about 92 so it fits). Keep line1.

**25. thumb2.json A: `line1`**
- Current: "HIS WIFE & HER BOYFRIEND"
- Problem: P describes the December 2020 divorce petition, and TMZ (2024 and 2026) uses "estranged wife". Plain "wife" understates how the two are separated, and the channel rule is "estranged wife".
- Replace with: "HIS ESTRANGED WIFE & BOYFRIEND" (reduce size1 to about 80).
- Line2, "STOLE UP TO $3M", is acceptable because $3M is P's upper bound and the zoom card shows the full range. "STOLE $1.5M–$3M" would be stricter.

**26. meta.json `title`**
- Current: "Earl Thomas: Wife & Boyfriend STOLE Up to $3M — Both GUILTY"
- Problem: Same "wife" versus "estranged wife" issue as item 25.
- Replace with: "Earl Thomas: Estranged Wife & Boyfriend STOLE Up to $3M — Both Plead GUILTY" (78 characters)

**27. sources.md (housekeeping; nothing on screen)**
- Line "released Aug 22, 2020": Wikipedia says the Ravens released him **Aug 23, 2020**. The script's "August 2020" is fine.
- Line "Dec 16, 2024 custody … | TMZ24": add TMZ13 as a source for "both".

---

## OK, but worth noting

- **"He has not played in the NFL since the Ravens released him in August 2020"** (line 14) is supported. Wikipedia lists no NFL games after the 2019 season and no team signing after the release, and notes that the Texans considered him but passed.
- **Super Bowl XLIX "started"** (line 11) is supported. The Wikipedia intro says he started, and the game section credits him with 9 combined tackles.
- **Super Bowl XLVIII** (line 10): 43–8 over Denver, Feb 2, 2014, is confirmed.
- **Honors and contracts** are confirmed by Wikipedia:
  - Orange, Texas
  - consensus All-American in 2009
  - BCS title game against Alabama
  - drafted 14th overall in 2010
  - 7 Pro Bowls
  - 3 first-team All-Pro selections (the article is internally inconsistent on 2012, but the infobox and PFR count 2012–14)
  - 2010s All-Decade Team
  - 2014 extension: 4 years, $40M
  - 2019 Ravens deal: 4 years, $55M, $32M guaranteed
- **Line 10: "the Seattle secondary that won the franchise's first Super Bowl."** The team won it, not the secondary alone. This is rhetorical and acceptable. "…the Seattle secondary, on the team that won…" would be more precise.
- **"Released shortly after her arrest"** (line 56) is supported by TMZ, Dec 21, 2024 ("released shortly afterward"). It is attributed.
- **Divorce month.** P says December 2020, while Wikipedia says November 2020. The script attributes the date to "court documents" or P, so it is fine.
- **Ages.** I gives Nina Thomas as 34 in December 2024, and P gives 37 in November 2026; those two cannot both be right. The script does not use ages, so leave them out.
- **Line 27, "in the New Orleans area".** P says "Eastern District of Louisiana". This is consistent with CBS (Jefferson Federal Credit Union) and P ("a bank in New Orleans"), so it is acceptable.
- **Lines 47–48: "bond reported at $730,000" and the car "reported stolen in Atlanta".** Both are confirmed by Fox and CBS, citing NOLA.com and JPSO.
- **Line 50 bars.** The "Nov 2026 · DOJ" bar is drawn at 3, the top of the range. Visually that overstates; consider drawing it as a range or at 1.5–3. The "~$1.9M" (Fox and CBS) and "$2.7M+" (TMZ24) figures are correct.
- **Line 74: "according to the guilty pleas, his estranged wife and her boyfriend were taking the money".** The pleas concern "the victim", and the identification comes from news reports. This is acceptable after line 18's explicit note, but "according to the pleas" ties the DOJ more closely to the name than the DOJ itself does.
- **Line 57: wire fraud "up to thirty years".** This matches I. The usual statutory maximum is 20 years, or 30 when a financial institution is affected, but the DOJ release says thirty.
- **Line 73 and the list: "$700,000+ withdrawn at the credit union".** P says the credit union reported more than $700,000 withdrawn "from the victim's account". This is acceptable.
- **Line 69, the forfeiture substitute-assets warning,** matches TMZ, Nov 16.
- **Thumb B: "WHO STOLE FROM EARL THOMAS?"** This is a question, and the identification rests on news reports. Acceptable.
- **The zoom_rolls card** omits P's comma after "THOMPSON", because the "…" replaces the whole clause. Acceptable.
- **meta.summary, docs_note, first_comment and question:** accurate and properly attributed, apart from the docket number (item 13).
