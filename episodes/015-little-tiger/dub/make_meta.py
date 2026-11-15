#!/usr/bin/env python3
"""Translated YouTube title + description for the dubbed languages of episode 015 (sources block kept in English: source titles + URLs)."""
import os, re
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D, "..", "youtube_description.txt"), encoding="utf-8").read()
SOURCES = src[src.index("- U.S. Attorney's Office S.D. Cal. — Chinese National in Viral"):src.index("\n\nEvery quotation")].strip()
CASE = "SWORN · Case 015 · United States v. Jiandong Chen, No. 24-cr-1317-RSH (S.D. Cal.)"
TIMES = ["0:00", "1:06", "2:40", "4:27", "6:34", "8:25", "10:51"]

M = {
"es": dict(
 title="Jiandong Chen: EXPUESTO en YouTube por estafa de $27M — 78 meses",
 l1="Condenado el estafador «Little Tiger»: Jiandong Chen, el mensajero de efectivo confrontado por Trilogy Media en el viral video del «funeral falso», recibe 78 meses de prisión en un fraude de 27 millones de dólares contra personas mayores.",
 l2="Estafa de reembolso, falso soporte técnico, cazaestafadores Trilogy Media y Scammer Payback, fraude a adultos mayores, mulas de dinero, identificaciones falsas, lavado con criptomonedas: el caso explicado con los documentos de la Fiscalía federal.",
 photo="Foto: diapositiva de sentencia del DOJ publicada por la Fiscalía federal del Distrito Sur de California (13 nov 2026), obra del gobierno de EE. UU.",
 summ="El 13 de noviembre de 2026, el juez federal Robert S. Huie, en San Diego, condenó a Jiandong Chen, alias «Little Tiger», a 78 meses (6 años y medio) de prisión. Chen se declaró culpable en abril de 2026 de conspiración para cometer fraude postal y electrónico y de conspiración para lavar dinero, en un esquema que, según la Fiscalía, costó más de 27 millones de dólares a más de 2.000 víctimas mayores entre 2021 y 2023. Admitió que su parte implicó más de 9,5 millones de dólares en pérdidas. El cabecilla, Zhao Wang («Oscar»), fue condenado a 151 meses en mayo de 2026.",
 ch=["Introducción", "La ventana emergente", "Efectivo en una caja", "Los videos de los paquetes", "La redada", "Los cazaestafadores", "La sentencia"],
 chh="Capítulos:", srch="Fuentes (registros públicos y prensa, en inglés):",
 notes="Cada cita en pantalla es textual de la fuente que la acompaña. Los documentos son comunicados de la Fiscalía federal (S.D. Cal.) y diapositivas de sentencia del DOJ (sello eliminado). Las afirmaciones de acusaciones son alegatos salvo que las cubra una declaración de culpabilidad o una sentencia. No se nombra a las víctimas. No se muestran imágenes de Trilogy Media ni de Scammer Payback.\nLa narración usa una voz sintética. Doblaje: traducción y voz sintética.\nSWORN es un canal independiente y no está afiliado a ningún tribunal ni agencia del gobierno.",
 tags="#estafa #fraude #truecrime #casoreal #juicio",
 q="¿Las personas que amas reconocerían una estafa de reembolso? Cuéntanos en los comentarios."),
"pt": dict(
 title="Jiandong Chen: EXPOSTO no YouTube em golpe de US$27 mi — 78 meses",
 l1="Condenado o golpista «Little Tiger»: Jiandong Chen, o mensageiro de dinheiro confrontado pelo Trilogy Media no vídeo viral do «funeral falso», pega 78 meses de prisão num golpe de 27 milhões de dólares contra idosos.",
 l2="Golpe do reembolso, falso suporte técnico, caçadores de golpistas Trilogy Media e Scammer Payback, fraude contra idosos, laranjas, documentos falsos, lavagem com criptomoedas — o caso explicado com os registros da Procuradoria federal dos EUA.",
 photo="Foto: slide de sentença do DOJ publicado pela Procuradoria federal do Distrito Sul da Califórnia (13 nov 2026), obra do governo dos EUA.",
 summ="Em 13 de novembro de 2026, o juiz federal Robert S. Huie, em San Diego, condenou Jiandong Chen, o «Little Tiger», a 78 meses (6 anos e meio) de prisão. Chen se declarou culpado em abril de 2026 de conspiração para fraude postal e eletrônica e de conspiração para lavagem de dinheiro, num esquema que, segundo a Procuradoria, causou mais de 27 milhões de dólares em perdas a mais de 2.000 idosos entre 2021 e 2023. Ele admitiu que sua parte envolveu mais de 9,5 milhões de dólares em perdas. O chefe, Zhao Wang («Oscar»), foi condenado a 151 meses em maio de 2026.",
 ch=["Abertura", "O pop-up", "Dinheiro na caixa", "Os vídeos dos pacotes", "A operação", "Os caçadores de golpistas", "A sentença"],
 chh="Capítulos:", srch="Fontes (registros públicos e imprensa, em inglês):",
 notes="Toda citação na tela é literal da fonte mostrada com ela. Os documentos são comunicados da Procuradoria federal (S.D. Cal.) e slides de sentença do DOJ (brasão removido). Afirmações de denúncias são acusações, salvo quando cobertas por confissão de culpa ou sentença. As vítimas não são identificadas. Imagens do Trilogy Media e do Scammer Payback não são exibidas.\nA narração usa voz sintética. Dublagem: tradução e voz sintética.\nO SWORN é um canal independente, sem vínculo com tribunais ou órgãos do governo.",
 tags="#golpe #fraude #truecrime #casoreal #julgamento",
 q="As pessoas que você ama reconheceriam um golpe do reembolso? Conte nos comentários."),
"hi": dict(
 title="Jiandong Chen: $27M ठगी का कूरियर YouTube पर बेनकाब — 78 महीने की जेल",
 l1="«Little Tiger» ठग को सज़ा: Jiandong Chen, वह नकदी कूरियर जिसका सामना Trilogy Media ने वायरल «फ़र्ज़ी अंतिम संस्कार» वीडियो में किया था, बुज़ुर्गों से 27 मिलियन डॉलर की ठगी के मामले में 78 महीने की जेल।",
 l2="रिफ़ंड स्कैम, टेक सपोर्ट स्कैम, स्कैमबेटर Trilogy Media और Scammer Payback, बुज़ुर्गों से ठगी, मनी म्यूल, नकली पहचान पत्र, क्रिप्टो से मनी लॉन्ड्रिंग — अमेरिकी अटॉर्नी के रिकॉर्ड से पूरा मामला।",
 photo="फ़ोटो: दक्षिणी कैलिफ़ोर्निया के अमेरिकी अटॉर्नी दफ़्तर द्वारा जारी DOJ सज़ा स्लाइड (13 नवंबर 2026), अमेरिकी सरकार का कार्य।",
 summ="13 नवंबर 2026 को San Diego में अमेरिकी ज़िला जज Robert S. Huie ने Jiandong Chen उर्फ़ «Little Tiger» को 78 महीने (साढ़े छह साल) की जेल की सज़ा दी। Chen ने अप्रैल 2026 में डाक और वायर धोखाधड़ी की साज़िश और मनी लॉन्ड्रिंग की साज़िश का अपराध कबूल किया था। अमेरिकी अटॉर्नी दफ़्तर के अनुसार इस धंधे से 2021–2023 में 2,000 से ज़्यादा बुज़ुर्ग पीड़ितों को 27 मिलियन डॉलर से ज़्यादा का नुकसान हुआ। उसने माना कि उसके हिस्से में 9.5 मिलियन डॉलर से ज़्यादा का नुकसान शामिल था। सरगना Zhao Wang («Oscar») को मई 2026 में 151 महीने की सज़ा मिली।",
 ch=["शुरुआत", "पॉप-अप", "डिब्बे में नकदी", "पैकेट वाले वीडियो", "धरपकड़", "ठगों के शिकारी", "सज़ा"],
 chh="अध्याय:", srch="स्रोत (सार्वजनिक रिकॉर्ड और रिपोर्टिंग, अंग्रेज़ी में):",
 notes="स्क्रीन पर हर उद्धरण साथ दिखाए गए स्रोत से शब्दशः है। दिखाए गए दस्तावेज़ अमेरिकी अटॉर्नी दफ़्तर (S.D. Cal.) की प्रेस रिलीज़ और DOJ की सज़ा स्लाइड हैं (मुहर हटाई गई)। अभियोग के कथन आरोप हैं, जब तक उन पर अपराध-स्वीकृति या सज़ा न हो। पीड़ितों के नाम नहीं दिए गए। Trilogy Media और Scammer Payback के फ़ुटेज नहीं दिखाए गए।\nनैरेशन में सिंथेटिक आवाज़ है। डबिंग: अनुवाद और सिंथेटिक आवाज़।\nSWORN एक स्वतंत्र चैनल है और किसी अदालत या सरकारी एजेंसी से जुड़ा नहीं है।",
 tags="#ठगी #स्कैम #truecrime #अदालत #फ़्रॉड",
 q="क्या आपके अपने रिफ़ंड स्कैम को पहचान पाएँगे? कमेंट में बताइए।"),
"fr": dict(
 title="Jiandong Chen : DÉMASQUÉ sur YouTube, arnaque à 27 M$ — 78 mois",
 l1="L'arnaqueur « Little Tiger » condamné : Jiandong Chen, le coursier confronté par Trilogy Media dans la vidéo virale du « faux enterrement », écope de 78 mois de prison dans une fraude de 27 millions de dollars visant des seniors.",
 l2="Arnaque au remboursement, faux support technique, chasseurs d'arnaqueurs Trilogy Media et Scammer Payback, fraude aux personnes âgées, mules financières, faux papiers, blanchiment en cryptomonnaie : l'affaire expliquée à partir du dossier du procureur fédéral.",
 photo="Photo : diapositive de condamnation du DOJ publiée par le bureau du procureur fédéral du district sud de Californie (13 nov. 2026), œuvre du gouvernement américain.",
 summ="Le 13 novembre 2026, à San Diego, le juge fédéral Robert S. Huie a condamné Jiandong Chen, alias « Little Tiger », à 78 mois (6 ans et demi) de prison. Chen avait plaidé coupable en avril 2026 d'association pour fraude postale et électronique et d'association pour blanchiment, dans un système qui, selon le procureur, a coûté plus de 27 millions de dollars à plus de 2 000 victimes âgées entre 2021 et 2023. Il a reconnu que sa part représentait plus de 9,5 millions de dollars de pertes. Le chef, Zhao Wang (« Oscar »), a été condamné à 151 mois en mai 2026.",
 ch=["Ouverture", "La fenêtre pop-up", "Du liquide dans un carton", "Les vidéos des colis", "Le coup de filet", "Les chasseurs d'arnaqueurs", "La peine"],
 chh="Chapitres :", srch="Sources (documents publics et presse, en anglais) :",
 notes="Chaque citation à l'écran est mot pour mot celle de la source affichée. Les documents montrés sont des communiqués du procureur fédéral (S.D. Cal.) et des diapositives de condamnation du DOJ (sceau retiré). Les éléments des actes d'accusation sont des allégations sauf s'ils sont couverts par un plaider-coupable ou une condamnation. Les victimes ne sont pas nommées. Aucune image de Trilogy Media ni de Scammer Payback n'est montrée.\nLa narration utilise une voix de synthèse. Doublage : traduction et voix de synthèse.\nSWORN est une chaîne indépendante, sans lien avec un tribunal ou une agence gouvernementale.",
 tags="#arnaque #fraude #truecrime #faitdivers #proces",
 q="Vos proches reconnaîtraient-ils une arnaque au remboursement ? Dites-le en commentaire."),
"it": dict(
 title="Jiandong Chen: SMASCHERATO su YouTube, truffa da 27 mln $ — 78 mesi",
 l1="Condannato il truffatore «Little Tiger»: Jiandong Chen, il corriere di contanti affrontato da Trilogy Media nel video virale del «finto funerale», prende 78 mesi di carcere per una frode da 27 milioni di dollari ai danni di anziani.",
 l2="Truffa del rimborso, finta assistenza tecnica, cacciatori di truffatori Trilogy Media e Scammer Payback, frodi agli anziani, money mule, documenti falsi, riciclaggio in criptovalute: il caso spiegato con gli atti della Procura federale USA.",
 photo="Foto: slide di condanna del DOJ pubblicata dalla Procura federale del Distretto Sud della California (13 nov 2026), opera del governo USA.",
 summ="Il 13 novembre 2026, a San Diego, il giudice federale Robert S. Huie ha condannato Jiandong Chen, detto «Little Tiger», a 78 mesi (6 anni e mezzo) di carcere. Chen si era dichiarato colpevole ad aprile 2026 di associazione per frode postale e telematica e di associazione per riciclaggio, in uno schema che, secondo la Procura, è costato oltre 27 milioni di dollari a più di 2.000 vittime anziane tra il 2021 e il 2023. Ha ammesso che la sua parte ha comportato oltre 9,5 milioni di dollari di perdite. Il capo, Zhao Wang («Oscar»), è stato condannato a 151 mesi a maggio 2026.",
 ch=["Apertura", "Il pop-up", "Contanti in una scatola", "I video dei pacchi", "Il blitz", "I cacciatori di truffatori", "La condanna"],
 chh="Capitoli:", srch="Fonti (atti pubblici e stampa, in inglese):",
 notes="Ogni citazione sullo schermo è testuale dalla fonte mostrata. I documenti sono comunicati della Procura federale (S.D. Cal.) e slide di condanna del DOJ (sigillo rimosso). Le affermazioni degli atti d'accusa sono accuse, salvo dove coperte da dichiarazione di colpevolezza o condanna. Le vittime non sono nominate. Non sono mostrate immagini di Trilogy Media né di Scammer Payback.\nLa narrazione usa una voce sintetica. Doppiaggio: traduzione e voce sintetica.\nSWORN è un canale indipendente e non è affiliato a tribunali o enti governativi.",
 tags="#truffa #frode #truecrime #cronaca #processo",
 q="Le persone che amate riconoscerebbero una truffa del rimborso? Scrivetelo nei commenti."),
"de": dict(
 title="Jiandong Chen: Auf YouTube ENTLARVT, 27-Mio.-$-Betrug — 78 Monate",
 l1="Betrüger «Little Tiger» verurteilt: Jiandong Chen, der Geldkurier, den Trilogy Media im viralen «Fake-Beerdigung»-Video zur Rede stellte, bekommt 78 Monate Haft im 27-Millionen-Dollar-Betrug an Senioren.",
 l2="Rückerstattungsbetrug, falscher Tech-Support, Scambaiter Trilogy Media und Scammer Payback, Betrug an Senioren, Geldkuriere, gefälschte Ausweise, Geldwäsche mit Krypto — der Fall erklärt aus den Akten der US-Bundesstaatsanwaltschaft.",
 photo="Foto: DOJ-Folie zur Strafverkündung, veröffentlicht von der Bundesstaatsanwaltschaft für den Southern District of California (13. Nov. 2026), Werk der US-Regierung.",
 summ="Am 13. November 2026 verurteilte Bundesrichter Robert S. Huie in San Diego Jiandong Chen, genannt «Little Tiger», zu 78 Monaten (sechseinhalb Jahren) Haft. Chen hatte sich im April 2026 der Verschwörung zu Post- und Überweisungsbetrug sowie der Verschwörung zur Geldwäsche schuldig bekannt – in einem System, das laut Staatsanwaltschaft 2021–2023 mehr als 2.000 ältere Opfer über 27 Millionen Dollar kostete. Er gab zu, dass sein Anteil Verluste von über 9,5 Millionen Dollar umfasste. Der Anführer Zhao Wang («Oscar») wurde im Mai 2026 zu 151 Monaten verurteilt.",
 ch=["Einstieg", "Das Pop-up", "Bargeld im Karton", "Die Paketvideos", "Der Zugriff", "Die Betrügerjäger", "Das Urteil"],
 chh="Kapitel:", srch="Quellen (öffentliche Akten und Berichte, auf Englisch):",
 notes="Jedes Zitat auf dem Bildschirm stammt wörtlich aus der jeweils gezeigten Quelle. Gezeigte Dokumente sind Mitteilungen der Bundesstaatsanwaltschaft (S.D. Cal.) und DOJ-Folien zur Strafverkündung (Siegel entfernt). Aussagen aus Anklageschriften sind Vorwürfe, sofern kein Schuldbekenntnis oder Urteil sie abdeckt. Opfer werden nicht genannt. Aufnahmen von Trilogy Media und Scammer Payback werden nicht gezeigt.\nDie Erzählstimme ist synthetisch. Synchronisation: Übersetzung und synthetische Stimme.\nSWORN ist ein unabhängiger Kanal und mit keinem Gericht und keiner Behörde verbunden.",
 tags="#betrug #scam #truecrime #gericht #urteil",
 q="Würden Ihre Liebsten einen Rückerstattungsbetrug erkennen? Schreiben Sie es in die Kommentare."),
"ru": dict(
 title="Jiandong Chen: курьер аферы на $27 млн РАЗОБЛАЧЁН на YouTube — 78 мес.",
 l1="Мошенник «Little Tiger» получил срок: Jiandong Chen, курьер с наличными, которого Trilogy Media разоблачили в вирусном видео с «фальшивыми похоронами», получил 78 месяцев тюрьмы по делу о мошенничестве против пожилых на 27 миллионов долларов.",
 l2="Афера с возвратом денег, фальшивая техподдержка, охотники на мошенников Trilogy Media и Scammer Payback, мошенничество против пожилых, денежные курьеры, поддельные документы, отмывание через криптовалюту — дело по материалам федеральной прокуратуры США.",
 photo="Фото: слайд Минюста США к приговору, опубликованный федеральной прокуратурой Южного округа Калифорнии (13 ноября 2026), работа правительства США.",
 summ="13 ноября 2026 года федеральный судья Robert S. Huie в San Diego приговорил Jiandong Chen по прозвищу «Little Tiger» к 78 месяцам (6,5 года) тюрьмы. В апреле 2026 года Chen признал вину в сговоре с целью почтового и электронного мошенничества и в сговоре с целью отмывания денег. По данным прокуратуры, схема в 2021–2023 годах обошлась более чем 2000 пожилых жертв в 27 с лишним миллионов долларов. Он признал, что на его долю пришлось более 9,5 млн долларов ущерба. Главарь Zhao Wang («Oscar») получил 151 месяц в мае 2026 года.",
 ch=["Вступление", "Всплывающее окно", "Наличные в коробке", "Видео с посылками", "Задержание", "Охотники на мошенников", "Приговор"],
 chh="Главы:", srch="Источники (публичные документы и пресса, на английском):",
 notes="Каждая цитата на экране дословно взята из показанного рядом источника. Показаны пресс-релизы федеральной прокуратуры (S.D. Cal.) и слайды Минюста к приговору (герб удалён). Утверждения из обвинительных документов — это обвинения, если их не подтверждает признание вины или приговор. Имена пострадавших не называются. Кадры Trilogy Media и Scammer Payback не показываются.\nОзвучка — синтетический голос. Дубляж: перевод и синтетический голос.\nSWORN — независимый канал, не связанный ни с одним судом или госорганом.",
 tags="#мошенничество #афера #truecrime #суд #приговор",
 q="Узнали бы ваши близкие аферу с возвратом денег? Напишите в комментариях."),
}

for k, m in M.items():
    assert len(m["title"]) <= 70, (k, len(m["title"]))
    os.makedirs(os.path.join(D, k), exist_ok=True)
    open(os.path.join(D, k, "title.txt"), "w", encoding="utf-8").write(m["title"] + "\n")
    out = [m["l1"], m["l2"], m["photo"], m["summ"], "", m["chh"]] + [f"{t} {c}" for t, c in zip(TIMES, m["ch"])]
    out += ["", m["srch"], SOURCES, "", m["notes"], "", CASE, m["tags"], "", m["q"]]
    open(os.path.join(D, k, "description.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(k, len(m["title"]), m["title"])
