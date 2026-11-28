#!/usr/bin/env python3
"""Episode 025 — "The Jury Duty Scam From Prison" (DOJ anti-scam surge, Nov 24, 2026 + D.N.J. seizure-warrant affidavit 26-mj-8230).
usage: make_spec.py <workdir>  > episode.json     (needs <workdir>/footage/*.mp4)
A line is (say, kind, payload[, show]): kind "G" = graphic scene dict, "C" = list of clip names (cut into <= ~8 s shots)."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W = sys.argv[1]
HL = json.load(open(os.path.join(HERE, "hl.json")))
SRC_PR = "U.S. Department of Justice, Office of Public Affairs, press release (Nov 24, 2026)"
SRC_SG = "Justice Department Criminal Division, 2026 anti-scam surge actions page (justice.gov/criminal)"
SRC_AF = "Affidavit in Support of an Application for a Seizure Warrant, D.N.J. Mag. No. 26-8230 (JSA), Doc. 1, filed Nov 5, 2026"
def doc(key, kicker, title, src=SRC_AF, pan=None):
    img, a, b = HL[key]
    if pan is None:
        c = a + (b - a) / 2; pan = [max(0.0, round(c - 0.22, 3)), max(0.0, round(c - 0.16, 3))]
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan, hl=[0.0, a, 1.0, round(b - a, 4)], kicker=kicker, title=title, src=src)
def fig(img, kicker, title, pan=(0.0, 0.2), src=SRC_AF):
    return dict(type="doc", img=f"img/{img}.jpg", pan=list(pan), kicker=kicker, title=title, src=src)
AK = "FEDERAL AFFIDAVIT · ALLEGATIONS · "
LB = {  # clip label per clip-name prefix
 "doj_": "Source: U.S. Department of Justice · press conference · Nov 24, 2026",
 "live_": "Source: LiveNOW from FOX · DOJ press conference · Nov 24, 2026",
 "econ_": "Source: The Economic Times · report on the DOJ announcement · Nov 2026",
 "fox4_": "Source: FOX 4 Dallas-Fort Worth · Georgia inmates charged in N.D. Texas · Nov 2026",
 "natdesk_": "Source: The National Desk · report on the DOJ announcement · Nov 2026",
 "cbs19": "Source: CBS19 · DOJ and the Georgia jury duty scheme · Nov 2026",
 "krcr": "Source: KRCR News Channel 7 · Georgia inmates accused of jury duty scam · Nov 2026",
 "fox10": "Source: FOX 10 Phoenix · DOJ anti-scam crackdown · Nov 2026",
 "cbs6_": "Source: CBS6 Albany · DOJ anti-scam crackdown · Nov 2026",
 "wis10": "Source: WIS News 10 · Georgia inmates arrested in a call-scam case · May 2026",
 "abc_dr": "Source: ABC News · contraband drones and prisons (file footage) · Dec 2025",
 "cnn_dr": "Source: CNN · the hunt for drones inside prisons (file footage) · May 2026",
 "fox5_dr": "Source: FOX 5 Atlanta · drone carrying contraband to a prison (file footage) · Jul 2026",
 "alive_dr": "Source: 11Alive · drone smuggling indictment, Georgia prisons (separate case) · Jun 2026",
 "tele_dr": "Source: The Telegraph · drone smuggling indictment (separate case) · Jun 2026",
 "wfaa_dr": "Source: WFAA · prison drone drops (file footage) · Dec 2025",
 "khou_dr": "Source: KHOU 11 · drone smuggling arrests, Texas prison (file footage) · Apr 2026",
 "wach_jam": "Source: WACH FOX · push to jam contraband phones in state prisons · Nov 2026",
 "thv_jam": "Source: THV11 · FCC approves contraband phone jamming · Nov 2026",
 "kens_jam": "Source: KENS 5 · FCC approves cell phone jamming in state prisons · Nov 2026",
 "n12_jam": "Source: 12 News · FCC approves cell phone signal jamming in prisons · Nov 2026",
 "abc7_atm": "Source: Eyewitness News ABC7NY · FBI warning on bitcoin ATM scams (file footage) · Dec 2025",
 "wtov": "Source: WTOV News 9 · sheriff warns of jury duty scam (file footage) · Apr 2026",
 "wbay": "Source: WBAY · sheriff's office warns of jury duty scam (file footage) · Aug 2026",
}
def label(n):
    for k, v in LB.items():
        if n.startswith(k): return v
    raise SystemExit("no label for " + n)
PLAN = {}
for _f in ("clips1.json", "clips2.json"):
    for _c in json.load(open(os.path.join(HERE, _f))):
        _t = lambda s: int(s.split(":")[0]) * 60 + int(s.split(":")[1])
        PLAN[_c["name"]] = _t(_c["end"]) - _t(_c["start"])
def clen(n):
    if not os.path.exists(f"{W}/footage/{n}.mp4"): return float(PLAN[n])   # planning estimate until the relay delivers
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{W}/footage/{n}.mp4"], capture_output=True, text=True)
    return float(r.stdout.strip() or 0)
CL = {}; ptr = {}
def take(n, d):
    if n not in CL: CL[n] = clen(n); ptr[n] = 0.0
    a = ptr[n]
    if a + d > CL[n] - 0.2: a = 0.0
    ptr[n] = a + d + 0.5
    return round(a, 2)
def clipscene(n, d): return {"type": "clip", "file": f"footage/{n}.mp4", "from": take(n, d + 0.6), "label": label(n)}

def L(say, kind, payload, show=None): return (say, kind, payload, show)
C = lambda say, *names, show=None: L(say, "C", list(names), show)
G = lambda say, scene, show=None: L(say, "G", scene, show)
D = lambda *n: list(n)
doj = [f"doj_p{i:02d}" for i in range(20)]
lines = [
 # COLD OPEN
 C("On November twenty-fourth, the Justice Department stood at a podium and announced what it called the largest crackdown on scammers in its history.", "doj_p00", "doj_p01", show="On November 24, the Justice Department stood at a podium and announced what it called the largest crackdown on scammers in its history."),
 C("More than eight hundred defendants. More than four hundred cases. And one scheme the department highlighted, in which prosecutors say the calls came from inside prisons.", "fox4_a", show="More than 800 defendants. More than 400 cases. And one scheme the department highlighted, in which prosecutors say the calls came from inside prisons."),
 C("Prosecutors say the calls came from inside Georgia state prisons.", "natdesk_a"),
 G("Someone phones you. The caller I.D. says it's your local sheriff. The voice says you missed jury duty, there's a warrant, and you'll be arrested unless you pay a bond today.", doc("call", AK + "THE PHONE CALL", "How the scheme starts"), show="Someone phones you. The caller ID says it's your local sheriff. The voice says you missed jury duty, there's a warrant, and you'll be arrested unless you pay a bond today."),
 C("You are told to stay on the line. You are told not to tell anyone. And you are told to pay in cash, at a crypto machine.", "abc7_atm_a", "wtov"),
 G("Federal prosecutors say the people behind the calls in these cases were Georgia prison inmates. This is how the scheme worked, according to the government, and what the government is doing about it.", dict(type="title", kicker="SWORN · CASE 025 · NEW", title="Jury Duty Scam Calls|From Georgia Prisons", sub="Prosecutors allege · DOJ anti-scam surge announced Nov 24, 2026 · defendants are presumed innocent")),
 # I
 G("Chapter one. The announcement.", dict(type="chapter", n="I", title="The Announcement")),
 C("The announcement came from Attorney General Todd Blanche, FBI Director Kash Patel, and Criminal Division leaders. The Justice Department said that since March sixth, prosecutors have taken action in more than four hundred cases, against more than eight hundred defendants.", "doj_p02", "doj_p03", show="The announcement came from Attorney General Todd Blanche, FBI Director Kash Patel, and Criminal Division leaders. The Justice Department said that since March 6, prosecutors have taken action in more than 400 cases, against more than 800 defendants."),
 G("Those actions include new charges, extraditions, guilty verdicts and sentences, in eighty-five federal districts. Thirty defendants were extradited to face scam charges in U.S. courts.", dict(type="stat", kicker="DOJ ANTI-SCAM SURGE · MAR 6 – NOV 24, 2026", value="800+", label="defendants · 400+ cases · 85 federal districts", src=SRC_PR), show="Those actions include new charges, extraditions, guilty verdicts and sentences, in 85 federal districts. Thirty defendants were extradited to face scam charges in U.S. courts."),
 G("The attorney general put it this way.", dict(type="quote", q="Predatory scams against the American people will not be tolerated.", case="Attorney General Todd Blanche", doc="Justice Department announcement of the anti-scam surge", cite="DOJ press release, Nov. 24, 2026")),
 C("The department says the surge followed an executive order signed by President Trump on March sixth, directing a government-wide crackdown on predatory schemes.", "doj_p04", "live_a", show="The department says the surge followed an executive order signed by President Trump on March 6, directing a government-wide crackdown on predatory schemes."),
 C("The FBI says its operation against scam compounds, called Operation Blackout, has restrained nearly seventeen billion dollars in illicit funds, and helped dismantle more than twenty-nine compounds across Asia, Africa and the Middle East.", "doj_p05", "live_b", show="The FBI says its operation against scam compounds, called Operation Blackout, has restrained nearly $17 billion in illicit funds, and helped dismantle more than 29 compounds across Asia, Africa and the Middle East."),
 C("It says foreign partners arrested or detained more than three hundred twenty people overseas, and that the FBI helped free and repatriate more than two thousand two hundred trafficked workers who were forced to work inside scam compounds.", "econ_a", "doj_p06", show="It says foreign partners arrested or detained more than 320 people overseas, and that the FBI helped free and repatriate more than 2,200 trafficked workers who were forced to work inside scam compounds."),
 G("The department also cites Gallup. Ten percent of U.S. adults experienced a scam last year, directly or through someone in their household, and Americans lost an estimated sixty-eight billion dollars to scams in twenty twenty-five.", dict(type="stat", kicker="AS CITED BY THE JUSTICE DEPARTMENT · GALLUP", value="$68B", label="estimated lost to scams by Americans in 2025", src=SRC_PR), show="The department also cites Gallup. 10 percent of U.S. adults experienced a scam last year, directly or through someone in their household, and Americans lost an estimated $68 billion to scams in 2025."),
 C("Behind those numbers are many kinds of schemes. Crypto investment fraud run from Southeast Asia. Inheritance scams. A call center in Peru. But in its release, the department described one scheme first. It is the one this video is about.", "live_c", "cbs6_a", "fox10"),
 # II
 G("Chapter two. The call.", dict(type="chapter", n="II", title="The Call")),
 G("A federal affidavit, filed in New Jersey in early November, describes how it starts. A victim gets a call. Caller I.D. shows a local sheriff's department, the U.S. Marshals Service, or another law enforcement agency.", doc("call", AK + "¶ 16", "The call"), show="A federal affidavit, filed in New Jersey in early November, describes how it starts. A victim gets a call. Caller ID shows a local sheriff's department, the U.S. Marshals Service, or another law enforcement agency."),
 G("The caller gives a name and a badge number, and says the victim failed to appear for jury duty. The affidavit says callers often claim a warrant has been issued, and that scammers often follow scripts. It reproduces a portion of one, handwritten, and says the Georgia Department of Corrections obtained it in a search of an inmate's cell.", fig("aff_p08", AK + "FIGURE 1", "A script used by an inmate", (0.0, 0.1))),
 G("Victims are then emailed or texted counterfeit arrest warrants and other official-looking documents, the affidavit says. It calls them bogus, and says they are sent to make the threats seem real.", fig("aff_p10", AK + "FIGURE 3", "A counterfeit arrest warrant", (0.0, 0.1))),
 C("Then the pressure. Victims are told to stay on the phone. They are told there is a gag order, and that they cannot tell family, friends or bank tellers. The affidavit says some victims reported calls that lasted more than a day.", "natdesk_b", "cbs19", "krcr"),
 G("How common is it? The affidavit cites the Federal Trade Commission. More than thirty thousand complaints about jury duty impostors from January twenty twenty-one through October twenty twenty-six, with reported losses above forty million dollars. In the first ten months of this year, about eleven thousand victims reported losing around thirteen million.", doc("ftc", AK + "¶ 15", "Jury duty impostor complaints"), show="How common is it? The affidavit cites the Federal Trade Commission. More than 30,000 complaints about jury duty impostors from January 2021 through October 2026, with reported losses above $40 million. In the first ten months of this year, about 11,000 victims reported losing around $13 million."),
 C("The inspector who wrote the affidavit says victims often blame themselves, and are too embarrassed or ashamed to report. The inspector says that results in widespread underreporting.", "natdesk_c", "krcr"),
 # III
 G("Chapter three. The payment.", dict(type="chapter", n="III", title="The Payment")),
 G("Scammers then offer a way out. A bond, which they falsely promise will be refunded. Victims, the affidavit says, typically pay thousands of dollars, and some pay hundreds of thousands.", doc("pay", AK + "¶ 19", "The payment")),
 C("The affidavit says scammers frequently direct victims to pay at a cryptocurrency ATM. First the victim withdraws cash at a bank. The affidavit says victims are coached either to say nothing to the teller about why, or to lie about the reason.", "abc7_atm_a", "wtov"),
 C("The affidavit says the victim then deposits the cash into a crypto kiosk and scans a QR code that the scammer sends, and the money becomes cryptocurrency, delivered to an address the scammer controls.", "abc7_atm_b", "wbay"),
 G("The affidavit includes a tracing graph. One victim's deposit hops across numerous crypto addresses in quick succession before reaching its destination. The postal inspector says that rapid movement is evidence of money laundering.", fig("aff_p21", AK + "FIGURE 10", "Tracing one victim's deposit", (0.0, 0.2))),
 G("Here are three of the victim reports in the affidavit.", dict(type="list", kicker="VICTIM REPORTS · AFFIDAVIT ¶¶ 49, 50, 53 · UNNAMED", items=[["MD", "Told to pay a $12,350 bail payment. Became suspicious."], ["TX", "Elderly woman. Paid $10,000 at a crypto ATM. On the phone over 6 hours."], ["NV", "Deposited over $12,000. Grew suspicious when no receipt came."]], src=SRC_AF)),
 C("The affidavit says an elderly woman in Texas was told there was a federal warrant, and a gag order. She withdrew the cash. When the teller asked why, the caller, still on the line, told her to say it was for repairs. She was on the phone for more than six hours.", "cbs6_b", "abc7_atm_b", show="The affidavit says an elderly woman in Texas was told there was a federal warrant, and a gag order. She withdrew the cash. When the teller asked why, the caller, still on the line, told her to say it was for repairs. She was on the phone for more than 6 hours."),
 C("A man in Nevada was told to drive to a police department and stay on the line. He ended up at a crypto ATM, and deposited more than twelve thousand dollars. When no receipt came, and the scammers asked for more, he grew suspicious. He drove to the real sheriff's office. The caller hung up.", "wtov", "wbay", "cbs19", show="A man in Nevada was told to drive to a police department and stay on the line. He ended up at a crypto ATM, and deposited more than $12,000. When no receipt came, and the scammers asked for more, he grew suspicious. He drove to the real sheriff's office. The caller hung up."),
 # IV
 G("Chapter four. The fake courts.", dict(type="chapter", n="IV", title="The Fake Courts")),
 G("The affidavit asks a judge to seize three websites. Ejuror courts dot org. Judicial services dot org. And civil services division dot org. It says victims reported being sent there to verify their information, and some typed in Social Security numbers and birth dates.", doc("table", AK + "¶¶ 35-37, 49", "The three target websites"), show="The affidavit asks a judge to seize three websites. ejurorcourts.org. judicialservices.org. And civilservicesdivision.org. It says victims reported being sent there to verify their information, and some typed in Social Security numbers and birth dates."),
 G("The affidavit says the sites imitate the real U.S. Courts website, down to the fonts, the layout and the logo. On November second, a representative of the Administrative Office of the U.S. Courts confirmed to an investigator that they are not official court sites.", fig("aff_p45", AK + "FIGURES 22–25", "Real site and imitations", (0.0, 0.1))),
 G("One detail. Official government sites carry a banner. It reads, quote, A dot gov website belongs to an official government organization in the United States. On the three sites, the postal inspector says, the banner reads, A dot gov or dot org website belongs to an official government organization in the United States. Only dot gov is official.", doc("banner", AK + "¶ 46", "The altered banner"), show="One detail. Official government sites carry a banner. It reads, “A .gov website belongs to an official government organization in the United States.” On the three sites, the postal inspector says, the banner reads, “A .gov or .org website belongs to an official government organization in the United States.” Only .gov is official."),
 G("And a chat window opens in the corner. The affidavit quotes the greeting.", dict(type="quote", q="Hi I'm the duty officer today. How can I assist you?", case="Chat window on all three sites", doc="Affidavit ¶ 48", cite="D.N.J. Mag. No. 26-8230, Doc. 1", size="lg")),
 C("The affidavit also points to a fourth site, walkthaduck dot com. It says the three court-imitation sites load, or try to load, content from it and share its I.P. address, and that the inspector believes whoever controls it is associated with them. It says one victim paid by card through a page on that site, to an account she labeled walkthaduck.", "doj_p07", "doj_p08", "live_d", show="The affidavit also points to a fourth site, walkthaduck.com. It says the three court-imitation sites load, or try to load, content from it and share its IP address, and that the inspector believes whoever controls it is associated with them. It says one victim paid by card through a page on that site, to an account she labeled walkthaduck."),
 G("The site's own pages, quoted in the affidavit, call it an awareness campaign, art, social commentary and cybersecurity education. Its terms of service say, quote, We are not the government. We are not the cops. They also say, We do not operate as scammers. The inspector writes that the operators appear to be integral to jury duty fraud, which the site's operators deny.", dict(type="quote", q="We are not the government. We are not the cops.", case="walkthaduck.com terms of service", doc="As quoted in the affidavit, ¶ 39", cite="D.N.J. Mag. No. 26-8230, Doc. 1")),
 C("The affidavit says webpages associated with walkthaduck dot com, including one called civiljuryservices dot org, have been the subject of more than one hundred victim complaints. Understand what this document is. It is a request to seize three web hosting accounts. It is not an indictment, and it charges no one.", "doj_p09", "doj_p10", show="The affidavit says webpages associated with walkthaduck.com, including one called civiljuryservices.org, have been the subject of more than 100 victim complaints. Understand what this document is. It is a request to seize three web hosting accounts. It is not an indictment, and it charges no one."),
 # V
 G("Chapter five. Behind the walls.", dict(type="chapter", n="V", title="Behind the Walls")),
 G("Who is on the other end of the line? The affidavit's author writes that, based on evidence from financial institutions, announced charges and experience, the author believes the vast majority of jury duty fraud perpetrators are inmates in the Georgia state prison system. That is a belief, not a court finding.", doc("scammers", AK + "¶ 27", "Who makes the calls")),
 G("The affidavit cites records from Bitcoin Depot, a crypto ATM company. Between September twenty twenty-two and May twenty twenty-six, victims reported losing more than nineteen million dollars to jury duty fraud there. More than forty percent of those complainants paid money mules located in Georgia.", doc("btc", AK + "¶ 29", "Where the money went"), show="The affidavit cites records from Bitcoin Depot, a crypto ATM company. Between September 2022 and May 2026, victims reported losing more than $19 million to jury duty fraud there. More than 40 percent of those complainants paid money mules located in Georgia."),
 C("How does an inmate get a phone? The affidavit says Georgia inmates bribe prison employees, and use drones, to smuggle in cell phones, cash and drugs.", "abc_dr_a", "cnn_dr", "abc_dr_b"),
 C("From twenty eighteen to twenty twenty-three, the affidavit says, at least three hundred sixty Georgia corrections employees were arrested for smuggling contraband into state prisons.", "wfaa_dr", "fox5_dr", show="From 2018 to 2023, the affidavit says, at least 360 Georgia corrections employees were arrested for smuggling contraband into state prisons."),
 C("Drone smuggling has led to federal charges. The affidavit cites one case, United States versus Hall, in which sixteen defendants were charged with using drones to fly drugs and phones into Georgia prisons. Those are allegations. The footage here is from separate drone cases.", "alive_dr", "tele_dr", "khou_dr", show="Drone smuggling has led to federal charges. The affidavit cites one case, United States v. Hall, in which 16 defendants were charged with using drones to fly drugs and phones into Georgia prisons. Those are allegations. The footage here is from separate drone cases."),
 C("With a phone, the affidavit says, a scammer can find victims with people-search apps, borrow a local sheriff's number with a spoofing app, and open the email, crypto and ATM accounts to collect the money.", "cnn_dr_b", "fox5_dr", "abc_dr_a"),
 C("Then, the affidavit says, they send money to relatives and friends, buy expensive jewelry or drugs, or have a drone or a prison guard smuggle cash back inside. It says scammers are frequently members of national gangs, and that flaunting the money brings status.", "doj_p11", "doj_p12", "doj_p13"),
 # VI
 G("Chapter six. The government closes in.", dict(type="chapter", n="VI", title="The Government Closes In")),
 G("The department's list also includes an October sentencing. On October sixteenth, two Georgia inmates who, the department says, extorted at least one hundred nineteen people over supposed missed jury duty fines were sentenced. One got two hundred months in prison. The other, one hundred twenty.", dict(type="stat", kicker="SENTENCED OCT 16, 2026 · PER THE DOJ CRIMINAL DIVISION", value="200 + 120", label="months in prison · two Georgia inmates · 119+ victims", src=SRC_SG), show="The department's list also includes an October sentencing. On October 16, two Georgia inmates who, the department says, extorted at least 119 people over supposed missed jury duty fines were sentenced. One got 200 months in prison. The other, 120."),
 C("On November third, a superseding indictment in Southern Illinois charged six Georgia inmates and two co-conspirators with conspiracy to commit wire fraud and money laundering. On November tenth, a grand jury in the Northern District of Texas charged two current inmates and one former inmate. Those are allegations. The defendants are presumed innocent.", "fox4_a", "fox4_b", "natdesk_b", show="On November 3, a superseding indictment in Southern Illinois charged six Georgia inmates and two co-conspirators with conspiracy to commit wire fraud and money laundering. On November 10, a grand jury in the Northern District of Texas charged two current inmates and one former inmate. Those are allegations. The defendants are presumed innocent."),
 C("On November ninth, Georgia state prosecutors indicted seventeen defendants for smuggling contraband phones into state prisons. The charges include racketeering.", "cbs19", "krcr", show="On November 9, Georgia state prosecutors indicted 17 defendants for smuggling contraband phones into state prisons. The charges include racketeering."),
 C("On November thirteenth, the Postal Inspection Service mailed warning letters to more than thirteen hundred people it says served as money mules for Georgia inmates. The letters warn that they could face criminal charges if they keep moving the money.", "doj_p14", "doj_p15", show="On November 13, the Postal Inspection Service mailed warning letters to more than 1,300 people it says served as money mules for Georgia inmates. The letters warn that they could face criminal charges if they keep moving the money."),
 C("The Postal Inspection Service also seized the three web addresses. The department says traffic to all three now goes to a government seizure banner.", "doj_p16", "doj_p17"),
 C("And on November nineteenth, the Federal Communications Commission approved a new rule that lets state prisons jam contraband cell phone signals.", "wach_jam_a", "thv_jam", "kens_jam", "n12_jam", show="And on November 19, the Federal Communications Commission approved a new rule that lets state prisons jam contraband cell phone signals."),
 C("The department's release lists the rule among the actions against the Georgia scheme.", "wach_jam_b", "n12_jam"),
 # VII
 G("Chapter seven. Beyond Georgia.", dict(type="chapter", n="VII", title="Beyond Georgia")),
 C("Jury duty was one front. The department's list of recent cases includes Southeast Asian scam centers running crypto investment fraud, Nigerian nationals accused of inheritance scams, a list broker in Mexico accused of selling elderly Americans' contact details to scammers, and a dozen defendants charged with a sweepstakes scheme targeting the elderly.", "live_a", "live_b", "econ_b", "doj_p18"),
 C("The Secret Service says a conspiracy run from scam centers in Cambodia targeted at least one hundred seventy-four U.S. victims. A Chinese national was extradited from the Netherlands in October, and arraigned in the Central District of California for his alleged role.", "econ_c", "doj_p19", show="The Secret Service says a conspiracy run from scam centers in Cambodia targeted at least 174 U.S. victims. A Chinese national was extradited from the Netherlands in October, and arraigned in the Central District of California for his alleged role."),
 C("The State Department says it helped freeze more than one billion dollars in stolen cryptocurrency in Southeast Asia, and take down more than one point four million fraudulent websites and accounts.", "live_c", "live_d", show="The State Department says it helped freeze more than $1 billion in stolen cryptocurrency in Southeast Asia, and take down more than 1.4 million fraudulent websites and accounts."),
 C("These figures come from the agencies themselves, in a press release announcing their own results. We have not independently verified them. Gallup's estimate, sixty-eight billion dollars in losses, shows the size of the problem. Whether eight hundred defendants changes it, is the open question.", "doj_p03", "doj_p06", "doj_p10", show="These figures come from the agencies themselves, in a press release announcing their own results. We have not independently verified them. Gallup's estimate, $68 billion in losses, shows the size of the problem. Whether 800 defendants changes it, is the open question."),
 C("If the call comes, the affidavit has one more detail. It says scammers send bogus documents to convince victims that paying at a crypto ATM is a legitimate form of payment accepted by the U.S. government.", "abc7_atm_a", "wtov", "cbs19"),
 G("Have you ever gotten a call like this? And should state prisons be allowed to jam phone signals? Tell us in the comments.", dict(type="end")),
]
out = []
for say, kind, payload, show in lines:
    item = {"say": say}
    if show: item["show"] = show
    if kind == "G":
        item["scene"] = payload
    else:
        d = len(say.split()) / 2.55; n = max(1, min(len(payload), -(-int(d * 10) // 85)))
        names = payload[:n] if len(payload) >= n else payload
        n = len(names); seg = d / n
        item["scene"] = clipscene(names[0], seg)
        if n > 1:
            item["cuts"] = [{"at": round(q / n, 3), "scene": clipscene(names[q], seg)} for q in range(1, n)]
    out.append(item)
json.dump({"label": "SWORN 025 · THE JURY DUTY SCAM FROM PRISON", "lines": out}, sys.stdout, indent=1, ensure_ascii=False)
words = sum(len(l[0].split()) for l in lines); sys.stderr.write(f"lines {len(lines)} words {words} est {words/155:.1f} min\n")
