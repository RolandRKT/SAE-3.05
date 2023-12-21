"""
    Fichier permettant la connexion avec la bd pour la composition.
"""
import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))

from composer import Composer


class Composer_bd:

    def __init__(self, conx):
        """
            Initialise une instance de la classe Composer_bd avec une connexion à la base de données.

            param conx: Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_composition(self):
        """
            Récupère toutes les compositions de parcours et d'étapes dans la base de données.

            return: Une liste d'objets Composer représentant les compositions.
        """
        try:
            query = text("select id_parcours, id_etape,numero from COMPOSER")
            resultat = self.cnx.execute(query)
            composition = []
            for idp, ide, numero in resultat:
                composition.append(Composer(idp, ide, numero))
            return composition
        except Exception as exp:
            print("la connexion a échoué, get_all_composition")
            print(exp)
            return None

    def get_par_etape_composition(self, ide):
        """
            Récupère les compositions associées à une étape spécifique.

            param ide: ID de l'étape pour laquelle on veut récupérer les compositions.
            return: Une liste d'objets Composer représentant les compositions pour l'étape donnée.
        """
        try:
            query = text(
                "select id_parcours, id_etape,numero from COMPOSER where id_etape= "
                + str(ide))
            resultat = self.cnx.execute(query)
            composition = []
            for idp, ide, numero in resultat:
                composition.append(Composer(idp, ide, numero))
            return composition
        except Exception as exp:
            print("la connexion a échoué, get_par_etape_composition")
            print(exp)
            return None

    def get_par_parcour_composition(self, idp):
        """
            Récupère les compositions associées à un parcours spécifique.

            param idp: ID du parcours pour lequel on veut récupérer les compositions.
            return: Une liste d'objets Composer représentant les compositions pour le parcours donné.
        """
        try:
            query = text(
                "select id_parcours, id_etape,numero from COMPOSER where id_parcours= "
                + str(idp))
            resultat = self.cnx.execute(query)
            composition = []
            for idp, ide, numero in resultat:
                composition.append(Composer(idp, ide, numero))
            return composition
        except Exception as exp:
            print("la connexion a échoué, get_par_parcour_composition")
            print(exp)
            return None

    def inserer_compose(self, idparc, ide, numero):
        """
            Insère une nouvelle composition de parcours et d'étape dans la base de données.

            param idparc: ID du parcours à composer.
            param ide: ID de l'étape à composer.
            param numero: Numéro d'ordre de la composition.
        """
        try:
            print(idparc, ide, numero)
            query = text(
                f"insert into COMPOSER values({str(idparc)} , {str(ide)},{str(numero)})"
            )
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as exp:
            print("la connexion a échoué, inserer_compose")
            print(exp)
            return None
    
    def get_prochain_numero_composer(self, idparc):
        """
            Récupère le prochain numero à insérer dans la base de données.

            return: Le prochain numero de la table COMPOSER
        """
        try:
            query = text("select max(numero) as m from COMPOSER where id_parcours = " + str(idparc))
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as exp:
            print("la connexion a échoué, get_prochain_numero_composer")
            print(exp)
            return None

    def get_max_etape_composer(self, idP):
        """
            Cette methode va nous retourner le numero de la derniere etape dans un parcours donner
        """
        try:
            query = text(
                f"select max(numero) as m from COMPOSER where id_parcours={idP}"
            )
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m))
                return int(result.m)
        except Exception as exp:
            print("la connexion a échoué, max_etape_composer")
            print(exp)
            return None

    def supprimer_etape_parcours(self, id_parc, id_etape):
        try:
            # Récupérer le numéro de l'étape à supprimer
            query_get_numero = text(f"SELECT numero FROM COMPOSER WHERE id_parcours = '{str(id_parc)}' AND id_etape = '{str(id_etape)}'")
            result = self.cnx.execute(query_get_numero).fetchone()
            uery_get_numero = text(f"SELECT * FROM SUIVRE WHERE id_parcours = {id_parc}")
            result2 = self.cnx.execute(uery_get_numero)
            if result2 and result:
                deleted_numero = result[0]
                query_update_numeros = text(f"UPDATE SUIVRE SET num_etape = num_etape - 1 WHERE id_parcours = {id_parc} AND num_etape >= {deleted_numero} and num_etape>1")
                self.cnx.execute(query_update_numeros)
                self.cnx.commit()
            if result:
                deleted_numero = result[0] 

                # Supprimer l'étape
                query_delete_etape = text(f"DELETE FROM COMPOSER WHERE id_parcours = '{str(id_parc)}' AND id_etape= '{str(id_etape)}'")                
                self.cnx.execute(query_delete_etape)
                self.cnx.commit()

                # Décrémenter les numéros des étapes suivantes
                query_update_numeros = text(f"UPDATE COMPOSER SET numero = numero - 1 WHERE id_parcours = '{str(id_parc)}' AND numero > {deleted_numero}")
                self.cnx.execute(query_update_numeros)
                self.cnx.commit()

        except Exception as exp:
            print("Erreur lors de la suppression de la composition :", str(exp))
