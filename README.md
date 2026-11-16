# BrevetQuest

Appli de révision du brevet des collèges : défi du jour, quiz par matière, XP, niveaux, série de jours et répétition espacée des questions ratées.

- `index.html` : l'appli (générée, ne pas modifier à la main).
- `questions.json` : la banque de questions (générée par `src/questions_source.py`).
- `config.js` : adresse et clé publique Supabase pour la sauvegarde en ligne.
- `supabase/setup.sql` : création de la table et des fonctions protégées par le code famille.

Pour régénérer après une modification :

```
python3 src/questions_source.py questions.json
python3 src/build.py
```
