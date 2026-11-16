# Figures affichées SOUS L'ÉNONCÉ (avant de répondre). Elles montrent les données, jamais la réponse.
# Seulement quand une figure aide vraiment à comprendre la question.
VERT, ROUGE, BLEU = "#3DDC97", "#FF7A7A", "#5B8CFF"
FIGURES = {
 "q001": {"type":"urne","boules":[[VERT,3],[ROUGE,5],[BLEU,2]]},
 "q007": {"type":"tri_rect","pts":["A","B","C"],"cotes":{"AB":"6 cm","AC":"8 cm","BC":"?"}},
 "q008": {"type":"tri_rect","pts":["A","B","C"],"sans_angle":True,"cotes":{"AB":"5 cm","AC":"12 cm","BC":"13 cm"},"legende":"Rectangle en A ?"},
 "q009": {"type":"thales","cotes":{"AM":"3","AB":"5","AC":"10","AN":"?"}},
 "q010": {"type":"tri_rect","pts":["A","B","C"],"cotes":{"AB":"adjacent","BC":"hypoténuse","AC":"opposé"},"angle":"B"},
 "q020": {"type":"solide","k":"cylindre","labels":{"r":"r = 3 cm","h":"h = 10 cm"}},
 "q021": {"type":"solide","k":"pave","labels":{"L":"20 cm","l":"10 cm","h":"5 cm"}},
 "q027": {"type":"polygone","n":6,"angle":"?"},
 "q147": {"type":"cercle","r":"5 cm","disque":True},
 "q148": {"type":"cercle","d":"10 cm"},
 "q149": {"type":"tri_hauteur","b":"8 cm","h":"5 cm"},
 "q150": {"type":"rect","w":"7 cm","h":"3 cm"},
 "q152": {"type":"solide","k":"cube","labels":{"L":"4 cm","l":"4 cm","h":"4 cm"}},
 "q153": {"type":"solide","k":"pyramide","labels":{"h":"10 cm","base":"aire de base : 30 cm²"}},
 "q155": {"type":"solide","k":"boule","labels":{"r":"r = 3 cm"}},
 "q161": {"type":"tri_rect","pts":["A","B","C"],"angle":"B"},
 "q102": {"type":"circuit","k":"serie","legende":"Circuit en série"},
 "q199": {"type":"circuit","k":"derivation","legende":"Circuit en dérivation"},
}
