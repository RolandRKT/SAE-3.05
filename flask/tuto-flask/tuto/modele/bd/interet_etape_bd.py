from sqlalchemy.sql.expression import text
import sys
import os
from connexion import cnx

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))



from interet_etape import Interet_etape

class Interet_etape_bd:
    def __init__(self,conx):
        self.cnx=conx
        
    def get_all_interet_etape(self):
        try:
            query = text("select * from INTERETETAPE")
            resultat = self.cnx.execute(query)
            composition=[]
            for idi,nom,desc in resultat:
                composition.append(Interet_etape(idi,nom,desc))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def get_par_photo_etape(self,idi):
        try:
            query = text("select * from INTERETETAPE where id_interet = "+str(idi))
            resultat = self.cnx.execute(query)
            composition=[]
            for id,nom,desc in resultat:
                composition.append(Interet_etape(id,nom,desc))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    
    def inserer_interet_etape(self,idi,nom_interet,desc):
        try:
            query = text(f"INSERT INTO INTERETETAPE VALUES({str(idi)}, '{nom_interet}', '{desc}')")
    
            print(query)
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_prochain_id_interet_etape(self):
        try:
            query = text("select max(id_interet) as m from INTERETETAPE")
            result = self.cnx.execute(query)
            return result[0]+1
        except Exception as e:
            print("la connexion a échoué")
            return None
        

def test():
    j=Interet_etape_bd(cnx)
    j.inserer_interet_etape(2,"ahmett","baba")
    print(j.get_all_interet_etape())
    cnx.close()

test()