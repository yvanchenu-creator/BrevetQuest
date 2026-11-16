# Corrections détaillées des questions de sciences.
def D(i, etapes, retenir, schema=None):
  DETAILS[i] = {"etapes": etapes, "retenir": retenir}
  if schema: DETAILS[i]["schema"] = schema

D("q091", ["On repère les données : d = 150 m et t = 30 s.", "On applique v = d ÷ t = 150 ÷ 30.", "v = 5 m/s : le cycliste parcourt 5 mètres chaque seconde."],
  "v = d ÷ t. Avec des mètres et des secondes, la vitesse est en m/s.",
  {"type":"table","head":["Temps (s)","1","10","30"],"rows":[["Distance (m)","5","50","!150"]]})
D("q092", ["Pour l'eau, 1 L a une masse de 1 kg : sa masse volumique est 1 kg/L.", "C'est aussi 1 g/mL ou 1 g/cm³."],
  "Masse volumique de l'eau : ρ = 1 kg/L = 1 g/cm³. Un objet moins dense que l'eau flotte.")
D("q093", ["Loi d'Ohm : U = R × I, avec U en volts, R en ohms et I en ampères.", "U = 100 × 0,05.", "U = 5 V."],
  "Loi d'Ohm : U = R × I. Les intensités doivent être en ampères (50 mA = 0,05 A).",
  {"type":"table","head":["Grandeur","Symbole","Unité"],"rows":[["Tension","U","volt (V)"],["Résistance","R","ohm (Ω)"],["Intensité","I","ampère (A)"]]})
D("q094", ["Puissance électrique : P = U × I.", "P = 230 × 2 = 460.", "P = 460 W."],
  "P = U × I, en watts (W). Plus la puissance est grande, plus l'appareil consomme vite de l'énergie.")
D("q095", ["Énergie = puissance × durée : E = P × t.", "Avec P en kW et t en h : 1 000 W = 1 kW, donc E = 1 × 2 = 2 kWh.", "En wattheures : 1 000 × 2 = 2 000 Wh = 2 kWh."],
  "E = P × t. En kW et en heures, l'énergie est en kWh, l'unité de la facture d'électricité.")
D("q096", ["La lumière est ce qu'il y a de plus rapide dans l'univers.", "Dans le vide (ou l'air), elle parcourt environ 300 000 km chaque seconde.", "Le son, lui, ne va qu'à environ 340 m/s dans l'air."],
  "Lumière : 300 000 km/s. Son dans l'air : 340 m/s. C'est pour ça qu'on voit l'éclair avant d'entendre le tonnerre.")
D("q097", ["Le son est une vibration qui se transmet de proche en proche dans la matière (air, eau, solide).", "Dans le vide, il n'y a pas de matière à faire vibrer.", "Le son ne peut donc pas s'y propager : dans l'espace, une explosion serait silencieuse."],
  "Le son a besoin d'un milieu matériel. La lumière, non : elle traverse le vide.")
D("q098", ["L'échelle de pH va de 0 à 14.", "pH < 7 : acide. pH = 7 : neutre. pH > 7 : basique.", "3 est inférieur à 7 : la solution est acide (comme le jus de citron)."],
  "Plus le pH est petit, plus la solution est acide.",
  {"type":"table","head":["pH 0 à 7","pH 7","pH 7 à 14"],"rows":[["!acide","neutre","basique"],["citron, vinaigre","eau pure","savon, eau de Javel"]]})
D("q099", ["Un atome est neutre : autant de charges + (protons) que de charges − (électrons).", "Na⁺ a une charge positive en trop.", "Il a donc perdu un électron (négatif). Les protons, dans le noyau, ne bougent pas."],
  "Ion positif : l'atome a perdu des électrons. Ion négatif : il en a gagné.")
D("q100", ["Dans une transformation chimique, les atomes des réactifs se réarrangent pour former les produits.", "Aucun atome n'apparaît ni ne disparaît.", "La masse totale reste donc la même : c'est la conservation de la masse (Lavoisier)."],
  "« Rien ne se perd, rien ne se crée, tout se transforme. » La masse des réactifs = la masse des produits.")
D("q101", ["Le poids se calcule avec P = m × g.", "P = 50 × 9,8 = 490.", "P = 490 N. La masse (50 kg) ne change pas, le poids dépend de la planète."],
  "Poids P = m × g, en newtons (N). Masse en kg. Sur la Lune, g est environ 6 fois plus petit.")
D("q102", ["Dans un circuit en série, il n'y a qu'une seule boucle.", "Le courant qui sort de la pile traverse chaque dipôle l'un après l'autre.", "L'intensité est donc la même en tout point du circuit."],
  "Série : même intensité partout, les tensions s'additionnent. Dérivation : même tension, les intensités s'additionnent.",
  {"type":"circuit","k":"serie"})
