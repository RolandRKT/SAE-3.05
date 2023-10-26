from ..connexion import cnx
from Modele.code_model.composer import Composer
from sqlalchemy.sql.expression import text

class Composer_bd:
    def get_all_composition(self):
        try:
            query = text("select id_parcours, id_etape from COMPOSER")
            resultat = cnx.execute(query)
            composition=[]
            for idp,ide in resultat:
                composition.append(Composer(idp,ide))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_par_etape_composition(self,ide):
        try:
            query = text("select id_parcours, id_etape from COMPOSER where id_etape= "+ide)
            resultat = cnx.execute(query)
            composition=[]
            for idp,ide in resultat:
                composition.append(Composer(idp,ide))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def get_par_parcour_composition(self,idp):
        try:
            query = text("select id_parcours, id_etape from COMPOSER where id_parcours= "+idp)
            resultat = cnx.execute(query)
            composition=[]
            for idp,ide in resultat:
                composition.append(Composer(idp,ide))
            return composition
        except Exception as e:
            print("la connexion a échoué")
            return None