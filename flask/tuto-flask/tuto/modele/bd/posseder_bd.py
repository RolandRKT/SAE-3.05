from connexion import cnx
from sqlalchemy.sql.expression import text

import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from posseder import Posseder

class Posseder_bd:
    def __init__(self,conx):
        """
            Initialise une instance de la classe Posseder_bd avec une connexion à la base de données.

            param conx: Objet de connexion à la base de données.
        """
        self.cnx=conx

    def get_all_posseder(self):
        """
            Récupère toutes les associations de possession depuis la base de données.

            return: Une liste d'objets Posseder représentant les associations de possession.
        """
        try:
            query = text("select * from POSSEDER")
            resultat = self.cnx.execute(query)
            possession=[]
            for ide,idi in resultat:
                possession.append(Posseder(ide,idi))
            return possession
        except Exception as e:
            print("la connexion a échoué")
            print(e)
            return None
    
    def get_posseder_by_idinteret(self,idinteret):
        """
            Récupère les associations de possession liées à un intérêt spécifique.

            param idinteret: ID de l'intérêt pour lequel on souhaite récupérer les associations de possession.
            return: Une liste d'objets Posseder représentant les associations de possession liées à l'intérêt donné.
        """
        try:
            query = text("select * from POSSEDER where id_interet = "+str(idinteret))
            resultat = self.cnx.execute(query)
            possession=[]
            for ide,idi in resultat:
                possession.append(Posseder(ide,idi))
            return possession
        except Exception as e:
            print("la connexion a échoué")
            print(e)
            return None
    
    def get_posseder_by_etape(self,idetape):
        """
            Récupère les associations de possession liées à une étape spécifique.

            param idetape: ID de l'étape pour laquelle on souhaite récupérer les associations de possession.
            return: Une liste d'objets Posseder représentant les associations de possession liées à l'étape donnée.
        """
        try:
            query = text("select * from POSSEDER where id_etape = "+str(idetape))
            resultat = self.cnx.execute(query)
            possession=[]
            for ide,idi in resultat:
                possession.append(Posseder(ide,idi))
            return possession
        except Exception as e:
            print("la connexion a échoué")
            print(e)
            return None
    
    def inserer_possede(self,idetape,idinteret):
        """
            Insère une nouvelle association de possession dans la base de données.
    
            param idetape: ID de l'étape liée à l'association de possession.
            param idinteret: ID de l'intérêt lié à l'association de possession.
        """
        try:
            query = text(f"insert into POSSEDER values({str(idetape)} , {str(idinteret)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("la connexion a échoué")
            print(e)
            return None
