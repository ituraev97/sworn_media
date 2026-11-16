# Fact-check — SWORN Case 016, United States v. Terry Rozier (E.D.N.Y. 25-cr-323)

- **Date:** 2026-11-16 (video publishes 2026-11-17)
- **Checker:** independent fact-check, not the script author
- **Files checked:** episode.json (70 lines: say, show and all scene text), short1.json, short2.json, short3.json (titles and all lines), thumb2.json (A/B/C), meta.json (title, summary, docs_note, question, first_comment, tags).
- **Method:** I checked every claim against the local primary sources in /home/claude/dl16: the USAO press release of Oct 23, 2025; the Indictment (ECF 17); the Superseding Indictment (ECF 101), checked against the page images sup_8/9/13/14; ECF 144; ECF 166; ECF 169; the M.D. Fla. docket (ECF 26); and the m69.png minute entry, which I viewed. I also viewed every doc image in img/ to confirm each kicker and title. I fetched the news sources live: ESPN (Nov 13, 2026), CBS (Apr 28, 2026), Covers (May 28, 2026) and Covers (Jan 22, 2026). I checked the game location against public box scores (basketball-reference, landofbasketball). Weekdays were checked with `date`: Mar 23, 2023 was a Thursday, Nov 12, 2026 a Thursday, Nov 13, 2026 a Friday, Nov 17, 2026 a Tuesday and Feb 8, 2027 a Monday.
- **Standard:** Rozier is charged, not convicted. Anything that comes from an indictment or a government filing must be attributed. On-screen quotes must be verbatim. Uncharged private people must not be named.

## Summary

**20 FIX**, **1 UNVERIFIABLE** (photo license page), everything else **OK**.

The two most serious problems:
1. **Wrong location (3 places).** The March 23, 2023 game was played **in New Orleans**. The box score lists it as "Charlotte Hornets at New Orleans Pelicans", game ID 202303230NOP, final score CHA 96, NOP 115. The script says "Charlotte.", "The Hornets were hosting the New Orleans Pelicans" and has the title card "Nine Minutes in Charlotte".
2. **"For two and a half years, nothing happened in public" is false.** ECF 169, p. 8, says the NBA investigated, and that in January 2025 the league "issued a statement that it had investigated, found no rule violation, and was cooperating with a federal investigation", citing Reuters, Jan 30, 2025. This also leaves out a fact that favours Rozier.

---

## FIX items (ready to paste)

### FIX 1 — episode.json, line 1 (say + show): wrong city
- **Current say:** `March twenty-third, twenty twenty-three. Charlotte. Terry Rozier, the Hornets' starting guard, walks off the court in the first quarter, and does not come back. He played nine minutes and thirty-four seconds.`
- **New say:** `March twenty-third, twenty twenty-three. New Orleans. Terry Rozier, the Hornets' starting guard, walks off the court in the first quarter, and does not come back. He played nine minutes and thirty-four seconds.`
- **Current show:** `March 23, 2023. Charlotte. Terry Rozier, the Hornets' starting guard, walks off the court in the first quarter, and does not come back. He played 9 minutes and 34 seconds.`
- **New show:** `March 23, 2023. New Orleans. Terry Rozier, the Hornets' starting guard, walks off the court in the first quarter, and does not come back. He played 9 minutes and 34 seconds.`
- **Evidence:** The box score is "Charlotte Hornets at New Orleans Pelicans, March 23, 2023" (basketball-reference 202303230NOP; landofbasketball lists New Orleans as the home team, 96–115). The indictment (¶36) says only "game against the New Orleans Pelicans". "Starting guard" is OK: ECF 144 p. 2 says "a starting shooting guard for the Charlotte Hornets". 9:34 is OK per Ind. ¶41 and the box score.

### FIX 2 — episode.json, line 6, title scene
- **Current:** `"title": "Nine Minutes|in Charlotte"`
- **New:** `"title": "Nine Minutes|in New Orleans"`
- **Evidence:** As in FIX 1.

### FIX 3 — episode.json, line 8 (say): the Hornets were the road team
- **Current:** `Start with the game. The Hornets were hosting the New Orleans Pelicans. According to the indictment, Rozier was not on the team's injury report, and Hornets officials did not know he planned to leave early.`
- **New:** `Start with the game. The Hornets were on the road, in New Orleans, against the Pelicans. According to the indictment, Rozier was not on the team's injury report, and Hornets officials did not know he planned to leave early.`
- **Evidence:** As in FIX 1. The injury-report part matches Ind. ¶36 on p. 9 ("ROZIER was not on the Hornets' injury report … Hornets officials were not aware of ROZIER's plan"). The kicker ¶36 is correct, because ind_9 starts with the end of ¶36.

