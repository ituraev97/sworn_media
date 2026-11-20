# SWORN 020 — Brinks heist — independent fact-check

**Case:** U.S. v. Carlos Victor Mestanza Cercado et al., C.D. Cal. 5:25-cr-00198-KK
**Checked (2026-11-20):** episode.json (lines 0–70: say, show, every scene text field, every doc highlight against hl.json/make_img.py), short1/2/3.json (title, say, show, hook number/label/tag, scene text), meta.json (title, summary, docs_note, question, first_comment, tags, sources), thumb2.json (all words), zoomcard.js (t_24, t_10m, t_texts, h_24, h_10m, h_texts).

**Sources used:**
- Indictment, Dkt. 1 (ind.txt)
- Plea agreement, Dkt. 158 (plea.txt, plus rendered signature pages: defendant signed 11-04-26, AUSA signed 11/9/2026)
- Stipulation, Dkt. 156 (C.D. Cal. trial-date history; "third request for a continuance")
- Dkt. 108 and Dkt. 116 (earlier continuances); Dkt. 113 (Presilla motion: already deported by Jan 2026)
- USAO press releases pr25.txt and pr26.txt
- Web sources:
  - AP (Stefanie Dazio, via NBC News and Claims Journal; the AP byline is confirmed on Claims Journal)
  - NPR (June 18, 2025)
  - Reuters via Yahoo (Steve Gorman, Nov 19, 2026)
  - LA Times via Yahoo ("Inside the Brink's heist probe…")
  - MyNewsLA (Nov 19, 2026)
  - Wikipedia "2022 Brink's theft"

**Verified from web sources:**
- **AP** confirms each of these:
  - Brink's suit filed Aug 4, 2022, in federal court in New York.
  - 22 bags.
  - Pickup manifests "reported a total of $8.7 million."
  - One driver in "the big rig's sleeping berth" while the other got food.
  - "He was gone for 27 minutes."
  - Jewelers' suit in Los Angeles (County Superior Court), about $100M.
  - A Brink's employee allegedly told them to "under-value their merchandise."
  - Kroll's quote, verbatim: "We are astounded by Brink's lack of support for their longtime customers who thought they were in safe hands with Brink's."
- **NPR** confirms:
  - The Davis quote, verbatim.
  - His title: "assistant director in charge of the FBI's Los Angeles field office."
  - The two men arrested Tuesday (June 17, 2025) were Presilla and Lugo.
  - 24 bags was "about one-third of the truck's load."
- **Reuters** confirms: "It was not clear from court documents whether any of the stolen jewelry from the heist was ever recovered."
- **MyNewsLA** confirms the plea was entered "in federal court in Riverside."
- **LA Times** confirms the traffic-collision/burner-phone account. It sources that detail to "two people involved with the case" and calls the number a "critical mistake."
- **Wikipedia** supports the location ("where I-5 climbs through Tejon Pass") and the time, about 2 a.m.

---

## FIX list

**FIX 1 — episode.json line 4 (say/show).**
- Problems:
  - "a sentence that changes the whole story" presents a disputed defense contention as decisive.
  - "that jewelry" narrows ¶ 9. The contention concerns "the jewelry that Brinks was to transport," which is not shown to be the 24 stolen bags.
- → say: "But inside his plea agreement is a sentence that puts that number in dispute. He contends that certain victims had declared the jewelry Brinks was carrying at a total value of less than ten million dollars."
- → show: "But inside his plea agreement is a sentence that puts that number in dispute. He contends that certain victims had declared the jewelry Brinks was carrying at a total value of less than $10 million."

**FIX 2 — episode.json line 7 (scene.hl): wrong paragraph highlighted.**
- The current hl [0.0, 0.087, 1.0, 0.0516] is pr26:plea, the "An Ecuadorian national pleaded guilty today…" paragraph. "33" and "previous addresses include one in Pasadena" are in the next paragraph.
- → hl: [0.0, 0.1391, 1.0, 0.04]. This is the computed box for "Carlos Victor Mestanza Cercado, 33, … (Hobbs Act)." Adjust pan to about [0.05, 0.11] if needed.

**FIX 3 — episode.json line 11 (say/show).**
- Problems:
  - "the others emptied the truck" is not in the record. ¶ 13 says only that others "stole Samsung electronics from the truck."
  - Spoken "about two hundred forty thousand" does not match the subtitle "$240,573".
