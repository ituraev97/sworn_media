import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def doc(key, kicker, src, pan=None):
    img, a, b = HL[key]
    c = (a + b) / 2
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [max(0.0, round(c - 0.2, 3)), max(0.0, round(c - 0.14, 3))],
                hl=[0.0, a, 1.0, round(b - a, 4)], kicker=kicker, src=src)
S_ALI = "Gov't sentencing memo, Ladan Ali (D. Minn. 24-cr-173, Dkt. 277)"
S_AZ = "Gov't sentencing memo, Abdiaziz Farah (D. Minn. 24-cr-173, Dkt. 216)"
S_SF = "Gov't sentencing memo, Said Farah (D. Minn. 24-cr-173, Dkt. 251)"
S_NUR = "Gov't sentencing memo, Abdimajid Nur (D. Minn. 24-cr-173, Dkt. 243)"
S_PRALI = "USAO D. Minn. press release, Sep 5, 2024"
S_PR24 = "USAO D. Minn. press release, Jun 26, 2024"
S_ACQ = "Judgment of acquittal (D. Minn. 22-cr-124, Dkt. 579)"
G = "GOV'T MEMO"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def hook(img, **kw):
    d = dict(type="hook", img=f"img/{img}.jpg", pos="50% 0%", zoom=1.3334); d.update(kw); return d
ALL5 = dict(type="verdict", kicker="MARCH – NOV 2026 · D. MINN.", stamp="ALL 5 SENTENCED", big="4 to 10 Years", sub="Bribery of a juror · Feeding Our Future trial", at=0.1)
ALI = dict(type="verdict", kicker="NOV 20, 2026 · D. MINN.", stamp="SENTENCED", big="4 Years", sub="Ladan Ali · Judge Eric C. Tostrud", at=0.1)
SAID = dict(type="verdict", kicker="OCT 30, 2026 · PER MPR NEWS", stamp="SENTENCED", big="6½ Years", sub="Said Farah · bribery of a juror", at=0.1)
shorts = [
 # S1 — the bag and the call (strongest, 10:00)
 {"title": "$120,000 in a Gift Bag: The Juror Who Called the Police", "template": "number reveal + verdict",
  "lines": [
  L("A hundred and twenty thousand dollars in cash, in a Hallmark gift bag, left at a juror's door in the first Feeding Our Future fraud trial.",
    hook("h_bag", tag="SENTENCED", number="$120,000", label="FOR JUROR 52|FEEDING OUR FUTURE"),
    show="$120,000 in cash, in a Hallmark gift bag, left at a juror's door in the first Feeding Our Future fraud trial."),
  L("A present, the courier told her stepfather. More, if she voted not guilty.",
    doc("a_present", G + " · ABDIAZIZ FARAH", S_AZ),
    show="A \"present,\" the courier told her stepfather. More, if she voted not guilty."),
  L("They picked Juror fifty-two, prosecutors say, because they thought she was the youngest juror.",
    doc("p_youngest", "USAO D. MINN. · JUN 26, 2024", S_PR24),
    show="They picked Juror 52, prosecutors say, because they thought she was the youngest juror."),
  L("She called the police that night. All five people behind the plot pleaded guilty, and got four to ten years.",
    ALL5, show="She called the police that night. All five people behind the plot pleaded guilty, and got 4 to 10 years."),
  L("Would you have picked up the phone?",
    dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S2 — the courier (14:00)
 {"title": "\"It's Done Babe\": She Skimmed $80K From a Juror Bribe", "template": "verbatim quote + twist",
  "lines": [
  L("Eighty thousand dollars. That's how much the courier kept for herself, out of a two hundred thousand dollar bribe meant for a juror.",
    hook("h_stole", tag="SENTENCED", number="$80,000", label="SKIMMED FROM|THE BRIBE"),
    show="$80,000. That's how much the courier kept for herself, out of a $200,000 bribe meant for a juror."),
  L("Ladan Ali told the plotters the juror wanted five hundred thousand. In the government's words, she fabricated this entire interaction.",
    doc("a_fabricated", G + " · LADAN ALI", S_ALI),
    show="Ladan Ali told the plotters the juror wanted $500,000. In the government's words, she \"fabricated this entire interaction.\""),
  L("She delivered the rest, and texted: It's done, babe.",
    doc("a_done", G + " · ABDIMAJID NUR", S_NUR),
    show="She delivered the rest, and texted: \"It's done babe.\""),
  L("The juror called the police. Ali pleaded guilty. Four years in prison.",
    ALI, show="The juror called the police. Ali pleaded guilty. Four years in prison."),
  L("Was four years enough?",
    dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S3 — the acquitted brother (18:00)
 {"title": "Acquitted on All Counts, Then Guilty of Bribing a Juror", "template": "irony / before→after",
  "lines": [
  L("Acquitted on all counts. And the government says he was the one who collected two hundred thousand dollars in cash to bribe one of its jurors.",
    hook("h_ironic", tag="SENTENCED", number="$200,000", label="“IRONICALLY|ACQUITTING”"),
    show="Acquitted on all counts. And the government says he was the one who collected $200,000 in cash to bribe one of its jurors."),
  L("Said Farah was on trial in the Feeding Our Future fraud case. The bribe went to Juror fifty-two. She called the police.",
    doc("a_reported", G + " · ABDIAZIZ FARAH", S_AZ),
    show="Said Farah was on trial in the Feeding Our Future fraud case. The bribe went to Juror 52. She called the police."),
  L("The remaining jurors acquitted him. The government's word for it: ironically.",
    doc("a_ironic", G + " · SAID FARAH", S_SF),
    show="The remaining jurors acquitted him. The government's word for it: \"ironically.\""),
  L("Then he pleaded guilty to bribing a juror. Six and a half years.",
    SAID, show="Then he pleaded guilty to bribing a juror. Six and a half years."),
  L("What would you have done on that jury?",
    dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
]
for i, s in enumerate(shorts, 1):
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), s["title"], sum(len(l["say"].split()) for l in s["lines"]), "words")