### FIX 4 — episode.json, line 10 (say + show): "two buyers", and the original vs. superseding difference
- **Current say:** `Prosecutors say Laster then sold that information. Two buyers, Marves Fairley and an unnamed co-conspirator, agreed to pay him about one hundred thousand dollars out of their expected winnings.`
- **New say:** `Prosecutors say Laster then sold that information. Two of the buyers, Marves Fairley and an unnamed co-conspirator, agreed to pay him about one hundred thousand dollars out of their expected winnings. In this first indictment, that money is a payment to Laster for the tip. The word bribe comes later.`
- **Current show:** `Prosecutors say Laster then sold that information. Two buyers, Marves Fairley and an unnamed co-conspirator, agreed to pay him about $100,000 out of their expected winnings.`
- **New show:** `Prosecutors say Laster then sold that information. Two of the buyers, Marves Fairley and an unnamed co-conspirator, agreed to pay him about $100,000 out of their expected winnings. In this first indictment, that money is a payment to Laster for the tip. The word bribe comes later.`
- **Evidence:** Ind. ¶37 says Laster sold the information "to multiple co-conspirators, including to the defendant MARVES FAIRLEY and Co-Conspirator 1 … FAIRLEY and Co-Conspirator 1 agreed to pay LASTER approximately $100,000 from their expected fraudulent gambling winnings." In Sup. ¶37 the ~$100,000 becomes Rozier's "bribe". Rule 3 requires the episode to show this difference. Without it, viewers hear the same $100,000 described two ways.

### FIX 5 — episode.json, line 17 (say + big lines): the government doesn't say the rebounds "prove" its case
- **Current say:** `But one number did not cooperate. Four rebounds. Hold on to that number. Both sides now say it proves their case.`
- **New say:** `But one number did not cooperate. Four rebounds. Hold on to that number. Both sides now use it to make their case.`
- **Current lines:** `["4 rebounds.", "Both sides|claim it."]`
- **New lines:** `["4 rebounds.", "Both sides|cite it."]`
- **Evidence:** ECF 169 p. 1 says he "exceeded his rebounding prop—precisely the opposite of what the alleged co-conspirators had wagered". Sup. ¶44 and ECF 144 p. 2 say the four rebounds led to the bribe being cut to ~$70,000. The government uses the stat for its story, but it never says the stat "proves" the case.

### FIX 6 — episode.json, line 26 (say + show): "nothing happened in public" is false
- **Current say:** `For two and a half years, nothing happened in public. Then, on October twenty-third, twenty twenty-five, the FBI made arrests across the country.`
- **New say:** `For two and a half years, Rozier was not charged. A defense filing says the NBA looked into the game, and in January twenty twenty-five said it had found no rule violation, and was cooperating with a federal investigation. Then, on October twenty-third, twenty twenty-five, the FBI made arrests across the country.`
- **Current show:** `For two and a half years, nothing happened in public. Then, on October 23, 2025, the FBI made arrests across the country.`
- **New show:** `For two and a half years, Rozier was not charged. A defense filing says the NBA looked into the game, and in January 2025 said it had found no rule violation, and was cooperating with a federal investigation. Then, on October 23, 2025, the FBI made arrests across the country.`
- **Evidence:** ECF 169 p. 8: "In March 2023, the NBA learned of unusual betting … The league investigated … In January 2025, the league issued a statement that it had investigated, found no rule violation, and was cooperating with a federal investigation", citing Reuters, Jan 30, 2025. Mar 23, 2023 to Oct 23, 2025 is 2 years 7 months, so "two and a half years" is fine as an approximation. The release supports "Today the FBI arrested six people" and "located across the country".

### FIX 7 — episode.json, line 30 (quote scene q): the quote is cut mid-sentence without an ellipsis
- **Current q:** `As alleged, the defendants turned professional basketball into a criminal betting operation`
- **New q:** `As alleged, the defendants turned professional basketball into a criminal betting operation …`
- **Evidence:** The release continues: "…a criminal betting operation, using private locker room and medical information to enrich themselves and cheat legitimate sportsbooks". The attribution (Nocella, Oct 23, 2025) is OK.

