class Participant:
    def __init__(self, id_participant,pseudo, email, mdp):
        self.__id_participant = id_participant
        self.__pseudo=pseudo
        self.__email = email
        self.__mdp = mdp

    # Getter pour id_participant
    def get_id_participant(self):
        return self.__id_participant

    # Getter pour email
    def get_email(self):
        return self.__email

    # Getter pour mdp
    def get_mdp(self):
        return self.__mdp
    
    def get_pseudo(self):
        return self.__pseudo

    def __str__(self):
        return "id participant : " + str(self.__id_participant) + " le mail : " + self.__email
