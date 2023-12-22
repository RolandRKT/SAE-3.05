"""
    La class parcours avec la liaison à la bd sera faite ici
"""
import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))

from parcours import Parcours


class Parcours_bd:
    """
        Class Parcours
    """

    def __init__(self, conx):
        """
            Initialise une instance de la classe Parcours_bd avec une
            connexion à la base de données.

            param conx: Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_parcours(self):
        """
            Récupère tous les parcours depuis la base de données.

            return: Une liste d'objets Parcours représentant les parcours.
        """
        try:
            query = text(
                "select id_parcours, nom_parcours, duree, description_parcours, id_image from PARCOURS"
            )
            resultat = self.cnx.execute(query)
            parcours = []
            for id_parcours, nom, duree, desc, id_img in resultat:
                parcours.append(Parcours(id_parcours, nom, duree, desc,
                                         id_img))
            return parcours
        except Exception as exp:
            print("la connexion a échoué")
            print(exp)
            return None

    def get_par_parcours(self, id_parcours):
        """
            Récupère un parcours spécifique en fonction de son ID.

            param id_parcours: ID du parcours que l'on souhaite récupérer.
            return: Une liste contenant un objet Parcours représentant le parcours correspondant.
        """
        try:
            query = text(
                "select id_parcours, nom_parcours,duree,description_parcours, id_image from PARCOURS where id_parcours= "
                + str(id_parcours))
            resultat = self.cnx.execute(query)
            parcours = []
            for id_parcours, nom, duree, desc, id_img in resultat:
                parcours.append(Parcours(id_parcours, nom, duree, desc,
                                         id_img))
            return parcours
        except Exception as exp:
            print("la connexion a échoué")
            print(exp)
            return None

    def get_par_parcours_image(self, id_image):
        """
            Récupère les parcours associés à une image spécifique.

            param id_image: ID de l'image pour laquelle on veut récupérer les parcours.
            return: Une liste d'objets Parcours représentant les parcours associés à l'image donnée.
        """
        try:
            query = text("select * from PARCOURS where id_image= " +
                         str(id_image))
            resultat = self.cnx.execute(query)
            parcours = []
            for id_parcours, nom, duree, desc, id_img in resultat:
                parcours.append(Parcours(id_parcours, nom, duree, desc,
                                         id_img))
            return parcours
        except Exception as exp:
            print("la connexion a échoué")
            print(exp)
            return None

    def inserer_parcours(self, idparc, nomparc, duree, descparc, idimg):
        """
            Insère un nouveau parcours dans la base de données.

            param idparc: ID du parcours.
            param nomparc: Nom du parcours.
            param duree: Durée du parcours.
            param descparc: Description du parcours.
            param idimg: ID de l'image associée au parcours.
        """
        try:
            query = text(
                f"insert into PARCOURS values({str(idparc)} , '{nomparc}' ,'{str(duree)}' , '{descparc}','{str(idimg)}')"
            )
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("la connexion a échoué")
            print(e)
            return None

    def get_prochain_id_parcours(self):
        """
            Récupère l'ID disponible pour le prochain parcours à insérer dans la base de données.

            return: L'ID du prochain parcours.
        """
        try:
            query = text("select max(id_parcours) as m from PARCOURS")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as exp:
            print("la connexion a échoué")
            print(exp)
            return None

    def delete_parcours(self, id_parcours):
        """
            Supprime un parcours de la base de données.

            param id_parcours: ID du parcours à supprimer.
        """
        try:
            query1 = text(
                f"delete from PARCOURS where id_parcours ={id_parcours}")
            query2 = text(
                f"delete from SUIVRE where id_parcours ={id_parcours}")
            query3 = text(
                f"delete from COMPOSER where id_parcours ={id_parcours}")
            query4 = text(
                f"delete from TERMINE where id_parcours ={id_parcours}")
            self.cnx.execute(query4)
            self.cnx.execute(query3)
            self.cnx.execute(query2)
            self.cnx.execute(query1)
            self.cnx.commit()
        except Exception as exp:
            print("la connexion a échoué, delete de parcours")
            print(exp)
            return None
