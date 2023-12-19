"""
    Fichier de la class posseder
"""


class Posseder:
    """
        La class posseder
    """

    def __init__(self, id_etape, id_interet):
        """
        Initialise un objet Posseder pour représenter la relation entre une étape et un intérêt.

        Args:
            id_etape (int): L'ID de l'étape.
            id_interet (int): L'ID de l'intérêt associé à l'étape.
        """
        self.__id_etape = id_etape
        self.__id_interet = id_interet

    def get_id_etape(self):
        """
        Getter pour l'ID de l'étape associée à la relation.

        Returns:
            int: L'ID de l'étape.
        """
        return self.__id_etape

    def get_id_interet(self):
        """
        Getter pour l'ID de l'intérêt associé à la relation.

        Returns:
            int: L'ID de l'intérêt.
        """
        return self.__id_interet
