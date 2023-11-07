class Parcours:
    def __init__(self, id, nom_parc, duree, description, id_photo):
        """
        Initialise un objet Parcours avec les informations du parcours.

        Args:
            id (int): L'ID du parcours.
            nom_parc (str): Le nom du parcours.
            duree (str): La durée estimée du parcours.
            description (str): La description du parcours.
            id_photo (int): L'ID de la photo associée au parcours.
        """
        self.__id_parc = id
        self.__nom_parc = nom_parc
        self.__duree = duree
        self.__description = description
        self.__id_photo = id_photo

    def get_id_parc(self):
        """
        Getter pour l'ID du parcours.

        Returns:
            int: L'ID du parcours.
        """
        return self.__id_parc

    def get_nom_parc(self):
        """
        Getter pour le nom du parcours.

        Returns:
            str: Le nom du parcours.
        """
        return self.__nom_parc

    def get_duree(self):
        """
        Getter pour la durée estimée du parcours.

        Returns:
            str: La durée estimée du parcours.
        """
        return self.__duree

    def get_description(self):
        """
        Getter pour la description du parcours.

        Returns:
            str: La description du parcours.
        """
        return self.__description

    def get_id_photo(self):
        """
        Getter pour l'ID de la photo associée au parcours.

        Returns:
            int: L'ID de la photo associée au parcours.
        """
        return self.__id_photo
