class Admin:
    def __init__(self, id_participant,pseudo, mdp):
        self.__id_participant = id_participant
        self.__pseudo=pseudo
        self.__mdp = mdp

    # Getter pour id_participant
    def get_id_participant(self):
        return self.__id_participant

    # Getter pour mdp
    def get_mdp(self):
        return self.__mdp
    
    def get_pseudo(self):
        return self.__pseudo

    def __str__(self):
        return "id participant : " + str(self.__id_participant) + " le pseudo : " + self.pseudo