### FIX 8 — episode.json, line 33 (src): the plea is not in the cited source
- **Current src:** `Gov't letter opposing severance, ECF 166 (Nov 3, 2026)`
- **New src:** `Minute entry, arraignment, ECF 69 (Dec 8, 2025) · Gov't letter opposing severance, ECF 166 (Nov 3, 2026)`
- **Evidence:** m69.png (ECF 69, 12/8/25): "Defendant arraigned on the: [X] indictment … Defendant pleads NOT GUILTY to ALL counts." ECF 166 is addressed to "The Honorable LaShann DeArcy Hall", which supports the judge. ESPN (Nov 13, 2026) adds: "Rozier and Laster have pleaded not guilty."

### FIX 9 — episode.json, line 35 (say + show): name the count precisely
- **Current say:** `… with two new counts against Rozier: bribery in sporting contests, and honest services fraud.`
- **New say:** `… with two new counts against Rozier: bribery in sporting contests, and honest services wire fraud conspiracy.`
- **Current show:** `In May 2026, the case got heavier. A grand jury returned a superseding indictment, with two new counts against Rozier: bribery in sporting contests, and honest services fraud.`
- **New show:** `In May 2026, the case got heavier. A grand jury returned a superseding indictment, with two new counts against Rozier: bribery in sporting contests, and honest services wire fraud conspiracy.`
- **Evidence:** ECF 144 pp. 1 and 12 say Count Four "charges honest-services wire fraud conspiracy", and the superseding indictment "added Counts Three and Four". Line 67's list already uses the correct name, so this makes the two consistent.

### FIX 10 — episode.json, line 36 (say): keep close to the charging language
- **Current:** `Honest services means this. Prosecutors allege he cheated the Hornets and the NBA out of an honest player, by taking a bribe.`
- **New:** `Honest services means this. Prosecutors allege he schemed to deprive the Hornets and the NBA of his honest and faithful services, through a bribe.`
- **Evidence:** Sup. ¶35 on sup_8: "engaged in a scheme to defraud the Charlotte Hornets and the NBA of honest and faithful services of ROZIER through bribery." The on-screen title "honest and faithful services" is verbatim and OK.

### FIX 11 — episode.json, line 40 (say + show): "the one line he went over" is not in the sources
- **Current say:** `Now, the four rebounds. Rebounds were the one line he went over. According to the superseding indictment, …`
- **New say:** `Now, the four rebounds. Of the four stats the indictment lists, rebounds were the only one where he went over his betting line. According to the superseding indictment, because of those four rebounds, not all of the bets won. So after the game, they negotiated the bribe down to about seventy thousand dollars.`
- **Current show:** `Now, the four rebounds. Rebounds were the one line he went over. According to the superseding indictment, because of those four rebounds, not all of the bets won. So after the game, they negotiated the bribe down to about $70,000.`
- **New show:** `Now, the four rebounds. Of the four stats the indictment lists, rebounds were the only one where he went over his betting line. According to the superseding indictment, because of those four rebounds, not all of the bets won. So after the game, they negotiated the bribe down to about $70,000.`
- **Evidence:** Ind. ¶41 and Sup. ¶43 give lines only for points, assists, three-pointers (below) and rebounds (above). No source covers any other prop line, such as minutes. Sup. ¶44 on sup_13 supports "negotiated to reduce ROZIER's bribe to approximately $70,000". The kicker ¶44 is correct.

### FIX 12 — episode.json, line 48 (big lines + src): Covers did not quote this
- **Current lines:** `["\"The player", "Fairley referenced|was Rozier.\""]`, with src `As quoted by Covers (May 28, 2026)`
- **New lines:** `["A prosecutor:", "the player|was Rozier."]`, with src `As reported by Covers (May 28, 2026)`
- **Evidence:** Covers writes this as narration, not in quotation marks: "A lawyer for the U.S. Attorney's Office later said the player Fairley referenced was Rozier." Putting it in quotation marks and crediting it "As quoted by" misstates the source. The spoken line ("According to Covers, a lawyer for the U.S. Attorney's Office told the court…") is OK. "Rozier's attorney disputed that his client was paid to alter his play" is OK: Covers says his attorney "disputed the idea that his client was paid to alter his play".

