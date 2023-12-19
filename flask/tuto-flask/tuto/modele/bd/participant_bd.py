from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))

from participant import Participant


class Participant_bd:
    def __init__(self,conx):
        """
            Initialise une instance de la classe Participant_bd avec une connexion à la base de données.

            param conx: Objet de connexion à la base de données.
        """
        self.cnx=conx

    def get_all_participant(self):
        """
            Récupère tous les participants depuis la base de données.

            return: Une liste d'objets Participant représentant les participants.
        """
        try:
            query = text("select id_participant,pseudo, email, mdp from PARTICIPANT")
            resultat = self.cnx.execute(query)
            participant=[]
            for id_participant,pseudo, email, mdp in resultat:
                participant.append(Participant(id_participant,pseudo, email, mdp))
            return participant
        except Exception as e:
            print(f"Erreur lors de la récupération des participants : {e}")
            return None
        
    def get_par_participant(self,id_participant):
        """
            Récupère un participant spécifique en fonction de son ID.

            param id_participant: ID du participant que l'on souhaite récupérer.
            return: Une liste contenant un objet Participant représentant le participant correspondant.
        """
        try:
            query = text("select id_participant,pseudo, email, mdp from PARTICIPANT where id_participant= "+str(id_participant))
            resultat = self.cnx.execute(query)
            participant=[]
            for id_participant,pseudo, email, mdp in resultat:
                participant.append(Participant(id_participant,pseudo, email, mdp))
            return participant
        except Exception as e:
            print("la connexion a échoué")
            return None

    def inserer_participant(self, idpart, pseudo, mail, mdp):
        """
            Insère un nouveau participant dans la base de données.

            param idpart: ID du participant.
            param pseudo: Pseudo du participant.
            param mail: Adresse email du participant.
            param mdp: Mot de passe du participant.
        """
        try:
            query = text(f"insert into PARTICIPANT values({str(idpart)} ,'{pseudo}', '{mail}' ,'{mdp}')")
            self.cnx.execute(query)
            self.cnx.commit()
            print("Reussi")
        except Exception as e:
            print("La connexion a échoué")
            return None


    def get_prochain_id_participant(self):
        """
            Récupère l'ID disponible pour le prochain participant à insérer dans la base de données.
    
            return: L'ID du prochain participant.
        """
        try:
            query = text("SELECT MAX(id_participant) as m FROM PARTICIPANT")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                return int(result.m) + 1
        except Exception as e:
            print("La connexion a échoué shushduz")
            return None