- → say: "It was a decoy. While the driver was distracted, others stole Samsung electronics from the truck. The victims later valued them at about two hundred forty thousand dollars."
- → show: "It was a decoy. While the driver was distracted, others stole Samsung electronics from the truck. The victims later valued them at about $240,000."
- The stat card "$240,573" can stay.

**FIX 4 — episode.json line 12 (say/show).** "This time he came back too early" is invented. ¶ 13 says only that the driver "caught defendant and co-conspirators in the act."
- → say: "Nine days later, in Fontana, it was Apple AirTags, shipped from China. The driver stopped for food. This time, he caught them in the act."
- → show: "9 days later, in Fontana, it was Apple AirTags, shipped from China. The driver stopped for food. This time, he caught them in the act."

**FIX 5 — episode.json line 14 (show).** Spoken "about fifty-seven thousand dollars" does not match the subtitle "$57,377".
- → show: "That moment matters more than the AirTags themselves, which were valued at about $57,000. Because a threat of force turns a theft into a robbery. Hold on to that. It comes back at the end."
- The scene figure "$57,377" can stay.

**FIX 6 — episode.json line 16 (show).** Spoken "about fourteen thousand dollars' worth" does not match the subtitle "about $14,081 worth", which also lacks the apostrophe.
- → show: "May 25, Fontana again. At a truck stop, a crowbar on a semitruck, and they fled. The same day, Samsung electronics from another truck, about $14,000 worth."

**FIX 7 — episode.json line 17 (say; subtitle = say).** "A few hundred thousand dollars in four months" is wrong on the timing. The three thefts ($240,573 + $57,377 + $14,081.54 = $312,031.54) fall between March 2 and May 25, which is under three months.
- → say: "About three hundred thousand dollars in under three months. Then, in July, they found a truck carrying something else entirely."
- → add show: "About $300,000 in under three months. Then, in July, they found a truck carrying something else entirely."

**FIX 8 — episode.json line 21 (say; subtitle = say).** Overt Act 18 names only charged co-defendants (Lugo, Alban, Padilla, Valencia). "lists the phone chain" presents it as fact.
- → say: "The indictment alleges a phone chain when the truck left: one defendant calling a second, the second a third, the third a fourth. Those are charges, not proof."

**FIX 9 — episode.json line 23 (scene.src).** The plea agreement does not describe Lebec's location. The I-5/mountains description comes from Wikipedia (I-5 at Tejon Pass). Say/show are otherwise OK.
- → src: "Background: Wikipedia, \"2022 Brink's theft\" (Lebec, on I-5 at Tejon Pass)"

**FIX 10 — episode.json line 25 (say/show).** AP and the lawsuit describe the two crew members as drivers, not guards.
- → say: "Where were the drivers? The court papers don't say. Brinks's own lawsuit, filed weeks later, did. According to the Associated Press, it said one driver was asleep in the truck's sleeping berth, and the other was getting food. He was gone, the suit said, for twenty-seven minutes."
- → show: "Where were the drivers? The court papers don't say. Brinks's own lawsuit, filed weeks later, did. According to the Associated Press, it said one driver was asleep in the truck's sleeping berth, and the other was getting food. He was gone, the suit said, for 27 minutes."

**FIX 11 — episode.json line 26 (scene).** The doc shown is indictment Overt Act 21, which names all seven defendants, including the charged-only co-defendants, as travelling to East Hollywood. The line presents it with no allegation framing. The same fact is in Mestanza's own admitted plea text (p_24 covers "…traveled to East Hollywood with the stolen jewelry").
- → scene: {"type":"doc","img":"img/p11.jpg","pan":[0.483,0.543],"hl":[0.0,0.6569,1.0,0.0916],"kicker":"PLEA AGREEMENT · ¶ 13 · JULY 11, 2022","title":"East Hollywood","src":"Plea agreement for defendant Mestanza, Dkt. 158 (C.D. Cal., filed Nov 9, 2026) — agreed facts"}

**FIX 12 — episode.json line 29 (say).** "for three years" is wrong. July 2022 to the June 2025 indictment is just under three years.
- → say: "And then the crew did the one thing that, for almost three years, seemed to work. They went silent."

