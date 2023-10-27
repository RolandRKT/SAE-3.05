from connexion import cnx

from sqlalchemy.sql.expression import text

import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from suivre import Suivre

class Suivre_bd:
    def get_all_suivre(self):
        try:
            query = text("select id_participant, id_parcours, note, comm from SUIVRE")
            resultat = self.cnx.execute(query)
            suivre=[]
            for id_participant, id_parcours, note, comm in resultat:
                suivre.append(Suivre(id_participant, id_parcours, note, comm))
            return suivre
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def get_par_suivre_parcours(self,id_parcours):
        try:
            query = text("select id_participant, id_parcours, note, comm from SUIVRE where id_parcours= "+str(id_parcours))
            resultat = self.cnx.execute(query)
            suivre=[]
            for id_participant, id_parcours, note, comm in resultat:
                suivre.append(Suivre(id_participant, id_parcours, note, comm))
            return suivre
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def get_par_suivre_participant(self,id_participant):
        try:
            query = text("select id_participant, id_parcours, note, comm from SUIVRE where id_participant= "+str(id_participant))
            resultat = self.cnx.execute(query)
            suivre=[]
            for id_participant, id_parcours, note, comm in resultat:
                suivre.append(Suivre(id_participant, id_parcours, note, comm))
            return suivre
        except Exception as e:
            print("la connexion a échoué")
            return None

    def inserer_suivre(self,id_part,id_parc,note,comm):
        try:
            query = text(f"insert into SUIVRE values({str(id_part)} , {str(id_parc)},{str(note)} , '{comm}'")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("la connexion a échoué")
            return None
