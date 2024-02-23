"""
    Fichier qui contient la classe Termine_bd permettant de récupérer les données de la table TERMINE de la base de données.
"""
import os
import sys
from flask import jsonify
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from termine import Termine

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))
from parcours_bd import Parcours_bd
from connexion import cnx

PARCOURS = Parcours_bd(cnx)


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

    def get_all_termine(self, id_participant):
        """
            Récupère tous les termine depuis la base de données.
        """
        try:
            query = text(
                f"select * from TERMINE where id_participant={id_participant}")
            resultat = self.cnx.execute(query)
            termine = []
            for id_parcours, id_participant, note, comm in resultat:
                termine.append(Termine(id_parcours, id_participant, note,
                                       comm))
            return termine
        except Exception as exp:
            print("la connexion a échoué, all termine")
            print(exp)
            return None

    def get_termine_id_part(self, id_participant, id_parcours):
        """
            Renvoie un boolean qui indique si le parcours existe dans la table TERMINE
        """
        try:
            query = text(
                f"select * from TERMINE where id_participant={id_participant} and id_parcours={id_parcours}"
            )
            resultat = self.cnx.execute(query)
            termine = []
            for id_parcours, id_participant, note, comm in resultat:
                termine.append(Termine(id_parcours, id_participant, note,
                                       comm))
            if len(termine) == 0:
                return False
            else:
                return True
        except Exception as exp:
            print("la connexion a échoué, all termine")
            print(exp)
            return False

    def inserer_termine(self, id_parcours, id_participant, note, comm):
        """
        Insère un termine dans la base de données.
        """
        try:
            query = text(
                "INSERT INTO TERMINE(id_parcours, id_participant, note, comm) VALUES (:id_parcours, :id_participant, :note, :comm)"
            )
            query_delete_suivre = text(
                "DELETE FROM SUIVRE WHERE id_parcours=:id_parcours AND id_participant=:id_participant"
            )

            params = {
                'id_parcours': id_parcours,
                'id_participant': id_participant,
                'note': note,
                'comm': comm
            }

            self.cnx.execute(query, params)
            self.cnx.execute(query_delete_suivre, params)
            self.cnx.commit()
        except Exception as exp:
            print("La connexion a échoué, inserer termine")
            print(exp)
            return None

    def get_note_comm(self, id_parcours):
        """
            Récupère la note et le commentaire d'un parcours.
        """
        try:
            query = text(
                f"select id_parcours, pseudo,note, comm from TERMINE NATURAL JOIN PARTICIPANT where id_parcours={id_parcours}"
            )
            resultat = self.cnx.execute(query)
            liste = []
            for idparc, pseudo, note, comm in resultat:
                liste.append((idparc, pseudo, note, comm))
            return liste
        except Exception as exp:
            print("la connexion a échoué, get note comm")
            print(exp)
            return []

    def supprimer_termine(self, id_parcours, id_participant):
        """
            Supprime une ligne de la table TERMINE en fonction de l'id de parcours et du pseudo du participant.
        """
        try:
            query = text(
                f"delete from TERMINE where id_parcours={id_parcours} and id_participant={id_participant}"
            )
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as exp:
            print("la connexion a échoué, supprimer termine")
            print(exp)
            return None


    def get_note_comm_parc_part(self, id_parcours, id_participant):
        """
            Récupère la note et le commentaire d'un parcours.
        """
        try:
            query = text(
                f"select note, comm from TERMINE where id_parcours={id_parcours} and id_participant={id_participant}"
            )
            resultat = self.cnx.execute(query)
            print(resultat, "kd ",query)
            liste=[]
            for note, comm in resultat:
                print(note,type(note), int(note))
                liste.append((int(note), comm))
            return liste
        except Exception as exp:
            print("la connexion a échoué, get_note_comm_parc_part")
            print(exp)
            return None
        

    def mettre_a_jour_note_comm(self, id_parcours, id_participant, note, comm):
        """
            Met à jour la note et le commentaire d'un parcours.
        """
        try:
            query = text(
                "UPDATE TERMINE SET note=:note, comm=:comm WHERE id_parcours=:id_parcours AND id_participant=:id_participant"
            )
            params = {
                'id_parcours': id_parcours,
                'id_participant': id_participant,
                'note': note,
                'comm': comm
            }
            self.cnx.execute(query, params)
            self.cnx.commit()
            
        except Exception as exp:
            print("la connexion a échoué, mettre à jour note comm")
            print(exp)
            return None
        
    def get_nb_personne(self, id_parcours):
        """
            Récupère le nombre de personne ayant terminé le parcours.
        """
        try:
            query = text(
                f"select count(*) from TERMINE where id_parcours={id_parcours}"
            )
            resultat = self.cnx.execute(query)
            for nb in resultat:
                return nb[0]
        except Exception as exp:
            print("la connexion a échoué, get_nb_personne")
            print(exp)
            return None
        
    def get_note_moyenne(self, id_parcours):
        """
            Récupère la note moyenne du parcours.
        """
        try:
            query = text(
                f"select avg(note) from TERMINE where id_parcours={id_parcours}"
            )
            resultat = self.cnx.execute(query)
            for nb in resultat:
                # permet d'arrondir à 2 chiffres après la virgule
                c= round(nb[0], 2)
                return c
        except Exception as exp:
            print("la connexion a échoué, get_note_moyenne")
            print(exp)
            return None