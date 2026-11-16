# Corrections détaillées des questions de maths : étapes, règle à retenir, schéma.
def D(i, etapes, retenir, schema=None):
  DETAILS[i] = {"etapes": etapes, "retenir": retenir}
  if schema: DETAILS[i]["schema"] = schema

VERT, ROUGE, BLEU = "#3DDC97", "#FF7A7A", "#5B8CFF"

D("q001", ["On compte toutes les boules : 3 + 5 + 2 = 10 issues possibles, toutes avec la même chance.",
  "On compte les issues favorables, ici les boules vertes : 3.",
  "P(verte) = nombre d'issues favorables ÷ nombre total d'issues = 3/10."],
  "Probabilité = (cas favorables) ÷ (cas possibles), quand tous les cas ont la même chance.",
  {"type":"urne","boules":[[VERT,3],[ROUGE,5],[BLEU,2]]})
D("q002", ["On divise par les plus petits nombres premiers possibles, l'un après l'autre.",
  "1 050 ÷ 2 = 525, puis 525 ÷ 3 = 175, puis 175 ÷ 5 = 35, puis 35 ÷ 5 = 7, et 7 est premier.",
  "On rassemble les diviseurs : 1 050 = 2 × 3 × 5 × 5 × 7 = 2 × 3 × 5² × 7.",
  "Vérification : 2 × 3 × 25 × 7 = 6 × 175 = 1 050."],
  "Dans une décomposition en facteurs premiers, chaque facteur doit être premier (2, 3, 5, 7, 11, 13…).",
  {"type":"table","head":["Nombre","÷ par"],"rows":[["1 050","2"],["525","3"],["175","5"],["35","5"],["7","7"],["1","!fini"]]})
D("q003", ["Augmenter de 14 %, c'est garder 100 % du prix et ajouter 14 % : on obtient 114 % du prix.",
  "114 % = 1,14. On multiplie donc par 1,14 : 50 × 1,14 = 57.",
  "Autre méthode : 14 % de 50 = 50 × 14 ÷ 100 = 7, puis 50 + 7 = 57 €."],
  "Augmenter de t % revient à multiplier par (1 + t/100). Baisser de t %, par (1 − t/100).")
D("q004", ["Un carré de côté 1 a une aire de 1 × 1 = 1.",
  "Agrandi 3 fois, son côté vaut 3 et son aire 3 × 3 = 9.",
  "L'aire est donc multipliée par 9, c'est-à-dire 3²."],
  "Agrandissement de rapport k : longueurs × k, aires × k², volumes × k³.",
  {"type":"fraction","parts":[[1,1],[1,9]]})
D("q005", ["On vérifie que la série est rangée dans l'ordre croissant : 152 ; 158 ; 160 ; 163 ; 171. C'est le cas.",
  "Il y a 5 valeurs. La médiane est celle du milieu : la 3e, avec 2 valeurs avant et 2 après.",
  "La médiane est 160 cm."],
  "La médiane partage la série rangée en deux groupes de même effectif. Avec un nombre pair de valeurs, on prend la moyenne des deux valeurs du milieu.",
  {"type":"barres","vals":[152,158,160,163,171],"hl":[2],"legende":"Valeurs rangées : la 3e est au milieu"})
D("q006", ["On additionne toutes les notes : 12 + 15 + 9 + 14 = 50.",
  "On divise par le nombre de notes, ici 4 : 50 ÷ 4 = 12,5."],
  "Moyenne = somme des valeurs ÷ nombre de valeurs.",
  {"type":"barres","vals":[12,15,9,14],"legende":"Moyenne : 50 ÷ 4 = 12,5"})
D("q007", ["L'hypoténuse est le côté opposé à l'angle droit, ici BC.",
  "Pythagore : BC² = AB² + AC² = 6² + 8² = 36 + 64 = 100.",
  "BC = √100 = 10 cm."],
  "Dans un triangle rectangle : (hypoténuse)² = somme des carrés des deux autres côtés.",
  {"type":"tri_rect","pts":["A","B","C"],"cotes":{"AB":"6 cm","AC":"8 cm","BC":"?"}})
