# Importer les modules nécessaires
from sqlalchemy import create_engine, text
import pandas as pd

# Créer un engine pour une base de données SQLite située dans "/content/my_db.db"
engine = create_engine("sqlite:////content/my_db.db")

# Établir une connexion à la base de données
conn = engine.connect()

# Exécuter la requête et récupérer les résultats
result_set = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))

# Afficher les noms des tables
for row in result_set:
    print(row[0])
