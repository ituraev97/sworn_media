import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def doc(key, kicker, src, pan=None):
    img, a, b = HL[key]
    c = (a + b) / 2
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [max(0.0, round(c - 0.2, 3)), max(0.0, round(c - 0.14, 3))],
                hl=[0.0, a, 1.0, round(b - a, 4)], kicker=kicker, src=src)
SRC_P = "Plea agreement, U.S. v. Mestanza Cercado, Dkt. 158 (C.D. Cal., Nov 9, 2026)"
SRC_I = "Indictment, U.S. v. Mestanza Cercado et al. (C.D. Cal., June 11, 2025)"
SRC_PR26 = "U.S. Attorney's Office, C.D. Cal. (Nov 19, 2026)"
SRC_AP = "Brinks lawsuit (2022), as reported by AP"
PA = "PLEA AGREEMENT"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def hook(img, **kw):
    d = dict(type="hook", img=f"img/{img}.jpg", pos="50% 0%", zoom=1.3334); d.update(kw); return d
PLEA = dict(type="verdict", kicker="NOV 19, 2026 · RIVERSIDE", stamp="GUILTY PLEA", big="Max 20 Years", sub="Sentencing April 15, 2027 · Mestanza Cercado", at=0.1)
shorts = [
 # S1 — the number dispute (strongest, 10:00)
 {"title": "$100M or Under $10M? The Brinks Heist Plea Twist", "template": "number reveal + twist",
  "lines": [
  L("A hundred million dollars in jewelry, stolen from a Brinks truck. Now the lead defendant has pleaded guilty, and says it was declared at under ten million.",
    hook("h_10m", tag="GUILTY PLEA", number="$100M", label="OR UNDER $10M?|HIS PLEA DEAL"),
    show="$100 million in jewelry, stolen from a Brinks truck. Now the lead defendant has pleaded guilty, and says it was declared at under $10 million."),
  L("July twenty twenty-two. His crew broke the locks and took twenty-four bags, which the victims valued at about a hundred million.",
    doc("p_24", PA + " · JULY 11, 2022", SRC_P),
    show="July 2022. His crew broke the locks and took 24 bags, which the victims valued at about $100 million."),
  L("In his plea deal, he contends certain victims declared a total of less than ten million to Brinks. Prosecutors dispute that, and say restitution is at least a hundred million.",
    doc("p_declared", PA + " · ¶ 9", SRC_P),
    show="In his plea deal, he contends certain victims declared a total of less than $10 million to Brinks. Prosecutors dispute that, and say restitution is at least $100 million."),
  L("He'll be sentenced in April. The maximum is twenty years.",
    PLEA, show="He'll be sentenced in April. The maximum is 20 years."),
  L("Should he owe a hundred million, or ten?",
    dict(type="end", cta="FULL CASE ON THE CHANNEL"), show="Should he owe $100 million, or $10 million?"),
 ]},
 # S2 — the run (14:00)
 {"title": "\"Stupidities From the Past\": The Brinks Heist Fugitive", "template": "verbatim quote + capture",
  "lines": [
  L("Stupidities from the past that I'm now paying for. That's what the lead defendant in a hundred-million-dollar jewelry heist texted, days after he was indicted.",
    hook("h_texts", tag="GUILTY PLEA", number="$100M", label="HEIST · THEN HE RAN|PER HIS PLEA DEAL"),
    show="\"Stupidities from the past that I'm now paying for.\" That's what the lead defendant in a $100 million jewelry heist texted, days after he was indicted."),
  L("His plea deal says he searched online about a person wanted by Interpol, and messaged about crossing the border after a robo grande. A big robbery.",
    doc("p_robo", PA + " · JUNE 28, 2025", SRC_P),
    show="His plea deal says he searched online about a person wanted by Interpol, and messaged about crossing the border after a \"robo grande.\" A big robbery."),
  L("On July first, twenty twenty-five, he was detained at the airport in Panama City, on a layover to Ecuador.",
    doc("p_panama", PA + " · JULY 1, 2025", SRC_P),
    show="On July 1, 2025, he was detained at the airport in Panama City, on a layover to Ecuador."),
  L("Extradited, he pleaded guilty on November nineteenth.",
    PLEA, show="Extradited, he pleaded guilty on November 19."),
  L("Would you have run?",
    dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S3 — how it worked (18:00)
 {"title": "24 Bags, 300 Miles: How the $100M Brinks Heist Worked", "template": "number reveal + method",
  "lines": [
  L("Twenty-four bags of jewelry, valued at a hundred million dollars, gone from one Brinks truck. The lead defendant just pleaded guilty, and admitted how it worked.",
    hook("h_24", tag="GUILTY PLEA", number="24 BAGS", label="$100M · 300 MILES|PER HIS PLEA DEAL"),
    show="24 bags of jewelry, valued at $100 million, gone from one Brinks truck. The lead defendant just pleaded guilty, and admitted how it worked."),
  L("A crew scouted a jewelry show near San Francisco, picked a Brinks semitruck with seventy-three bags, and followed it about three hundred miles.",
    doc("p_300", PA + " · JULY 10–11, 2022", SRC_P),
    show="A crew scouted a jewelry show near San Francisco, picked a Brinks semitruck with 73 bags, and followed it about 300 miles."),
  L("At a truck stop in Lebec, they broke the locks. Brinks's own lawsuit said one guard was asleep, the other getting food.",
    doc("p_24", PA + " · JULY 11, 2022", SRC_P + "; " + SRC_AP)),
  L("Then they switched off their phones. It took almost three years to charge them.",
    doc("i_oa22", "INDICTMENT · OVERT ACT 22", SRC_I)),
  L("How did they think they'd get away with it?",
    dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
]
def F(si, i, say=None, show=None):
    l = shorts[si]["lines"][i]
    if say is not None: l["say"] = say
    if show is not None: l["show"] = show
    elif say is not None: l.pop("show", None)
F(0, 0, "A hundred million dollars in jewelry, stolen from a Brinks truck. The lead defendant just pleaded guilty, and contends victims had declared it at under ten million.",
  "$100 million in jewelry, stolen from a Brinks truck. The lead defendant just pleaded guilty, and contends victims had declared it at under $10 million.")
F(0, 1, "In twenty twenty-two, his crew broke the locks and took twenty-four bags.", "In 2022, his crew broke the locks and took 24 bags.")
F(0, 2, "In his plea deal, he contends certain victims declared a total of under ten million to Brinks. Prosecutors say restitution is at least a hundred million.",
  "In his plea deal, he contends certain victims declared a total of under $10 million to Brinks. Prosecutors say restitution is at least $100 million.")
F(0, 3, "Sentencing is in April. The maximum is twenty years.", "Sentencing is in April. The maximum is 20 years.")
F(2, 0, "Twenty-four bags of jewelry, valued at a hundred million dollars. The lead defendant just pleaded guilty, and admitted how it worked.",
  "24 bags of jewelry, valued at $100 million. The lead defendant just pleaded guilty, and admitted how it worked.")
F(2, 1, "A crew scouted a jewelry show, picked a Brinks truck with seventy-three bags, and followed it about three hundred miles.",
  "A crew scouted a jewelry show, picked a Brinks truck with 73 bags, and followed it about 300 miles.")
F(2, 2, "At a truck stop in Lebec, they broke the locks. Brinks's lawsuit said one guard slept, the other was getting food.")
F(2, 3, "Then they switched off their phones. Charges took almost three years.")

# ---- independent fact-check fixes (factcheck.md) ----
F(0, 0, "Jewelry its owners valued at a hundred million dollars, stolen from a Brinks truck. The lead defendant just pleaded guilty, and contends certain victims had declared a total of under ten million to Brinks.",
  "Jewelry its owners valued at $100 million, stolen from a Brinks truck. The lead defendant just pleaded guilty, and contends certain victims had declared a total of under $10 million to Brinks.")
F(0, 1, "In twenty twenty-two, he and his co-conspirators broke the locks and took twenty-four bags.", "In 2022, he and his co-conspirators broke the locks and took 24 bags.")
F(0, 4, "Should he owe a hundred million, or less than ten?", "Should he owe $100 million, or less than $10 million?")
F(0, 2, "Prosecutors dispute that, and say restitution is at least a hundred million.", "Prosecutors dispute that, and say restitution is at least $100 million.")
shorts[0]["lines"][0]["scene"]["label"] = "OR UNDER $10M?|HIS PLEA DEAL"
shorts[1]["lines"][0]["scene"]["label"] = "INDICTED · THEN HE RAN|PER HIS PLEA DEAL"
F(2, 0, "Twenty-four bags of jewelry, valued by the victims at a hundred million dollars. The lead defendant just pleaded guilty and admitted how.",
  "24 bags of jewelry, valued by the victims at $100 million. The lead defendant just pleaded guilty and admitted how.")
F(2, 2, "At a truck stop in Lebec, they broke the locks. Brinks's lawsuit said one driver slept, the other was getting food.")

for i, s in enumerate(shorts, 1):
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), s["title"], sum(len(l["say"].split()) for l in s["lines"]), "words")
