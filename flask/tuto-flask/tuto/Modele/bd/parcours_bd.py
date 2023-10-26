from ..connexion import cnx
from Modele.code_model.parcours import Parcours
from sqlalchemy.sql.expression import text

class Parcours_bd:
    def get_all_parcours(self):
        try:
            query = text("select id_parcours, nom_parcours, duree, description_parcours, id_image from PARCOURS")
            resultat = cnx.execute(query)
            parcours=[]
            for id_parcours, nom, duree, desc, id_img in resultat:
                parcours.append(Parcours(id_parcours, nom,duree, desc, id_img))
            return parcours
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def get_par_parcours(self,id_parcours):
        try:
            query = text("select id_parcours, nom_parcours,duree,description_parcours, id_img from PARCOURS where id_parcours= "+id_parcours)
            resultat = cnx.execute(query)
            parcours=[]
            for id_parcours, nom,duree, desc, id_img in resultat:
                parcours.append(Parcours(id_parcours, nom, duree, desc, id_img))
            return parcours
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def get_par_parcours_image(self,id_image):
        try:
            query = text("select * from PARCOURS where id_image= "+id_image)
            resultat = cnx.execute(query)
            parcours=[]
            for id_parcours, nom, duree, desc, id_img in resultat:
                parcours.append(Parcours(id_parcours, nom,duree, desc, id_img))
            return parcours
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    
    def inserer_etape(self,idparc,nomparc,duree,descparc,idimg):
        try:
            query = text("insert into PARCOURS values("+idparc+" , "+nomparc+" ,"+duree+" , "+descparc+" , "+idimg+")")
            cnx.execute(query)
        except Exception as e:
            print("la connexion a échoué")
            return None
