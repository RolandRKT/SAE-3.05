from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))

from composer import Composer

class Composer_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_composition(self):
        try:
            query = text("select id_parcours, id_etape,numero from COMPOSER")
            resultat = self.cnx.execute(query)
            composition=[]
            for idp,ide,numero in resultat:
                composition.append(Composer(idp,ide,numero))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_par_etape_composition(self,ide):
        try:
            query = text("select id_parcours, id_etape,numero from COMPOSER where id_etape= "+str(ide))
            resultat = self.cnx.execute(query)
            composition=[]
            for idp,ide,numero in resultat:
                composition.append(Composer(idp,ide,numero))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def get_par_parcour_composition(self,idp):
        try:
            query = text("select id_parcours, id_etape,numero from COMPOSER where id_parcours= "+str(idp))
            resultat = self.cnx.execute(query)
            composition=[]
            for idp,ide,numero in resultat:
                composition.append(Composer(idp,ide,numero))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def inserer_compose(self,idparc,ide,numero):
        try:
            query = text(f"insert into COMPOSER values({str(idparc)} , {str(ide)},{str(numero)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("la connexion a échoué")
            return None
    