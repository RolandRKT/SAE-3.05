"""
    Ce fichier va nous permettre de prendre des valeurs
    des etapes de la bd.
"""
import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from etape import Etape


class Etape_bd:
    """
        La class Etape bd
    """

    def __init__(self, conx):
        """
            Initialise une instance de la classe Etape_bd avec une connexion à la base de données.

            param conx: Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_etape(self):
        """
            Récupère toutes les étapes depuis la base de données.

            return: Une liste d'objets Etape représentant les étapes.
        """
        try:
            query = text("select * from ETAPE")
            resultat = self.cnx.execute(query)
            etapes = []
            for ide, nom, idph, coordX, coordY, interet, question, reponse in resultat:
                etapes.append(Etape(ide, nom, idph, coordX, coordY, interet, question, reponse))
            return etapes
        except Exception as exp:
            print("la connexion a échoué, get_all_etape")
            print(exp)
            return None

    def get_par_photo_etape(self, idph):
        """
            Récupère les étapes associées à une photo spécifique.
            param idph: ID de la photo pour laquelle on veut récupérer les étapes.
            return: Une liste d'objets Etape représentant les étapes pour la photo donnée.
        """
        try:
            query = text("select * from ETAPE where id_photo = " + str(idph))
            resultat = self.cnx.execute(query)
            etapes = []
            for ide, nom, idp, coordX, coordY, interet, question, reponse in resultat:
                etapes.append(Etape(ide, nom, idp, coordX, coordY, interet, question, reponse))
            return etapes
        except Exception as exp:
            print("la connexion a échoué, get_par_photo_etape")
            print(exp)
            return None

    def inserer_etape(self, idetape, nometape, idimage, coordX, coordY,
                      interet, question=None, reponse=None):
        """
            Insère une nouvelle étape dans la base de données.

            param idetape: ID de l'étape.
            param nometape: Nom de l'étape.
            param coordX : coordonnée x de l'étape.
            param coordY : coordonnée y de l'étape.
            param idimage: ID de l'image associée à l'étape.
        """
        try:
            if interet is None:
                interet2 = 'null'
            else:
                interet2 = interet
            if (idimage is None):
                print(type(question))
                print(type(reponse))
                if question != None and reponse != None:
                    print("sans question")
                    query = text(
                    f"insert into ETAPE values({str(idetape)},'{nometape}', null, '{str(coordX)}', '{str(coordY)}','{str(interet2)}','{str(question)}','{str(reponse)}')"
                )
                else:
                    print("avec question")
                    query = text(
                        f"insert into ETAPE values({str(idetape)},'{nometape}', null, '{str(coordX)}', '{str(coordY)}','{str(interet2)}',null,null)"
                    )
            else:
                if question is not None and reponse is not None:
                    query = text(
                    f"insert into ETAPE values({str(idetape)},'{nometape}', {str(idimage)}, '{str(coordX)}', '{str(coordY)}','{str(interet2)}','{str(question)}','{str(reponse)}')"
                )
                else:
                    query = text(
                        f"insert into ETAPE values({str(idetape)},'{nometape}', {str(idimage)}, '{str(coordX)}', '{str(coordY)}','{str(interet2)}', null, null)"
                    )
            self.cnx.execute(query)
            self.cnx.commit()

        except Exception as exp:
            print("la connexion a échoué, inserer_etape")
            print(exp)
            return None

    def get_prochain_id_etape(self):
        """
            Récupère l'ID disponible pour la prochaine étape à insérer dans la base de données.

            return: L'ID de la prochaine étape.
        """
        try:
            query = text("select max(id_etape) as m from ETAPE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as exp:
            print("la connexion a échoué, get_prochain_id_etape")
            return None

    def get_par_id_etape(self, idetape):
        """
            Récupère une étape spécifique en fonction de son ID.

            param idetape: ID de l'étape que l'on souhaite récupérer.
            return: Une liste contenant un objet Etape représentant le parcours correspondant.
        """
        try:
            query = text("select * from ETAPE where id_etape = " +
                         str(idetape))
            resultat = self.cnx.execute(query)
            for ide, nom, idp, coordX, coordY, interet, question, reponse in resultat:
                return Etape(ide, nom, idp, coordX, coordY, interet, question, reponse)

            return None
        except Exception as exp:
            print("la connexion a échoué, get_par_id_etape")
            print(exp)
            return None

    def supprimer_etape_composer(self, idetape):
        """
            Supprime une étape de la table composer.
            param idetape: ID de l'étape que l'on souhaite supprimer.
        """
        try:
            query = text("delete from COMPOSER where id_etape = " +
                         str(idetape))
            query2 = text("delete from ETAPE where id_etape = " + str(idetape))
            query3 = text(
                "update SUIVRE set num_etape=num_etape-1 where num_etape>=(select num_etape from SUIVRE where id_etape="
                + str(idetape) + ")")
            query4 = text(
                "update COMPOSER set numero=numero-1 where numero>=(select numero from COMPOSER where id_etape="
                + str(idetape) + ")")

            self.cnx.execute(query)
            self.cnx.execute(query3)
            self.cnx.execute(query4)
            self.cnx.execute(query2)
            self.cnx.commit()
        except Exception as exp:
            print("la connexion a échoué, supprimer_etape_composer")
            print(exp)
            return None

    def supprimer_toutes_les_etapes_composer(self, cnx_parcours, id_etape):
        """
            Supprime toutes les étapes de la table composer.
            Args:
                param 
                    cnx_parcours: connexion à la table parcours
                    idetape: ID de l'étape que l'on souhaite supprimer.
        """
        try:
            for parc in cnx_parcours.get_all_parcours():
                # Récupére le numéro de l'étape à supprimer
                query_get_numero = text(
                    f"SELECT numero FROM COMPOSER WHERE id_parcours = {parc.get_id_parc()} AND id_etape = {id_etape}"
                )
                result = self.cnx.execute(query_get_numero).fetchone()
                uery_get_numero = text(
                    f"SELECT * FROM SUIVRE WHERE id_parcours = {parc.get_id_parc()}"
                )
                result2 = self.cnx.execute(uery_get_numero)
                if result2 and result:
                    deleted_numero = result[0]
                    query_update_numeros = text(
                        f"UPDATE SUIVRE SET num_etape = num_etape - 1 WHERE id_parcours = {parc.get_id_parc()} AND num_etape >= {deleted_numero} and num_etape>1"
                    )
                    self.cnx.execute(query_update_numeros)
                    self.cnx.commit()
                if result:
                    deleted_numero = result[0]
                    # Supprimer l'étape
                    query_delete_etape = text(
                        f"DELETE FROM COMPOSER WHERE id_parcours = {parc.get_id_parc()} AND id_etape= {id_etape}"
                    )
                    self.cnx.execute(query_delete_etape)
                    self.cnx.commit()
                    # Décrémenter les numéros des étapes suivantes
                    query_update_numeros = text(
                        f"UPDATE COMPOSER SET numero = numero - 1 WHERE id_parcours = {parc.get_id_parc()} AND numero > {deleted_numero}"
                    )
                    self.cnx.execute(query_update_numeros)
                    self.cnx.commit()

            query_delete_etape = text(
                f"DELETE FROM ETAPE WHERE id_etape= {id_etape}")
            self.cnx.execute(query_delete_etape)
            self.cnx.commit()
        except Exception as exp:
            print("Erreur lors de la suppression de la composition :",
                  str(exp))

    def update(self, nom_etape, interet, id_image, question="", reponse=""):
        """
            Cette fonction permet de changer certaine info
        """
        try:
            query = text(
                f"update ETAPE set nom_etape = :nom_etape where id_etape= :id_etape"
            )
            query2 = text(
                f"update ETAPE set interet = :interet where id_etape= :id_etape"
            )
            query3 = text(
                f"update ETAPE set id_image = :id_image where id_etape= :id_etape"
            )
            if question != "" and reponse != "":
                query4 = text(
                    f"update ETAPE set question = :question where id_etape= :id_etape"
                )
                query5 = text(
                    f"update ETAPE set reponse = :reponse where id_etape= :id_etape"
                )
                params4 = {
                "question": question,
                'id_etape': self.get_prochain_id_etape() - 1
                }
                params5 = {
                    "reponse": reponse,
                    'id_etape': self.get_prochain_id_etape() - 1
                }

            params1 = {
                'nom_etape': nom_etape,
                'id_etape': self.get_prochain_id_etape() - 1
            }
            params2 = {
                "interet": interet,
                'id_etape': self.get_prochain_id_etape() - 1
            }
            params3 = {
                "id_image": id_image,
                'id_etape': self.get_prochain_id_etape() - 1
            }
            

            self.cnx.execute(query, params1)
            self.cnx.execute(query2, params2)
            self.cnx.execute(query3, params3)
            if question != "" and reponse != "":
                self.cnx.execute(query4, params4)
                self.cnx.execute(query5, params5)
            self.cnx.commit()
        except Exception as exp:
            print("la connexion a échoué, update")
            print(exp)
            return None

    def update_par_id(self, id_etape, nom_etape, interet):
        """
            Cette fonction permet de changer certaine info
        """
        try:
            query = text(
                f"update ETAPE set nom_etape = :nom_etape where id_etape= :id_etape"
            )
            query2 = text(
                f"update ETAPE set interet = :interet where id_etape= :id_etape"
            )

            params1 = {'nom_etape': nom_etape, 'id_etape': id_etape}
            params2 = {"interet": interet, 'id_etape': id_etape}

            print("Lalala")
            self.cnx.execute(query, params1)
            self.cnx.execute(query2, params2)
            self.cnx.commit()
        except Exception as exp:
            print("la connexion a échoué, update")
            print(exp)
            return None