D("q103", ["Énergie cinétique : Ec = ½ × m × v².", "La vitesse est au carré : si v est multipliée par 2, v² est multipliée par 2² = 4.", "L'énergie cinétique est donc multipliée par 4 : un choc à 100 km/h est 4 fois plus violent qu'à 50 km/h."],
  "Ec = ½ m v². Doubler la vitesse multiplie l'énergie (et la distance de freinage) par 4.",
  {"type":"barres","vals":[1,4,9],"legende":"Énergie cinétique pour une vitesse × 1, × 2, × 3"})
D("q104", ["Le noyau de chaque cellule du corps contient 46 chromosomes.", "Ils vont par paires : 23 paires.", "Une paire, les chromosomes sexuels, est XX chez la femme et XY chez l'homme."],
  "Cellule humaine : 46 chromosomes (23 paires). Gamète : 23 chromosomes.")
D("q105", ["Les gamètes (spermatozoïde, ovule) ne reçoivent qu'un chromosome de chaque paire.", "Ils ont donc 23 chromosomes, la moitié de 46.", "À la fécondation, 23 + 23 = 46 : le nombre normal est rétabli."],
  "Gamète : 23 chromosomes. Cellule-œuf : 23 + 23 = 46.")
D("q106", ["Un spermatozoïde (du père) rencontre un ovule (de la mère).", "Leurs noyaux fusionnent : ils forment une cellule-œuf.", "Cette cellule unique va se diviser des milliards de fois pour former un nouvel individu."],
  "Fécondation = fusion de deux gamètes → cellule-œuf, avec un mélange des informations des deux parents.")
D("q107", ["Les lymphocytes sont des globules blancs.", "Les lymphocytes B fabriquent des anticorps qui se fixent sur un microbe précis (son antigène) pour le neutraliser.", "Les lymphocytes T, eux, détruisent les cellules infectées."],
  "Lymphocytes B → anticorps. Lymphocytes T → destruction des cellules infectées. Phagocytes → « mangent » les microbes.")
D("q108", ["Les antibiotiques attaquent des éléments que seules les bactéries possèdent.", "Les virus sont très différents : ils se multiplient à l'intérieur de nos cellules.", "Un antibiotique ne sert donc à rien contre la grippe ou un rhume, qui sont des virus."],
  "« Les antibiotiques, c'est pas automatique » : efficaces contre les bactéries, inutiles contre les virus.")
D("q109", ["Le vaccin contient un microbe tué, affaibli, ou un morceau de microbe : il est inoffensif.", "Le système immunitaire réagit et fabrique des cellules mémoire.", "Si le vrai microbe arrive plus tard, la réponse est rapide et forte : on ne tombe pas malade."],
  "Vaccin = prévention, grâce à la mémoire immunitaire. Il ne soigne pas une maladie déjà déclarée.")
D("q110", ["Les feuilles captent l'énergie lumineuse grâce à la chlorophylle.", "Elles absorbent le dioxyde de carbone de l'air, et les racines puisent l'eau.", "La plante fabrique du glucose (matière organique) et rejette du dioxygène."],
  "Photosynthèse : CO₂ + eau + lumière → glucose + O₂.",
  {"type":"table","head":["La plante prend","La plante produit"],"rows":[["dioxyde de carbone (CO₂)","!glucose (sucre)"],["eau","!dioxygène (O₂)"],["lumière",""]]})
D("q111", ["Les végétaux chlorophylliens fabriquent leur matière avec la lumière : ils sont producteurs.", "Les herbivores les mangent, puis les carnivores mangent les herbivores : ce sont des consommateurs.", "Les décomposeurs recyclent les restes."],
  "Chaîne alimentaire : producteur → consommateur primaire → consommateur secondaire. La flèche veut dire « est mangé par ».",
  {"type":"table","rows":[["!herbe","→","lapin","→","renard"]]})
D("q112", ["L'effet de serre naturel garde une partie de la chaleur du Soleil : sans lui, il ferait −18 °C sur Terre.", "En brûlant pétrole, charbon et gaz, les humains rejettent beaucoup de CO₂.", "Ce CO₂ renforce l'effet de serre et réchauffe le climat."],
  "Le CO₂ (dioxyde de carbone) est le principal gaz à effet de serre rejeté par les activités humaines.")
D("q113", ["Une énergie renouvelable se reconstitue rapidement à l'échelle humaine.", "Le soleil, le vent, l'eau des rivières sont renouvelables.", "Charbon, pétrole et gaz ont mis des millions d'années à se former : ce sont des énergies fossiles, épuisables."],
  "Renouvelables : solaire, éolien, hydraulique, géothermie, biomasse. Non renouvelables : fossiles et nucléaire.")
