from ..connexion import cnx
from Modele.code_model.etape import Etape
from sqlalchemy.sql.expression import text

class Etape_bd:
    def get_all_etape(self):
        try:
            query = text("select * from ETAPE")
            resultat = cnx.execute(query)
            composition=[]
            for ide,nom,idph,local in resultat:
                composition.append(Etape(ide,nom,idph,local))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_par_photo_etape(self,idph):
        try:
            query = text("select * from ETAPE where id_photo = "+idph)
            resultat = cnx.execute(query)
            composition=[]
            for ide,nom,idp,local in resultat:
                composition.append(Etape(ide,nom,idp,local))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def inserer_etape(self,idetape,nometape,localisation,idimage):
        try:
            query = text("insert into ETAPE values("+idetape+" , "+nometape+" ,"+localisation+" , "+idimage+")")
            cnx.execute(query)
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_prochain_id_etape(self):
        try:
            query = text("select max(id_etape) as m from ETAPE")
            result = cnx.execute(query)
            return result[0]+1
        except Exception as e:
            print("la connexion a échoué")
            return None