D("q008", ["Le plus grand côté est 13 cm : s'il y a un angle droit, il est en face de ce côté.",
  "On calcule séparément : 13² = 169, et 5² + 12² = 25 + 144 = 169.",
  "Les deux résultats sont égaux, donc d'après la réciproque du théorème de Pythagore, le triangle est rectangle."],
  "Réciproque de Pythagore : si (plus grand côté)² = somme des carrés des deux autres, le triangle est rectangle.",
  {"type":"tri_rect","pts":["A","B","C"],"cotes":{"AB":"5 cm","AC":"12 cm","BC":"13 cm"}})
D("q009", ["Les droites (MN) et (BC) sont parallèles : on peut utiliser le théorème de Thalès.",
  "On écrit les rapports égaux : AM/AB = AN/AC = MN/BC.",
  "On remplace : 3/5 = AN/10.",
  "Produit en croix : AN = 10 × 3 ÷ 5 = 6."],
  "Thalès : avec deux droites parallèles, les longueurs du petit triangle sont proportionnelles à celles du grand.",
  {"type":"thales","cotes":{"AM":"3","AB":"5","AC":"10","AN":"?"}})
D("q010", ["On repère l'hypoténuse : le côté en face de l'angle droit.",
  "Le côté adjacent touche l'angle étudié, sans être l'hypoténuse.",
  "cos = adjacent ÷ hypoténuse."],
  "CAH SOH TOA : Cos = Adj/Hyp, Sin = Opp/Hyp, Tan = Opp/Adj.",
  {"type":"tri_rect","pts":["A","B","C"],"cotes":{"AB":"adjacent","BC":"hypoténuse","AC":"opposé"},"angle":"B"})
D("q011", ["Pour une vitesse en km/h, la durée doit être en heures : 45 min = 45/60 h = 0,75 h.",
  "v = d ÷ t = 12 ÷ 0,75 = 16 km/h.",
  "Vérification : en 15 min (un quart d'heure), Malo fait 4 km, donc 16 km en une heure."],
  "v = d ÷ t, avec des unités cohérentes : km et h donnent des km/h.",
  {"type":"table","head":["Distance","Durée"],"rows":[["4 km","15 min"],["12 km","45 min"],["!16 km","!60 min"]]})
D("q012", ["On choisit 5.", "Ajouter 3 : 5 + 3 = 8.", "Multiplier par 2 : 8 × 2 = 16.", "Soustraire 6 : 16 − 6 = 10.",
  "Avec x au départ : 2(x + 3) − 6 = 2x + 6 − 6 = 2x. Le programme donne toujours le double."],
  "Pour étudier un programme de calcul, on remplace le nombre de départ par x et on développe.",
  {"type":"table","head":["Étape","Avec 5","Avec x"],"rows":[["Départ","5","x"],["+ 3","8","x + 3"],["× 2","16","2x + 6"],["− 6","!10","!2x"]]})
D("q013", ["On utilise la double distributivité : chaque terme de la 1re parenthèse multiplie chaque terme de la 2e.",
  "x × x = x², x × (−2) = −2x, 3 × x = 3x, 3 × (−2) = −6.",
  "On regroupe : x² − 2x + 3x − 6 = x² + x − 6."],
  "(a + b)(c + d) = ac + ad + bc + bd.",
  {"type":"table","head":["×","x","−2"],"rows":[["x","x²","−2x"],["3","3x","−6"]]})
D("q014", ["On reconnaît la forme a² − b² : x² − 9 = x² − 3².",
  "On applique l'identité remarquable : a² − b² = (a − b)(a + b).",
  "x² − 9 = (x − 3)(x + 3). Vérification en développant : x² + 3x − 3x − 9 = x² − 9."],
  "Les 3 identités remarquables : (a+b)² = a²+2ab+b² ; (a−b)² = a²−2ab+b² ; (a−b)(a+b) = a²−b².")