### FIX 13 — episode.json, line 50 (say + big lines): overbroad, and implies guilt by contrast
- **Current say:** `So the people who allegedly bought the information, and placed the bets, are admitting it. The man whose minutes they bet on is not.`
- **New say:** `So some of the people accused of buying the information, or betting on it, have pleaded guilty. Rozier has not. He says he never knew about any bets.`
- **Current lines:** `["They admit it.", "He doesn't."]`
- **New lines:** `["Some plead guilty.", "He pleads|not guilty."]`
- **Evidence:** Only Fairley (Covers, May 28, 2026) and McCormack (Covers, Jan 22, 2026) are shown to have pleaded guilty. Hennen is still a named defendant in the superseding indictment, and no source here shows a plea from him. "They admit it. He doesn't." suggests Rozier is hiding something that others admitted, which is a defamation risk. For his denial see ECF 166 p. 2 ("He did not know about any bets") and ECF 169.

### FIX 14 — episode.json, line 54 (list kicker + item 3): it isn't in the defense's own words
- **Current kicker:** `THE DEFENSE, IN ITS OWN WORDS`. **New kicker:** `THE DEFENSE'S THREE POINTS`
- **Current item 3:** `["3", "\"Dont tell Chum bout the bet\""]`. **New item 3:** `["3", "the \"don't tell chum\" text"]`
- **Evidence:** Items 1 and 2 are paraphrases. ECF 169 spells the text "don't tell chum bout the bet" (p. 1, n. 1); the "Dont [sic] tell Chum" spelling comes from ECF 144 n. 2. The spoken line is OK: ECF 169 p. 1 cites medical evidence, the rebounding prop and the co-conspirators' communications.

### FIX 15 — episode.json, line 59 (say + show): the severance motion was joint
- **Current say:** `Rozier also asked to be tried separately from Laster. The government opposed it, calling his defense, in effect, an argument that no crime occurred, and asked to keep the joint trial, about three weeks long, starting February eighth, twenty twenty-seven.`
- **New say:** `Rozier and Laster also asked to be tried separately. The government opposed it, calling Rozier's defense, in effect, an argument that no crime occurred, and asked to keep the joint trial, about three weeks long, starting February eighth, twenty twenty-seven.`
- **Current show:** `Rozier also asked to be tried separately from Laster. The government opposed it, calling his defense, in effect, an argument that no crime occurred, and asked to keep the joint trial, about three weeks long, starting February 8, 2027.`
- **New show:** `Rozier and Laster also asked to be tried separately. The government opposed it, calling Rozier's defense, in effect, an argument that no crime occurred, and asked to keep the joint trial, about three weeks long, starting February 8, 2027.`
- **Evidence:** ECF 166 p. 1 refers to "the defendants Deniro Laster … and Terry Rozier's … joint motion to sever their trials (ECF No. 158)" and says it "essentially amounts to an argument that no crime occurred". It also gives "approximately three weeks" and "February 8, 2027, as scheduled". ECF 166 p. 2 says "Though styled as a joint motion, the instant motion is really made on behalf of Laster."

### FIX 16 — episode.json, line 62 (big lines + kicker): not a verbatim quote
- **Current kicker:** `APRIL 2023 · AS DESCRIBED BY ESPN`. **New kicker:** `APRIL 2023 · ALLEGED · AS DESCRIBED BY ESPN`
- **Current lines:** `["\"Another", "under bet\"|— a teammate."]`
- **New lines:** `["Another under bet?", "A teammate,|prosecutors say."]`
- **Evidence:** ESPN's wording is "setting up another under bets, this one involving one of Rozier's then-teammates". "Another under bet" in quotation marks is neither ESPN's text nor the text message. The spoken line is OK: ESPN says "In April 2023, Deniro Laster allegedly texted co-conspirator Marves Fairley …" and "about two weeks after Rozier left a March 23, 2023, game".

### FIX 17 — episode.json, line 63 (say + list item 4): ESPN's no-charges statement is narrower
- **Current say:** `Be careful with this one. ESPN reports it is unclear whether Rozier knew about that text, whether the teammate knew of any plan, or whether any bet was ever placed. No one has been charged over it.`
- **New say:** `Be careful with this one. ESPN reports it is unclear whether Rozier knew about that text, whether the teammate knew of any plan, or whether any bet was ever placed. The government has not charged Laster or Rozier over it.`
- **Current item:** `["0", "charges over the teammate plan"]`. **New item:** `["0", "charges against Laster or Rozier over it"]`
- **Evidence:** ESPN: "The government has not charged Laster or Rozier in relation to the alleged plan involving the Hornets teammate." ESPN also says: "It is unclear whether Rozier knew about Laster's text … whether the teammate, who was not named, was aware of any plan … or whether any attempt to bet on his unders took place." The teammate is unnamed, as he should be.

