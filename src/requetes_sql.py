import sqlite3


def execute_queries():
    conn = sqlite3.connect('sales_data.db')
    cursor = conn.cursor()

    # Total des ventes
    cursor.execute('''INSERT INTO Analyses_Resultats (description, resultat)
                      SELECT 'Total des ventes', SUM(Prix * V.Quantité) FROM Ventes
                      LEFTJOIN Produits ON V.ID_produit = Produits.ID''')

    # Ventes par produit
    cursor.execute('''INSERT INTO Analyses_Resultats (description, resultat)
                      SELECT 'Ventes par produit', Produits.Nom || ' : ' || SUM(Quantité) FROM Ventes
                      JOIN Produits ON Ventes.ID_produit = Produits.ID
                      GROUP BY Produits.Nom''')

    # Ventes par région
    cursor.execute('''INSERT INTO Analyses_Resultats (description, resultat)
                      SELECT 'Ventes par région', Magasins.Ville || ' : ' || SUM(Quantité) FROM Ventes
                      JOIN Magasins ON Ventes.ID_magasin = Magasins.ID
                      GROUP BY Magasins.Ville''')

    conn.commit()
    conn.close()
