# Scanned filings: highlight y-ranges measured with tesseract TSV on the 220-dpi raster (see /home/claude/research/tfind.py)
P = 'gov.uscourts.nysd.481447.'
M = {
 'inf_s1':   (P + '30.0.pdf', 1, 0.03, 0.70, [(0.4522, 0.5324)]),   # S1 Superseding Information, Count One
 'jdg_72':   (P + '68.0.pdf', 3, 0.03, 0.40, [(0.200, 0.250)]),     # Judgment: 72 months
 'jdg_forf': (P + '68.0.pdf', 9, 0.55, 0.93, [(0.834, 0.870)]),     # Judgment: forfeit $26,191,306.28
 'sub_shirts': (P + '79.0.pdf', 1, 0.30, 0.93, [(0.7409, 0.7897)]), # Racz decl.: boxes of Fyre-branded clothing
 'ltr_2020': (P + '98.0.pdf', 1, 0.20, 0.72, [(0.4632, 0.4959)]),   # Judge Buchwald letter, May 11, 2020
}
