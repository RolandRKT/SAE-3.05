from ..connexion import cnx
from Modele.code_model.posseder import Posseder
from sqlalchemy.sql.expression import text

class Posseder_bd:
    def get_all_posseder(self):
        try:
            query = text("select * from POSSEDER")
            resultat = cnx.execute(query)
            composition=[]
            for ide,idi in resultat:
                composition.append(Posseder(ide,idi))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def get_posseder_by_idinteret(self,idinteret):
        try:
            query = text("select * from POSSEDER where id_interet = "+idinteret)
            resultat = cnx.execute(query)
            composition=[]
            for ide,idi in resultat:
                composition.append(Posseder(ide,idi))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def get_posseder_by_etape(self,idetape):
        try:
            query = text("select * from POSSEDER where id_etape = "+idetape)
            resultat = cnx.execute(query)
            composition=[]
            for ide,idi in resultat:
                composition.append(Posseder(ide,idi))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def inserer_possede(self,idetape,idinteret):
        try:
            query = text("insert into POSSEDER values("+idetape+" , "+idinteret+")")
            cnx.execute(query)
        except Exception as e:
            print("la connexion a échoué")
            return None