### FIX 18 — episode.json, line 68 (big scene): the claims appear on screen without attribution
- **Current:** no kicker; lines `["Planned. Sold.", "Counted."]`
- **New:** add `"kicker": "THE GOVERNMENT'S CASE · ALLEGED"`, and keep the lines.
- **Evidence:** The narration attributes these claims to the government, but a still frame or clip showing "Planned. Sold. Counted." reads as fact. Rule 2 applies.

### FIX 19 — short2.json, line 3 (say): use "superseding" and "alleges"
- **Current:** `But four rebounds went over. Some bets lost. So, the indictment says, the bribe was negotiated down.`
- **New:** `But four rebounds went over. Some bets lost. So, the superseding indictment alleges, the bribe was negotiated down.`
- **Evidence:** The original indictment (ECF 17) has no bribe and no reduction to $70,000. Both appear only in Sup. ¶44, which is the kicker of that same scene.

### FIX 20 — short3.json, title: the government does not "claim" the text
- **Current:** `"Dont Tell Chum Bout the Bet": The Text Both Sides Claim`
- **New:** `"Dont Tell Chum Bout the Bet": The Text Both Sides Fight Over`
- **Evidence:** ECF 144 n. 2 says the "text chain does not relate to sports gambling". ECF 169 n. 1 says the government "may move to exclude the text". The two sides dispute the text; only the defense relies on it.

---

## UNVERIFIABLE

- **Photo license** (episode line 1 src, meta summary and docs_note): "Keith Allison · CC BY-SA 2.0 · 2017". The WebFetch of https://commons.wikimedia.org/wiki/File:Terry_Rozier_(33650529273).jpg was blocked, because the permission request timed out, and the Commons API call returned no JSON. Partial check: the local file's EXIF (dl16/rozier_commons.jpg) has Artist "Keith Allison" and ImageDescription "Celtics at Wizards 5/4/17". That matches the author and the 2017 date. **Fix:** open the Commons page by hand and confirm the license reads "CC BY-SA 2.0" before publishing. CC BY-SA also needs the "cropped" change notice, which meta already has.

---

## Line-by-line verdicts