D("q015", ["On isole le terme en x : on enlève 5 des deux côtés. 3x = 20 − 5 = 15.",
  "On divise les deux côtés par 3 : x = 15 ÷ 3 = 5.",
  "Vérification : 3 × 5 + 5 = 20. C'est juste."],
  "Pour résoudre une équation, on fait la même opération des deux côtés du signe égal.")
D("q016", ["f(4) signifie : on remplace x par 4 dans l'expression.",
  "f(4) = 2 × 4 − 3 = 8 − 3 = 5.",
  "Sur le graphique, le point (4 ; 5) est sur la droite."],
  "L'image de a par f est f(a) : on remplace x par a.",
  {"type":"droite","a":2,"b":-3,"point":[4,5],"label":"f(x) = 2x − 3"})
D("q017", ["Un antécédent de 12, c'est un nombre x tel que f(x) = 12.",
  "On résout 3x = 12, donc x = 12 ÷ 3 = 4.",
  "Vérification : f(4) = 3 × 4 = 12."],
  "Image : on part de x et on calcule f(x). Antécédent : on connaît le résultat et on cherche x.",
  {"type":"table","head":["x (antécédent)","f(x) (image)"],"rows":[["1","3"],["2","6"],["!4","!12"]]})
D("q018", ["Chaque lot doit avoir le même nombre de rouges et de noirs : le nombre de lots divise 84 et 60.",
  "On cherche le plus grand diviseur commun (PGCD). 84 = 2² × 3 × 7 et 60 = 2² × 3 × 5.",
  "Facteurs communs : 2² × 3 = 12. On peut faire 12 lots.",
  "Chaque lot contient 84 ÷ 12 = 7 rouges et 60 ÷ 12 = 5 noirs."],
  "« Le plus grand nombre de lots identiques » : c'est le PGCD des quantités.")
D("q019", ["Un nombre premier n'a que deux diviseurs : 1 et lui-même.",
  "91 = 7 × 13, 87 = 3 × 29 (8 + 7 = 15, divisible par 3), 51 = 3 × 17.",
  "97 n'est divisible ni par 2, ni 3, ni 5, ni 7. Comme 10 × 10 = 100 > 97, inutile d'aller plus loin : 97 est premier."],
  "Pour tester si n est premier, on essaie les nombres premiers jusqu'à √n.")
D("q020", ["Le volume d'un cylindre = aire de la base × hauteur.",
  "La base est un disque : π × r² = π × 3² = 9π cm².",
  "V = 9π × 10 = 90π cm³ ≈ 282,7 cm³."],
  "Cylindre : V = π × r² × h. Pense à mettre le rayon au carré, pas le diamètre.",
  {"type":"solide","k":"cylindre","labels":{"r":"r = 3 cm","h":"h = 10 cm"}})
D("q021", ["Volume d'un pavé droit = longueur × largeur × hauteur.",
  "20 × 10 × 5 = 1 000 cm³.",
  "1 L = 1 dm³ = 1 000 cm³, donc l'aquarium contient 1 L."],
  "1 dm³ = 1 L et 1 cm³ = 1 mL.",
  {"type":"solide","k":"pave","labels":{"L":"20 cm","l":"10 cm","h":"5 cm"}})
D("q022", ["2,5 h = 2 h + 0,5 h.", "0,5 h = la moitié de 60 min = 30 min.", "Donc 2,5 h = 2 h 30 min (et pas 2 h 50 !)."],
  "Une heure compte 60 minutes : 0,25 h = 15 min, 0,5 h = 30 min, 0,75 h = 45 min.")
D("q023", ["Baisser de 25 %, c'est garder 75 % du prix : on multiplie par 0,75.",
  "80 × 0,75 = 60 €.",
  "Autre méthode : 25 % de 80 = 80 ÷ 4 = 20, puis 80 − 20 = 60 €."],
  "Baisser de t % revient à multiplier par (1 − t/100).")
D("q024", ["Le prix est proportionnel à la masse. On cherche d'abord le prix d'un kilo : 7,50 ÷ 3 = 2,50 €.",
  "Pour 5 kg : 5 × 2,50 = 12,50 €."],
  "Dans une situation de proportionnalité, on peut passer par l'unité (règle de trois) ou faire un produit en croix.",
  {"type":"table","head":["Masse (kg)","1","3","5"],"rows":[["Prix (€)","2,50","7,50","!12,50"]]})
