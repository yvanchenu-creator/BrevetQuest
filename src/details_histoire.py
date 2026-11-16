# Corrections détaillées des questions d'histoire-géographie et d'EMC.
def D(i, etapes, retenir, schema=None):
  DETAILS[i] = {"etapes": etapes, "retenir": retenir}
  if schema: DETAILS[i]["schema"] = schema

G1 = [1914, 1918, "1re Guerre mondiale", "#FF6B9A"]
G2 = [1939, 1945, "2de Guerre mondiale", "#FF6B9A"]
GF = [1947, 1991, "Guerre froide", "#5B8CFF"]

def frise(de, a, ev, focus, periodes=()):
  return {"type":"frise","de":de,"a":a,"ev":ev,"focus":focus,"periodes":list(periodes)}

D("q061", ["Après 1945, le Royaume-Uni sort affaibli de la guerre, et le mouvement pour l'indépendance de l'Inde est très fort.", "Le Parti du Congrès, avec Gandhi et Nehru, obtient des négociations.", "L'Inde devient indépendante le 15 août 1947, au début de la guerre froide."],
  "1947 : indépendance de l'Inde, l'une des premières grandes décolonisations.",
  frise(1930, 1965, [[1930,"marche du sel"],[1947,"indépendance"],[1962,"Algérie"]], 1947))
D("q062", ["Gandhi refuse la violence.", "Il prône la désobéissance civile : boycott des produits britanniques, refus de payer certains impôts, marches pacifiques.", "Cette stratégie attire l'attention du monde entier et affaiblit l'autorité britannique."],
  "Gandhi = non-violence et désobéissance civile pour l'indépendance de l'Inde.")
D("q063", ["Les Britanniques avaient le monopole du sel : les Indiens devaient l'acheter et payer une taxe.", "En 1930, Gandhi marche plus de 300 km jusqu'à la mer avec des milliers de partisans.", "Là, il ramasse du sel lui-même : un geste simple et symbolique de désobéissance."],
  "Marche du sel (1930) : un symbole de la désobéissance civile non violente.",
  frise(1920, 1950, [[1920,"campagnes de Gandhi"],[1930,"marche du sel"],[1947,"indépendance"]], 1930))
D("q064", ["Les tensions entre hindous et musulmans sont fortes au moment de l'indépendance.", "En 1947, le territoire est partagé : l'Inde (majorité hindoue) et le Pakistan (majorité musulmane).", "Cette partition provoque environ 10 millions de réfugiés et des centaines de milliers de morts."],
  "1947 : partition entre Inde et Pakistan. Le conflit sur le Cachemire dure encore aujourd'hui.")
D("q065", ["Le droit de vote est accordé aux femmes par une ordonnance du 21 avril 1944, à la Libération.", "Elles votent pour la première fois aux élections municipales d'avril 1945.", "Avant, seuls les hommes votaient (suffrage « universel » masculin depuis 1848)."],
  "1944 : droit de vote des femmes. 1945 : premier vote.",
  frise(1935, 1980, [[1936,"Front populaire"],[1944,"droit de vote"],[1945,"1er vote"],[1975,"loi Veil"]], 1945, [G2]))
D("q066", ["La Première Guerre mondiale commence en 1914.", "L'armistice, c'est-à-dire l'arrêt des combats, est signé le 11 novembre 1918.", "La paix est signée ensuite en 1919 par le traité de Versailles. Le 11 novembre est un jour férié."],
  "1914-1918 : Première Guerre mondiale. 11 novembre 1918 : armistice.",
  frise(1912, 1921, [[1914,"début"],[1916,"Verdun"],[1918,"armistice"],[1919,"Versailles"]], 1918, [G1]))
D("q067", ["La guerre commence le 1er septembre 1939 avec l'invasion de la Pologne par l'Allemagne.", "Elle se termine en Europe le 8 mai 1945 (capitulation de l'Allemagne).", "En Asie, le Japon capitule le 2 septembre 1945, après les bombes atomiques."],
  "1939-1945 : Seconde Guerre mondiale. 8 mai 1945 : fin en Europe.",
  frise(1936, 1948, [[1939,"Pologne"],[1940,"défaite française"],[1944,"débarquement"],[1945,"fin"]], 1945, [G2]))
