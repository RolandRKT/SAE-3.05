class Termine:
    """
    La classe Termine représente un objet terminé avec des attributs tels que l'ID du parc, l'ID de la partie,
    une note et un commentaire.

    Attributes:
        _id_parc (int): L'ID du parc associé à l'objet.
        _id_part (int): L'ID de la partie associée à l'objet.
        _note (str): La note associée à l'objet.
        _comm (str): Le commentaire associé à l'objet.
    """

    def __init__(self, id_parc, id_part, note, comm):
        """
        Initialise un nouvel objet Termine.

        Parameters:
            id_parc (int): L'ID du parc.
            id_part (int): L'ID de la partie.
            note (str): La note associée à l'objet.
            comm (str): Le commentaire associé à l'objet.
        """
        self._id_parc = id_parc
        self._id_part = id_part
        self._note = note
        self._comm = comm

    def get_id_parc(self):
        """
        Getter pour l'ID du parc.

        Returns:
            int: L'ID du parc associé à l'objet.
        """
        return self._id_parc

    def get_id_part(self):
        """
        Getter pour l'ID de la partie.

        Returns:
            int: L'ID de la partie associée à l'objet.
        """
        return self._id_part

    def get_note(self):
        """
        Getter pour la note.

        Returns:
            str: La note associée à l'objet.
        """
        return self._note

    def get_comm(self):
        """
        Getter pour le commentaire.

        Returns:
            str: Le commentaire associé à l'objet.
        """
        return self._comm
