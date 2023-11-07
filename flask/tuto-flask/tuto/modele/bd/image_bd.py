from connexion import cnx
from sqlalchemy.sql.expression import text
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))

from image import Image


class Image_bd:
    def __init__(self,conx):
        """
            Initialise une instance de la classe Image_bd avec une connexion à la base de données.

            param conx: Objet de connexion à la base de données.
        """
        self.cnx=conx


    def get_all_image(self):
        """
            Récupère toutes les images depuis la base de données.

            return: Une liste d'objets Image représentant les images.
        """
        try:
            query = text("select id_image, nom_image, img_data, nom_fic from IMAGE")
            resultat = self.cnx.execute(query)
            image=[]
            for id_image, nom, img_d, img_f in resultat:
                image.append(Image(id_image, nom, img_f, img_d))
            return image
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def get_par_image(self,id_image):
        """
            Récupère une image spécifique en fonction de son ID.

            param id_image: ID de l'image que l'on souhaite récupérer.
            return: Une liste contenant un objet Image représentant l'image correspondante.
        """
        try:
            query = text("select id_image, nom_image, img_data, nom_fic from IMAGE where id_image= "+str(id_image))
            resultat = self.cnx.execute(query)
            image=[]
            for id_image, nom, img_d, img_f in resultat:
                image.append(Image(id_image, nom, img_f, img_d))
            return image
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    
    def inserer_image(self,idimage,nomimage,img_data,nomfic):
        """
            Insère une nouvelle image dans la base de données.

            param idimage: ID de l'image.
            param nomimage: Nom de l'image.
            param img_data: Données de l'image.
            param nomfic: Nom du fichier image.
        """
        try:
            query = text(f"insert into IMAGE values({str(idimage)}, '{nomimage} , '{img_data}' , '{nomfic}')")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("la connexion a échoué")
            return None

    def get_prochain_id_image(self):
        """
            Récupère l'ID disponible pour la prochaine image à insérer dans la base de données.

            return: L'ID de la prochaine image.
        """
        try:
            query = text("select max(id_image) as m from IMAGE")
            result = self.cnx.execute(query)
            return result[0]+1
        except Exception as e:
            print("la connexion a échoué")
            return None