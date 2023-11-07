class Composer:
    def __init__(self, participant_id, parcours_id, numero):
        """
            Initialise un objet Composer avec les informations du participant, du parcours, et du numéro.

            param participant_id: ID du participant lié à la composition.
            param parcours_id: ID du parcours lié à la composition.
            param numero: Numéro de la composition.
        """
        self.__participant_id = participant_id
        self.__parcours_id = parcours_id
        self.__num = numero

    def get_participant_id(self):
        """
            Getter pour l'ID du participant lié à la composition.

            return: L'ID du participant.
        """
        return self.__participant_id

    def get_parcours_id(self):
        """
            Getter pour l'ID du parcours lié à la composition.

            return: L'ID du parcours.
        """
        return self.__parcours_id

    def get_numero(self):
        """
            Getter pour le numéro de la composition.
        
            return: Le numéro de la composition.
        """
        return self.__num
