from ..connexion import cnx
from Modele.code_model.participant import Participant
from sqlalchemy.sql.expression import text

class Participant_bd:
    def get_all_participant(self):
        try:
            query = text("select id_participant, email, mdp from PARTICIPANT")
            resultat = cnx.execute(query)
            participant=[]
            for id_participant, email, mdp in resultat:
                participant.append(participant(id_participant, email, mdp))
            return participant
        except Exception as e:
            print("la connexion a échoué")

            return None
        
    def get_par_participant(self,id_participant):
        try:
            query = text("select id_participant, email, mdp from PARTICIPANT where id_participant= "+id_participant)
            resultat = cnx.execute(query)
            participant=[]
            for id_participant, email, mdp in resultat:
                participant.append(participant(id_participant, email, mdp))
            return participant
        except Exception as e:
            print("la connexion a échoué")
            return None