from .connexion import cnx
from modele.code_model.composer import Composer
from sqlalchemy.sql.expression import text

class Composer_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_composition(self):
        try:
            query = text("select id_parcours, id_etape from COMPOSER")
            resultat = self.cnx.execute(query)
            composition=[]
            for idp,ide in resultat:
                composition.append(Composer(idp,ide))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_par_etape_composition(self,ide):
        try:
            query = text("select id_parcours, id_etape from COMPOSER where id_etape= "+str(ide))
            resultat = self.cnx.execute(query)
            composition=[]
            for idp,ide in resultat:
                composition.append(Composer(idp,ide))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def get_par_parcour_composition(self,idp):
        try:
            query = text("select id_parcours, id_etape from COMPOSER where id_parcours= "+str(idp))
            resultat = self.cnx.execute(query)
            composition=[]
            for idp,ide in resultat:
                composition.append(Composer(idp,ide))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def inserer_compose(self,idparc,idinter):
        try:
            query = text("insert into COMPOSER values("+str(idparc)+" , "+str(idinter)+")")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("la connexion a échoué")
            return None
    