D("q068", ["Les nazis ont voulu exterminer les Juifs d'Europe.", "Environ 6 millions de Juifs sont assassinés, notamment dans les centres de mise à mort comme Auschwitz-Birkenau.", "On appelle ce génocide la Shoah (« catastrophe » en hébreu). Les Tsiganes ont aussi été victimes d'un génocide."],
  "Génocide : extermination volontaire et organisée d'un peuple. Shoah : génocide des Juifs par les nazis.")
D("q069", ["En février 1917, le tsar Nicolas II abdique.", "En octobre 1917, Lénine et les bolcheviks prennent le pouvoir par la force.", "Ils créent ensuite l'URSS (1922), un régime communiste."],
  "1917 : révolutions russes. Lénine puis Staline installent un régime totalitaire.",
  frise(1910, 1945, [[1917,"révolution russe"],[1922,"URSS"],[1933,"Hitler"]], 1917, [G1, G2]))
D("q070", ["En juin 1940, la France est battue par l'Allemagne.", "Le maréchal Pétain signe l'armistice et obtient les pleins pouvoirs en juillet 1940.", "Son régime, installé à Vichy, collabore avec l'Allemagne nazie et participe à la déportation des Juifs."],
  "Régime de Vichy (1940-1944) : Pétain, fin de la République, collaboration.")
D("q071", ["Le 18 juin 1940, le général de Gaulle est à Londres.", "À la radio BBC, il appelle les Français à refuser la défaite et à continuer le combat.", "C'est le début de la France libre."],
  "18 juin 1940 : appel du général de Gaulle, naissance de la France libre.",
  frise(1938, 1946, [[1940,"appel du 18 juin"],[1943,"CNR"],[1944,"Libération"]], 1940, [G2]))
D("q072", ["En 1958, la IVe République est en crise à cause de la guerre d'Algérie.", "Le général de Gaulle revient au pouvoir.", "Une nouvelle Constitution, adoptée par référendum en 1958, fonde la Ve République, avec un président fort."],
  "1958 : Ve République. Depuis 1962, le président est élu au suffrage universel direct.",
  frise(1944, 1970, [[1946,"IVe République"],[1954,"guerre d'Algérie"],[1958,"Ve République"],[1962,"élection directe"]], 1958))
D("q073", ["En 1961, la RDA construit un mur pour empêcher les Berlinois de l'Est de fuir à l'Ouest.", "Le 9 novembre 1989, le mur tombe sous la pression des habitants.", "L'Allemagne est réunifiée en 1990 et l'URSS disparaît en 1991 : fin de la guerre froide."],
  "Mur de Berlin : 1961-1989. Symbole de la guerre froide.",
  frise(1945, 1995, [[1947,"début"],[1961,"construction du mur"],[1989,"chute du mur"],[1991,"fin de l'URSS"]], 1989, [GF]))
D("q074", ["Après 1945, deux superpuissances dominent le monde.", "Les États-Unis (capitalisme, démocratie) et l'URSS (communisme, parti unique).", "Elles s'opposent sans guerre directe, par des crises (Berlin, Cuba) et des guerres indirectes (Corée, Vietnam)."],
  "Guerre froide (1947-1991) : affrontement indirect entre les États-Unis et l'URSS.",
  frise(1945, 1995, [[1948,"blocus de Berlin"],[1962,"crise de Cuba"],[1989,"chute du mur"],[1991,"fin de l'URSS"]], 1962, [GF]))
D("q075", ["Le 1er novembre 1954, des attentats du FLN marquent le début de la guerre.", "La guerre dure huit ans et fait des centaines de milliers de morts.", "Les accords d'Évian (mars 1962) mènent à l'indépendance de l'Algérie en juillet 1962."],
  "Guerre d'Algérie : 1954-1962. Elle provoque la fin de la IVe République en 1958.",
  frise(1950, 1965, [[1954,"début de la guerre"],[1958,"Ve République"],[1962,"indépendance"]], 1962, [[1954,1962,"guerre d'Algérie","#FFA94D"]]))