### episode.json
| # | Content (short) | Verdict | Source / note |
|---|---|---|---|
| 1 | Cold open, "Charlotte", starting guard, 9:34, photo | **FIX 1** | Game was in New Orleans. Rest OK (ECF 144 p. 2; Ind. ¶41). Photo: see UNVERIFIABLE |
| 2 | Prosecutors allege ~$100,000 bribe; doc sup_9 ¶37, "an approximately $100,000 bribe" | OK | Sup. ¶37 verbatim. Attributed ("They allege") |
| 3 | "Terry Rozier is innocent. The objective evidence proves it." Nov 12 | OK | ECF 169 p. 1, verbatim; filed 11/12/26 |
| 4 | "One day later, according to ESPN, prosecutors filed new papers…" | OK | ESPN: government "court filing Friday" (Nov 13); Markus filing "Thursday" (Nov 12) |
| 5 | Not guilty; presumed innocent; trial Feb 8, 2027 | OK | ECF 69; release; ECF 166 |
| 6 | Title card "Nine Minutes in Charlotte" | **FIX 2** | New Orleans |
| 7 | Chapter I | OK | |
| 8 | "Hornets were hosting"; injury report; doc ind_9 ¶36 | **FIX 3** | Location wrong; rest OK |
| 9 | Told Laster: "supposed injury", not return; ind_8 ¶36 | OK | Ind. ¶36 verbatim; "longtime friend" from release |
| 10 | Two buyers, ~$100,000; ind_9 ¶37 | **FIX 4** | "multiple co-conspirators, including"; and the original vs. superseding difference |
| 11 | Hennen ~$61,200 at a retail sportsbook; associate ~$107,000; ind_10 ¶39 | OK | Ind. ¶39 and ¶39(a) |
| 12 | Under-bet explainer | OK | Ind./Sup. ¶26, ¶29 |
| 13 | DOJ: more than $200,000 placed and directed | OK | Release: "place and direct more than $200,000 in wagers" |
| 14 | 5 pts / 2 ast / 1 three vs 21.1 / 5.1 / 2.6; ind_12 ¶41 | OK | Ind. ¶41; box score matches |
| 15 | 9:34 vs 35.3 avg (bars) | OK | Ind. ¶41 |
| 16 | Hornets lost; gov't says many bets paid off; g144_7 quote | OK | ECF 144 p. 2 verbatim; release "many of the bets paid off"; final score 96–115 |
| 17 | "Both sides now say it proves their case" | **FIX 5** | |
| 18 | Chapter II | OK | |
| 19 | Five days later, Philadelphia; Rozier "arranged and paid for"; ind_12 ¶42 | OK | Ind. ¶42: "On or about March 28, 2023" = 5 days; verbatim |
| 20 | Cash late night Mar 28 to early Mar 29, "allegedly" | OK | Ind. ¶42 / Sup. ¶45 |
| 21 | "drove hundreds of miles through the night"; g144_8 | OK | ECF 144 p. 3 verbatim |
| 22 | Counted money early Apr 1, 2023; sup_14 ¶46 | OK | Sup. ¶46 (also Ind. ¶43) |
| 23 | "photographed themselves counting the cash" | OK | ECF 144 p. 3 verbatim; "August filing" = Aug 26, 2026 |
| 24 | Rozier denies; "Cash is not a confession" | OK | ECF 166 p. 2; ECF 169. Editorial line, not presented as a quote |
| 25 | Chapter III | OK | |
| 26 | "nothing happened in public" | **FIX 6** | ECF 169 p. 8 (NBA Jan 2025 statement) |
| 27 | Arrested in Orlando; "USA v. Rozier" | OK | M.D. Fla. 6:25-mj-02183, filed 10/23/2025, "Arrest pursuant to Rule 5(c)(2)"; ECF 26 filed 10/27/25 |
| 28 | Unsealed; six defendants; two conspiracy charges; "Scary Terry", "Chum"; ind_1 | OK | Release; ind_1 caption |
| 29 | "Chum" — remember it | OK | Release |
| 30 | Nocella quote | **FIX 7** | Ellipsis needed |
| 31 | Tisch quote | OK | Release, verbatim, full sentence |
| 32 | Jones; Blazers 3/24/23; Magic 4/6/23; Lakers 2/9/23 and 1/15/24; Porter 2024, pleaded guilty | OK | Release |
| 33 | Not guilty; Judge LaShann DeArcy Hall | **FIX 8** | Add ECF 69 to src |
| 34 | Chapter IV | OK | |
| 35 | May 2026 superseding; two new counts; sup_8 ¶35 | **FIX 9** | Count Four's name |
| 36 | "cheated … out of an honest player"; "honest and faithful services" | **FIX 10** | Sup. ¶35 |
| 37 | Lower leg injury; kept playing; planned to use it; sup_9 ¶37 | OK | Sup. ¶37 verbatim; attributed ("it alleges") |
| 38 | ~$100,000 bribe; to-be-determined game; portion to Laster | OK | Sup. ¶37 |
| 39 | Encrypted applications | OK | Sup. ¶37 |
| 40 | "the one line he went over"; reduced to ~$70,000; sup_13 ¶44 | **FIX 11** | |
| 41 | $100K agreed → $70K "delivered"; "$30,000 discount" | OK | Sup. ¶44; ECF 144 p. 3 ("picked up approximately $70,000 cash"). $30K is plain subtraction under the government's attribution; bars are labelled ALLEGED |
| 42 | "For taking a bribe … four distinct but related crimes"; g144_6 | OK | ECF 144 p. 1 verbatim; attributed as the government's sentence |
| 43 | Chapter V | OK | |
| 44 | "He fights. Others plead." | OK | |
| 45 | McCormack, 2 years, Judge DeArcy Hall, Jan 2026; with "another man" ~$41,000 | OK | Covers Jan 22, 2026; Ind. ¶39(b). Pham is not named on screen; he is a convicted co-defendant in any case |
| 46 | Jones: 2 counts of wire fraud conspiracy, two cases; AP "insider information"; sentencing Jan 6, 2027; Apr 28, 2026 | OK | CBS News (Tabachnick), crediting AP |
| 47 | Fairley May 28: 7 felony counts in 2 cases; quote | OK | Covers: "seven felony charges in two cases"; quote verbatim |
| 48 | "The player Fairley referenced was Rozier" in quotation marks | **FIX 12** | Covers narration, not a quote |
| 49 | Sentencing in February; up to 20 years on 6 counts; $676,700 penalty | OK | Covers: "next February"; "maximum of 20 years in prison in six of the seven counts"; "$676,700 penalty" |
| 50 | "They admit it. He doesn't." | **FIX 13** | |
| 51 | Chapter VI | OK | |
| 52 | "He did not know about any bets." / hurt; g166_2 | OK | ECF 166 p. 2 verbatim |
| 53 | "he never placed a bet …" | OK | ECF 169 p. 1 verbatim |
| 54 | Three points; "IN ITS OWN WORDS" | **FIX 14** | |
| 55 | "Dont [sic] tell Chum bout the bet"; g144_8 fn 2 | OK | ECF 144 n. 2 verbatim; "third party" |
| 56 | Defense says the text "guts" the case | OK | ECF 169 n. 1: "guts its case" |
| 57 | Gov't "evidence from multiple sources … does not relate to sports gambling"; defense says table games at a casino | OK | ECF 144 n. 2 verbatim; ECF 169 n. 1 |
| 58 | "If the text is admitted at all" | OK | ECF 169 n. 1: "may move to exclude the text" |
| 59 | "Rozier also asked to be tried separately" | **FIX 15** | Joint motion |
| 60 | Chapter VII | OK | |
| 61 | "last week … November 13, ESPN reported" | OK | Nov 13, 2026 (Fri) falls in the week before Tue Nov 17. ESPN byline David Purdum |
| 62 | April 2023 teammate text; "Another under bet" in quotation marks | **FIX 16** | Spoken line OK |
| 63 | Unknowns; "No one has been charged" | **FIX 17** | |
| 64 | Lied to NBA; phones; legal fees; "last game of the season" | OK | ESPN: "lying to the NBA during the league's investigation and failing to turn over all his phones"; "paying for the legal defense of Laster and his siblings"; "told people close to him that the March 23 game would be his last of the season". Labelled alleged |
| 65 | Markus: "in the strongest possible way" | OK | ESPN: "David Markus, Rozier's attorney, told ESPN on Friday that they deny the new allegations 'in the strongest possible way.'" |
| 66 | NBA statement; q "We continue to cooperate with the government's investigation." | OK | ESPN, "an NBA spokesperson told ESPN in a statement"; q verbatim; paraphrase is faithful |
| 67 | Four counts; original charges max 20 years each | OK | ECF 144 p. 1; release |
| 68 | "Planned. Sold. Counted." | **FIX 18** | No on-screen attribution |
| 69 | "Hurt or paid?"; Feb 8, 2027 | OK | ECF 166. Optional: "is set to be asked" instead of "will be asked", in case the trial date moves |
| 70 | End card; "presumed innocent" | OK | |

