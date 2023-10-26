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
        
    
    def inserer_image(self,idimage,nomimage,img_data,nomfic):
        try:
            query = text("insert into IMAGE values("+idimage+" , "+nomimage+" ,"+img_data+" , "+nomfic+")")
            cnx.execute(query)
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_prochain_id_image(self):
        try:
            query = text("select max(id_image) as m from IMAGE")
            result = cnx.execute(query)
            return result[0]+1
        except Exception as e:
            print("la connexion a échoué")
            return None