D("q076", ["En 1957, six pays signent le traité de Rome : France, RFA, Italie, Belgique, Pays-Bas, Luxembourg.", "Il crée la Communauté économique européenne (CEE), un marché commun.", "La CEE deviendra l'Union européenne en 1992 (traité de Maastricht)."],
  "1957 : traité de Rome (CEE, 6 pays). 1992 : Maastricht (Union européenne). 2002 : l'euro.",
  frise(1950, 2025, [[1957,"traité de Rome"],[1992,"Maastricht"],[2002,"euro"],[2020,"Brexit"]], 1957))
D("q077", ["Simone Veil est ministre de la Santé.", "En 1975, elle fait voter une loi qui légalise l'interruption volontaire de grossesse (IVG).", "Elle défend ce texte malgré des attaques très violentes à l'Assemblée."],
  "Loi Veil (1975) : légalisation de l'IVG, une étape importante pour les droits des femmes.")
D("q078", ["En 1936, le Front populaire (une alliance de gauche dirigée par Léon Blum) gagne les élections.", "Après de grandes grèves, les accords de Matignon accordent des avancées sociales.", "Deux semaines de congés payés et la semaine de 40 heures."],
  "1936 : Front populaire, congés payés et semaine de 40 heures.",
  frise(1918, 1945, [[1929,"crise économique"],[1933,"Hitler"],[1936,"Front populaire"]], 1936, [G2]))
D("q079", ["« Giga » signifie géant. Une gigafactory est une usine immense.", "Dans les Hauts-de-France, la « vallée de la batterie » produit des batteries pour voitures électriques.", "Ces usines créent des milliers d'emplois dans une ancienne région industrielle."],
  "Gigafactory : usine géante, souvent de batteries électriques, symbole de la réindustrialisation.")
D("q080", ["Un espace productif est un espace aménagé pour produire des richesses.", "Il peut être industriel (usines), agricole (champs) ou de services (bureaux, commerces, tourisme).", "Une zone d'usines et d'entrepôts est un espace productif industriel."],
  "Les espaces productifs : industriels, agricoles, de services. Ils sont reliés par des réseaux de transport.")
D("q081", ["Les grandes villes attirent de plus en plus d'habitants et d'activités.", "Elles concentrent les emplois, les universités, les sièges d'entreprises, les fonctions de commandement.", "Ce mouvement s'appelle la métropolisation. Paris est la principale métropole française."],
  "Métropolisation : concentration de la population, des activités et des pouvoirs dans les grandes villes.")
D("q082", ["Les 5 DROM (départements et régions d'outre-mer) sont : Guadeloupe, Martinique, Guyane, La Réunion, Mayotte.", "La Nouvelle-Calédonie n'en fait pas partie.", "Elle a un statut particulier, avec une large autonomie."],
  "5 DROM : Guadeloupe, Martinique, Guyane, La Réunion, Mayotte.",
  {"type":"table","head":["DROM","Océan / continent"],"rows":[["Guadeloupe","Antilles (Atlantique)"],["Martinique","Antilles (Atlantique)"],["Guyane","Amérique du Sud"],["La Réunion","océan Indien"],["Mayotte","océan Indien"]]})
D("q083", ["La ZEE (zone économique exclusive) est l'espace maritime où un pays exploite seul les ressources (pêche, pétrole…).", "Grâce à ses territoires dans tous les océans, la France a environ 10 millions de km² de ZEE.", "C'est la 2e du monde, après les États-Unis."],
  "ZEE : jusqu'à 370 km (200 milles marins) des côtes. Celle de la France est la 2e du monde grâce à l'outre-mer.")
