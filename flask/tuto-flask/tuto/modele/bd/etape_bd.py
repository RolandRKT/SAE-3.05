from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from etape import Etape

class Etape_bd:
    def __init__(self,conx):
        """
            Initialise une instance de la classe Etape_bd avec une connexion à la base de données.

            param conx: Objet de connexion à la base de données.
        """
        self.cnx=conx

    def get_all_etape(self):
        """
            Récupère toutes les étapes depuis la base de données.

            return: Une liste d'objets Etape représentant les étapes.
        """
        try:
            query = text("select * from ETAPE")
            resultat = self.cnx.execute(query)
            etapes=[]
            for ide,nom,idph,local in resultat:
                etapes.append(Etape(ide,nom,idph,local))
            return etapes
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_par_photo_etape(self,idph):
        """
            Récupère les étapes associées à une photo spécifique.
            param idph: ID de la photo pour laquelle on veut récupérer les étapes.
            return: Une liste d'objets Etape représentant les étapes pour la photo donnée.
        """
        try:
            query = text("select * from ETAPE where id_photo = "+str(idph))
            resultat = self.cnx.execute(query)
            etapes=[]
            for ide,nom,idp,local in resultat:
                etapes.append(Etape(ide,nom,idp,local))
            return etapes
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def inserer_etape(self,idetape,nometape,localisation,idimage):
        """
            Insère une nouvelle étape dans la base de données.

            param idetape: ID de l'étape.
            param nometape: Nom de l'étape.
            param localisation: Localisation de l'étape.
            param idimage: ID de l'image associée à l'étape.
        """
        try:
            query = text(f"insert into ETAPE values({str(idetape)},'{nometape}','{localisation}' , {str(idimage)})")
            self.cnx.execute(query)
            self.cnx.commit()

        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_prochain_id_etape(self):
        """
            Récupère l'ID disponible pour la prochaine étape à insérer dans la base de données.

            return: L'ID de la prochaine étape.
        """
        try:
            query = text("select max(id_etape) as m from ETAPE")
            result = self.cnx.execute(query)
            return result[0]+1
        except Exception as e:
            print("la connexion a échoué")
            return None