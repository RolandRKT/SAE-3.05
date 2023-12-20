"""
    Fichier contenant les etapes
"""
class Etape:
    """
    Classe représentant une étape dans un parcours.

    Attributes:
        __id_etape (int): L'ID de l'étape.
        __nom_etape (str): Le nom de l'étape.
        __id_photo (int): L'ID de la photo associée à l'étape.
        _coordonneX (float): La coordonnée X de l'étape.
        _coordonneY (float): La coordonnée Y de l'étape.
    """

    def __init__(self, id_etape, nom_etape, id_photo, coordonne_x, coordonne_y,interet):
        """
        Initialise un objet Etape avec les informations de l'étape.

        Args:
            id (int): L'ID de l'étape.
            nom_etape (str): Le nom de l'étape.
            id_photo (int): L'ID de la photo associée à l'étape.
            coordonneX (float): La coordonnée X de l'étape.
            coordonneY (float): La coordonnée Y de l'étape.
        """
        self.__id_etape = id_etape
        self.__nom_etape = nom_etape
        self.__id_photo = id_photo
        self._coordonneX = coordonne_x
        self._coordonneY = coordonne_y
        self._interet=interet
        
    def to_dict(self):
        return {
            'id_etape': self.__id_etape,
            'nom_etape': self.__nom_etape,
            'id_photo': self.__id_photo,
            'coordonneX': self._coordonneX,
            'coordonneY': self._coordonneY,
            'interet':self._interet
        }
        
    def get_id_etape(self):
        """
        Récupère l'ID de l'étape.

        Returns:
            int: L'ID de l'étape.
        """
        return self.__id_etape

    def get_nom_etape(self):
        """
        Récupère le nom de l'étape.

        Returns:
            str: Le nom de l'étape.
        """
        return self.__nom_etape

    def get_id_photo(self):
        """
        Récupère l'ID de la photo associée à l'étape.

        Returns:
            int: L'ID de la photo.
        """
        return self.__id_photo

    def get_coordonneX(self):
        """
        Récupère la coordonnée X de l'étape.

        Returns:
            float: La coordonnée X de l'étape.
        """
        return self._coordonneX

    def get_coordonneY(self):
      """
        Récupère la coordonnée Y de l'étape.

        Returns:
            float: La coordonnée Y de l'étape.
      """
      return self._coordonneY
    
    def get_interet(self):
        """
            Cette fonction permet de retourner l'interet de l'etape
        """
        return self._interet
    
    def __repr__(self):
      return "nom : " + self.__nom_etape + " id : " + str(self.__id_etape)