**FIX 13 — episode.json line 32 (say/show + scene.hl).**
- Problem 1: Overt Acts 22–23 are allegations against co-defendants (Presilla, Alban, Lugo, Valencia) who are presumed innocent. Only Mestanza has admitted deactivating his number.
  - → say: "According to the indictment, on July fourteenth, fifteenth and sixteenth, three of the defendants deactivated the cellphone numbers they had used for the heist, and on July twentieth, two more did the same. For everyone but Mestanza, those are still only allegations."
  - → show: "According to the indictment, on July 14, 15 and 16, three of the defendants deactivated the cellphone numbers they had used for the heist, and on July 20, two more did the same. For everyone but Mestanza, those are still only allegations."
- Problem 2: the highlight covers only OA 22, although the kicker says "OVERT ACTS 22–23" and the line cites July 20 (OA 23).
  - → hl: [0.0, 0.1568, 1.0, 0.2263]. This is the computed box for OA 22 through OA 23.

**FIX 14 — episode.json line 39 (say; subtitle = say).** Dkt. 156 is a joint stipulation, not "the government's filings." It lists discovery produced.
- → say: "So how do you find a crew that switched off its phones? A joint filing in the case lists the discovery the government has turned over: law enforcement reports, videos, photographs, license plate reader information, and cell-site location information."

**FIX 15 — episode.json line 40 (show).** Spoken "one point eight nine terabytes" does not match the subtitle "1.89569 terabytes".
- → show: "By September 2026, the discovery handed to the defense came to 1.89 terabytes, 33,164 files."

**FIX 16 — episode.json line 41 (say/scene.src).**
- Problems:
  - The LA Times sources the collision/burner-phone detail to "two people involved with the case." "officials who were not authorized to speak publicly" is its general sourcing, not this detail's.
  - "one of the men" should be "one of the alleged thieves" (presumption of innocence; he is unnamed).
- → say: "The Los Angeles Times later reported, citing two people involved with the case, that one break came from a burner-phone number one of the alleged thieves had given to a police officer after witnessing a traffic collision. That account has not been tested in court."
- → src: "Los Angeles Times, \"Inside the Brink's heist probe\" (2025), citing two people involved with the case"

**FIX 17 — episode.json line 44 (say/show).** "a federal grand jury in Los Angeles" is unsourced. The indictment shows only "March 2025 Grand Jury" in a 5: (Riverside) case number.
- → say: "On June eleventh, twenty twenty-five, a federal grand jury returned an indictment against seven men, Mestanza listed first."
- → show: "On June 11, 2025, a federal grand jury returned an indictment against seven men, Mestanza listed first."

**FIX 18 — episode.json line 45 (say/show).** "Count six alone covered the jewelry" is inaccurate. Count one (the § 371 conspiracy) also covers the jewelry theft (Overt Acts 14–23).
- → say: "The charges: conspiracy, theft from interstate shipment, and, for five of them, robbery under the Hobbs Act. Count six, a theft count, covered the jewelry, valued by the victims at about one hundred million dollars."
- → show: "The charges: conspiracy, theft from interstate shipment, and, for five of them, robbery under the Hobbs Act. Count six, a theft count, covered the jewelry, valued by the victims at about $100 million."

**FIX 19 — episode.json line 47 (say/show + scene.case).** NPR gives Davis's title as of June 2025 as "assistant director in charge of the FBI's Los Angeles field office." "Los Angeles chief" is loose and not dated. The quote itself is verbatim (OK).
- → say: "On June seventeenth, the indictment was made public, and two of the men were arrested. Akil Davis, then the assistant director in charge of the F.B.I.'s Los Angeles field office, said in a statement quoted by NPR: I'm gratified that we can finally begin to give answers to the victims of this massive theft."
- → show: "On June 17, the indictment was made public, and two of the men were arrested. Akil Davis, then the assistant director in charge of the FBI's Los Angeles field office, said in a statement quoted by NPR: \"I'm gratified that we can finally begin to give answers to the victims of this massive theft.\""
- → case: "Akil Davis, then assistant director in charge, FBI Los Angeles · June 2025"

