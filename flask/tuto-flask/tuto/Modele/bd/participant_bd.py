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

    def inserer_participant(self,idpart,mail,mdp):
        try:
            query = text("insert into PARTICIPANT values("+idpart+" , "+mail+" ,"+mdp+")")
            cnx.execute(query)
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_prochain_id_participant(self):
        try:
            query = text("select max(id_participant) as m from PARTICIPANT")
            result = cnx.execute(query)
            return result[0]+1
        except Exception as e:
            print("la connexion a échoué")
            return None