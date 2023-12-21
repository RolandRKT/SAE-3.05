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
    
    def get_all_termine(self,id_participant):
        """
            Récupère tous les termine depuis la base de données.
        """
        try:
            query = text(
                f"select * from TERMINE where id_participant={id_participant}")
            resultat = self.cnx.execute(query)
            termine = []
            for id_parcours, id_participant, note, comm in resultat:
                termine.append(Termine(id_parcours, id_participant, note, comm))
            return termine
        except Exception as exp:
            print("la connexion a échoué, all termine")
            print(exp)
            return None
        
    def get_termine_id_part(self,id_participant,id_parcours):
        """
            Renvoie un boolean qui indique si le parcours existe dans la table TERMINE
        """
        try:
            query = text(
                f"select * from TERMINE where id_participant={id_participant} and id_parcours={id_parcours}")
            resultat = self.cnx.execute(query)
            termine = []
            for id_parcours, id_participant, note, comm in resultat:
                termine.append(Termine(id_parcours, id_participant, note, comm))
            if len(termine)==0:
                return False
            else:
                return True
        except Exception as exp:
            print("la connexion a échoué, all termine")
            print(exp)
            return None

    def inserer_termine(self, id_parcours, id_participant, note, comm):
        """
            Insère un termine dans la base de données.
        """
        try:
            query = text(
                f"insert into TERMINE(id_parcours, id_participant, note, comm) values({id_parcours}, {id_participant}, {note}, '{comm}')")
            query_delete_suivre = text(
                f"delete from SUIVRE where id_parcours={id_parcours} and id_participant={id_participant}")
            self.cnx.execute(query)
            self.cnx.execute(query_delete_suivre)
            self.cnx.commit()
        except Exception as exp:
            print("la connexion a échoué, inserer termine")
            print(exp)
            return None

    def get_note_comm(self,id_parcours):
        """
            Récupère la note et le commentaire d'un parcours.
        """
        try:
            query = text(
                f"select id_parcours, pseudo,note, comm from TERMINE NATURAL JOIN PARTICIPANT where id_parcours={id_parcours}")
            resultat = self.cnx.execute(query)
            liste=[]
            for idparc,pseudo,note, comm in resultat:
                liste.append((idparc,pseudo,note,comm))
            return liste
        except Exception as exp:
            print("la connexion a échoué, get note comm")
            print(exp)
            return None

    def supprimer_termine(self, id_parcours, id_participant):
        """
            Supprime une ligne de la table TERMINE en fonction de l'id de parcours et du pseudo du participant.
        """
        try:
            query = text(
                f"delete from TERMINE where id_parcours={id_parcours} and id_participant={id_participant}")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as exp:
            print("la connexion a échoué, supprimer termine")
            print(exp)
            return None
