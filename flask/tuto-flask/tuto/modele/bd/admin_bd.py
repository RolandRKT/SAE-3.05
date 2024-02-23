"""
    Class qui fait la liaison avec la bd
"""
import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))

from admin import Admin


class Admin_bd:
    """
    Classe représentant l'interface d'accès à la base de données pour les administrateurs.

    Attributes:
        cnx: La connexion à la base de données.
    """

    def __init__(self, conx):
        """
        Initialise un objet Admin_bd avec la connexion à la base de données.

        Args:
            conx: La connexion à la base de données.
        """
        self.cnx = conx

    def get_all_admin(self):
        """
        Récupère tous les administrateurs depuis la base de données.

        Returns:
            list: Une liste d'objets Admin représentant tous les administrateurs.
        """
        try:
            query = text("select id_admin, pseudo, mdp from ADMIN")
            resultat = self.cnx.execute(query)
            admin = [
                Admin(id_admin, pseudo, mdp)
                for id_admin, pseudo, mdp in resultat
            ]
            return admin
        except Exception as exp:
            print("Erreur lors de la récupération des administrateurs :",
                  str(exp))
            return None

    def get_par_admin(self, id_admin):
        """
        Récupère un administrateur spécifique depuis la base de données.

        Args:
            id_admin (int): L'ID de l'administrateur à récupérer.

        Returns:
            list: Une liste d'objets Admin représentant l'administrateur spécifié.
        """
        try:
            query = text(
                "select id_admin, pseudo, mdp from ADMIN where id_admin= " +
                str(id_admin))
            resultat = self.cnx.execute(query)
            admin = [
                Admin(id_admin, pseudo, mdp)
                for id_admin, pseudo, mdp in resultat
            ]
            return admin
        except Exception as exp:
            print("Erreur lors de la récupération de l'administrateur :",
                  str(exp))
            return None

    def inserer_admin(self, idadmin, pseudo, mail, mdp):
        """
        Insère un nouvel administrateur dans la base de données.

        Args:
            idadmin (int): L'ID du nouvel administrateur.
            pseudo (str): Le pseudo du nouvel administrateur.
            mail (str): L'adresse e-mail du nouvel administrateur.
            mdp (str): Le mot de passe du nouvel administrateur.
        """
        try:
            query = text(
                f"insert into ADMIN values({str(idadmin)}, '{pseudo}', '{mail}','{mdp}')"
            )
            self.cnx.execute(query)
            self.cnx.commit()
            print("Insertion réussie")
        except Exception as exp:
            print("Erreur lors de l'insertion de l'administrateur :", str(exp))
            return None

    def get_prochain_id_admin(self):
        """
        Récupère le prochain ID disponible pour un nouvel administrateur.

        Returns:
            int: Le prochain ID disponible.
        """
        try:
            query = text("SELECT MAX(id_admin) as m FROM ADMIN")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                return int(result.m) + 1
        except Exception as exp:
            print(
                "Erreur lors de la récupération du prochain ID administrateur :",
                str(exp))
            return None

    def delete_suivre_par_part(self, pseudo):
        """
        Supprime les entrées de suivi associées à un participant dans la base de données.

        Args:
            pseudo (str): Le pseudo du participant à supprimer du suivi.
        """
        try:
            query = text(
                f"DELETE FROM SUIVRE USING SUIVRE NATURAL JOIN PARTICIPANT WHERE PARTICIPANT.pseudo = :pseudo"
            )
            query2 = text(
                f"DELETE FROM TERMINE NATURAL JOIN PARTICIPANT WHERE PARTICIPANT.pseudo = :pseudo"
            )
            self.cnx.execute(query, {'pseudo': pseudo})
            self.cnx.execute(query2, {'pseudo': pseudo})
            self.cnx.commit()
        except Exception as exp:
            print("Erreur lors de la suppression du suivi par participant :",
                  str(exp))

    def delete_part(self, pseudo):
        """
        Supprime un participant de la base de données, y compris toutes les entrées de suivi associées.

        Args:
            pseudo (str): Le pseudo du participant à supprimer.
        """
        try:
            self.delete_suivre_par_part(pseudo)
            query = text(
                f"delete from PARTICIPANT where pseudo = '{str(pseudo)}'")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as exp:
            print("Erreur lors de la suppression du participant :", str(exp))