**FIX 20 — episode.json line 60 (say/show).** "Why that one?" presents an unsourced motive for why count three was chosen. Nothing in the record explains the choice of count.
- → say: "Why does that matter? A theft charge from an interstate shipment carries up to ten years. Robbery under the Hobbs Act carries up to twenty."
- → show: "Why does that matter? A theft charge from an interstate shipment carries up to 10 years. Robbery under the Hobbs Act carries up to 20."

**FIX 21 — episode.json line 61 (say).** The spoken figure drops the cents but the subtitle quotes "$100,312,031.54". Digits must match.
- → say: "And the Brinks heist is still in the deal. He admits it in the factual basis, and he agrees the court may order restitution for conduct beyond the count he pleaded to. The government believes that restitution is at least one hundred million, three hundred twelve thousand, thirty-one dollars and fifty-four cents."

**FIX 22 — episode.json line 67 (say/show + scene.hl).**
- Problems:
  - USAO says Valencia and Macias "have not appeared in a U.S. courtroom to face the criminal charges against them." "never appeared in a U.S. courtroom" overstates.
  - These two and Presilla are not described as presumed innocent.
  - "February" has no year (Feb 12, 2026).
  - The highlight covers only the Presilla paragraph.
- → say: "Two other co-defendants have not appeared in a U.S. courtroom to face the charges. And the charges against one more were dismissed without prejudice in February twenty twenty-six, after he was removed from the United States. All of them are presumed innocent."
- → show: "Two other co-defendants have not appeared in a U.S. courtroom to face the charges. And the charges against one more were dismissed without prejudice in February 2026, after he was removed from the United States. All of them are presumed innocent."
- → hl: [0.0, 0.8621, 1.0, 0.0687], covering pr26:atlarge plus pr26:removed. Optionally retitle "Not appeared · dismissed".
- Note: the "after he was removed" order is supported by Dkt. 113, filed Jan 9, 2026, which says he had already been deported.

**FIX 23 — episode.json line 68 (say/show).** The clause "beyond the government's word in 2025 that some of it was" is not Reuters'. As written it is attributed to Reuters.
- → say: "Reuters noted it was not clear from court documents whether any of the stolen jewelry from the heist was ever recovered. In twenty twenty-five, the government said some of it was, but not how much."
- → show: "Reuters noted it was not clear from court documents whether any of the stolen jewelry from the heist was ever recovered. In 2025, the government said some of it was, but not how much."

**FIX 24 — episode.json line 69 (say/show).** "went silent for three years" should be "almost three years."
- → say: "So here is where it stands. Seventy-three bags. Twenty-four taken in the night. A crew that went silent for almost three years. A fugitive caught on a layover. And a guilty plea that leaves the biggest number in the case still open."
- → show: "So here is where it stands. 73 bags. 24 taken in the night. A crew that went silent for almost three years. A fugitive caught on a layover. And a guilty plea that leaves the biggest number in the case still open."

**FIX 25 — short1.json line 0 (say/show).**
- Problems:
  - "$100 million in jewelry, stolen" states the victims' valuation as fact.
  - "contends victims had declared it" — ¶ 9 is about "certain victims" and "the jewelry that Brinks was to transport."
- → say: "Jewelry its owners valued at a hundred million dollars, stolen from a Brinks truck. The lead defendant just pleaded guilty, and contends certain victims had declared a total of under ten million to Brinks."
- → show: "Jewelry its owners valued at $100 million, stolen from a Brinks truck. The lead defendant just pleaded guilty, and contends certain victims had declared a total of under $10 million to Brinks."

**FIX 26 — short1.json line 1 (say/show).** "his crew" implies he led the crew, which the record does not establish ("lead defendant" means he is listed first).
- → say: "In twenty twenty-two, he and his co-conspirators broke the locks and took twenty-four bags."
- → show: "In 2022, he and his co-conspirators broke the locks and took 24 bags."

**FIX 27 — short1.json line 4 (say/show).** "or ten" turns "less than $10M declared" into a $10M figure.
- → say: "Should he owe a hundred million, or less than ten?"
- → show: "Should he owe $100 million, or less than $10 million?"

**FIX 28 — short2.json line 0 (scene.label).** "HEIST · THEN HE RAN" implies he fled right after the 2022 heist. He left in June 2025, after the indictment.
- → label: "INDICTED · THEN HE RAN|PER HIS PLEA DEAL"
- Say/show OK. The texts of June 18–20, 2025, came 7–9 days after the June 11 indictment.

