class Participant:
    def __init__(self, id_participant, email, mdp):
        self.__id_participant = id_participant
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

    def __str__(self):
        return "id participant : " + str(self.__id_participant) + " le mail : " + self.__email
