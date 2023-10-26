from ..connexion import cnx
from Modele.code_model.image import Image
from sqlalchemy.sql.expression import text

class Image_bd:
    def get_all_image(self):
        try:
            query = text("select id_image, nom_image, img_data, nom_fic from IMAGE")
            resultat = cnx.execute(query)
            image=[]
            for id_image, nom, img_d, img_f in resultat:
                image.append(Image(id_image, nom, img_f, img_d))
            return image
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def get_par_image(self,id_image):
        try:
            query = text("select id_image, nom_image, img_data, nom_fic from IMAGE where id_image= "+id_image)
            resultat = cnx.execute(query)
            image=[]
            for id_image, nom, img_d, img_f in resultat:
                image.append(Image(id_image, nom, img_f, img_d))
            return image
        except Exception as e:
            print("la connexion a échoué")
            return None