**FIX 29 — short3.json line 0 (say/show).** The valuation must be attributed to the victims.
- → say: "Twenty-four bags of jewelry, valued by the victims at a hundred million dollars. The lead defendant just pleaded guilty, and admitted how it worked."
- → show: "24 bags of jewelry, valued by the victims at $100 million. The lead defendant just pleaded guilty, and admitted how it worked."

**FIX 30 — short3.json line 2 (say; subtitle = say).** The lawsuit as reported by AP says "driver," not "guard."
- → say: "At a truck stop in Lebec, they broke the locks. Brinks's lawsuit said one driver slept, the other was getting food."

**FIX 31 — meta.json summary.**
- Problems:
  - It never says what he pleaded guilty to, so it reads as a plea to the heist.
  - "the owners had declared" should be "certain victims."
  - Only three co-defendants are flagged as presumed innocent.
- → Replace the sentence "…pleaded guilty in federal court in Riverside." with "…pleaded guilty in federal court in Riverside to one count of Hobbs Act robbery (a March 2022 AirTags robbery)."
- → Replace "his contention that the owners had declared a total of less than $10 million to Brinks" with "his contention that certain victims had declared a total of less than $10 million to Brinks."
- → Replace the last line with "All co-defendants are presumed innocent; three have pleaded not guilty and their trial is set for March 22, 2027."

**FIX 32 — meta.json first_comment.** "His plea deal says certain victims declared…" presents his contention as a stated fact, and omits the government's dispute.
- → "In his plea deal, he contends certain victims declared less than $10 million to Brinks; prosecutors dispute that and say restitution is at least $100.3 million. Which number should the judge use?"

**FIX 33 — thumb2.json A (left.q).** "$100M OR $10M?" invents a $10M figure. The plea says less than $10M was declared, and only as his contention.
- → q: ["$100M", "OR UNDER", "$10M?"]

**FIX 34 — thumb2.json C (line1).** "$100M HEIST: HE RAN" implies he fled after the heist. He fled in June 2025, after the indictment.
- → line1: "$100M HEIST: INDICTED, HE RAN"
- Keep line2 "THEN PLEADED GUILTY".

**FIX 35 — zoomcard.js t_24 and h_24 (T24).** The excerpt is verbatim, but it stops mid-sentence (", and traveled to East Hollywood…") with no omission mark.
- → t_24: `broke the locks on the Brinks truck and stole <mark>24 bags of jewelry</mark>, which the victims later valued at approximately <mark>$100,000,000</mark> . . .`
- → T24: `defendant and co-conspirators broke the locks on the Brinks truck and stole <mark>24 bags of jewelry</mark>, which the victims later valued at approximately <mark>$100,000,000</mark> . . .`

**FIX 36 — zoomcard.js t_10m and h_10m (T10).** The excerpt stops mid-sentence with no omission mark. It also cuts the qualifier "for the jewelry that Brinks was to transport" and the USAO's dispute.
- → T10: `certain victims declared in their transportation contracts with Brinks a total value of <mark>less than $10,000,000</mark> for the jewelry that Brinks was to transport, and the USAO disputes that those declarations limit the victims’ actual losses.`
- If space forbids the full text in t_10m, at minimum end it with ` . . .` after `</mark>`.

**FIX 37 — zoomcard.js t_texts.** The excerpt stops mid-sentence (it continues "and that he did not know whether the police were after him…") with no omission mark. h_texts already ends with " . . ." (OK).
- → t_texts: `<div class="who">JUNE 18–20, 2025:</div>${TX} . . .`

---

## OK — verified, no change needed

**Cold open (lines 0–5).**
- Line 0:
  - July 11, 2022, early hours (¶ 13).
  - 73 bags.
  - Truck stop in Lebec (pr26: "at a truck stop in Lebec").
  - The p_73 highlight is correct.
- Line 1: 24 bags, victims' valuation about $100M.
- Line 2: the release has "in what is considered to be the largest jewelry heist in U.S. history." NPR's headline is "Prosecutors call it…". The pr25:largest highlight is correct.
- Line 3: Riverside (pr26 dateline, MyNewsLA); "lead defendant"; sentencing date.
- Line 5: framing OK once line 4 is fixed.

