"""
    Fichier qui contient la classe Termine_bd permettant de récupérer les données de la table TERMINE de la base de données.
"""
import os
import sys
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))

from termine import Termine

class Termine_bd:
    """
        Class termine bd
    """

    def __init__(self, conx):
        """
            Initialise une instance de la classe Termine_bd avec une connexion à la base de données.

            param conx: Objet de connexion à la base de données.
        """
        self.cnx = conx
    
    def get_all_termine(self):
        """
            Récupère tous les termine depuis la base de données.
        """
        try:
            query = text(
                "select id_parcours, id_participant, note, comm from TERMINE")
            resultat = self.cnx.execute(query)
            termine = []
            for id_parcours, id_participant, note, comm in resultat:
                termine.append(Termine(id_parcours, id_participant, note, comm))
            return termine
        except Exception as exp:
            print("la connexion a échoué, all termine")
            print(exp)
            return None