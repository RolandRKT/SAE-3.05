"""
    Ce fichier contient la class participant
"""


class Participant:
    """
    Classe représentant un participant.

    Attributes:
        __id_participant (int): L'ID du participant.
        __pseudo (str): Le pseudo du participant.
        __email (str): L'adresse e-mail du participant.
        __mdp (str): Le mot de passe du participant.
    """

    def __init__(self, id_participant, pseudo, email, mdp):
        """
        Initialise un objet Participant avec les informations du participant.

        Args:
            id_participant (int): L'ID du participant.
            pseudo (str): Le pseudo du participant.
            email (str): L'adresse e-mail du participant.
            mdp (str): Le mot de passe du participant.
        """
        self.__id_participant = id_participant
        self.__pseudo = pseudo
        self.__email = email
        self.__mdp = mdp

    def get_id(self):
        """
        Récupère l'ID du participant.

        Returns:
            int: L'ID du participant.
        """
        return self.__id_participant

    def get_email(self):
        """
        Récupère l'adresse e-mail du participant.

        Returns:
            str: L'adresse e-mail du participant.
        """
        return self.__email

    def get_mdp(self):
        """
        Récupère le mot de passe du participant.

        Returns:
            str: Le mot de passe du participant.
        """
        return self.__mdp

    def get_pseudo(self):
        """
        Récupère le pseudo du participant.

        Returns:
            str: Le pseudo du participant.
        """
        return self.__pseudo

    def set_pseudo(self, pseudo):
        """
        Modifie le pseudo du participant.

        Args:
            pseudo (str): Le nouveau pseudo du participant.
        """
        self.__pseudo = pseudo

    def set_email(self, email):
        """
        Modifie l'adresse e-mail du participant.

        Args:
            email (str): La nouvelle adresse e-mail du participant.
        """
        self.__email = email

    def set_mdp(self, mdp):
        """
        Modifie le mot de passe du participant.

        Args:
            mdp (str): Le nouveau mot de passe du participant.
        """
        self.__mdp = mdp

    def set_id(self, id_part):
        """
        Modifie l'ID du participant.

        Args:
            id (int): Le nouvel ID du participant.
        """
        self.__id_participant = id_part

    def set_all(self, id_part, pseudo, email, mdp):
        """
        Modifie tous les attributs du participant en une seule méthode.

        Args:
            id (int): Le nouvel ID du participant.
            pseudo (str): Le nouveau pseudo du participant.
            email (str): La nouvelle adresse e-mail du participant.
            mdp (str): Le nouveau mot de passe du participant.
        """
        self.set_id(id_part)
        self.set_pseudo(pseudo)
        self.set_email(email)
        self.set_mdp(mdp)

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères du participant.

        Returns:
            str: Une chaîne de caractères représentant le participant.
        """
        return f"id participant : {self.__id_participant}, le mail : {self.__email}"
