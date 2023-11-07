from sqlalchemy.sql.expression import text
import sys
import os
from connexion import cnx

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))



from interet_etape import Interet_etape

class Interet_etape_bd:
    def __init__(self,conx):
        """
            Initialise une instance de la classe Interet_etape_bd avec une connexion à la base de données.

            param conx: Objet de connexion à la base de données.
        """
        self.cnx=conx
        
    def get_all_interet_etape(self):
        """
            Récupère tous les intérêts d'étape depuis la base de données.

            return: Une liste d'objets Interet_etape représentant les intérêts d'étape.
        """
        try:
            query = text("select * from INTERETETAPE")
            resultat = self.cnx.execute(query)
            interets=[]
            for idi,nom,desc in resultat:
                interets.append(Interet_etape(idi,nom,desc))
            return interets
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def get_par_photo_etape(self,idi):
        """
            Récupère un intérêt d'étape spécifique en fonction de son ID.

            param idi: ID de l'intérêt d'étape que l'on souhaite récupérer.
            return: Une liste contenant un objet Interet_etape représentant l'intérêt d'étape correspondant.
        """
        try:
            query = text("select * from INTERETETAPE where id_interet = "+str(idi))
            resultat = self.cnx.execute(query)
            interets=[]
            for id,nom,desc in resultat:
                interets.append(Interet_etape(id,nom,desc))
            return interets
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    
    def inserer_interet_etape(self,idi,nom_interet,desc):
        """
            Insère un nouvel intérêt d'étape dans la base de données.

            param idi: ID de l'intérêt d'étape.
            param nom_interet: Nom de l'intérêt d'étape.
            param desc: Description de l'intérêt d'étape.
        """
        try:
            query = text(f"INSERT INTO INTERETETAPE VALUES({str(idi)}, '{nom_interet}', '{desc}')")
            print(query)
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_prochain_id_interet_etape(self):
        """
            Récupère l'ID disponible pour le prochain intérêt d'étape à insérer dans la base de données.

            return: L'ID du prochain intérêt d'étape.
        """
        try:
            query = text("select max(id_interet) as m from INTERETETAPE")
            result = self.cnx.execute(query)
            return result[0]+1
        except Exception as e:
            print("la connexion a échoué")
            return None
        
