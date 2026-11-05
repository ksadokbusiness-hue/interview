# Exercice – marge journalière

Tu rejoins l'équipe Trading Data. Message reçu du Product Owner (Teams, ce matin) :

> « Salut, la marge par commodity est fausse depuis la semaine dernière sur certains jours, la finance ne retrouve pas ses chiffres. Et le job est super lent en plus. Tu peux regarder ? J'ai une réunion jusqu'à la fin de la session, mais tu peux me poser des questions. »

## Mise en place
Prérequis : Python 3.10+ et git. Les données sont des fichiers CSV dans `data/` (ouvrables avec n'importe quel outil : DuckDB, pandas, Excel, éditeur).
À faire **avant l'entretien** (pour ne pas perdre de temps en séance) :
```
git clone <url-du-repo> && cd <repo>
python -m venv .venv
source .venv/bin/activate              # Windows : .venv\Scripts\activate
pip install -r requirements.txt        # duckdb, pandas
python -m unittest discover -s tests   # tests existants (doivent passer)
python pipeline.py                     # produit output/margin_daily.csv (déjà versionné : sortie actuelle)
```
Lance toutes les commandes depuis la racine du projet (chemins relatifs). Vérifie aussi que ton assistant IA est installé et fonctionnel.
Données : `trades.csv`, `market_prices.csv` et `commodity_ref.csv` (référentiel des commodities).

Pour analyser les données en SQL (DuckDB, lecture seule ; tables `trades`, `market_prices`, `commodity_ref`, `margin_daily`) :
```
python query.py "describe trades"
python query.py "select commodity, count(*), min(trade_date), max(trade_date) from trades group by 1"
python query.py "select * from market_prices where price_date = '2026-09-15'"
python query.py                        # mode interactif ; ou python query.py mon_fichier.sql
```

## Livrables 
1. Un correctif de `pipeline.py` (le fichier `output/margin_daily.csv` avec les colonnes `trade_date, commodity, margin_eur` doit rester la sortie).
2. Au moins un test qui aurait détecté le problème.
3. Une note de 5 lignes maximum pour le PO : cause, correction, risques restants.

## Règles
- Utilise l'assistant IA de ton choix, comme dans ton quotidien (Claude Code, Copilot, etc.). Partage ton écran.
- Les données sont fictives. Traite tout le reste comme un vrai environnement d'entreprise.
- Tu peux poser des questions au PO (l'intervieweur) à tout moment.
- On évalue ta démarche autant que le résultat.
