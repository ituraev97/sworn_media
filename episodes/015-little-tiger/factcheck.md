# SWORN 015 — "Little Tiger" — Independent fact-check

**Checked (Nov 15, 2026):** every `say`, `show` and on-screen scene string in episode.json (lines #0–#75, numbered from 0 in file order), short1/2/3.json (titles, hook scenes, all lines), thumb2.json (A/B/C), meta.json (title, summary, docs_note, question, first_comment, tags, hashtags), and every doc-scene highlight (hl coordinates mapped back to `P[name][i]` in make_img.py).

**Sources read in full:** /home/claude/dl/doj/sent.txt (Nov 13, 2026), chenplea.txt (Apr 2, 2026), wangplea.txt (Jan 15, 2026), wangsent.txt (May 8, 2026), ind.txt (Jul 31, 2024), ring65.txt (Aug 27, 2025), final65.txt (Oct 26, 2026); YouTube Data API facts for qjiFJWsHbwE as supplied; Bitdefender article (fetched; it says "Americans aged 60 and older reported more than $7.7 billion in losses in 2025 alone, **the bureau announced** last week" and does not name IC3 for this figure); images img/slide_0222.jpg, slide_0223.jpg, slide_0519.jpg, chen_panel.jpg, sent.jpg viewed.

Line numbers below (#n) are 0-based positions in episode.json `lines`.

---

## FIXES

### A. Wording / accuracy

**1. episode.json #0** — "In July twenty twenty-three, a man went…"
Problem: "a package of cash" is not in any source. This was an in-person pickup of "bulk cash" at a residence; no package is mentioned.
- say: `In July twenty twenty-three, a man went to a house in the Los Angeles area to pick up bulk cash from someone he believed was an elderly fraud victim.`
- show: `In July 2023, a man went to a house in the Los Angeles area to pick up bulk cash from someone he believed was an elderly fraud victim.`

**2. episode.json #2** — "Court records list the man as Jiandong Chen…"
Problem: the identification comes from U.S. Attorney's Office press releases and a DOJ slide, not from court records the episode shows.
- say: `Federal prosecutors identify the man as Jiandong Chen, also known as Little Tiger.`
- show: `Federal prosecutors identify the man as Jiandong Chen, also known as "Little Tiger."`

**3. episode.json #5** — "This is how the scam worked, how the cash…"
Problem: no source calls Trilogy Media a "prank channel". The sources call them YouTubers or scambaiters.
- say / show: `This is how the scam worked, how the cash moved, and how a YouTube channel ended up in a federal sentencing hearing.`

**4. episode.json #7** — "It usually started on a screen…"
Problem: "usually … on a screen" is not supported. The sources list phone calls, emails and pop-up ads with no frequency, and phone calls are not on a screen. The highlight problem for this line is fix 26.
- say / show: `It could start with a phone call, an email, or a pop-up ad. According to the Justice Department, victims received unsolicited phone calls, emails and pop-up ads, telling them to call a phone number.`

**5. episode.json #10** — "This is not a small problem. According to the FBI's Internet Crime Complaint Center…"
Problem: the cited article attributes the $7.7B figure to "the bureau" (the FBI announcement), not to IC3 by name.
- say: `This is not a small problem. According to the FBI, Americans sixty and older reported more than seven point seven billion dollars in losses in twenty twenty-five alone.`
- show: `This is not a small problem. According to the FBI, Americans 60 and older reported more than $7.7 billion in losses in 2025 alone.`
- scene.kicker: `FBI · AGE 60+ · 2025`
- scene.src: `FBI figures for 2025, as reported by Bitdefender (May 19, 2026)`

**6. episode.json #11** — "In this case, one of the most frequent…"
Problem: the scene kicker "THE MOST FREQUENT SCAM" is a superlative. The source says "One of the most frequent scams". The say is correct.
- scene.kicker: `ONE OF THE MOST FREQUENT SCAMS`

**7. episode.json #12** — "The victim was told they were owed…"
Problem: the source says "an **alleged** unauthorized charge". Dropping "alleged" makes it sound as if the charge was real.
- say: `The victim was told they were owed a small refund, for example, from a retailer, for an alleged unauthorized charge. While pretending to process it, the caller would accidentally over-refund them.`
- show: `The victim was told they were owed a small refund, for example, from a retailer, for an alleged unauthorized charge. While pretending to process it, the caller would "accidentally" over-refund them.`

**8. episode.json #18** — "In his plea agreement, Chen admitted exactly that…"
Problem: "exactly that" overstates. The indictment passage on screen covers fake names, retail and CVS addresses, and fake IDs. Chen admitted only the fake-ID retrieval.
- say / show: `In his plea agreement, Chen admitted using fraudulent driver's licenses or IDs, matching the fictitious recipient names, to retrieve the victim packages containing bulk cash.`

**9. episode.json #20 and #74** — "His partners overseas supplied a cryptocurrency wallet…" / "THE CASE IN NUMBERS"
Problem: the source says "upwards of 18%". A bare "18%" on screen understates it and reads as an exact figure. The say/show of #20 is correct.
- #20 scene.value: `18%+`
- #20 scene.label: `his cut ("upwards of 18%") — the rest went out in crypto`
- #74 scene.items[2]: `["18%+", "the ringleader's cut (\"upwards of 18%\"), as he admitted"]`

**10. episode.json #23** — "And here is the strangest detail. The couriers…"
Problem: "The couriers filmed themselves." is stated as fact, but it is the government's argument in Wang's sentencing papers. The highlight problem is fix 29.
- say / show: `And here is the strangest detail. According to prosecutors, the couriers filmed themselves. In Wang's sentencing papers, the government said co-conspirators documented themselves retrieving packages, opening them, and counting the money inside.`

**11. episode.json #24** — "Agents seized countless such photos and videos…"
Problem: "Some of those videos, prosecutors say, show the Little Tiger" is not supported. No source says any of the Chen videos came from Wang's phone. The Nov 13 release only says the prosecutor cited "numerous videos of Chen retrieving victim packages and counting victims' money".
- say: `Agents seized countless such photos and videos from Wang's phone. And at Chen's own sentencing, prosecutors pointed to numerous videos of him doing the same.`
- show: `"Agents seized countless such photos and videos from Wang's phone." And at Chen's own sentencing, prosecutors pointed to numerous videos of him doing the same.`

**12. episode.json #31 and #37** — "In June twenty twenty-three, local police arrested him…"
Problem: the source says "arrested by local law enforcement", and the agency is not identified. It may not have been a police department.
- #31 say: `In June twenty twenty-three, local law enforcement arrested him. Based on publicly filed documents, it did not stop him.`
- #31 show: `In June 2023, local law enforcement arrested him. Based on publicly filed documents, it did not stop him.`
- #37 scene.events[2].text: `arrested by local law enforcement`

**13. episode.json #32** — "A month later came the house in the Los Angeles…"
Problem: neither date is exact (June arrest, July confrontation), so "a month later" is not established. "The next month" is.
- say / show: `The next month came the house in the Los Angeles area. Chen arrived to pick up bulk cash from someone he believed to be an elderly victim. Bingham and Kulik confronted him about working for a scam organization.`

**14. episode.json #46 and #48** — "And he explained why age mattered…" / "The judge said: it's really hard…"
Problem: both quotes are from **Zhao Wang's** sentencing on May 8, 2026, but the quote card is labelled with Chen's case.
- #46 scene.case: `UNITED STATES v. WANG`
- #48 scene.case: `UNITED STATES v. WANG`

**15. episode.json #49** — "But this story is bigger than one crew…"
Problem: "hunting **these** couriers for years" ties the 2020–21 stings to Chen's crew. They were in a separate $65M case.
- say / show: `But this story is bigger than one crew. Because the same YouTubers had been confronting cash couriers for years.`

**16. episode.json #54** — "And the Justice Department credited YouTube. Scammer Payback, run by…"
Problem: "run by" is not in the source, which says "YouTuber Pierogi from 'Scammer Payback'".
- say: `And the Justice Department credited YouTube. A YouTuber known as Pierogi, from Scammer Payback, teamed up with Trilogy Media for coordinated stings. Videos they posted in twenty twenty and twenty twenty-one helped law enforcement identify three of the defendants.`
- show: `And the Justice Department credited YouTube. A YouTuber known as Pierogi, from Scammer Payback, teamed up with Trilogy Media for coordinated stings. Videos they posted in 2020 and 2021 helped law enforcement identify three of the defendants.`

**17. episode.json #57** — "The U.S. Attorney, Adam Gordon, put it this way…"
Problem: Gordon said this on Aug 27, 2025 about the separate $65M ring case, but the quote card is labelled "UNITED STATES v. CHEN".
- scene.case: `THE $65 MILLION RING CASE`

**18. episode.json #58** — "The ring rented short-term homes in what prosecutors called…"
Problem: (a) The source says defendants **admitted in their plea agreements** to the hub-and-spoke rentals, which is stronger than "what prosecutors called". (b) "smaller spokes" is not in the source, which says "spoke locations would be booked nearby for shorter stays".
- say: `In their plea agreements, defendants in that ring admitted booking short-term rentals in a hub-and-spoke pattern. A hub for about a week, spokes nearby for shorter stays, then move and repeat.`
- show: `In their plea agreements, defendants in that ring admitted booking short-term rentals in a "hub-and-spoke pattern." A hub for about a week, spokes nearby for shorter stays, then move and repeat.`

**19. episode.json #59** — "By late October twenty twenty-six, the last of…"
Problem: "are still fugitives" states their status today, but the source is from Oct 26.
- say: `By late October twenty twenty-six, the last of the twenty-five arrested defendants had admitted their crimes. Three charged defendants remained fugitives.`
- show: `By late October 2026, the last of the 25 arrested defendants had admitted their crimes. Three charged defendants remained fugitives.`

**20. episode.json #70** — "And he thanked the YouTubers by name…"
Problem: Gordon did not thank them. He called them "friends to our cause".
- say: `And he named the YouTubers. Stopping fraud takes an online village, he said. With friends to our cause like Ash and Art, we can do even more.`
- show: `And he named the YouTubers. "Stopping fraud takes an online village," he said. "With friends to our cause like Ash and Art, we can do even more."`

**21. episode.json #71** — "Put the sentences side by side…"
Problem: (a) "have received" and "SENTENCES SO FAR" present the Oct 26 table as current. Other ring defendants had sentencings set for Nov 6 and Nov 13, 2026, so the list may be out of date. (b) Na Rong is in a separate 2021 case (21-CR-1454-TWR). It is listed in the ring release but is not one of the 25 defendants.
- say: `Put the sentences side by side. The ringleader, Zhao Wang: one hundred fifty-one months. The Little Tiger: seventy-eight. As of late October, in the related sixty-five million dollar investigation, two defendants, Na Rong and Bing Shen, had been sentenced to seventy-eight and seventy months.`
- show: `Put the sentences side by side. The ringleader, Zhao Wang: 151 months. The Little Tiger: 78. As of late October, in the related $65 million investigation, two defendants, Na Rong and Bing Shen, had been sentenced to 78 and 70 months.`
- scene.kicker: `SENTENCES ANNOUNCED · S.D. CAL.`
- scene.items[2].label: `NA RONG · RELATED CASE (AS OF OCT 26)`
- scene.items[3].label: `BING SHEN · $65M RING (AS OF OCT 26)`

**22. episode.json #72** — "Back in twenty twenty-four, the U.S. Attorney's Office…"
Problem: the quote was said by then-U.S. Attorney Tara McGrath, so it should be attributed to her.
- say: `Back in twenty twenty-four, then-U.S. Attorney Tara McGrath gave one piece of advice. Use caution and consult with others before sending money to strangers you know only through phone calls, texts, or a computer.`
- show: `Back in 2024, then-U.S. Attorney Tara McGrath gave one piece of advice: "use caution and consult with others before sending money to strangers they know only through phone calls, texts, or a computer."`

**23. short1.json line 4** — "Prosecutors say he kept picking up victims' packages…"
Problem: the source says his "involvement continued", and that on Dec 22, 2023 agents encountered him "attempting to retrieve" packages. It does not say he kept picking them up.
- say (no show needed): `Prosecutors say his involvement continued for months, until federal agents encountered him in December trying to retrieve more victim packages.`

**24. short2.json line 1 (hook)** — "Twenty-seven million dollars from about two thousand…"
Problem: "The most frequent trick" is a superlative. The source says "one of the most frequent". Losses were "more than" $27M.
- say: `More than twenty-seven million dollars from about two thousand seniors. One of the most frequent tricks: a refund that never existed.`
- show: `More than $27 million from about 2,000 seniors. One of the most frequent tricks: a refund that never existed.`

**25. short2.json line 2** — "A call or pop-up says you're owed…"
Problem: the subtitle equals the say, and without quotes "accidentally over-refunds" reads as a real mistake. In the source, the caller only pretends.
- say: `A call or pop-up says you're owed a small refund. Then the caller pretends to over-refund you by accident.`

**26. short3.json line 1 (hook)** — "Not all heroes wear capes. Some have…"
Problem: the hook pairs Chen's face and "78 MONTHS" with a quote from 2025 about a different case. The line should date it.
- say: `Not all heroes wear capes. Some have YouTube channels. A U.S. Attorney said that in twenty twenty-five, about scambaiters.`
- show: `"Not all heroes wear capes. Some have YouTube channels." A U.S. Attorney said that in 2025, about scambaiters.`

**27. meta.json title**
Problem: "$27M Elder Scam Courier" reads as if Chen couriered $27M. $27M is the whole scheme, and he admitted more than $9.5M.
- title: `Jiandong Chen: Courier in $27M Elder Scam, EXPOSED on YouTube — 78 Months`

**28. meta.json summary, first sentence**
Problem: the "elder refund-scam case" also covered tech-support, bank and government impersonation scams.
- replace `gets 78 months in the $27 million elder refund-scam case.` with `gets 78 months in the $27 million elder fraud case.`

**29. meta.json first_comment**
Problem: same as fix 23. "kept picking up victims' cash" overstates what the source says.
- first_comment: `He was confronted on YouTube in July 2023 — prosecutors say his involvement continued until at least December 22, when federal agents encountered him trying to retrieve more victim packages. Was 78 months enough?`

### B. Highlights (make_img.py `P` and make_spec.py indexes; re-run make_img.py, then make_spec.py and make_shorts.py)

**30. episode.json #7** (+ #8, which inherits the scene). The highlight is `chenplea[3]`, which covers only the "Unbeknownst…" sentence. The line and the title ("Unsolicited calls, emails, pop-up ads") are about the sentence before it. `chenplea[3]` is used only here.
- make_img.py: `P['chenplea'][3] = ('Victims received unsolicited', 'call centers.')`

**31. episode.json #19** — the highlight is `wangplea[0]` (the 18% sentence only), but the line is about the daily delivery of money. `wangplea[0]` is used only here.
- make_img.py: `P['wangplea'][0] = ('Wang admitted that typically each day', 'his co-conspirators.')` (covers daily delivery, the crypto wallet and the 18%)

**32. episode.json #22** — the highlight is `sent[8]` ("Investigators identified over 2,000 … 70s and 80s."). The laundering admission is the next sentence. `sent[8]` is used only here.
- make_img.py: `P['sent'][8] = ('Chen also admitted that he and his', 'Las Vegas, Nevada.')`

**33. episode.json #23** — the highlight is `wangsent[1]` (only "Agents seized countless…"). The narration is the sentence before it.
- make_img.py: `P['wangsent'][1] = ('In sentencing papers, the government argued', 'Wang’s phone.')` (curly apostrophe, as in the existing entry)

**34. episode.json #30** — the highlight is `sent[2]` (moved to the U.S. … actively participating). The "same distinctive clothing" clause is not marked.
- make_img.py: append to `P['sent']` a new 10th entry `('as evidenced by numerous videos', 'viral YouTube video.')` → index 9
- make_spec.py: change the #30 doc call to use `i=9`

**35. episode.json #63** (and #32) — the highlight is `sent[1]` = "Chen was confronted in a viral … Art Kulik from". It stops before "both of whom attended today's sentencing hearing", which is the #63 title.
- make_img.py: `P['sent'][1] = ('Chen was confronted in a viral', 'sentencing hearing.')` (also fine for #32)

**36. episode.json #55** (minor) — `ring65[2]` begins at "Trilogy Media followed up…". It misses the memo attribution and the "Hans Bum" instruction that the line narrates.
- make_img.py: `P['ring65'][2] = ('That memo says that the YouTubers', 'role in the scheme.')`

---

## OK (verified)

- **Core facts:** sentenced Fri Nov 13, 2026, to 78 months / 6½ years by U.S. District Judge Robert S. Huie in San Diego; aka "Little Tiger"; case 24-cr-1317-RSH(-02); Bingham and Kulik (Trilogy Media) attended the hearing; more than 2,000 victims; more than $27M; 2021–2023; victims in their 70s and 80s; more than $9.5M admitted; fake IDs; relocating "to evade law enforcement"; crypto laundering, paying co-conspirators, travel including Las Vegas (sent, chenplea).
- **Timeline:** moved to the U.S. in Nov 2022; active by Feb 2023; local arrest Jun 2023; confrontation July 2023; video posted Aug 19, 2023; Upland on Dec 22, 2023; indicted June 2024; unsealed and four arrested Jul 31, 2024 (about 60 officers; Pomona; LA and Las Vegas); "seven months later" from Dec 22, 2023 to Jul 31, 2024 is correct.
- **Date conflicts:**
  - sent.txt has "Jn July 2023" (a source typo for "In July 2023"). The script says July 2023 for the confrontation and Aug 19, 2023 for posting, which is correct and consistent.
  - The Apr 2 and Jan 15 releases say "In August 2024 … nationwide takedown", but the Jul 31, 2024 release reports the arrests "this morning". The script correctly uses Jul 31, 2024 and never says "August 2024" for the takedown.
- **Wang:** pleaded guilty Jan 15, 2026; Chen pleaded Apr 2, 2026. Wang got 151 months on May 8, 2026, which is 12.58 years, so "just over twelve and a half" is correct. Also correct: "Oscar"; lead defendant/ringleader; daily delivery; crypto wallet; upwards of 18%; obtained fake IDs personally; recruited co-defendants; "staggering"; "100 percent reprehensible"; the vulnerability quote; the 83-year-old victim's wife and daughter; "It's really hard to fathom…" (all verbatim).
- **Charges and maximums:** 40 years and 20 years (ind, chenplea, sent). The plea to the "fraud and money laundering conspiracy" is consistent with the two listed counts.
- **Chen-sentencing quotes, all verbatim:** Huie ("engaged in extensive course of conduct…", "more than just money", "people's self-respect, their dignity, trust with their family members", "desperation in the last years of somebody's life", "tragic thing to suffer") and Gordon ("These victims weren't foolish…", "Stopping fraud takes an online village", "with friends to our cause like Ash and Art, we can do even more").
- **$65M ring:** 28 alleged members; "Chinese organized crime ring" (attributed); 97-year-old widow, unnamed; investigation began Dec 2020 with 11 packages and about $135,000; videos posted 2020–2021 identified three defendants; "Hans Bum", South San Francisco, decoy, Zhang (framed via the memo and the government). Zhang's identity in #56 is backed by his later guilty plea and his admission that he was in the YouTube videos (final65). LAX arrest Aug 2025; last of 25 defendants admitted; three fugitives; Zhang and Huajian Chen plea admissions; Bing Shen 70 months, Na Rong 78 months; Gordon "Not all heroes…" verbatim and correctly dated Aug 2025.
- **Allegation framing:** the indictment content (#17, #42) is labelled as allegations and followed by the admissions. The detention-memo content (#55–#56) is attributed. No immigration status is stated anywhere: the "many in the U.S. illegally" line in ring65/final65 is correctly not used. No private victim is named.
- **YouTube:** the title is verbatim. "More than 1.4 million" matches 1,423,991 views. The narration never claims the YouTubers caused Chen's arrest.
- **Hotline and advice:** 1-833-FRAUD-11 / 1-833-372-8311, age 60+, ic3.gov, and the advice quote are verbatim from ind. Spoken numbers equal the subtitle numbers throughout.
- **Slides:** no DOJ seal is visible on any of the three (the top-left is painted navy).
  - 2/22/2023 shows a package being cut open with a box cutter and $100 bills counted by hand.
  - 2/23/2023 shows "CVS – 1302 W Mission Rd, San Marcos, CA", a UPS Next Day Air label (an express shipping label), and a book with bills between its pages.
  - 5/19/2023 shows another box being opened and cash counted.
  - Each slide carries Chen's ID photo labelled "Jiandong CHEN aka 'Little Tiger'".
- **Other highlights**, which mark the right passage: #0 / short1 line 2 (chenplea[1]); #9 (chenplea[4]); #12 / short2 line 2 (chenplea[0]); #17 / short2 line 4 (ind[2]); #18 (chenplea[2]); #21 (wangplea[1]); #26 (sent[2]); #31, #35 and short1 line 4 (sent[3]); #36 and #64 (sent[4]); #39 (ind[0]); #40 (ind[1]); #45 (wangsent[4]); #47 (wangsent[3]); #51 (ring65[0]); #53 (final65[2]); #54 / short3 lines 2–3 (ring65[3]); #58 (final65[3]); #59 (final65[0]); #60 (final65[1]); #65 (sent[6]); #67 (sent[7]); #70 (sent[5]); #72 (ind[4]).
- **Thumbnails:**
  - "BREAKING" on A is allowed now: the news is 2 days old. It must come off if A is used after Nov 20, 2026.
  - "EXPOSED ON YOUTUBE", "SENTENCED TO 78 MONTHS", "$27M ELDER SCAM" (the scheme), "78 MONTHS", "\"LITTLE TIGER\"", "THE SCAMBAITER STING" (Chen went to meet someone he believed was a victim; final65 calls these YouTubers "scambaiters"), "2,000 SENIORS" and "FAKE REFUND. REAL CASH." are all supported.
- **Shorts:** the titles for short1, short2 and short3 are true. short3's title is verbatim, title-cased. The hook tags, numbers and labels, and the remaining lines, are supported.
- **meta.json:** the rest of the summary, docs_note, question, tags and hashtags are accurate.
