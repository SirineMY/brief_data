import sqlite3
from import_data import *
from requetes_sql import *


def setup_database():
    conn = sqlite3.connect('sales_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''DROP TABLE IF EXISTS Magasins;''')
    cursor.execute('''DROP TABLE IF EXISTS Ventes;''')
    cursor.execute('''DROP TABLE IF EXISTS Produits;''')

    # Création des tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS Produits (
                    Nom VARCHAR(255),
                    ID VARCHAR(255) PRIMARY KEY,
                    Prix FLOAT,
                    Stock INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Magasins (
                        ID INTEGER PRIMARY KEY,
                        Ville VARCHAR(255),
                        nb_salaries INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Ventes (
                    Date DATE,
                    ID_produit VARCHAR(255),
                    Quantite INTEGER,
                    ID_magasin INTEGER,
                    FOREIGN KEY (ID_produit) REFERENCES Produits(ID),
                    FOREIGN KEY (ID_magasin) REFERENCES Magasins(ID))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Analyses_Resultats (
                        requete_id INTEGER PRIMARY KEY,
                        description TEXT,
                        resultat TEXT)''')

    conn.commit()
    conn.close()

def main():
    setup_database()  # Configurer et créer la base de données et les tables
    import_data()  # Importer les données dans la base de données
    execute_queries()  # Exécuter les requêtes SQL et stocker les résultats


if __name__ == "__main__":
    main()
