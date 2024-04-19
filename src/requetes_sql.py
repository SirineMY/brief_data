

import sqlite3

def execute_queries():
    conn = sqlite3.connect('sales_data.db')
    cursor = conn.cursor()

    # Total des ventes
    cursor.execute('''
        SELECT 'Total des ventes', SUM(Prix * Quantite) as Total
        FROM Ventes
        JOIN Produits ON Ventes.ID_produit = Produits.ID
    ''')
    total_sales = cursor.fetchone()
    print(f"{total_sales[0]}: {total_sales[1]}")

    # Ventes par produit
    cursor.execute('''
        SELECT Produits.Nom, SUM(Quantite) as Total
        FROM Ventes
        JOIN Produits ON Ventes.ID_produit = Produits.ID
        GROUP BY Produits.Nom
    ''')
    print("Ventes par produit:")
    for product_sales in cursor.fetchall():
        print(f"{product_sales[0]} : {product_sales[1]}")

    # Ventes par région
    cursor.execute('''
        SELECT Magasins.Ville, SUM(Quantite) as Total
        FROM Ventes
        JOIN Magasins ON Ventes.ID_magasin = Magasins.ID
        GROUP BY Magasins.Ville
    ''')
    print("Ventes par région:")
    for region_sales in cursor.fetchall():
        print(f"{region_sales[0]} : {region_sales[1]}")



    # # Total des ventes
    # cursor.execute('''INSERT INTO Analyses_Resultats (description, resultat)
    #                   SELECT 'Total des ventes', SUM(Prix * Quantite) FROM Ventes
    #                   JOIN Produits ON ID_produit = Produits.ID''')

    # # Ventes par produit
    # cursor.execute('''INSERT INTO Analyses_Resultats (description, resultat)
    #                   SELECT 'Ventes par produit', Produits.Nom || ' : ' || SUM(Quantite) FROM Ventes
    #                   JOIN Produits ON Ventes.ID_produit = Produits.ID
    #                   GROUP BY Produits.Nom''')

    # # Ventes par région
    # cursor.execute('''INSERT INTO Analyses_Resultats (description, resultat)
    #                   SELECT 'Ventes par région', Magasins.Ville || ' : ' || SUM(Quantite) FROM Ventes
    #                   JOIN Magasins ON Ventes.ID_magasin = Magasins.ID
    #                   GROUP BY Magasins.Ville''')

    

    conn.close()

if __name__ == "__main__":
    execute_queries()
