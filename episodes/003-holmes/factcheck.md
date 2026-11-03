# Fact-check — SWORN Case 003: United States v. Elizabeth A. Holmes

Checked 2026-11-03 by an independent fact-checker. The script and sources.md were used only as pointers; every claim was checked against the primary sources below.

## Sources actually opened
- Dkt. 1 Indictment (Jun 14, 2018) — cover page (text layer); filed 06/14/18.
- Dkt. 469 Third Superseding Indictment (Jul 28, 2020) — p.6 ¶(C) "null protocol"; p.10 counts 3–8 wire table (investors anonymized as Investor #1–#6).
- Dkt. 1235 Final verdict form (Jan 3, 2022) — rasterized all 3 pages and read them: Ct 1 Guilty; Ct 2 Not Guilty; Cts 3–5 blank; Cts 6, 7, 8 Guilty; Cts 10, 11, 12 Not Guilty. (Page 2 shows patient initials "E.T." and "M.E." in Counts 10–11.)
- Dkt. 1236 Minute order (Jan 3, 2022) — mistrial as to Cts 3, 4, 5.
- Dkt. 1642 Defense sentencing memo — "a term of eighteen months or less"; "home confinement … is sufficient."
- Dkt. 1643 Gov't sentencing memo (Nov 11, 2022) — pp. 6–12, 17–21.
- Dkt. 1660 Sentencing minutes (Nov 18, 2022); Dkt. 1712 Order on sentencing (Jan 10, 2023); Dkt. 1716 Judgment (Jan 11, 2023); Dkt. 1757 Order denying release pending appeal (Apr 10, 2023); Dkt. 1760 Order on restitution (May 16, 2023); Dkt. 1762 Order setting reporting date (May 30, 2023).
- Dkt. 1790 (9th Cir. opinion, Feb 24, 2025) and Dkt. 1802 (order and amended opinion, Dec 22, 2025).
- Dkt. 1816 Order granting sentence modification (Mar 26, 2026).
- DOJ USAO-NDCA release, Jan 4, 2022 (WebFetch); DOJ USAO-NDCA case page (WebFetch); SEC press release 2018-41 (WebFetch); Forbes, Sept 24, 2026 (WebFetch); ABC News, Jan 21, 2026 (WebFetch).
- WebSearch: Balwani verdict date (CNBC/KPBS/NPR affiliates, Jul 7, 2022). I also searched for any clemency decision. I found no report of a grant or denial as of 2026-11-03. The latest dated status is Forbes, Sept 24, 2026: "pending".
- Image crops in img/ were checked against make_img.py: memo_rev.jpg, memo_trial.jpg and memo_wsj.jpg were viewed directly; verdict pages were viewed through the Dkt. 1235 rasters.

Key cross-source finding: the restitution order (Dkt. 1760, p.18) orders $452,047,268 to **14** payees: 12 investors identified at sentencing plus Walgreens ($40,000,000) and Safeway ($14,500,000). The Ninth Circuit agrees ("$452 million to fourteen victims"; "$397 million for the twelve victims identified at sentencing and $54.5 million for two other victims, Safeway and Walgreens"). Dkt. 1816's background paragraph says "ten investor-victims … in addition to Walgreens and Safeway, for a total of 12". That is a miscount in the 2026 order and should not be used as the source.

## episode.json

| file | line# | field | claim | verdict | source | fix text |
|---|---|---|---|---|---|---|
| episode | 0 | say/show/scene | Jan 3, 2022 verdict; San Jose; kicker "FINAL VERDICT FORM" | OK | Dkt. 1235 p.1 (San Jose Division, dated 1/3/22) | |
| episode | 1 | say/scene | Count 1, conspiracy vs. investors: "Guilty" | OK | Dkt. 1235 p.1 | |
| episode | 2 | say/scene | Count 2, conspiracy vs. patients: "Not Guilty" | OK | Dkt. 1235 p.1 ("paying patients") | |
| episode | 3 | say/scene | 3 more investor counts guilty; patient counts not guilty; 3 counts hung | OK | Dkt. 1235 pp.2–3; Dkt. 1236 | |
| episode | 3 | scene.img (verdict2.jpg) | Crop shows Counts 10–11 with patient initials "E.T." and "M.E." | NOTE | Dkt. 1235 p.2 lines 21–28 | These are initials, not names, and they are in the public record. To be cautious, blur them or crop page 2 at y≤0.68 (above Count 10). verdict2.jpg is also used in short1 line 3. |
| episode | 4 | say/scene | Split verdict; jury found she defrauded investors | OK | Dkt. 1716 | |
| episode | 4 | say | "This is how prosecutors proved it" | NOTE | — | Many later details are prosecutors' allegations or the government's sentencing account, not jury findings. Optional wording: "This is the case prosecutors made, and what happened to her after." |
| episode | 5 | scene | Title, N.D. Cal., 2018–2026 | OK | — | |
| episode | 6 | say | Chapter title | OK | — | |
| episode | 7 | say/show/scene | Founded 2003; CEO until 2018, per appeals court | OK | Dkt. 1802 p.9 | |
| episode | 8 | say/scene.q | "[O]ne tiny drop changes everything." Court opens with it | OK (verbatim) | Dkt. 1802 p.8 | |
| episode | 9 | say/scene | fast, accurate and affordable tests with a drop of blood from the prick of a finger | OK | Dkt. 1802 p.8 | |
| episode | 10 | say/show | "In the fall of 2013, it launched its testing services in Walgreens stores, and began raising money." | FIX | Dkt. 1802 p.11: "After publicly launching its testing services at Walgreens in the fall of 2013, Theranos raised funds by offering shares to investors." Theranos had raised money for years before 2013 (e.g. Dkt. 1643 p.8, Safeway 2010). | say: "In two thousand ten, Theranos partnered with Walgreens. In the fall of two thousand thirteen, it launched its testing services in Walgreens stores, then raised new money from investors." show: "In 2010, Theranos partnered with Walgreens. In the fall of 2013, it launched its testing services in Walgreens stores, then raised new money from investors." |
| episode | 10 | scene.events | 2003 / 2010 / Fall 2013 | OK | Dkt. 1802 pp.9, 11 | |
| episode | 11 | say/show/scene | End of 2014, shares valued at >$4B, per prosecutors | OK | Dkt. 1643 p.12 | |
| episode | 12 | say/show/scene | Covers of Fortune, Forbes (Inc.); Time 100 | OK | Dkt. 1643 p.12 | |
| episode | 13 | say | Chapter title | OK | — | |
| episode | 14 | say/scene | Pitch: one device / any test / fingerstick / pharma validated / military / healthy business | OK | Dkt. 1643 p.7 | |
| episode | 14 | scene.items[3] | "A healthy, profitable business" | NOTE | Dkt. 1643 p.7: "a profitable company and had a healthy ongoing relationship with … Walgreens" | Here "healthy" describes the Walgreens relationship. Optional wording: "A profitable business". |
| episode | 15 | say/show/scene | Device never completed more than 12 test types; used modified and unmodified third-party machines | OK | Dkt. 1643 p.8 (verbatim title); Dkt. 1802 p.10 | |
| episode | 16 | say/show/scene | $0 revenue in 2012–13; projections of $140M (2014) and nearly $1B (2015) | OK | Dkt. 1643 pp.8–9; Dkt. 1802 p.13 (controller testimony of no revenue) | |
| episode | 17 | say/show/scene | Nov 2013: Balwani told Holmes $15M cash, up to $2M/week; 2015 total income under $2M ($1,944,948) | OK | Dkt. 1802 p.13 | |
| episode | 18 | say/scene | Medevac/battlefield claims; "never used Theranos' device to clinically treat patients" | OK (verbatim) | Dkt. 1643 p.9 | |
| episode | 19 | say/scene.q | VIP demos; "In reality, the device was running a "null protocol" while some of the VIP samples were surreptitiously run on third-party devices." | OK (verbatim) | Dkt. 1802 pp.12–13 | |
| episode | 20 | say/show/scene | April 2010 email to Walgreens execs; Pfizer, GSK, Schering-Plough logos | OK | Dkt. 1643 p.8 | |
| episode | 21 | say/scene | Holmes admitted personally affixing logos; company witnesses neither validated nor authorized logos | OK | Dkt. 1802 p.15 | |
| episode | 22 | say | Chapter title | OK | — | |
| episode | 23 | say/show/scene | Scientists warned in 2013 (Aug–Sept); some resigned before Walgreens launch, per prosecutors | OK | Dkt. 1643 p.9 | |
| episode | 24 | say/scene.q | "she has a promise to deliver to the customer, she doesn't have much of a choice but to go ahead with the launch." Labeled trial testimony, as quoted in gov't memo | OK (verbatim; apostrophe style only) | Dkt. 1643 p.6 (Tr. 1216) | |
| episode | 25 | say/show/scene | Sept 22, 2015 texts: "Our validation reports are terrible." / "Praying" | OK (excerpt) | Dkt. 1643 p.12 | |
| episode | 26 | say/show/scene | Late 2015 news reporting revealed internal struggles in the lab | OK | Dkt. 1802 p.8 | |
| episode | 27 | say/scene | Learned of WSJ reporter; hired Boies to get him to drop story; appealed to owner who was a significant investor | OK | Dkt. 1643 p.18 | NOTE: these events (April 2015 onward) happened before the late-2015 publication in line 26, and the memo says "they" (Holmes and Balwani) hired Boies. Optional wording: "Earlier that year, according to prosecutors, …" |
| episode | 28 | say/scene.q | Mad Money Oct 15, 2015: "every test that we offer in our laboratory can run on our proprietary devices."; prosecutors said false | OK (verbatim) | Dkt. 1643 p.14 [ECF p.19] | |
| episode | 29 | say/scene | CMS inspection; Theranos admitted "a global and long-term failure of the quality control program for this instrument" | OK | Dkt. 1643 pp.17–18; Dkt. 1802 p.12 | |
| episode | 30 | say/scene | Voided every patient test result run on Edison in clinical lab | OK | Dkt. 1643 p.18; Dkt. 1802 p.4 | |
| episode | 31 | say/show/scene | Mar 14, 2018 SEC charged Theranos, Holmes, Balwani; "massive fraud"; >$700M | OK | SEC 2018-41 (headline "…Charged With Massive Fraud"; "more than $700 million from investors") | |
| episode | 32 | say/show/scene | $500,000 penalty; 10-yr officer/director bar; 18.9M shares; voting control | OK | SEC 2018-41 | |
| episode | 33 | say/scene.q | Peikin quote; "enforcement co-director" | OK (verbatim; release has a comma after "executives") | SEC 2018-41 | |
| episode | 33 | scene.case | "U.S. v. HOLMES" on an SEC civil-enforcement quote | FIX | SEC 2018-41: this was an SEC action, not the criminal case | scene.case: "SEC v. HOLMES" |
| episode | 34 | say/show/scene | June 14, 2018 grand jury indictment, 3 months after SEC | OK | Dkt. 1 (filed 06/14/18); DOJ case page ("On June, 14, 2018, a grand jury returned an indictment") | |
| episode | 35 | say | Chapter title | OK | — | |
| episode | 36 | say/scene | TSI Jul 28, 2020: 2 conspiracies + 10 wire counts; tried separately | OK | Dkt. 469; Dkt. 1643 p.15; Dkt. 1802 p.16 | |
| episode | 37 | say/show/scene | Trial began Aug 31, 2021; four months; 32 witnesses; >900 exhibits | OK | Dkt. 1643 p.15 [ECF p.20] | |
| episode | 37 | scene.img (memo_trial.jpg) | Crop of Dkt. 1643 p.20 (y 0.03–0.40) shows "(Mosley, RDV, and PFM)", the surname of a private individual investor-victim, on screen | FIX | Dkt. 1643 ECF p.20 line 8; viewed img/memo_trial.jpg | Re-crop memo_trial to end above line 7 (about y 0.03–0.27, ending after "32 witnesses testified."), or blur "(Mosley, RDV, and PFM)". Adjust hl to [0.0, 0.55, 1.0, 0.35] or similar after re-cropping. |
| episode | 38 | say/scene.q | Blame quote ("At trial, she blamed her COO (and longtime boyfriend), … everyone, that is, but herself.") | OK (verbatim; narration shortens list but is attributed to prosecutors) | Dkt. 1643 p.6 | |
| episode | 39 | say/show/scene | Guilty of investor conspiracy + 3 wire counts; $38,336,632 (Feb 6, 2014), $99,999,984 and $5,999,997 (Oct 31, 2014) | OK | Dkt. 1235 p.2; Dkt. 469 p.10; Dkt. 1716 | |
| episode | 40 | say/scene | Not guilty on 4 (Ct 2 + 10–12); mistrial on 3 hung counts; later dismissed | OK | Dkt. 1716 (Cts 3–5 and 9 dismissed on motion of the U.S.); Dkt. 1236; DOJ Jan 4, 2022 release | |
| episode | 41 | say/scene.q | "Elizabeth Holmes chose fraud over business failure." — FBI SAC Craig Fair, DOJ Jan 4, 2022 release | OK (verbatim) | DOJ release Jan 4, 2022 | |
| episode | 42 | say/show/scene | Separate trial; Balwani guilty on all 12; kicker JULY 2022 | OK | Dkt. 1643 p.15; Dkt. 1802 p.16; CNBC Jul 7, 2022 (date not in cited src) | NOTE: the cited memo does not give the July 2022 date. Adding "CNBC, Jul 7, 2022" to src would be optional. |
| episode | 43 | say | Chapter title | OK | — | |
| episode | 44 | say/show/scene | Gov't 180 months (15 yrs); probation 108 months (9 yrs); defense ≤18 months, home confinement | OK | Dkt. 1643 pp.2, 15; Dkt. 1642 | |
| episode | 45 | say/show/scene | PSR loss $730,840,209; judge rejected; stock not "practically worthless", retained some value apart from the fraud | OK | Dkt. 1712 pp.5–6 | |
| episode | 46 | say/show/scene | Loss $120,146,247; range 135–168 | OK | Dkt. 1712; Dkt. 1802 p.16; Dkt. 1816 p.2 | |
| episode | 47 | say/scene.q | "Ms. Holmes apologized more generally for Theranos and its "failings," but did not acknowledge nor accept responsibility for her conduct …" | OK (verbatim) | Dkt. 1712 (acceptance section) | |
| episode | 48 | say/show/scene | 135 months = 11 yrs 3 mos; low end; 3 yrs supervised release | OK | Dkt. 1660; Dkt. 1716; Dkt. 1816 p.2 | |
| episode | 49 | say/show | "$452 million in restitution to twelve investor victims, including Walgreens and Safeway" | FIX | Dkt. 1760 p.18 lists 14 payees (12 investors plus Walgreens and Safeway); Dkt. 1802: "fourteen victims". Dkt. 1816's "total of 12" is a miscount. | say: "In May two thousand twenty-three, the judge ordered Holmes and Balwani to pay four hundred fifty-two million dollars in restitution to fourteen investor victims, including Walgreens and Safeway." show: "In May 2023, the judge ordered Holmes and Balwani to pay $452 million in restitution to 14 investor victims, including Walgreens and Safeway." |
| episode | 49 | scene.src | Cites Dkt. 1816 for the restitution count | FIX | as above | scene.src: "Order on restitution, Dkt. 1760, May 16, 2023 · U.S. Court of Appeals, 9th Cir., No. 22-10312 (amended Dec 22, 2025)" |
| episode | 49 | scene.title | $452,047,268; May 16, 2023 | OK | Dkt. 1760 p.1 | |
| episode | 50 | say/show/scene | Release pending appeal denied (Apr 10, 2023); reported May 30, 2023; Balwani 155 months = 12 yrs 11 mos | OK | Dkt. 1757; Dkt. 1762; Dkt. 1816 p.2; DOJ case page | |
| episode | 51 | say | Chapter title | OK | — | |
| episode | 52 | say/show/scene | Feb 2025 9th Cir. affirmed convictions, sentence, restitution; "nothing more than a mirage" | OK | Dkt. 1790/1802 (Filed Feb 24, 2025; amended Dec 22, 2025) | |
| episode | 53 | scene.q | "The grandiose achievements touted by Holmes and Balwani were half-truths and outright lies." | OK (verbatim) | Dkt. 1802 p.8 | |
| episode | 53 | say | "Their grandiose achievements were half-truths and outright lies." | FIX | Dkt. 1802 p.8. The court wrote about achievements Holmes and Balwani *touted*, not their achievements, and the on-screen quote should match. | say: "The vision Holmes and Balwani sold, the judges wrote, was nothing more than a mirage. The grandiose achievements they touted were half-truths and outright lies." |
| episode | 54 | say/show/scene | March 2026 guideline change; 135 → 123 months | OK | Dkt. 1816 pp.1, 3, 10 (Amendment 821, §4C1.1 "Zero-Point Offenders") | NOTE: "first-time offenders" simplifies "zero-point offenders" (no criminal-history points). Optional wording: "for offenders with no criminal history". |
| episode | 55 | say/scene.q | "To be clear, this sentence reduction does not diminish the enormity of Holmes's crimes …" | OK (verbatim) | Dkt. 1816 p.10 | |
| episode | 56 | say | Asked President Trump to commute; per Forbes, as of late Sept DOJ listed it as pending | OK | Forbes Sept 24, 2026; ABC Jan 21, 2026. No grant or denial found as of 2026-11-03. | |
| episode | 56 | scene.lines | "Still pending." presents a Sept 2026 status as current | FIX | Forbes Sept 24, 2026 | scene.lines: ["Commutation requested.", "Pending as of|Sept. 2026."] |
| episode | 57 | say/show/scene | Halfway house approved for Aug 2027; release scheduled Feb 2030; May 2023 report date | OK | Forbes (Austin Transitional Center, Aug 23, 2027; Feb 22, 2030); Dkt. 1762 | |
| episode | 58 | say/scene | "One tiny drop changes everything," the company promised | OK | Dkt. 1802 p.8 | |
| episode | 59 | say/scene | Jury, judge and three appellate judges decided on what investors were told | OK (editorial; consistent with investor-only convictions) | Dkt. 1716; Dkt. 1802 | |
| episode | 60 | say | Outro | OK | — | |

## short1.json

| file | line# | field | claim | verdict | source | fix text |
|---|---|---|---|---|---|---|
| short1 | — | title/hook | Guilty on investors, not guilty on patients | OK | Dkt. 1235; Dkt. 1716 | |
| short1 | 0 | say/show/scene | Jan 3, 2022 jury fills out verdict form | OK | Dkt. 1235 | |
| short1 | 1 | say/scene | Count 1 guilty | OK | Dkt. 1235 | |
| short1 | 2 | say/scene | Count 2 not guilty | OK | Dkt. 1235 | |
| short1 | 3 | say/scene | 3 more investor counts guilty; every patient count that reached the jury not guilty; 3 hung | OK | Dkt. 1235; Dkt. 1236; Dkt. 1716 (Ct 9 dismissed) | NOTE: verdict2.jpg shows patient initials (see episode line 3). |
| short1 | 4 | say/scene | Convictions concern what she told investors | OK | Dkt. 1716 | |
| short1 | 5 | say/show/scene | 11 yrs 3 mos, later cut to 123 months | OK | Dkt. 1660; Dkt. 1816 | |
| short1 | 6 | say | Outro | OK | — | |

## short2.json

| file | line# | field | claim | verdict | source | fix text |
|---|---|---|---|---|---|---|
| short2 | — | title/hook | Pfizer logo on her own (Theranos-written) report | OK | Dkt. 1643 p.8 ("reports written by Theranos"); Dkt. 1802 p.15 | |
| short2 | 0 | say/show/scene | April 2010, courting Walgreens | OK | Dkt. 1643 p.8; Dkt. 1802 p.11 | |
| short2 | 1 | say/scene | Emailed Walgreens execs reports with logos, per prosecutors | OK | Dkt. 1643 p.8 | |
| short2 | 2 | say/scene.q | "three independent due diligence reports on Theranos systems"; "from" those companies | OK (verbatim) | Dkt. 1643 p.8 | |
| short2 | 3 | say/scene | Admitted at trial she added logos | OK | Dkt. 1802 p.15 | |
| short2 | 4 | say/scene | Drug-company witnesses: never validated, never authorized logos | OK | Dkt. 1802 p.15 | |
| short2 | 5 | say/show/scene | Kept sending Pfizer report to investors in 2014–2015, per prosecutors; convicted on 4 investor counts | OK | Dkt. 1643 p.8; Dkt. 1716 | |
| short2 | 6 | say | Outro | OK | — | |

## short3.json

| file | line# | field | claim | verdict | source | fix text |
|---|---|---|---|---|---|---|
| short3 | — | title/hook | "$0 revenue … $1B projected" | NOTE | Dkt. 1643 p.9 ("nearly $1 billion") | Rounding is acceptable in a title; the body correctly says "nearly". |
| short3 | 0 | say/show/scene | Zero revenue 2012–13, per prosecutors | OK | Dkt. 1643 pp.8–9; Dkt. 1802 p.13 | |
| short3 | 1 | say/show/scene | $140M (2014), nearly $1B (2015) projections | OK | Dkt. 1643 p.9 | |
| short3 | 2 | say/show/scene | Nov 2013 $15M cash, up to $2M/week, per appeals court | OK | Dkt. 1802 p.13 (what Balwani told Holmes) | |
| short3 | 3 | say/show/scene | One investor told >$200M from military + pharma; never more than $10M from both | OK | Dkt. 1643 p.9 | NOTE: the first sentence carries no attribution in narration, but the kicker says "PER PROSECUTORS" and the next sentence attributes it. Dkt. 1802 p.13 separately supports the $200M DoD claim (investor testimony). |
| short3 | 4 | say/show/scene | $452M restitution to investors; May 16, 2023 | OK | Dkt. 1760 | |
| short3 | 5 | say | Outro | OK | — | |

## short4.json

| file | line# | field | claim | verdict | source | fix text |
|---|---|---|---|---|---|---|
| short4 | — | title/hook | Demo ran a "null protocol"; "tested nothing" | OK | Dkt. 469 p.6; Dkt. 1802 p.13 | |
| short4 | 0 | say/scene.q | Promised full range of tests from a drop; "[O]ne tiny drop changes everything." | OK | Dkt. 1802 p.8; Dkt. 1643 p.7 (any test a conventional lab ran) | |
| short4 | 1 | say/scene | VIP guests led to believe device ran their blood | OK | Dkt. 1802 p.13 | |
| short4 | 2 | say/scene.q | Null protocol quote | OK (verbatim) | Dkt. 1802 p.13 | |
| short4 | 3 | say/scene | Indictment said null protocol was to make analyzer appear to be operating | OK (framed as indictment) | Dkt. 469 p.6 ¶(C) | |
| short4 | 4 | say/show/scene | Device could never run more than 12 test types, per prosecutors | OK | Dkt. 1643 p.8; Dkt. 1802 p.10 | |
| short4 | 5 | say/scene | Convicted of defrauding investors | OK | Dkt. 1716 | |
| short4 | 6 | say | Outro | OK | — | |

## short5.json

| file | line# | field | claim | verdict | source | fix text |
|---|---|---|---|---|---|---|
| short5 | — | title/hook | Prosecutors wanted 15 years | OK | Dkt. 1643 p.2 (180 months) | |
| short5 | 0 | say/show/scene | Nov 18, 2022 sentenced for defrauding investors | OK | Dkt. 1660 | |
| short5 | 1 | say/show/scene | 180 / 108 / ≤18 months | OK | Dkt. 1643; Dkt. 1642 | |
| short5 | 2 | say/show/scene | Loss $120.1M; range 135–168 | OK | Dkt. 1712 | |
| short5 | 3 | say/show/scene | Bottom of range, 135 months = 11 yrs 3 mos | OK | Dkt. 1712; Dkt. 1816 | |
| short5 | 4 | say/show/scene | March 2026 guideline change, cut to 123 months | OK | Dkt. 1816 | NOTE: "first-time offenders" means zero-point offenders (see episode line 54). |
| short5 | 5 | say | Outro | OK | — | |

## short6.json

| file | line# | field | claim | verdict | source | fix text |
|---|---|---|---|---|---|---|
| short6 | — | title/hook | Where Holmes is now (2026) | OK | Forbes Sept 24, 2026 | |
| short6 | 0 | say/show/scene | Reported May 30, 2023 | OK | Dkt. 1762; Dkt. 1816 p.2 | |
| short6 | 1 | say/show/scene | Feb 2025 9th Cir. affirmed; "nothing more than a mirage" | OK | Dkt. 1790/1802 | |
| short6 | 2 | say/show/scene | Mar 2026 cut 135 → 123 | OK | Dkt. 1816 | |
| short6 | 3 | say | Asked Trump to commute; per Forbes, pending as of late Sept | OK | Forbes; ABC | |
| short6 | 3 | scene.lines | "Still pending." presents a Sept 2026 status as current | FIX | Forbes Sept 24, 2026 | scene.lines: ["Commutation requested.", "Pending as of|Sept. 2026."] |
| short6 | 4 | say/show/scene | Halfway house Aug 2027; release Feb 2030 | OK | Forbes | |
| short6 | 5 | say | Outro | OK | — | |

## meta.json / thumb.json

| file | line# | field | claim | verdict | source | fix text |
|---|---|---|---|---|---|---|
| meta | — | title | Guilty on investors, not guilty on patients | OK | Dkt. 1235; Dkt. 1716 | |
| meta | — | summary | Jan 3, 2022 San Jose verdict; Davila 135 months; cut in 2026 | OK | Dkt. 1235; Dkt. 1660; Dkt. 1816 | NOTE: "what was really happening inside Theranos" is largely drawn from the government's sentencing memo. The episode attributes it correctly, so this is acceptable. |
| meta | — | sources | Docket links and dates | OK | as opened | |
| thumb | A | words/hook | "SPLIT VERDICT · GUILTY · NOT GUILTY" | OK | Dkt. 1235 | |
| thumb | C | words/stamp | "135 MONTHS" with GUILTY stamp | NOTE | Dkt. 1816 | This was the original sentence; the current sentence is 123 months. Optional wording: "135→123 MONTHS". |

## Summary

**FIX items: 8**
1. episode line 10 (say/show): "began raising money" is wrong. Use "…then raised new money from investors."
2. episode line 33 (scene.case): "U.S. v. HOLMES" on the SEC quote. Change to "SEC v. HOLMES".
3. episode line 37 (scene.img memo_trial.jpg): the private investor surname "Mosley" is visible. Re-crop or blur.
4. episode line 49 (say/show): "twelve investor victims" should be "fourteen investor victims".
5. episode line 49 (scene.src): remove Dkt. 1816 (it contains the miscount). Cite Dkt. 1760 and the 9th Cir.
6. episode line 53 (say): "Their grandiose achievements" should be "The grandiose achievements they touted".
7. episode line 56 (scene.lines): "Still pending." should be "Pending as of|Sept. 2026."
8. short6 line 3 (scene.lines): "Still pending." should be "Pending as of|Sept. 2026."

No narration or on-screen text says or implies that she was convicted of harming patients. Patient-harm material is limited to prosecutors' quoted statements (line 24) and Theranos's own CMS admission and voiding of results (lines 29–30). No private victim is named in narration or scene text. The only on-screen exposure found is the image issue in FIX 3, plus patient initials in verdict2.jpg (NOTE).

## Fixes applied (2026-11-03, by the script author, before the final build)
All 8 FIX items applied verbatim: episode line 10 say/show ("then raised new money from investors"); line 33 case → "SEC v. HOLMES"; line 37 memo_trial re-cropped to page 20 y 0.03–0.27 (investor-victim names no longer on screen), hl adjusted; line 49 say/show → "fourteen victims"/"14 victims" (verified: Dkt. 1760 p.18 lists 14 payees; 9th Cir. "fourteen victims"); line 49 src → Dkt. 1760 + 9th Cir.; line 53 say → "The grandiose achievements they touted were half-truths and outright lies."; line 56 and short6 line 3 → "Pending as of Sept. 2026."
Optional notes also applied: verdict2.jpg re-cropped above Count 10 (patient initials removed; hl adjusted in episode line 3 and short1 line 3); line 4 → "This is the case prosecutors made"; line 14 → "A profitable business"/"the business was profitable"; thumb C now "THE MIRAGE" with "135 → 123 MONTHS".
