import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def doc(key, kicker, src, pan=None):
    img, a, b = HL[key]
    c = (a + b) / 2
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [max(0.0, round(c - 0.2, 3)), max(0.0, round(c - 0.14, 3))],
                hl=[0.0, a, 1.0, round(b - a, 4)], kicker=kicker, src=src)
def photo(img, caption, src):
    return dict(type="photo", img=f"img/{img}.jpg", caption=caption, src=src, fit="cover")
SRC_I = "Indictment, U.S. v. Owens, Lumumba & Banks (S.D. Miss. 3:24-cr-103)"
SRC_IPH = "Image printed in the indictment — FBI recording"
SRC_WLBT = "WLBT (Nov 20, 2026), sentencing hearing"
SRC_MT = "Mississippi Today (Nov 5, 2026)"
IND = "INDICTMENT"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def hook(img, **kw):
    d = dict(type="hook", img=f"img/{img}.jpg", pos="50% 0%", zoom=1.3334); d.update(kw); return d
SENT_L = dict(type="verdict", kicker="NOV 20, 2026 · JACKSON, MISS.", stamp="SENTENCED", big="37 Months", sub="Ex-Mayor Chokwe Antar Lumumba · Judge Daniel Jordan", at=0.1)
SENT_O = dict(type="verdict", kicker="NOV 5, 2026 · JACKSON, MISS.", stamp="SENTENCED", big="41 Months", sub="Ex-DA Jody Owens · plus a $100,000 fine", at=0.1)
shorts = [
 # S1 — the mayor (strongest, 10:00)
 {"title": "37 Months: Jackson's Ex-Mayor and the $50K FBI Sting", "template": "number reveal + verdict",
  "lines": [
  L("Thirty-seven months in prison. That's the sentence for the former mayor of Jackson, Mississippi, who took fifty thousand dollars from developers secretly working for the F.B.I.",
    hook("h_face", tag="SENTENCED", number="37 MONTHS", label="EX-MAYOR · $50K|FBI STING"),
    show="37 months in prison. That's the sentence for the former mayor of Jackson, Mississippi, who took $50,000 from developers secretly working for the FBI."),
  L("On a yacht in Florida, Chokwe Antar Lumumba was handed five ten-thousand-dollar checks.",
    doc("i_checks", IND + " · ¶ 57 · APRIL 2, 2024", SRC_I),
    show="On a yacht in Florida, Chokwe Antar Lumumba was handed five $10,000 checks."),
  L("He made one phone call, to move a city deadline up by fifteen days. The F.B.I. was recording.",
    photo("ph_call", "INDICTMENT ¶ 56 · FBI RECORDING", SRC_IPH),
    show="He made one phone call, to move a city deadline up by 15 days. The FBI was recording."),
  L("He pleaded guilty. The judge told him: You were the top elected official in the city of Jackson.",
    SENT_L, show="He pleaded guilty. The judge told him: \"You were the top elected official in the city of Jackson.\""),
  L("Was thirty-seven months enough?",
    dict(type="end", cta="FULL CASE ON THE CHANNEL"), show="Was 37 months enough?"),
 ]},
 # S2 — the DA's line (14:00)
 {"title": "\"They're Not FBI by the Way\": The DA Who Vouched", "template": "verbatim quote + twist",
  "lines": [
  L("They're not F.B.I., by the way. That's what a Mississippi district attorney told his city's mayor about two developers, according to the indictment.",
    hook("h_call", tag="SENTENCED", number="“NOT FBI”", label="THEY WERE FBI|FBI RECORDING · INDICTMENT"),
    show="\"They're not FBI by the way.\" That's what a Mississippi district attorney told his city's mayor about two developers, according to the indictment."),
  L("They were. Both worked for the F.B.I.",
    doc("i_fbi", IND + " · ¶ 1", SRC_I)),
  L("The indictment says district attorney Jody Owens took a hundred twenty-five thousand dollars in cash on a yacht, and told them: Everybody needs something fixed.",
    doc("i_fixed", IND + " · ¶ 27 · DEC 13, 2023", SRC_I),
    show="The indictment says district attorney Jody Owens took $125,000 in cash on a yacht, and told them: \"Everybody needs something fixed.\""),
  L("He steered fifty thousand to the mayor.",
    doc("i_conv", IND + " · ¶ 54 · MARCH 2024", SRC_I),
    show="He steered $50,000 to the mayor."),
  L("Owens pleaded guilty. Forty-one months, and a hundred-thousand-dollar fine.",
    SENT_O, show="Owens pleaded guilty. 41 months, and a $100,000 fine."),
  L("Would you have believed him?",
    dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S3 — the lockbox (18:00)
 {"title": "$20,000 Inside a Fake Constitution: The DA's Lockbox", "template": "evidence reveal",
  "lines": [
  L("About twenty thousand dollars in cash, in a lockbox made to look like the Constitution. The F.B.I. found it in a district attorney's office.",
    hook("h_book", tag="SENTENCED", number="$20,000", label="INSIDE “THE CONSTITUTION”|FBI SEARCH"),
    show="About $20,000 in cash, in a lockbox made to look like \"The Constitution.\" The FBI found it in a district attorney's office."),
  L("That day, an agent asked him about safes or lockboxes. According to the indictment, he said: none exist.",
    doc("i_none", IND + " · COUNT 11 · MAY 22, 2024", SRC_I),
    show="That day, an agent asked him about safes or lockboxes. According to the indictment, he said: \"none exist.\""),
  L("About nine thousand nine hundred of that cash matched, by serial number, money undercover F.B.I. developers gave him on a yacht.",
    doc("i_lockbox", IND + " · ¶ 65", SRC_I),
    show="About $9,900 of that cash matched, by serial number, money undercover FBI developers gave him on a yacht."),
  L("Jody Owens pleaded guilty. Forty-one months.", SENT_O, show="Jody Owens pleaded guilty. 41 months."),
  L("Was that enough for a prosecutor?",
    dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
]
for i, s in enumerate(shorts, 1):
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), s["title"], sum(len(l["say"].split()) for l in s["lines"]), "words")
