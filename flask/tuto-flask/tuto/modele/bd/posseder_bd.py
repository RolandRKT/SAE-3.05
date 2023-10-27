from .connexion import cnx
from modele.code_model.posseder import Posseder
from sqlalchemy.sql.expression import text

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
            query = text("insert into POSSEDER values("+str(idetape)+" , "+str(idinteret)+")")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("la connexion a échoué")
            return None