D("q025", ["Le signe du rapport indique le côté : négatif, l'image est de l'autre côté du centre O.",
  "La valeur sans le signe (2) indique la taille : plus grand que 1, c'est un agrandissement.",
  "L'image est donc 2 fois plus grande et retournée de l'autre côté de O."],
  "Homothétie de rapport k : |k| > 1 agrandit, |k| < 1 réduit ; k < 0 place l'image de l'autre côté du centre.",
  {"type":"transfo","k":"homothetie_neg","legende":"Rapport −2 : 2 fois plus grand, de l'autre côté de O"})
D("q026", ["Le lutin trace 3 côtés de même longueur (50).",
  "À chaque coin il tourne de 120°. En 3 virages, il fait 3 × 120° = 360°, un tour complet : la figure se referme.",
  "3 côtés égaux : c'est un triangle équilatéral."],
  "Pour un polygone régulier à n côtés, le lutin tourne de 360° ÷ n à chaque sommet.",
  {"type":"polygone","n":3,"angle":"120°"})
D("q027", ["Un hexagone a 6 côtés, donc 6 virages.", "Les 6 virages doivent faire un tour complet : 360°.", "360 ÷ 6 = 60°."],
  "Angle à tourner pour un polygone régulier = 360° ÷ nombre de côtés.",
  {"type":"polygone","n":6,"angle":"60°"})
D("q028", ["Une formule de tableur commence toujours par le signe =.", "La multiplication s'écrit avec * : 3 fois A1 s'écrit 3*A1.", "On ajoute 2 : =3*A1+2."],
  "Tableur : = pour commencer, * pour multiplier, / pour diviser, : pour une plage (A1:A5).",
  {"type":"table","head":["","A","B"],"rows":[["1","4","!=3*A1+2 → 14"]]})
D("q029", ["Issues possibles : 1, 2, 3, 4, 5, 6, soit 6 issues.", "Multiples de 3 : 3 et 6, soit 2 issues favorables.", "P = 2/6 = 1/3."],
  "Pense à simplifier la fraction obtenue.",
  {"type":"table","rows":[["1","2","!3","4","5","!6"]]})
D("q030", ["Pour multiplier deux puissances de 10, on additionne les exposants.", "3 + (−5) = −2.", "10³ × 10⁻⁵ = 10⁻² = 0,01."],
  "10ᵃ × 10ᵇ = 10ᵃ⁺ᵇ et 10ᵃ ÷ 10ᵇ = 10ᵃ⁻ᵇ.")
D("q121", ["Priorités : d'abord la multiplication, ensuite l'addition.", "4 × 5 = 20.", "3 + 20 = 23. (Calculer 3 + 4 = 7 puis 7 × 5 = 35 est l'erreur classique.)"],
  "Ordre des calculs : parenthèses, puis puissances, puis × et ÷, puis + et −.")
D("q122", ["D'abord les parenthèses : 3 + 4 = 7.", "Puis la multiplication : 2 × 7 = 14.", "Enfin la soustraction : 20 − 14 = 6."],
  "Ordre des calculs : parenthèses, puis puissances, puis × et ÷, puis + et −.")
D("q123", ["On multiplie les nombres sans les signes : 3 × 4 = 12.", "On compte les signes − : il y en a 2, un nombre pair.", "Le résultat est positif : 12."],
  "Règle des signes : un nombre pair de facteurs négatifs donne un produit positif, un nombre impair un produit négatif.")
D("q124", ["On place −5 sur la droite graduée.", "Ajouter 8, c'est avancer de 8 graduations vers la droite.", "On arrive à 3."],
  "Ajouter un nombre positif fait avancer vers la droite sur la droite graduée.",
  {"type":"axe","de":-6,"a":6,"depart":-5,"pas":8})
