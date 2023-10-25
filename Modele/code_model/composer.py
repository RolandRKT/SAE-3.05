class Composer:
    def __init__(self, participant_id, parcours_id):
        self.__participant_id = participant_id
        self.__parcours_id = parcours_id

    # Getter pour participant_id
    def get_participant_id(self):
        return self.__participant_id

    # Getter pour parcours_id
    def get_parcours_id(self):
        return self.__parcours_id
