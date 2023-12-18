from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))

from composer import Composer

class Composer_bd:
    def __init__(self,conx):
        """
            Initialise une instance de la classe Composer_bd avec une connexion à la base de données.

            param conx: Objet de connexion à la base de données.
        """
        self.cnx=conx

    def get_all_composition(self):
        """
            Récupère toutes les compositions de parcours et d'étapes dans la base de données.

            return: Une liste d'objets Composer représentant les compositions.
        """
        try:
            query = text("select id_parcours, id_etape,numero from COMPOSER")
            resultat = self.cnx.execute(query)
            composition=[]
            for idp,ide,numero in resultat:
                composition.append(Composer(idp,ide,numero))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_par_etape_composition(self,ide):
        """
            Récupère les compositions associées à une étape spécifique.

            param ide: ID de l'étape pour laquelle on veut récupérer les compositions.
            return: Une liste d'objets Composer représentant les compositions pour l'étape donnée.
        """
        try:
            query = text("select id_parcours, id_etape,numero from COMPOSER where id_etape= "+str(ide))
            resultat = self.cnx.execute(query)
            composition=[]
            for idp,ide,numero in resultat:
                composition.append(Composer(idp,ide,numero))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def get_par_parcour_composition(self,idp):
        """
            Récupère les compositions associées à un parcours spécifique.

            param idp: ID du parcours pour lequel on veut récupérer les compositions.
            return: Une liste d'objets Composer représentant les compositions pour le parcours donné.
        """
        try:
            query = text("select id_parcours, id_etape,numero from COMPOSER where id_parcours= "+str(idp))
            resultat = self.cnx.execute(query)
            composition=[]
            for idp,ide,numero in resultat:
                composition.append(Composer(idp,ide,numero))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def inserer_compose(self,idparc,ide,numero):
        """
            Insère une nouvelle composition de parcours et d'étape dans la base de données.

            param idparc: ID du parcours à composer.
            param ide: ID de l'étape à composer.
            param numero: Numéro d'ordre de la composition.
        """
        try:
            query = text(f"insert into COMPOSER values({str(idparc)} , {str(ide)},{str(numero)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_max_etape_composer(self,idP):
        try :
            query=text(f"select max(numero) from COMPOSER where id_parcours={idP}")
            resultat=self.cnx.execute(query)
            for numero in resultat:
                return numero
        except Exception as e:
            print("la connexion a échoué")
            return None