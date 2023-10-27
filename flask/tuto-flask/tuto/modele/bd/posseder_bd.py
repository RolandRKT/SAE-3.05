from connexion import cnx
from sqlalchemy.sql.expression import text

import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from posseder import Posseder

class Posseder_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_posseder(self):
        try:
            query = text("select * from POSSEDER")
            resultat = self.cnx.execute(query)
            composition=[]
            for ide,idi in resultat:
                composition.append(Posseder(ide,idi))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def get_posseder_by_idinteret(self,idinteret):
        try:
            query = text("select * from POSSEDER where id_interet = "+str(idinteret))
            resultat = self.cnx.execute(query)
            composition=[]
            for ide,idi in resultat:
                composition.append(Posseder(ide,idi))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def get_posseder_by_etape(self,idetape):
        try:
            query = text("select * from POSSEDER where id_etape = "+str(idetape))
            resultat = self.cnx.execute(query)
            composition=[]
            for ide,idi in resultat:
                composition.append(Posseder(ide,idi))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def inserer_possede(self,idetape,idinteret):
        try:
            query = text(f"insert into POSSEDER values({str(idetape)} , {str(idinteret)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("la connexion a échoué")
            return None
