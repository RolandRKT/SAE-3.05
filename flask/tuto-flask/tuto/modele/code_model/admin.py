"""
    Ce fichier va nous permettre de crée un admin
"""
class Admin:
    """
    Classe représentant un administrateur.

    Attributes:
        __id_admin (int): L'identifiant unique de l'administrateur.
        __pseudo (str): Le pseudonyme de l'administrateur.
        __mdp (str): Le mot de passe de l'administrateur.
    """

    def __init__(self, id_admin, pseudo, mdp):
        """
        Initialise un objet Admin.

        Args:
            id_admin (int): L'identifiant unique de l'administrateur.
            pseudo (str): Le pseudonyme de l'administrateur.
            mdp (str): Le mot de passe de l'administrateur.
        """
        self.__id_admin = id_admin
        self.__pseudo = pseudo
        self.__mdp = mdp

    def get_id(self):
        """
        Récupère l'identifiant de l'administrateur.

        Returns:
            int: L'identifiant de l'administrateur.
        """
        return self.__id_admin

    def get_pseudo(self):
        """
        Récupère le pseudonyme de l'administrateur.

        Returns:
            str: Le pseudonyme de l'administrateur.
        """
        return self.__pseudo

    def get_mdp(self):
        """
        Récupère le mot de passe de l'administrateur.

        Returns:
            str: Le mot de passe de l'administrateur.
        """
        return self.__mdp

    def set_id(self, id_admin):
        """
        Modifie l'identifiant de l'administrateur.

        Args:
            id_admin (int): Le nouvel identifiant de l'administrateur.
        """
        self.__id_admin = id_admin

    def set_pseudo(self, pseudo):
        """
        Modifie le pseudonyme de l'administrateur.

        Args:
            pseudo (str): Le nouveau pseudonyme de l'administrateur.
        """
        self.__pseudo = pseudo

    def set_mdp(self, mdp):
        """
        Modifie le mot de passe de l'administrateur.

        Args:
            mdp (str): Le nouveau mot de passe de l'administrateur.
        """
        self.__mdp = mdp

    def set_all(self, id_admin, pseudo, mdp):
        """
        Modifie tous les attributs de l'administrateur en une seule méthode.

        Args:
            id_admin (int): Le nouvel identifiant de l'administrateur.
            pseudo (str): Le nouveau pseudonyme de l'administrateur.
            mdp (str): Le nouveau mot de passe de l'administrateur.
        """
        self.set_id(id_admin)
        self.set_pseudo(pseudo)
        self.set_mdp(mdp)