D("q114", ["Les plaques de la Terre bougent lentement et exercent des forces sur les roches.", "Les roches se déforment jusqu'à se casser brutalement le long d'une faille.", "L'énergie libérée se propage sous forme d'ondes sismiques : le sol tremble."],
  "Séisme = rupture brutale de roches le long d'une faille. Le foyer est en profondeur, l'épicentre juste au-dessus en surface.")
D("q115", ["Charles Darwin observe que les individus d'une espèce sont tous un peu différents.", "Ceux qui ont des caractères avantageux dans leur milieu survivent et se reproduisent davantage.", "Au fil des générations, ces caractères deviennent plus fréquents : c'est la sélection naturelle (1859)."],
  "Évolution : variations entre individus + sélection naturelle par le milieu, sur de nombreuses générations.")
D("q116", ["Un actionneur agit sur le monde réel : il produit un mouvement, de la lumière, du son…", "Le moteur transforme l'énergie électrique en mouvement : c'est un actionneur.", "Un capteur, à l'inverse, prélève une information (température, présence…)."],
  "Capteur : il mesure, il prélève une information. Actionneur : il agit (moteur, lampe, buzzer).")
D("q117", ["Un bit est la plus petite information : 0 ou 1.", "Un octet regroupe 8 bits.", "Avec 8 bits, on peut coder 2⁸ = 256 valeurs différentes."],
  "1 octet = 8 bits. 1 ko ≈ 1 000 octets, 1 Mo ≈ 1 million, 1 Go ≈ 1 milliard.")
D("q118", ["Un détecteur de mouvement prélève une information : quelqu'un est-il là ?", "Il fait donc partie de la chaîne d'information (acquérir, traiter, communiquer).", "La chaîne d'énergie, elle, alimente, distribue, convertit et transmet l'énergie (moteur, lampe…)."],
  "Chaîne d'information : capteur → microcontrôleur → message. Chaîne d'énergie : alimentation → actionneur.",
  {"type":"table","head":["Acquérir","Traiter","Communiquer"],"rows":[["!capteur","microcontrôleur","ordre à l'actionneur"]]})
D("q119", ["« Si… alors… » teste une condition.", "Si la température est supérieure à 25, le ventilateur s'allume. Sinon, il ne se passe rien.", "C'est une instruction conditionnelle."],
  "Structures d'un programme : séquence (à la suite), boucle (répéter), condition (si… alors… sinon).")
D("q120", ["Le sang passe dans les reins, qui le filtrent.", "Les déchets (comme l'urée) et l'eau en trop forment l'urine.", "L'urine est stockée dans la vessie puis éliminée."],
  "Les reins filtrent le sang et produisent l'urine. Les poumons, eux, rejettent le CO₂.")
D("q196", ["Une force modélise une action (pousser, tirer, attirer).", "Son unité est le newton, noté N, en hommage à Isaac Newton.", "On la mesure avec un dynamomètre."],
  "Force et poids : newton (N). Masse : kilogramme (kg). Énergie : joule (J). Puissance : watt (W).")
D("q197", ["En hauteur, l'objet possède une énergie de position.", "En tombant, il perd de l'altitude et gagne de la vitesse.", "L'énergie de position se transforme donc en énergie cinétique (énergie de mouvement)."],
  "Pendant une chute : énergie de position ↓, énergie cinétique ↑. Leur somme reste à peu près constante.",
  {"type":"barres","vals":[10,6,2],"legende":"Énergie de position au cours de la chute"})
D("q198", ["L'intensité du courant se mesure en ampères (A).", "L'appareil s'appelle donc un ampèremètre.", "Il se branche en série, dans la boucle, alors que le voltmètre se branche en dérivation."],
  "Ampèremètre : intensité, en série. Voltmètre : tension, en dérivation.")
D("q199", ["Dans un circuit en dérivation, chaque branche est reliée directement aux bornes de la pile.", "Chaque lampe reçoit donc la même tension.", "Si une lampe grille, les autres continuent de briller : c'est le montage des maisons."],
  "Dérivation : même tension aux bornes de chaque branche, et les intensités des branches s'additionnent.",
  {"type":"circuit","k":"derivation"})
D("q200", ["Un court-circuit relie directement les deux bornes de la pile ou de la prise, sans rien entre elles.", "Rien ne limite le courant : son intensité devient très grande.", "Les fils chauffent fortement : risque de brûlure ou d'incendie. Les fusibles et disjoncteurs coupent alors le courant."],
  "Court-circuit = courant très intense = danger. Fusibles et disjoncteurs protègent les installations.")
D("q201", ["Une molécule d'eau est formée de 2 atomes d'hydrogène (H) et 1 atome d'oxygène (O).", "On l'écrit H₂O : le petit 2 indique deux atomes d'hydrogène."],
  "Formules à connaître : H₂O (eau), CO₂ (dioxyde de carbone), O₂ (dioxygène), N₂ (diazote).")