D("q125", ["On multiplie les numérateurs entre eux : 2 × 9 = 18.", "On multiplie les dénominateurs entre eux : 3 × 4 = 12.", "18/12 se simplifie par 6 : 3/2."],
  "a/b × c/d = (a × c)/(b × d). Simplifier avant de multiplier rend les calculs plus faciles.")
D("q126", ["On cherche un diviseur commun à 18 et 24 : 6 marche (18 = 6 × 3 et 24 = 6 × 4).", "On divise le haut et le bas par 6 : 18/24 = 3/4.", "3 et 4 n'ont plus de diviseur commun : la fraction est irréductible."],
  "Simplifier une fraction, c'est diviser le numérateur et le dénominateur par le même nombre.",
  {"type":"fraction","parts":[[18,24],[3,4]]})
D("q127", ["2⁵ signifie 2 multiplié 5 fois par lui-même.", "2 × 2 = 4, × 2 = 8, × 2 = 16, × 2 = 32."],
  "aⁿ = a × a × … × a (n facteurs). Ne pas confondre avec a × n.")
D("q128", ["L'écriture scientifique est a × 10ⁿ avec a entre 1 et 10 (10 exclu).", "On déplace la virgule de 45 000 pour obtenir 4,5 : elle recule de 4 rangs.", "45 000 = 4,5 × 10⁴."],
  "Grand nombre : exposant positif. Petit nombre (moins de 1) : exposant négatif.")
D("q129", ["On veut a entre 1 et 10 : ici a = 3.", "Pour passer de 0,003 à 3, la virgule avance de 3 rangs vers la droite.", "0,003 = 3 × 10⁻³."],
  "10⁻¹ = 0,1 ; 10⁻² = 0,01 ; 10⁻³ = 0,001.")
D("q130", ["(−2)⁴ = (−2) × (−2) × (−2) × (−2).", "(−2) × (−2) = 4, puis 4 × 4 = 16.", "4 facteurs négatifs, un nombre pair : le résultat est positif."],
  "Attention : (−2)⁴ = 16 mais −2⁴ = −16, car sans parenthèses la puissance ne porte que sur 2.")
D("q131", ["Pour diviser des puissances de 10, on soustrait les exposants.", "6 − 2 = 4, donc 10⁶ ÷ 10² = 10⁴ = 10 000.", "Vérification : 1 000 000 ÷ 100 = 10 000."],
  "10ᵃ ÷ 10ᵇ = 10ᵃ⁻ᵇ.")
D("q132", ["Les préfixes vont de 1 000 en 1 000.", "kilo = 10³ (mille), méga = 10⁶ (million), giga = 10⁹ (milliard), téra = 10¹²."],
  "Petits préfixes : milli = 10⁻³, micro = 10⁻⁶, nano = 10⁻⁹.",
  {"type":"table","head":["kilo","méga","giga","téra"],"rows":[["10³","10⁶","!10⁹","10¹²"]]})
D("q133", ["On cherche les paires de nombres dont le produit fait 12.", "1 × 12, 2 × 6, 3 × 4.", "Diviseurs : 1, 2, 3, 4, 6, 12, soit 6 diviseurs."],
  "On trouve les diviseurs par paires, en s'arrêtant quand les deux nombres se croisent.")
D("q134", ["Critère : un nombre est divisible par 9 si la somme de ses chiffres est divisible par 9.", "728 : 17 ; 738 : 18 ; 745 : 16 ; 812 : 11.", "Seul 738 convient : 738 = 9 × 82."],
  "Divisible par 3 ou 9 : somme des chiffres divisible par 3 ou 9. Par 5 : se termine par 0 ou 5.")
D("q135", ["35 = 5 × 7.", "24 = 2 × 2 × 2 × 3.", "Aucun facteur premier en commun : PGCD = 1. On dit que 35 et 24 sont premiers entre eux."],
  "Si le PGCD du numérateur et du dénominateur vaut 1, la fraction est irréductible.")
D("q136", ["On veut les x d'un seul côté : on enlève 2x des deux côtés. −7 = x + 1.", "On enlève 1 des deux côtés : −8 = x.", "Vérification : 2 × (−8) − 7 = −23 et 3 × (−8) + 1 = −23."],
  "On regroupe les x d'un côté et les nombres de l'autre, en faisant la même opération des deux côtés.")
