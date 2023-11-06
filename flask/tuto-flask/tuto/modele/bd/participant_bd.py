from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))

from participant import Participant


class Participant_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_participant(self):
        try:
            query = text("select id_participant,pseudo, email, mdp from PARTICIPANT")
            resultat = self.cnx.execute(query)
            participant=[]
            for id_participant,pseudo, email, mdp in resultat:
                participant.append(Participant(id_participant,pseudo, email, mdp))
            return participant
        except Exception as e:
            print("aaaaaaaaaaaaaaah")
            return None
        
    def get_par_participant(self,id_participant):
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
        try:
            query = text(f"insert into PARTICIPANT values({str(idpart)} ,'{pseudo}', '{mail}' ,'{mdp}')")
            self.cnx.execute(query)
            self.cnx.commit()
            print("Reussi")
        except Exception as e:
            print("La connexion a échoué")
            return None


    def get_prochain_id_participant(self):
        try:
            query = text("SELECT MAX(id_participant) as m FROM PARTICIPANT")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("La connexion a échoué shushduz")
            return None
