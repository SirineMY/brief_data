import sqlite3
import pandas as pd
import requests

def fetch_data(url):
    response = requests.get(url)
    df = pd.read_csv(pd.compat.StringIO(response.content.decode('utf-8')))
    return df

def import_data():
    conn = sqlite3.connect('sales_data.db')

    # URL pour chaque fichier de données
    urls = {
        'Produits': 'https://path.to/your/products.csv',
        'Magasins': 'https://path.to/your/stores.csv',
        'Ventes': 'https://path.to/your/sales.csv'
    }

    # Importer les données pour Produits et Magasins sans vérification spéciale
    for table in ['Produits', 'Magasins']:
        print(f"Importing data for {table}")
        df = fetch_data(urls[table])
        df.to_sql(table, conn, if_exists='append', index=False)

    # Importation spéciale pour les Ventes
    print("Importing data for Ventes")
    df_ventes = fetch_data(urls['Ventes'])

    # Extraire les identifiants existants sous forme d'un DataFrame pour vérifier les doublons
    existing_sales = pd.read_sql_query("""
        SELECT produit_id, magasin_id, date FROM Ventes
    """, conn)

    # Convertir les colonnes pertinentes en un type approprié si nécessaire
    df_ventes['date'] = pd.to_datetime(df_ventes['date'])

    # Création d'une clé temporaire pour vérifier les doublons
    df_ventes['temp_key'] = df_ventes['produit_id'].astype(str) + '-' + df_ventes['magasin_id'].astype(str) + '-' + df_ventes['date'].dt.strftime('%Y-%m-%d')
    existing_sales['temp_key'] = existing_sales['produit_id'].astype(str) + '-' + existing_sales['magasin_id'].astype(str) + '-' + existing_sales['date']

    # Filtrer les nouvelles ventes qui ne sont pas déjà dans la base de données
    new_ventes = df_ventes[~df_ventes['temp_key'].isin(existing_sales['temp_key'])]

    # Importer les nouvelles ventes
    if not new_ventes.empty:
        new_ventes.drop(columns=['temp_key'], inplace=True)
        new_ventes.to_sql('Ventes', conn, if_exists='append', index=False)
    else:
        print("No new sales data to import.")

    # Fermer la connexion à la base de données
    conn.close()

if __name__ == "__main__":
    import_data()