D("q137", ["On applique (a + b)² = a² + 2ab + b² avec a = 2x et b = 1.", "a² = (2x)² = 4x² ; 2ab = 2 × 2x × 1 = 4x ; b² = 1.", "(2x + 1)² = 4x² + 4x + 1."],
  "Erreur à éviter : (a + b)² n'est pas a² + b², il manque le double produit 2ab.",
  {"type":"table","head":["×","2x","1"],"rows":[["2x","4x²","2x"],["1","2x","1"]]})
D("q138", ["Une fonction linéaire est de la forme f(x) = ax, sans nombre ajouté.", "Exemple : f(x) = 3x.", "Elle traduit une situation de proportionnalité, et sa droite passe par l'origine."],
  "Linéaire : f(x) = ax. Affine : f(x) = ax + b. Une fonction linéaire est une fonction affine avec b = 0.",
  {"type":"droite","a":1.5,"b":0,"label":"f(x) = 1,5x passe par (0 ; 0)"})
D("q139", ["Une fonction affine s'écrit f(x) = ax + b.", "Quand x augmente de 1, f(x) augmente toujours de a : la « pente » est constante.", "Sa représentation graphique est donc une droite."],
  "a est le coefficient directeur (la pente), b l'ordonnée à l'origine (où la droite coupe l'axe vertical).",
  {"type":"droite","a":0.5,"b":2,"label":"f(x) = 0,5x + 2"})
D("q140", ["On écrit f(x) sous la forme ax + b : f(x) = −2x + 5.", "a = −2 est le coefficient directeur, b = 5 l'ordonnée à l'origine.", "a est négatif : la droite descend."],
  "a > 0 : la droite monte. a < 0 : elle descend. b : la droite coupe l'axe des ordonnées en (0 ; b).",
  {"type":"droite","a":-2,"b":5,"point":[0,5],"label":"f(x) = −2x + 5"})
D("q141", ["On remplace x par −3 avec des parenthèses : g(−3) = (−3)² − 1.", "(−3)² = (−3) × (−3) = 9.", "g(−3) = 9 − 1 = 8."],
  "Toujours mettre des parenthèses autour d'un nombre négatif qu'on remplace dans une expression.")
D("q142", ["Échelle 1/25 000 : 1 cm sur la carte représente 25 000 cm en vrai.", "4 cm représentent 4 × 25 000 = 100 000 cm.", "100 000 cm = 1 000 m = 1 km."],
  "Distance réelle = distance sur la carte × dénominateur de l'échelle, puis on convertit.",
  {"type":"table","head":["Carte","Réalité"],"rows":[["1 cm","25 000 cm"],["4 cm","!100 000 cm = 1 km"]]})
D("q143", ["Hausse = 50 − 40 = 10 €.", "On compare la hausse au prix de départ : 10 ÷ 40 = 0,25.", "0,25 = 25 %."],
  "Taux d'évolution = (valeur d'arrivée − valeur de départ) ÷ valeur de départ.")
D("q144", ["On cherche le coefficient de proportionnalité : 6 ÷ 2 = 3.", "On multiplie : 5 × 3 = 15."],
  "Dans un tableau de proportionnalité, on passe d'une ligne à l'autre en multipliant toujours par le même nombre.",
  {"type":"table","rows":[["2","5"],["6","!15"]]})
D("q145", ["Plus grande valeur : 15. Plus petite valeur : 4.", "Étendue = 15 − 4 = 11."],
  "L'étendue mesure la dispersion : l'écart entre la plus grande et la plus petite valeur.",
  {"type":"barres","vals":[4,9,12,7,15],"hl":[0,4],"legende":"Étendue = 15 − 4"})
D("q146", ["Un événement certain se produit à coup sûr, par exemple « obtenir un nombre entre 1 et 6 » avec un dé.", "Sa probabilité vaut 1.", "Un événement impossible a une probabilité de 0."],
  "Une probabilité est toujours comprise entre 0 et 1.")
