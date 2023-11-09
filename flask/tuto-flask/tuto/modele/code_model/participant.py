class Participant:
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
        Getter pour l'ID du participant.

        Returns:
            int: L'ID du participant.
        """
        return self.__id_participant

    def get_email(self):
        """
        Getter pour l'adresse e-mail du participant.

        Returns:
            str: L'adresse e-mail du participant.
        """
        return self.__email

    def get_mdp(self):
        """
        Getter pour le mot de passe du participant.

        Returns:
            str: Le mot de passe du participant.
        """
        return self.__mdp
    
    def get_pseudo(self):
        """
        Getter pour le pseudo du participant.

        Returns:
            str: Le pseudo du participant.
        """
        return self.__pseudo

    def set_pseudo(self,pseudo):
        self.__pseudo=pseudo
    def set_email(self,email):
        self.__email=email
    def set_mdp(self,mdp):
        self.__mdp=mdp
    def set_id(self,id):
        self.__id_participant=id

    def __str__(self):
        return "id participant : " + str(self.__id_participant) + " le mail : " + self.__email
