"""
    Ce fichier va contenir la class suivre entre un user et un parcours
"""


class Suivre:
    """
        La class suivre
    """

    def __init__(self, id_user, id_parc, numero_etape):
        """
        Initialise un objet Suivre pour représenter
        la relation entre un utilisateur et un parcours suivi.

        Args:
            id_parc (int): L'ID du parcours suivi.
            id_user (int): L'ID de l'utilisateur qui suit le parcours.
            point (float): Les points attribués par l'utilisateur au parcours.
            comm (str): Le commentaire laissé par l'utilisateur sur le parcours.
            numero_etape (int): Le numéro de l'étape atteinte dans le parcours.
        """
        self.__id_user = id_user
        self.__id_parc = id_parc
        self.__num_etape = numero_etape

    def get_id_parc(self):
        """
        Getter pour l'ID du parcours suivi.

        Returns:
            int: L'ID du parcours suivi.
        """
        return self.__id_parc

    def get_id_user(self):
        """
        Getter pour l'ID de l'utilisateur qui suit le parcours.

        Returns:
            int: L'ID de l'utilisateur.
        """
        return self.__id_user

    def get_numero(self):
        """
        Getter pour le numéro de l'étape atteinte dans le parcours.

        Returns:
            int: Le numéro de l'étape.
        """
        return self.__num_etape
