from ..connexion import cnx
from Modele.code_model.parcours import Parcours
from sqlalchemy.sql.expression import text

class Parcours_bd:
    def get_all_parcours(self):
        try:
            query = text("select id_parcours, nom_parcours, date_debut, date_fin, description_parcours, id_image from PARCOURS")
            resultat = cnx.execute(query)
            parcours=[]
            for id_parcours, nom, date_d, date_f, desc, id_img in resultat:
                parcours.append(Parcours(id_parcours, nom, date_d, date_f, desc, id_img))
            return parcours
        except Exception as e:
            return None
        
    def get_par_parcours(self,id_parcours):
        try:
            query = text("select id_parcours, nom_parcours, img_data, nom_fic from PARCOURS where id_parcours= "+id_parcours)
            resultat = cnx.execute(query)
            parcours=[]
            for id_parcours, nom, date_d, date_f, desc, id_img in resultat:
                parcours.append(Parcours(id_parcours, nom, date_d, date_f, desc, id_img))
            return parcours
        except Exception as e:
            return None
        
    def get_par_parcours_image(self,id_image):
        try:
            query = text("select id_parcours, nom_parcours, img_data, nom_fic from PARCOURS where id_image= "+id_image)
            resultat = cnx.execute(query)
            parcours=[]
            for id_parcours, nom, date_d, date_f, desc, id_img in resultat:
                parcours.append(Parcours(id_parcours, nom, date_d, date_f, desc, id_img))
            return parcours
        except Exception as e:
            return None