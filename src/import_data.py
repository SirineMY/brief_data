import sqlite3
import pandas as pd
import os
from tqdm import tqdm

def import_data():
    conn = sqlite3.connect('sales_data.db')
    cursor = conn.cursor()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, '../data')

    file_paths = {
        'Produits': 'Produits.csv',
        'Magasins': 'Magasins.csv',
        'Ventes': 'Ventes.csv'
    }

    # Insertion for Produits
    df_produits = pd.read_csv(os.path.join(data_dir, file_paths['Produits']))
    total_rows = len(df_produits)
    successful_inserts = 0
    for index, row in tqdm(df_produits.iterrows(), total=total_rows, desc="Insertion des produits"):
        query = "INSERT INTO Produits (Nom, ID, Prix, Stock) VALUES (?, ?, ?, ?)"
        parameters = (row['Nom'], row['ID'], row['Prix'], row['Stock'])
        try:
            cursor.execute(query, parameters)
            conn.commit()
            successful_inserts += 1
        except Exception as e:
            print("Erreur lors de l'insertion pour la ligne", index, ":", e)

    print(f"Toutes les lignes de la table Produits ont été ajoutées avec succès: {successful_inserts}/{total_rows}")

    # Insertion for Magasins
    df_magasins = pd.read_csv(os.path.join(data_dir, file_paths['Magasins']))
    total_rows = len(df_magasins)
    successful_inserts = 0
    for index, row in tqdm(df_magasins.iterrows(), total=total_rows, desc="Insertion des magasins"):
        query = "INSERT INTO Magasins (ID, Ville, nb_salaries) VALUES (?, ?, ?)"
        parameters = (row['ID'], row['Ville'], row['nb_salaries'])
        try:
            cursor.execute(query, parameters)
            conn.commit()
            successful_inserts += 1
        except Exception as e:
            print("Erreur lors de l'insertion pour la ligne", index, ":", e)

    print(f"Toutes les lignes de la table Magasins ont été ajoutées avec succès: {successful_inserts}/{total_rows}")

    # Insertion for Ventes
    df_ventes = pd.read_csv(os.path.join(data_dir, file_paths['Ventes']))
    total_rows = len(df_ventes)
    successful_inserts = 0
    for index, row in tqdm(df_ventes.iterrows(), total=total_rows, desc="Insertion des ventes"):
        query = "INSERT INTO Ventes (Date, ID_produit, Quantite, ID_magasin) VALUES (?, ?, ?, ?)"
        parameters = (row['Date'], row['ID_produit'], row['Quantité'], row['ID_magasin'])
        try:
            cursor.execute(query, parameters)
            conn.commit()
            successful_inserts += 1
        except Exception as e:
            print("Erreur lors de l'insertion pour la ligne", index, ":", e)

    print(f"Toutes les lignes de la table Ventes ont été ajoutées avec succès: {successful_inserts}/{total_rows}")

    conn.close()

if __name__ == "__main__":
    import_data()
