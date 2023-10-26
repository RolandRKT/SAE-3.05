from ..connexion import cnx
from Modele.code_model.suivre import Suivre
from sqlalchemy.sql.expression import text

class Suivre_bd:
    def get_all_suivre(self):
        try:
            query = text("select id_participant, id_parcours, note, comm from SUIVRE")
            resultat = cnx.execute(query)
            suivre=[]
            for id_participant, id_parcours, note, comm in resultat:
                suivre.append(Suivre(id_participant, id_parcours, note, comm))
            return suivre
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def get_par_suivre_parcours(self,id_parcours):
        try:
            query = text("select id_participant, id_parcours, note, comm from SUIVRE where id_parcours= "+id_parcours)
            resultat = cnx.execute(query)
            suivre=[]
            for id_participant, id_parcours, note, comm in resultat:
                suivre.append(Suivre(id_participant, id_parcours, note, comm))
            return suivre
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def get_par_suivre_participant(self,id_participant):
        try:
            query = text("select id_participant, id_parcours, note, comm from SUIVRE where id_participant= "+id_participant)
            resultat = cnx.execute(query)
            suivre=[]
            for id_participant, id_parcours, note, comm in resultat:
                suivre.append(Suivre(id_participant, id_parcours, note, comm))
            return suivre
        except Exception as e:
            print("la connexion a échoué")
            return None