D("q084", ["Les Hauts-de-France sont proches du Royaume-Uni, de la Belgique et de l'Allemagne : une situation de carrefour.", "La région a déjà des usines automobiles et une main-d'œuvre formée.", "Les pouvoirs publics y investissent beaucoup pour réindustrialiser une ancienne région minière et textile."],
  "Pour expliquer une localisation : situation, main-d'œuvre, transports, aides publiques, héritage industriel.")
D("q085", ["La devise de la République est « Liberté, Égalité, Fraternité ».", "Elle vient de la Révolution française et est inscrite dans la Constitution de 1958.", "« Travail, Famille, Patrie » était la devise du régime de Vichy."],
  "Symboles de la République : la devise, le drapeau tricolore, La Marseillaise, Marianne, le 14 Juillet.")
D("q086", ["La loi du 9 décembre 1905 sépare les Églises et l'État.", "L'État ne reconnaît et ne finance aucune religion, et garantit la liberté de croire ou de ne pas croire.", "C'est le fondement de la laïcité."],
  "Laïcité : neutralité de l'État, liberté de conscience, égalité de tous quelle que soit la religion.",
  frise(1880, 1960, [[1882,"école laïque (Ferry)"],[1905,"loi de séparation"],[1958,"Constitution"]], 1905))
D("q087", ["En France, on devient majeur à 18 ans.", "On peut alors voter à toutes les élections.", "La majorité est passée de 21 à 18 ans en 1974."],
  "Droit de vote à 18 ans depuis 1974. L'inscription sur les listes électorales est automatique à 18 ans.")
D("q088", ["Le 26 août 1789, pendant la Révolution, les députés adoptent la Déclaration des droits de l'homme et du citoyen.", "Son article 1er dit : « Les hommes naissent et demeurent libres et égaux en droits. »", "Elle fait toujours partie de nos textes fondamentaux."],
  "DDHC (1789) : libertés et égalité des droits, toujours en vigueur.")
D("q089", ["Le préambule de la Constitution de 1946, repris en 1958, l'affirme.", "« La loi garantit à la femme, dans tous les domaines, des droits égaux à ceux de l'homme. »", "L'égalité femmes-hommes est donc une valeur de la République, même si des inégalités existent encore (salaires…)."],
  "L'égalité entre les femmes et les hommes est inscrite dans la Constitution.")
D("q090", ["La Ve République est fondée en 1958.", "Charles de Gaulle est élu président en décembre 1958 et prend ses fonctions en janvier 1959.", "Il reste président jusqu'en 1969."],
  "De Gaulle : chef de la France libre (1940), fondateur et 1er président de la Ve République (1958-1969).",
  frise(1955, 1975, [[1958,"Ve République"],[1962,"élection directe"],[1969,"démission"]], 1958))
D("q183", ["En 1914, les armées avancent vite : c'est la guerre de mouvement.", "Fin 1914, le front se bloque. Les soldats creusent des tranchées pour se protéger.", "De 1915 à 1917, c'est la guerre de position, avec des batailles terribles comme Verdun (1916)."],
  "1914 : guerre de mouvement. 1915-1917 : guerre de position (tranchées). 1918 : retour du mouvement et victoire alliée.",
  frise(1913, 1919, [[1914,"mouvement"],[1916,"Verdun"],[1918,"armistice"]], 1916, [[1915,1917.9,"guerre de position","#FFA94D"]]))
D("q184", ["Après la mort de Lénine (1924), Staline prend le pouvoir en URSS.", "Il impose un régime totalitaire : parti unique, culte du chef, propagande, terreur.", "Des millions de personnes sont envoyées dans les camps du goulag."],
  "Régime totalitaire : un chef, un parti unique, la propagande et la terreur contrôlent toute la société.")
D("q185", ["L'Allemagne est frappée par la crise économique de 1929.", "Hitler est nommé chancelier en janvier 1933.", "Il supprime très vite les libertés et installe une dictature nazie."],
  "1933 : Hitler au pouvoir. 1939 : il envahit la Pologne, début de la Seconde Guerre mondiale.",
  frise(1918, 1945, [[1919,"Versailles"],[1929,"crise"],[1933,"Hitler chancelier"],[1939,"guerre"]], 1933, [G2]))