**Chapter I (lines 6–17).**
- Line 8: "no later than" March 2, 2022. The p_guilty highlight is correct.
- Line 9: method (¶ 13, p_series).
- Line 10: 7-Eleven, Ontario, translation ruse (p_711).
- Line 13: quote with "[expletive]" is a correct bracketed change of "fuck"; small knife; driver did not intervene.
- Line 15: van; 87 minutes (p_87).
- Line 16 timeline: the event entries are correct.

**Chapter II (lines 18–29).**
- Line 19: July 8–10 scouting, San Mateo (p_scout).
- Line 20: Overt Act 17 title is verbatim ("millions of dollars in jewelry").
- Line 22: about 300 miles; Buttonwillow and Lebec (p_300).
- Line 24: quote is verbatim from ¶ 13 (p_24).
- Line 27: 22 vs 24 bags (AP vs indictment and plea).
- Line 28: 24/73 ≈ one in three (NPR: "about one-third"). "middle of the night" is supported by reporting of about 2 a.m. and ¶ 13's "early hours."

**Chapter III (lines 30–42).**
- Line 31: almost three years.
- Line 33: "to try to conceal their identities" is verbatim (p_deact).
- Lines 35–38:
  - The AP lawsuit details, the $8.7M manifests and the New York filing all check out.
  - The jewelers' Los Angeles suit, about $100M, and the under-value allegation check out.
  - The Kroll quote is verbatim.
- Line 42: June 2025.

**Chapter IV (lines 43–55).**
- Line 46: June 16 search warrants; "Some of that jewelry was recovered" (pr25:recovered).
- Line 48: Mestanza was not among those arrested (NPR: Presilla and Lugo).
- Line 49: searches (p_search).
- Line 50: both quotes verbatim, including "ha[s]" (p_texts).
- Line 51: "robo grande" (p_robo).
- Line 52: fled in June 2025 (pr26:fled).
- Line 53: July 1, 2025, Tocumen, layover from Guatemala to Ecuador.
- Line 54: custody since August 2025; extradited (pr26:custody). First appearance was Aug 6, 2025, per Dkt. 156.
- Line 55: "pushed back again and again." Mestanza's trial date moved from Sep 29, 2025 to Feb 23, 2026, then to Oct 5, 2026, then to Mar 22, 2027 (Dkt. 156 calls it the third continuance request). "signed in November 2026": the defendant signed on Nov 4, 2026.

**Chapter V (lines 56–70).**
- Line 57: filed Nov 9; plea to count three (p_count3).
- Line 58: count three is the March 11, 2022 AirTags Hobbs Act robbery (indictment, p. 9).
- Line 59: ¶ 3(c) (p_dismiss).
- Line 62: ¶ 9 contention is accurately worded (p_declared).
- Line 63: USAO disputes; both sides may present evidence.
- Line 64: the same declared-versus-claimed dispute.
- Line 65: Judge Kenly Kiya Kato; April 15, 2027; 20-year maximum.
- Line 66: three co-defendants pleaded not guilty; trial March 22, 2027; presumed innocent.
- Line 70: framed as a question.

**Shorts (otherwise OK).**
- short1:
  - Title is OK.
  - Lines 2 and 3 are OK ("at least a hundred million" is accurate for $100,312,031.54).
- short2:
  - Title is OK.
  - Lines 1–3 are OK.
- short3:
  - Title is OK.
  - Lines 1, 3 and 4 are OK.
- Every hook tag "GUILTY PLEA" is OK.
- All short highlights match their phrases (p_24, p_declared, p_robo, p_panama, p_300, i_oa22).

**Meta and thumbnail (otherwise OK).**
- meta.json:
  - Title "Brinks $100M Jewelry Heist: Lead Defendant Pleads GUILTY" is accurate; DOJ uses the same framing.
  - question, docs_note, tags and the sources list are OK. The LA Times year "(2025)" is plausible but not shown on the syndicated page.
- thumb2.json B ("$100M JEWELRY HEIST / CAUGHT ON A LAYOVER", stamp "CAUGHT", tag "GUILTY PLEA") is accurate.

**Private names.** No private victim or driver is named anywhere.

FIXES: 37
