import sqlite3
import import_data
import requetes_sql


def setup_database():
    conn = sqlite3.connect('sales_data.db')
    cursor = conn.cursor()

    # Création des tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS Produits (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Nom TEXT,
                        Prix REAL,
                        Stock TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Magasins (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Ville TEXT,
                        nb_salaries INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Ventes (
                        produit_id INTEGER,
                        magasin_id INTEGER,
                        date DATE,
                        quantite INTEGER,
                        FOREIGN KEY (produit_id) REFERENCES Produits(id),
                        FOREIGN KEY (magasin_id) REFERENCES Magasins(id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Analyses_Resultats (
                        requete_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT,
                        resultat TEXT)''')

    conn.commit()
    conn.close()

def main():
    setup_database()  # Configurer et créer la base de données et les tables
    import_data.import_data()  # Importer les données dans la base de données
    requetes_sql.execute_queries()  # Exécuter les requêtes SQL et stocker les résultats


if __name__ == "__main__":
    main()
