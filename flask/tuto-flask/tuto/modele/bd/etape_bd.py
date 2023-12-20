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
            for ide, nom, idph, coordX, coordY, interet in resultat:
                etapes.append(Etape(ide, nom, idph, coordX, coordY,interet))
            return etapes
        except Exception as exp:
            print("la connexion a échoué, get_all_etape")
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
            for ide, nom, idp, coordX, coordY,interet in resultat:
                etapes.append(Etape(ide, nom, idp, coordX, coordY,interet))
            return etapes
        except Exception as exp:
            print("la connexion a échoué, get_par_photo_etape")
            print(exp)
            return None

    def inserer_etape(self, idetape, nometape, idimage, coordX, coordY,interet):
        """
            Insère une nouvelle étape dans la base de données.

            param idetape: ID de l'étape.
            param nometape: Nom de l'étape.
            param coordX : coordonnée x de l'étape.
            param coordY : coordonnée y de l'étape.
            param idimage: ID de l'image associée à l'étape.
        """
        try:
            if(idimage is None):
                query = text(f"insert into ETAPE values({str(idetape)},'{nometape}', null, '{str(coordX)}', '{str(coordY)}','{str(interet)}')")
            else:
                query = text(f"insert into ETAPE values({str(idetape)},'{nometape}', {str(idimage)}, '{str(coordX)}', '{str(coordY)}','{str(interet)}')")
            self.cnx.execute(query)
            self.cnx.commit()

        except Exception as exp:
            print("la connexion a échoué, inserer_etape")
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
            print("la connexion a échoué, get_prochain_id_etape")
            return None
        
    def get_par_id_etape(self, idetape):
        """
            Récupère une étape spécifique en fonction de son ID.

            param idetape: ID de l'étape que l'on souhaite récupérer.
            return: Une liste contenant un objet Etape représentant le parcours correspondant.
        """
        try:
            query = text("select * from ETAPE where id_etape = " +str(idetape))
            resultat = self.cnx.execute(query)
            for ide,nom,idp,coordX, coordY,interet in resultat:
                return Etape(ide,nom,idp,coordX, coordY,interet)
            
            return None
        except Exception as exp:
            print("la connexion a échoué, get_par_id_etape")
            print(exp)
            return None
