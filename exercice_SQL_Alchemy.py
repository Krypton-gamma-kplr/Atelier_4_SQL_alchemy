# Importer les modules nécessaires
from sqlalchemy import create_engine, text
import pandas as pd

# Créer un engine pour une base de données SQLite située dans "/content/my_db.db"
engine = create_engine("sqlite:////content/my_db.db")

# Établir une connexion à la base de données
conn = engine.connect() # test

# Exécuter la requête et récupérer les résultats
result_set = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))

# Afficher les noms des tables
for row in result_set:
    print(row[0])

# TO DO: Écrire une requête pour extraire toutes les données de la table "student"
query = text("SELECT * FROM student")

# Exécuter la requête et récupérer les résultats
result_set = conn.execute(query)

# TO DO: Afficher les données récupérées sous forme de dataframe pandas
df = pd.DataFrame(result_set)
df