D("q186", ["Le 6 juin 1944, les Alliés débarquent sur les plages de Normandie : c'est le D-Day.", "Ils ouvrent un nouveau front à l'ouest contre l'Allemagne.", "Paris est libéré le 25 août 1944."],
  "6 juin 1944 : débarquement en Normandie. 25 août 1944 : libération de Paris.",
  frise(1939, 1946, [[1940,"défaite"],[1942,"Stalingrad"],[1944,"débarquement"],[1945,"capitulation"]], 1944, [G2]))
D("q187", ["La Résistance intérieure est divisée en plusieurs mouvements.", "De Gaulle charge Jean Moulin de les unifier.", "En 1943, Jean Moulin crée le Conseil national de la Résistance (CNR). Il est arrêté et meurt sous la torture la même année."],
  "Jean Moulin : unificateur de la Résistance, créateur du CNR (1943).")
D("q188", ["Le programme du CNR prévoyait de protéger tous les Français.", "En 1945, la Sécurité sociale est créée.", "Elle rembourse les soins et verse des pensions de retraite et des allocations familiales."],
  "1945 : Sécurité sociale, droit de vote des femmes : la France se reconstruit sur de nouvelles bases.")
D("q189", ["Beaucoup de citadins quittent le centre des villes, où les logements sont chers.", "Ils s'installent dans les communes autour, souvent en maison individuelle.", "La ville s'étend sur les campagnes : c'est la périurbanisation. Elle augmente l'usage de la voiture."],
  "Périurbanisation : extension de la ville vers les campagnes environnantes.")
D("q190", ["Une ville attire des travailleurs bien au-delà de ses limites.", "L'aire d'attraction regroupe le pôle (la ville et sa banlieue) et les communes autour.", "Une commune en fait partie si au moins 15 % de ses actifs travaillent dans le pôle."],
  "Aire d'attraction = pôle urbain + couronne, définie par les trajets domicile-travail.")
D("q191", ["La Guyane se trouve en Amérique du Sud, entre le Brésil et le Suriname.", "Elle est couverte en grande partie par la forêt amazonienne.", "Elle accueille le centre spatial de Kourou, d'où partent les fusées Ariane."],
  "Guyane : seul territoire français en Amérique du Sud, base spatiale de Kourou.")
D("q192", ["La Réunion est une île volcanique.", "Elle se trouve dans l'océan Indien, à l'est de Madagascar.", "Mayotte est aussi dans l'océan Indien. La Guadeloupe et la Martinique sont dans les Antilles."],
  "Océan Indien : La Réunion, Mayotte. Antilles : Guadeloupe, Martinique. Pacifique : Polynésie, Nouvelle-Calédonie.")
D("q193", ["L'Union européenne comptait 28 pays.", "Le Royaume-Uni l'a quittée en 2020 : c'est le Brexit.", "Elle compte donc 27 pays."],
  "UE : 27 pays depuis 2020. 20 d'entre eux utilisent l'euro (depuis 2023).",
  frise(1950, 2025, [[1957,"6 pays"],[1992,"UE"],[2004,"25 pays"],[2020,"27 pays"]], 2020))
D("q194", ["L'euro a été mis en circulation en 2002 (pièces et billets).", "Il a remplacé le franc en France.", "C'est la monnaie de la zone euro, une partie des pays de l'UE."],
  "2002 : l'euro remplace le franc.")
D("q195", ["En France, le pouvoir législatif (faire les lois) appartient au Parlement.", "Il est formé de deux assemblées : l'Assemblée nationale et le Sénat.", "Le gouvernement applique les lois (pouvoir exécutif) et les juges les font respecter (pouvoir judiciaire)."],
  "Séparation des pouvoirs : législatif (Parlement), exécutif (président et gouvernement), judiciaire (juges).",
  {"type":"table","head":["Pouvoir","Qui ?","Rôle"],"rows":[["!législatif","!Parlement","!vote les lois"],["exécutif","président, gouvernement","applique les lois"],["judiciaire","juges","juge selon les lois"]]})
