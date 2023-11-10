class Etape:

    def __init__(self,id, nom_etape, id_photo, coordonneX, coordonneY):
        """
        Initialise un objet Etape avec les informations de l'étape.

        Args:
            id (int): L'ID de l'étape.
            nom_etape (str): Le nom de l'étape.
            id_photo (int): L'ID de la photo associée à l'étape.
            coordonneeX (float): coordonnée x de l'étape
            coordonneeY (float) : coordonnée y de l'étape
        """
        self.__id_etape = id
        self.__nom_etape = nom_etape
        self.__id_photo = id_photo
        self._coordonneX = coordonneX
        self._coordonneY = coordonneY
        
    def get_id_etape(self):
        """
        Getter pour l'ID de l'étape.

        Returns:
            int: L'ID de l'étape.
        """
        return self.__id_etape

    def get_nom_etape(self):
        """
        Getter pour le nom de l'étape.

        Returns:
            str: Le nom de l'étape.
        """
        return self.__nom_etape

    def get_id_photo(self):
        """
        Getter pour l'ID de la photo associée à l'étape.

        Returns:
            int: L'ID de la photo.
        """
        return self.__id_photo

    def get_coordonneX(self):
        return self._coordonneX
    
    def get_coordonneY(self):
        return self._coordonneY
    
    def __repr__(self):
        return "nom : " + self.__nom_etape + " id : " + str(self.__id_etape)