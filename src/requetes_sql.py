import sqlite3


def execute_queries():
    conn = sqlite3.connect('sales_data.db')
    cursor = conn.cursor()

    # Total des ventes
    cursor.execute('''INSERT INTO Analyses_Resultats (description, resultat)
                      SELECT 'Total des ventes', SUM(prix * quantite) FROM Ventes
                      JOIN Produits ON Ventes.produit_id = Produits.id''')

    # Ventes par produit
    cursor.execute('''INSERT INTO Analyses_Resultats (description, resultat)
                      SELECT 'Ventes par produit', Produits.nom || ' : ' || SUM(quantite) FROM Ventes
                      JOIN Produits ON Ventes.produit_id = Produits.id
                      GROUP BY Produits.nom''')

    # Ventes par région
    cursor.execute('''INSERT INTO Analyses_Resultats (description, resultat)
                      SELECT 'Ventes par région', Magasins.emplacement || ' : ' || SUM(quantite) FROM Ventes
                      JOIN Magasins ON Ventes.magasin_id = Magasins.id
                      GROUP BY Magasins.emplacement''')

    conn.commit()
    conn.close()
