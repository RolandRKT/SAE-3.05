class Interet_etape:
    def __init__(self, id_interet, nom_interet, description_interet):
        """
        Initialise un objet Interet_etape avec les informations de l'intérêt lié à une étape.

        Args:
            id_interet (int): L'ID de l'intérêt.
            nom_interet (str): Le nom de l'intérêt.
            description_interet (str): La description de l'intérêt.
        """
        self.__id_interet = id_interet
        self.__nom_interet = nom_interet
        self.__description_interet = description_interet

    def __repr__(self) -> str:
        return "interte : " + self.__nom_interet + " id : " + str(self.__id_interet)

    def get_id_interet(self):
        """
        Getter pour l'ID de l'intérêt.

        Returns:
            int: L'ID de l'intérêt.
        """
        return self.__id_interet
    
    def get_nom_interet(self):
        """
        Getter pour le nom de l'intérêt.

        Returns:
            str: Le nom de l'intérêt.
        """
        return self.__nom_interet
    
    def get_description_interet(self):
        """
        Getter pour la description de l'intérêt.

        Returns:
            str: La description de l'intérêt.
        """
        return self.__description_interet
