# Fact-check — SWORN 021 (Lumumba)

Checker: independent; did not write the script. Checked: episode.json (lines 0–81), short1–3.json (incl. titles), thumb2.json (A/B/C), meta.json (title, summary, question, first_comment, docs_note).

## Sources
Opened and used:
- Indictment, Dkt. 3 (OCR pp. 1–32, /home/claude/dl/ind_pages.txt) plus page images p-16 to p-19 (photos) and p-33 (Dkt. 3-1, notice of maximum penalties).
- USAO S.D. Miss. press release, Nov 7, 2024 (/home/claude/dl/doj/pr24.txt).
- WLBT Nov 20, 2026, "what was said": opened. Quotes from Jordan, Lumumba and Evelyn confirmed. The fetch tool limits quotes, so the Ask Antar wording was checked twice.
- WLBT Nov 20, 2026, "former mayor sentenced": opened ($50,000 forfeiture in lieu of a fine; one count of conspiracy).
- WAPT Nov 20, 2026: opened (3 yrs 1 mo; forfeiture of $50,000 "just days prior"; all three report Jan 4).
- Magnolia Tribune Nov 20, 2026: opened (Lee first official charged, pleaded Aug 2024 and resigned that day; all three initially pleaded not guilty; motions on entrapment, misconduct, venue and severance; disbarred in October).
- SuperTalk Nov 20, 2026: opened (Owens 41 mo + $100K; Banks 45 mo + $15K; unseated by Horhn June 2025; Lee still awaiting sentencing).
- The Hill Nov 20, 2026: opened (son of former mayor Chokwe Lumumba; "youngest mayor in city history … at just 34").
- Mississippi Today Nov 5, 2026: opened (see FIX 13: the Fulcher exchange was part of LUMUMBA's presentence hearing, not Owens's).
- WLOX July 6, 2026: opened (plea Monday July 6, 2026; AUSA Fulcher read the facts; "I accept the facts…"; up to 5 yrs + $250K).
- Mississippi Free Press July 6, 2026: opened (Banks pleaded shortly after; Owens a week earlier; "more substantive charges"; Lee and Smith also pleaded guilty).
- NBC News (undated in the fetch, 2024): opened (Smith, Owens's relative, pleaded guilty to conspiracy to commit bribery; Lee resigned and pleaded guilty; "two men").
Could not open: none. Limitation: the fetch tool returns quotes of 125 characters or fewer, so long quotes were checked in segments.

Status of people: Owens, Lumumba and Banks pleaded guilty (one conspiracy count each) and were sentenced. Lumumba accepted the facts AUSA Fulcher read at his plea: $50K in five $10K checks from FBI sources posing as developers, received Apr 2, 2024 in Ft. Lauderdale, the RFQ due-date change, the Apr 4 deposit and a partial withdrawal for personal use. Lee and Smith pleaded guilty to conspiracy (Magnolia, MFP, NBC) and as of Nov 5 / Nov 20, 2026 had not been sentenced (MS Today, SuperTalk). Facts beyond those read at the plea come only from the indictment.

## FIX items

1. **episode.json line 10 (say/show)**: "…introduced them to the most powerful prosecutor in the county."
   Problem: "Most powerful" is the narrator's characterization. Also, per ¶21 Witness 1 introduced Developer 1 only, not "them."
   Replace say: "In August twenty twenty-three, a local man introduced one of them to the county's top prosecutor. Jody Owens, the district attorney of Hinds County, which includes Jackson."
   Replace show: "In August 2023, a local man introduced one of them to the county's top prosecutor. Jody Owens, the district attorney of Hinds County, which includes Jackson."

2. **episode.json line 15 (say + scene.lines)**: "Remember, the district attorney is the person who decides who gets prosecuted in Jackson. And he had just set a price." / lines ["The prosecutor","set a price."]
   Problem: Overstated (¶5 says only that he was "responsible for … enforcing criminal laws in Jackson"). The "price" (the ¶25 fee) is unattributed narration of an indictment-only allegation.
   Replace say: "Remember, the district attorney is the county's chief prosecutor. And, according to the indictment, he had just negotiated his price."
   Replace lines: ["The prosecutor", "named his price."] and add kicker "PER THE INDICTMENT".

3. **episode.json line 17 (say/show)**: "The FBI's jet takes Owens to Fort Lauderdale."
   Problem: ¶26 says "a private jet paid for by the FBI on behalf of the Developers." The FBI did not own the jet.
   Replace say: "December thirteenth, twenty twenty-three. A private jet, paid for by the F.B.I., takes Owens to Fort Lauderdale. …" (rest unchanged)
   Replace show: "December 13, 2023. A private jet, paid for by the FBI, takes Owens to Fort Lauderdale. …" (rest unchanged)

4. **episode.json line 26 (say + scene.lines)**: say "…almost everything the mayor said and did with them would end up in an indictment." / lines ["They were FBI.", "Everything was recorded."]
   Problem: The indictment says only that the Apr 2 yacht meeting was "audio and video recorded" (¶55). "Everything was recorded" is unsupported. Developer 1 was an FBI confidential source, not an FBI employee.
   Replace say: "They were. And much of what the mayor said and did with them would end up in a federal indictment."
   Replace lines: ["They worked for the FBI.", "The yacht was recorded."]

5. **episode.json line 33 (say/show)**: "Then came the question of the mayor. …"
   Problem: Sequence error. This exchange is ¶39, Feb 28, 2024, but line 32 just described Lee's Mar 27–28 shopping trip, so "Then" is false. Also, per ¶39 the answer came from Smith.
   Replace say: "Back on February twenty-eighth, the question of the mayor had come up. Why do we need him, one developer asked. Because, Owens's relative answered, according to the indictment, he could make things a lot harder."
   Replace show: "Back on February 28, the question of the mayor had come up. \"Why do we need [him]?\" one developer asked. Because, Owens's relative answered, according to the indictment, he \"could make things a lot harder.\""

6. **episode.json line 38 (say/show)**: "On March ninth, Owens met the mayor at the mayor's house. The next day he told the developers…"
   Problem: The house meeting is known only from Owens's Mar 10 call to Developer 1 (¶49). The indictment itself shows only a Mar 9 "outside" text (¶48). The script states it as fact about Lumumba, and it was not among the facts read at his plea.
   Replace say: "On the evening of March ninth, Owens texted the mayor that he was outside. The next day, according to the indictment, he told the developers he had met the mayor at his house, and that everyone was on one accord. Fifty thousand dollars in Florida. And, he said, the mayor's final number was a hundred thousand."
   Replace show: "On the evening of March 9, Owens texted the mayor that he was \"outside.\" The next day, according to the indictment, he told the developers he had met the mayor at his house, and that everyone was \"on one accord.\" $50,000 in Florida. And, he said, the mayor's \"final number\" was $100,000."

7. **episode.json line 39 (say/show)**: "…Then he paid them all back."
   Problem: ¶54 says "OWENS reimbursed SMITH and the two associates in full." Owens and Company B were not "paid back."
   Replace say: "…Then he reimbursed his relative and the two associates in full."
   Replace show: "…Then he reimbursed his relative and the two associates in full."

8. **episode.json line 42 (say/show)**: "…The F.B.I. records it all."
   Problem: ¶55 says the yacht meeting was audio- and video-recorded, not the whole trip.
   Replace say: "…They meet in a private room on a yacht. The meeting is recorded, on audio and video."
   Replace show: "…They meet in a private room on a yacht. The meeting is recorded, on audio and video."

9. **episode.json line 44 (show)**: 'Owens: "So we did five $10,000 checks to make it very simple." Lumumba: "Yeah."'
   Problem: In ¶55 Owens's sentence continues ("…and then when we get past the process, to our second phase … we'll do something similar.") before Lumumba says "Yeah." The subtitle's closed quote implies a direct reply. The scene.q card correctly uses "…".
   Replace show: 'Owens: "So we did five $10,000 checks to make it very simple …" Lumumba: "Yeah."'
   Optional say: "Owens: So we did five ten-thousand-dollar checks to make it very simple, and, he went on, they'd do something similar later. Lumumba: Yeah."

10. **episode.json line 48 (say)**: "…That was the official act that was for sale."
   Problem: This is the narrator's conclusion, stated as fact. It is the indictment's theory (¶58, Counts 4/5), and at sentencing the prosecutor himself argued the scheme was broader (see FIX 13).
   Replace say: "Why does a deadline matter? Because, as the indictment puts it, an earlier deadline made it likely that competition for the project would be eliminated. In the indictment, that was the official act the money bought."

11. **episode.json line 53 (say/show)**: "…And the man who paid it all was an F.B.I. employee."
   Problem: Imprecise. The $50K went from "the Developers" to Owens (¶54), and the checks were handed over by Developer 2, an "undercover employee and CHS employed by the FBI" (¶11). "The man who paid it all" is not supported.
   Replace say: "Fifty thousand dollars in. Fourteen thousand five hundred out, to the mayor himself. And the money had come from the F.B.I.'s own undercover developers."
   Replace show: "$50,000 in. $14,500 out, to the mayor himself. And the money had come from the FBI's own undercover developers."

12. **episode.json line 63 (scene.q)**: "not going to walk around as if I'm guilty of something I am not."
   Problem: WLBT puts the quote marks after "not". The article quotes "going to walk around as if I'm guilty of something I am not." and paraphrases the "not."
   Replace q: "… going to walk around as if I'm guilty of something I am not." (say is unchanged; it is a paraphrase).

13. **episode.json line 71 (say/show/scene.q/case)**: "At Owens's hearing, Lumumba's lawyers had argued about what exactly the mayor was paid to do. The lead prosecutor, Dave Fulcher, answered: The bribery scheme was not, we need him to move the R.F.Q. The bribery scheme was, we need him involved."
   Problem: Mississippi Today places this in LUMUMBA's presentence hearing on Nov 5 (the same day Owens was sentenced), while the judge was weighing Lumumba's objections. The judge said "The ask was to move the date of the RFQ." Fulcher called that "a strawman that has been set up by Lumumba's counsel" and said "The bribery scheme was, 'We need him involved.'" The first half of the card quote ("The bribery scheme was not, 'We need him to move the RFQ.'") could not be verified verbatim.
   Replace say: "On November fifth, the day Owens was sentenced, Lumumba's own sentencing hearing began. The judge noted that the ask had been to move the date of the R.F.Q. The lead prosecutor, Dave Fulcher, called that a strawman set up by Lumumba's lawyers. The bribery scheme, he said, was: we need him involved."
   Replace show: "On November 5, the day Owens was sentenced, Lumumba's own sentencing hearing began. The judge noted that \"the ask was to move the date of the RFQ.\" The lead prosecutor, Dave Fulcher, called that \"a strawman that has been set up by Lumumba's counsel.\" \"The bribery scheme was, 'We need him involved.'\""
   Replace q: "That is a strawman that has been set up by Lumumba's counsel. … The bribery scheme was, 'We need him involved.'"
   case: "Dave Fulcher, federal prosecutor · Nov 5, 2026 · Lumumba presentence hearing"

14. **episode.json line 72 (say)**: "Then, on November twentieth, it was the mayor's turn."
   Problem: Follows from FIX 13. His hearing began Nov 5 and concluded Nov 20.
   Replace say: "Then, on November twentieth, the mayor's hearing resumed. His lawyer, Gerald Evelyn, told the court: He has no prior record or arrest of any kind."

15. **episode.json line 69 (say)**: "…the government dropped the other, more serious charges, according to the Mississippi Free Press."
   Problem: MFP says "drop the more substantive charges in exchange for Monday's pleas." "Serious" is not MFP's word.
   Replace say: "The conspiracy count carries up to five years in prison. In exchange for the pleas, the government agreed to drop the more substantive charges, according to the Mississippi Free Press."

16. **short3.json line 0 (say/show)**: "Twenty thousand dollars in cash, in a lockbox…" / "$20,000 in cash…"
   Problem: ¶65 says "approximately $20,000." The long video already says "about."
   Replace say: "About twenty thousand dollars in cash, in a lockbox made to look like the Constitution. The F.B.I. found it in a district attorney's office."
   Replace show: "About $20,000 in cash, in a lockbox made to look like \"The Constitution.\" The FBI found it in a district attorney's office."
   (The title and hook number "$20,000" can stay as rounding.)

## Verified OK (high level)
- Cold open and chapters I–V: all other dates, amounts and paragraph numbers match the indictment, including ¶¶16, 18, 19, 21–35, 37, 39–40, 44, 46–47, 49, 52, 54–63 and 65, and Count 11. Spoken and subtitle numbers match on every line.
- Verbatim quotes match the indictment: ¶23 ("own enough of the city"; "a bag of [expletive] information on all the city councilmen"; "get votes approved"), ¶24, ¶26 "easier", ¶27, ¶30, ¶31, ¶32, ¶33 (with ellipses), ¶39, ¶40, ¶46, ¶47, ¶55 (q card), ¶57, and Count 11 "none exist".
- Indictment-only allegations about Owens, Banks, Lee and Smith are attributed in narration or on cards citing the indictment. Lee and Smith's guilty pleas and unsentenced status are stated correctly (line 79; meta summary).
- Photo captions: ph_call is the still under ¶56 (p.16). ph_sofa is the still at the top of p.17, between ¶57 and ¶58, so "¶¶ 57–59" is acceptable. ph_bag follows ¶60 (p.18). ph_book is the ¶65 lockbox photo (p.19). t_checks is a typeset ¶57 quote card, not a fabricated check image.
- Press release: Gee quote verbatim (spoken version truncated, card complete); "merely an allegation"; 5 counts for Lumumba; FBI agent "approached Owens, identified himself" (line 55).
- Hearings: 37 months, Judge Daniel Jordan, all WLBT quotes (Evelyn, Lumumba ×2, Jordan ×3, and the paraphrase of the "below the guideline range" line); law license given up and disbarred in October; can never hold elected office; $50K forfeiture; report date Jan 4 for all three; Owens 41 mo + $100K, sentenced Nov 5; Banks 45 mo + $15K; MS Today's 37–46 range; plea July 6, 2026, one conspiracy count, Banks the same afternoon, Owens about a week earlier; up to 5 years (Dkt. 3-1, Count 1); Lee first charged, Aug 2024 plea and resignation; all three initially pleaded not guilty; defense motions; Horhn 2025; The Hill (son of a former mayor, youngest at 34); "two men" (NBC).
- Titles and thumbnails: "bribe", "$50K", "FBI sting", "THE FBI WAS FILMING" (¶55 audio and video), "37 MONTHS", "FIVE $10K CHECKS" and "$50K TO MOVE A DEADLINE?" (a question; matches ¶58 and the judge's "The ask was to move the date of the RFQ") are all supported by the plea facts and the indictment. "BREAKING" is OK: the sentencing was Nov 20 and the publish date is Nov 22, 2026, inside 7 days. Short titles are OK.
- meta.json title, summary, question and first_comment are OK. Nit: docs_note says hearing quotes come from "…and the Mississippi Free Press", but no MFP quote is used. Optional: drop MFP from that sentence.

FIX count: 16
