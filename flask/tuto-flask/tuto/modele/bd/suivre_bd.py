from connexion import cnx

from sqlalchemy.sql.expression import text

import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from suivre import Suivre

class Suivre_bd:    
    def __init__(self,conx):
        """
            Initialise une instance de la classe Suivre_bd avec une connexion à la base de données.

            param conx: Objet de connexion à la base de données.
        """
        self.cnx=conx
    def get_all_suivre(self):
        """
            Récupère toutes les entrées de suivi depuis la base de données.

            return: Une liste d'objets Suivre représentant les entrées de suivi.
        """
        try:
            query = text("select id_participant, id_parcours, note, comm,num_etape from SUIVRE")
            resultat = self.cnx.execute(query)
            suivre=[]
            for id_participant, id_parcours, note, comm,num_etape in resultat:
                suivre.append(Suivre(id_participant, id_parcours, note, comm,num_etape))
            return suivre
        except Exception as e:
            print("la connexion a échoué")
            return None
        
    def get_par_suivre_parcours(self,id_parcours):
        """
            Récupère les entrées de suivi liées à un parcours spécifique.

            param id_parcours: ID du parcours pour lequel on souhaite récupérer les entrées de suivi.
            return: Une liste d'objets Suivre représentant les entrées de suivi liées au parcours donné.
        """
        try:
            query = text("select id_participant, id_parcours, note, comm,num_etape from SUIVRE where id_parcours= "+str(id_parcours))
            resultat = self.cnx.execute(query)
            suivre=[]
            for id_participant, id_parcours, note, comm,num_etape in resultat:
                suivre.append(Suivre(id_participant, id_parcours, note, comm,num_etape))
            return suivre
        except Exception as e:
            print("la connexion a échoué")
            return None
    
    def get_par_suivre_participant(self,id_participant):
        """
            Récupère les entrées de suivi liées à un participant spécifique.
    
            param id_participant: ID du participant pour lequel on souhaite récupérer les entrées de suivi.
            return: Une liste d'objets Suivre représentant les entrées de suivi liées au participant donné.
        """
        try:
            query = text("select id_participant, id_parcours, note, comm,num_etape from SUIVRE where id_participant= "+str(id_participant))
            resultat = self.cnx.execute(query)
            suivre=[]
            for id_participant, id_parcours, note, comm,num_etape in resultat:
                suivre.append(Suivre(id_participant, id_parcours, note, comm,num_etape))
            return suivre
        except Exception as e:
            print("la connexion a échoué")
            return None

    def inserer_suivre(self,id_part,id_parc,note,comm,num_etape):
        """
            Insère une nouvelle entrée de suivi dans la base de données.

            param id_part: ID du participant lié à l'entrée de suivi.
            param id_parc: ID du parcours lié à l'entrée de suivi.
            param note: Note attribuée à l'entrée de suivi.
            param comm: Commentaire associé à l'entrée de suivi.
            param num_etape: Numéro de l'étape liée à l'entrée de suivi.
        """
        try:
            query = text(f"insert into SUIVRE values({str(id_part)} , {str(id_parc)},{str(note)} , '{comm}',{str(num_etape)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("la connexion a échoué")
            return None
