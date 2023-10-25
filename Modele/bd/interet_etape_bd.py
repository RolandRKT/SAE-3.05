from ..connexion import cnx
from Modele.code_model.interet_etape import Interet_etape
from sqlalchemy.sql.expression import text

class Interet_etape_bd:
    def get_all_interet_etape(self):
        try:
            query = text("select * from INTERETETAPE")
            resultat = cnx.execute(query)
            composition=[]
            for idi,nom,desc in resultat:
                composition.append(Interet_etape(idi,nom,desc))
            return composition
        except Exception as e:
            return None
        
    def get_par_photo_etape(self,idi):
        try:
            query = text("select * from INTERETETAPE where id_interet = "+idi)
            resultat = cnx.execute(query)
            composition=[]
            for id,nom,desc in resultat:
                composition.append(Interet_etape(id,nom,desc))
            return composition
        except Exception as e:
            return None
    