D("q147", ["Aire d'un disque = π × r².", "r² = 5 × 5 = 25.", "A = 25π cm² ≈ 78,5 cm²."],
  "Aire du disque : π × r². Périmètre du cercle : 2 × π × r (ou π × d).",
  {"type":"cercle","r":"5 cm","disque":True})
D("q148", ["Périmètre d'un cercle = π × diamètre.", "P = π × 10 = 10π cm ≈ 31,4 cm."],
  "Périmètre = π × d = 2 × π × r. Le diamètre est le double du rayon.",
  {"type":"cercle","d":"10 cm"})
D("q149", ["Aire d'un triangle = base × hauteur ÷ 2.", "8 × 5 = 40.", "40 ÷ 2 = 20 cm²."],
  "La hauteur est perpendiculaire à la base et passe par le sommet opposé.",
  {"type":"tri_hauteur","b":"8 cm","h":"5 cm"})
D("q150", ["Le périmètre est la longueur du tour : 7 + 3 + 7 + 3.", "= 2 × (7 + 3) = 20 cm.", "Ne pas confondre avec l'aire : 7 × 3 = 21 cm²."],
  "Périmètre : une longueur (cm). Aire : une surface (cm²).",
  {"type":"rect","w":"7 cm","h":"3 cm"})
D("q151", ["1 m = 100 cm.", "Un carré de 1 m de côté mesure 100 cm × 100 cm.", "Son aire vaut 10 000 cm²."],
  "Pour les aires, on multiplie par 100 à chaque unité : 1 m² = 100 dm² = 10 000 cm².",
  {"type":"rect","w":"100 cm","h":"100 cm"})
D("q152", ["Volume d'un cube = arête × arête × arête.", "4 × 4 × 4 = 64 cm³."],
  "Pour les volumes, on multiplie par 1 000 à chaque unité : 1 dm³ = 1 000 cm³.",
  {"type":"solide","k":"cube","labels":{"L":"4 cm","l":"4 cm","h":"4 cm"}})
D("q153", ["Volume d'une pyramide = aire de la base × hauteur ÷ 3.", "30 × 10 = 300.", "300 ÷ 3 = 100 cm³."],
  "Pyramide et cône : on divise par 3. Prisme et cylindre : on ne divise pas.",
  {"type":"solide","k":"pyramide","labels":{"h":"10 cm","base":"aire de base : 30 cm²"}})
D("q154", ["La base d'un cône est un disque d'aire π × r².", "Comme pour une pyramide, on multiplie par la hauteur et on divise par 3.", "V = π × r² × h ÷ 3."],
  "Un cône « remplit » un tiers du cylindre de même base et même hauteur.",
  {"type":"solide","k":"cone","labels":{"r":"r","h":"h"}})
D("q155", ["Volume d'une boule = 4/3 × π × r³.", "r³ = 3 × 3 × 3 = 27.", "V = 4/3 × 27 × π = 36π cm³ ≈ 113 cm³."],
  "Boule : V = 4/3 × π × r³. Sphère : aire = 4 × π × r².",
  {"type":"solide","k":"boule","labels":{"r":"r = 3 cm"}})
D("q156", ["1 m³ = 1 000 dm³ (car 10 × 10 × 10).", "1 dm³ = 1 L.", "Donc 1 m³ = 1 000 L."],
  "1 m³ = 1 000 L ; 1 dm³ = 1 L ; 1 cm³ = 1 mL.")
D("q157", ["90 km/h : 90 km en 1 heure, soit 90 000 m en 3 600 s.", "90 000 ÷ 3 600 = 25 m/s."],
  "Astuce : pour passer de km/h à m/s, on divise par 3,6. Pour l'inverse, on multiplie par 3,6.")
D("q158", ["On convertit la durée en heures : 2 h 30 min = 2,5 h.", "d = v × t = 60 × 2,5 = 150 km."],
  "Les trois formules : v = d ÷ t ; d = v × t ; t = d ÷ v.")
D("q159", ["Le débit est un volume par unité de temps.", "60 L ÷ 5 min = 12 L/min."],
  "Débit = volume ÷ durée. Unité : L/min, m³/h…")