D("q202", ["Lors de la combustion, le carbone (C) réagit avec le dioxygène (O₂).", "Il se forme du dioxyde de carbone : C + O₂ → CO₂.", "On le reconnaît car il trouble l'eau de chaux."],
  "Combustion du carbone : C + O₂ → CO₂. Test du CO₂ : l'eau de chaux se trouble.")
D("q203", ["Le son se propage dans l'air à environ 340 m/s.", "Il va plus vite dans l'eau (environ 1 500 m/s) et dans les solides.", "Astuce : en comptant les secondes entre l'éclair et le tonnerre, on estime la distance de l'orage (environ 1 km toutes les 3 s)."],
  "Son dans l'air : 340 m/s, soit environ 1 km en 3 s.")
D("q204", ["L'oreille humaine entend les sons de 20 Hz à 20 000 Hz.", "Au-dessous de 20 Hz : infrasons. Au-dessus de 20 000 Hz : ultrasons.", "Les chauves-souris et l'échographie utilisent les ultrasons."],
  "Fréquence en hertz (Hz) : plus elle est grande, plus le son est aigu.",
  {"type":"table","head":["< 20 Hz","20 à 20 000 Hz","> 20 000 Hz"],"rows":[["infrasons","sons audibles","!ultrasons"]]})
D("q205", ["Le Soleil est à environ 150 millions de km de la Terre.", "La lumière va à 300 000 km/s : t = d ÷ v = 150 000 000 ÷ 300 000 = 500 s.", "500 s, c'est environ 8 minutes et 20 secondes."],
  "t = d ÷ v. Quand on regarde le Soleil, on le voit tel qu'il était il y a 8 minutes.")
D("q206", ["Une année-lumière est la distance que parcourt la lumière en une année.", "Malgré son nom, ce n'est pas une durée mais une distance.", "Elle vaut environ 9 500 milliards de km : on l'utilise pour les distances entre étoiles."],
  "Année-lumière (al) = une distance, environ 9 500 milliards de km.")
D("q207", ["Les globules rouges contiennent de l'hémoglobine, qui fixe le dioxygène.", "Ils prennent le dioxygène dans les poumons et le transportent jusqu'aux organes.", "Les globules blancs, eux, défendent l'organisme contre les microbes."],
  "Globules rouges : transport du O₂. Globules blancs : défense. Plaquettes : coagulation.")
D("q208", ["La digestion découpe les aliments en petites molécules : les nutriments.", "Dans l'intestin grêle, ces nutriments traversent la paroi et passent dans le sang.", "La paroi est très repliée (villosités) : sa grande surface facilite le passage."],
  "Absorption des nutriments : dans l'intestin grêle. Le sang les distribue ensuite à toutes les cellules.")
D("q209", ["Les chromosomes sont faits d'une longue molécule : l'ADN.", "Un gène est une portion de cette molécule.", "Il porte une information qui détermine un caractère héréditaire (groupe sanguin, couleur des yeux…)."],
  "ADN → chromosomes → gènes. Les différentes versions d'un gène s'appellent des allèles.")
D("q210", ["Une seule cellule-œuf se forme après la fécondation.", "Très tôt, elle se sépare en deux groupes de cellules qui se développent chacun en un embryon.", "Les deux enfants ont exactement le même ADN : ce sont de vrais jumeaux. Les faux jumeaux viennent de deux ovules différents."],
  "Vrais jumeaux : 1 cellule-œuf, même ADN. Faux jumeaux : 2 ovules fécondés par 2 spermatozoïdes.")
D("q211", ["Un fossile est un reste (os, coquille) ou une trace (empreinte) d'un être vivant.", "Il s'est conservé dans une roche sédimentaire pendant des millions d'années.", "Les fossiles montrent que les espèces ont changé au cours du temps."],
  "Les fossiles sont des preuves de l'évolution des êtres vivants.")
D("q212", ["Le microcontrôleur est le « cerveau » de l'objet.", "Il reçoit les informations des capteurs, exécute le programme et décide.", "Il envoie ensuite des ordres aux actionneurs (moteur, lampe, buzzer)."],
  "Capteur → microcontrôleur (programme) → actionneur.",
  {"type":"table","rows":[["capteur","→","!microcontrôleur","→","actionneur"]]})
D("q213", ["Avant de fabriquer un objet, on écrit son cahier des charges.", "Il décrit le besoin (à quoi sert l'objet) et les contraintes (taille, coût, sécurité, énergie…).", "Il sert ensuite à vérifier que l'objet fabriqué convient."],
  "Cahier des charges = besoin + fonctions + contraintes.")