### short1.json
| Item | Verdict | Note |
|---|---|---|
| Title "$100,000 to Leave a Game Early? The Terry Rozier Case" | OK | Phrased as a question; the line itself attributes it to prosecutors |
| L1 hook: tag CHARGED, "$100K", "ALLEGED BRIBE / TO LEAVE A GAME"; "prosecutors say … agreed to" | OK | Sup. ¶37 |
| L2 9:34; not on injury report; ind_12 ¶41 | OK | Ind. ¶41, ¶36 |
| L3 more than $200,000 bet on his unders | OK | Release |
| L4 says hurt, never knew; trial Feb 8 | OK | ECF 166 |
| L5 "Injury, or a setup?" | OK | |

### short2.json
| Item | Verdict | Note |
|---|---|---|
| Title "Four Rebounds Cut the Alleged Bribe to $70K, Feds Say" | OK | Sup. ¶44 |
| L1 hook "$70K", "AFTER 4 REBOUNDS / PROSECUTORS SAY"; $100,000 → $70,000 | OK | Sup. ¶37, ¶44 (both approximate) |
| L2 left after nine minutes; points, assists and threes under the lines | OK | Ind. ¶41 |
| L3 "the indictment says, the bribe was negotiated down" | **FIX 19** | Superseding only |
| L4 defense: played hard, beat rebounding prop | OK | ECF 169 p. 1 |
| L5 end | OK | |

### short3.json
| Item | Verdict | Note |
|---|---|---|
| Title "… The Text Both Sides Claim" | **FIX 20** | |
| L1 hook "Dont tell Chum bout the bet"; Chum = nickname | OK | ECF 144 n. 2; release. "may decide his case" is opinion |
| L2 Laster sold word of the early exit; ind_8 ¶36 | OK | Ind. ¶37 (sold). ¶36 is visible on ind_8 |
| L3 sent from Philadelphia; defense says it proves he never knew | OK | ECF 144 n. 2; ECF 169 |
| L4 gov't: nothing to do with sports gambling | OK | Faithful paraphrase of ECF 144 n. 2 ("does not relate to sports gambling") |
| L5 trial in February | OK | |

