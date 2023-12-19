"""
    Ce fichier va nous permettre de prendre des valeurs
    des etapes de la bd.
"""
import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from etape import Etape


class Etape_bd:
    """
        La class Etape bd
    """

    def __init__(self, conx):
        """
            Initialise une instance de la classe Etape_bd avec une connexion à la base de données.

            param conx: Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_etape(self):
        """
            Récupère toutes les étapes depuis la base de données.

            return: Une liste d'objets Etape représentant les étapes.
        """
        try:
            query = text("select * from ETAPE")
            resultat = self.cnx.execute(query)
            etapes = []
            for ide, nom, idph, coordX, coordY in resultat:
                etapes.append(Etape(ide, nom, idph, coordX, coordY))
            return etapes
        except Exception as exp:
            print("la connexion a échoué")
            print(exp)
            return None

    def get_par_photo_etape(self, idph):
        """
            Récupère les étapes associées à une photo spécifique.
            param idph: ID de la photo pour laquelle on veut récupérer les étapes.
            return: Une liste d'objets Etape représentant les étapes pour la photo donnée.
        """
        try:
            query = text("select * from ETAPE where id_photo = " + str(idph))
            resultat = self.cnx.execute(query)
            etapes = []
            for ide, nom, idp, coordX, coordY in resultat:
                etapes.append(Etape(ide, nom, idp, coordX, coordY))
            return etapes
        except Exception as exp:
            print("la connexion a échoué")
            print(exp)
            return None

    def inserer_etape(self, idetape, nometape, idimage, coordX, coordY):
        """
            Insère une nouvelle étape dans la base de données.

            param idetape: ID de l'étape.
            param nometape: Nom de l'étape.
            param coordX : coordonnée x de l'étape.
            param coordY : coordonnée y de l'étape.
            param idimage: ID de l'image associée à l'étape.
        """
        try:
            query = text(
                f"insert into ETAPE values({str(idetape)},'{nometape}', {str(idimage)}, '{str(coordX)}', '{str(coordY)}')"
            )
            self.cnx.execute(query)
            self.cnx.commit()

        except Exception as exp:
            print("la connexion a échoué")
            print(exp)
            return None

    def get_prochain_id_etape(self):
        """
            Récupère l'ID disponible pour la prochaine étape à insérer dans la base de données.

            return: L'ID de la prochaine étape.
        """
        try:
            query = text("select max(id_etape) as m from ETAPE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as exp:
            print("la connexion a échoué")
            print(exp)
            return None
