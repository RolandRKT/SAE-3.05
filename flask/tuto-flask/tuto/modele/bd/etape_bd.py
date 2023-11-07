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
            etapes=[]
            for ide,nom,idph,coordX, coordY in resultat:
                etapes.append(Etape(ide,nom,idph,coordX, coordY))
            return etapes
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_par_photo_etape(self,idph):
        try:
            query = text("select * from ETAPE where id_photo = "+str(idph))
            resultat = self.cnx.execute(query)
            etapes=[]
            for ide,nom,idp,coordX, coordY in resultat:
                etapes.append(Etape(ide,nom,idp,coordX, coordY))
            return etapes
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def inserer_etape(self,idetape,nometape,idimage, coordX, coordY):
        try:
            query = text(f"insert into ETAPE values({str(idetape)},'{nometape}', {str(idimage)}, '{coordX}', '{coordY}')")
            self.cnx.execute(query)
            self.cnx.commit()

        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_prochain_id_etape(self):
        try:
            query = text("select max(id_etape) as m from ETAPE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("la connexion a échoué")
            return None