### thumb2.json
| Thumb | Verdict | Note |
|---|---|---|
| A: BREAKING / "NBA STAR CHARGED" / "LEFT GAME AFTER 9 MIN" / "$100K ALLEGED BRIBE" | OK | "Charged" is accurate. "Star" is a judgement call for a former 21.1-ppg starter with a ~$96M extension (ECF 169 p. 9), and it doesn't imply guilt. "Left after 9 min" is a record fact (9:34). "BREAKING" is a stretch for news 4 days old, but it isn't a factual claim |
| B: CHARGED / "TERRY ROZIER" / "HURT OR PAID?" / "9:34 MINUTES PLAYED" | OK | Neutral question; 9:34 matches the box score |
| C: CHARGED / "4 REBOUNDS" / "COST $30K, FEDS SAY" / "$70K CASH, FEDS ALLEGE" | OK (note) | $30K is ~$100K − ~$70K from Sup. ¶37/¶44, and ECF 144 p. 3 gives "$70,000 cash". Both are qualified with FEDS SAY / FEDS ALLEGE. The government never states "$30K" itself; if you want zero inference, use line2 "$100K → $70K, FEDS SAY" |

### meta.json
| Field | Verdict | Note |
|---|---|---|
| title "Terry Rozier: The Alleged $100K Bribe to LEAVE an NBA Game" | OK | "Alleged" |
| summary | OK | "Former Charlotte Hornets guard" is correct (he was traded later; CBS says Miami released him in April 2026). The four charges match ECF 144. "Laster has also pleaded not guilty" — ESPN: "Rozier and Laster have pleaded not guilty". "Fairley and Damon Jones have pleaded guilty" — Covers and CBS. Filings Nov 12–13 are correct |
| docs_note | OK | Docket caption and ECF numbers correct; the photo license is UNVERIFIABLE (see above) |
| question / first_comment | OK | first_comment: "played hard" — ECF 169 says "played hard and exceeded his rebounding prop" |
| tags / hashtags | OK | Neither the docket "(LDH)" nor any tag implies guilt |
| sources list | OK | URLs as listed. Note that ECF 17/144 point at RECAP docket 537695 while the others use 537701; both are the 25-cr-323 dockets |

## Doc-scene kicker and title audit (rule 6)
I viewed all of the images.
- ind_1 (p. 1, caption: six defendants, nicknames) — OK
- ind_8 (p. 8, ¶36 "a supposed injury") — OK
- ind_9 (p. 9: end of ¶36, the injury report; ¶37, ~$100,000) — both kickers OK
- ind_10 (p. 10, ¶39 continued, $61,200) — OK
- ind_12 (p. 12, ¶41 stats; ¶42 "arranged and paid for") — OK
- sup_8 (¶35, honest and faithful services) — OK
- sup_9 (¶37: lower leg injury, ~$100,000 bribe, encrypted applications) — OK
- sup_13 (¶44, ~$70,000) — OK
- sup_14 (¶46, April 1 count) — OK
- g144_6 (preliminary statement, four crimes) — OK
- g144_7 ("His team, the Hornets, lost the game.") — OK
- g144_8 ("through the night", "photographed themselves counting the cash", fn 2) — OK
- g166_1 (joint trial Feb 8, 2027) — OK
- g166_2 ("He did not know about any bets.") — OK

## Private individuals (rule 5)
No uncharged private individual is named. Co-Conspirators 1–9, Laster's relatives, Rozier's relative and the Hornets teammate are all unnamed. People who are named are defendants, people who have pleaded guilty or been convicted (Fairley, Jones, McCormack, Porter), public officials, or counsel.

## Say/show number match (rule 4)
Every spoken number matches the digits on screen.

## Applied (2026-11-16, before the final build)
- All 20 FIX items applied in make_spec.py / make_shorts.py (episode.json, short1–3.json regenerated). Game location confirmed independently: NBA official box score "20230323_CHANOP" (Charlotte at New Orleans, 96–115) — added to meta.json sources.
- Thumbnail C line 2 changed to "$100K TO $70K, FEDS SAY" (checker's optional suggestion). Thumbnail A "NBA STAR CHARGED" kept (checker: acceptable).
- Short 3 title shortened to "\"Dont Tell Chum Bout the Bet\": The Disputed Text" (≤ 60 chars, neutral).
- UNVERIFIABLE photo license: resolved — Commons API extmetadata (fetched 2026-11-16) for File:Terry_Rozier_(33650529273).jpg: Artist Keith Allison, LicenseShortName "CC BY-SA 2.0", description "Celtics at Wizards 5/4/17".