D("q160", ["La masse volumique est la masse d'une unité de volume : ρ = m ÷ V.", "200 g ÷ 250 cm³ = 0,8 g/cm³.", "C'est moins que l'eau (1 g/cm³) : l'objet flotte."],
  "ρ = m ÷ V. Un objet flotte sur l'eau si sa masse volumique est inférieure à 1 g/cm³.")
D("q161", ["L'angle étudié est B.", "Le côté opposé à B est celui qui ne touche pas B : AC.", "L'hypoténuse est BC. Donc sin(B) = AC / BC."],
  "SOH : Sinus = Opposé / Hypoténuse.",
  {"type":"tri_rect","pts":["A","B","C"],"cotes":{"AC":"opposé à B","BC":"hypoténuse"},"angle":"B"})
D("q162", ["Dans tout triangle, la somme des 3 angles fait 180°.", "Exemple : un triangle équilatéral a 3 angles de 60°, et 3 × 60 = 180.", "Dans un triangle rectangle, les deux angles aigus font donc 90° à eux deux."],
  "Somme des angles d'un triangle = 180°.")
D("q163", ["La translation fait glisser la figure : même direction, même sens, même longueur pour tous les points.", "La figure ne tourne pas et n'est pas retournée."],
  "Translation : glisser. Rotation : tourner. Symétrie axiale : retourner comme dans un miroir. Homothétie : agrandir ou réduire.",
  {"type":"transfo","k":"translation"})
D("q164", ["Rapport 0,5 : toutes les longueurs sont multipliées par 0,5, donc divisées par 2.", "0,5 est entre 0 et 1 : c'est une réduction.", "Les aires sont multipliées par 0,5² = 0,25."],
  "Homothétie de rapport k : longueurs × k. Si 0 < k < 1, c'est une réduction.",
  {"type":"transfo","k":"homothetie","r":0.5,"legende":"Rapport 0,5 : 2 fois plus petit"})
D("q165", ["Une rotation fait tourner la figure autour d'un point, sans la déformer.", "Les longueurs, les angles et les aires sont conservés."],
  "Translation, rotation et symétries conservent les longueurs, les angles et les aires. L'homothétie conserve seulement les angles.",
  {"type":"transfo","k":"rotation","legende":"Rotation de 90° autour de O"})
D("q166", ["La symétrie centrale de centre O envoie chaque point de l'autre côté de O, à la même distance.", "C'est exactement un demi-tour autour de O, soit une rotation de 180°."],
  "Symétrie centrale = rotation de 180° (demi-tour).",
  {"type":"transfo","k":"symetrie","legende":"Symétrie de centre O = demi-tour"})
D("q167", ["Un carré a 2 axes qui passent par les milieux des côtés opposés.", "Et 2 axes qui sont ses diagonales.", "Total : 4 axes de symétrie."],
  "Un rectangle (non carré) n'a que 2 axes, un losange aussi : ses diagonales.")
D("q168", ["Une variable est une « boîte » avec un nom, qui garde une valeur.", "Exemple : la variable score vaut 0 au départ, puis augmente de 1 à chaque bonne réponse.", "Sa valeur peut changer pendant que le programme tourne."],
  "Variable : stocke une valeur. Boucle : répète. Condition (si… alors) : choisit.")
D("q169", ["Le bloc « avancer de 20 pas » est répété 10 fois.", "Distance totale = 10 × 20 = 200 pas."],
  "Dans une boucle « répéter n fois », les instructions à l'intérieur s'exécutent n fois.")
D("q170", ["Une formule commence par =.", "La fonction SOMME additionne une plage de cellules.", "A1:A5 signifie « de A1 jusqu'à A5 ». Avec A1;A5, on n'additionnerait que A1 et A5."],
  "Plage de cellules : deux-points (A1:A5). Liste de cellules : point-virgule (A1;A5).",
  {"type":"table","head":["","A"],"rows":[["1","4"],["2","7"],["3","2"],["4","5"],["5","1"],["6","!=SOMME(A1:A5) → 19"]]})
