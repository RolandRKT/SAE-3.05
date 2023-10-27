from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from etape import Etape

class Etape_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_etape(self):
        try:
            query = text("select * from ETAPE")
            resultat = self.cnx.execute(query)
            composition=[]
            for ide,nom,idph,local in resultat:
                composition.append(Etape(ide,nom,idph,local))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_par_photo_etape(self,idph):
        try:
            query = text("select * from ETAPE where id_photo = "+str(idph))
            resultat = self.cnx.execute(query)
            composition=[]
            for ide,nom,idp,local in resultat:
                composition.append(Etape(ide,nom,idp,local))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def inserer_etape(self,idetape,nometape,localisation,idimage):
        try:
            query = text(f"insert into ETAPE values({str(idetape)},'{nometape}','{localisation}' , {str(idimage)})")
            self.cnx.execute(query)
            self.cnx.commit()

        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_prochain_id_etape(self):
        try:
            query = text("select max(id_etape) as m from ETAPE")
            result = self.cnx.execute(query)
            return result[0]+1
        except Exception as e:
            print("la connexion a échoué")
            return None