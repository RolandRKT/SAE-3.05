from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))

from parcours import Parcours


class Parcours_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_parcours(self):
        try:
            query = text("select id_parcours, nom_parcours, duree, description_parcours, id_image from PARCOURS")
            resultat = self.cnx.execute(query)
            parcours=[]
            for id_parcours, nom, duree, desc, id_img in resultat:
                parcours.append(Parcours(id_parcours, nom,duree, desc, id_img))
            return parcours
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def get_par_parcours(self,id_parcours):
        try:
            query = text("select id_parcours, nom_parcours,duree,description_parcours, id_img from PARCOURS where id_parcours= "+str(id_parcours))
            resultat = self.cnx.execute(query)
            parcours=[]
            for id_parcours, nom,duree, desc, id_img in resultat:
                parcours.append(Parcours(id_parcours, nom, duree, desc, id_img))
            return parcours
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def get_par_parcours_image(self,id_image):
        try:
            query = text("select * from PARCOURS where id_image= "+str(id_image))
            resultat = self.cnx.execute(query)
            parcours=[]
            for id_parcours, nom, duree, desc, id_img in resultat:
                parcours.append(Parcours(id_parcours, nom,duree, desc, id_img))
            return parcours
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def inserer_etape(self,idparc,nomparc,duree,descparc,idimg):
        try:
            query = text(f"insert into PARCOURS values({str(idparc)} , '{nomparc}' ,'{duree}' , '{descparc}','{str(idimg)}')")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def get_prochain_id_parcours(self):
        try:
            query = text("select max(id_parcours) as m from PARCOURS")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("la connexion a échoué")
            return None