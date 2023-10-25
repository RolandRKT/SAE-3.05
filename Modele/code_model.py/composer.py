class Composer:

    def __init__(self, id, participant_id, parcours_id):
        self.id = id
        self.participant_id = participant_id
        self.parcours_id = parcours_id

    # Getter pour id
    def get_id(self):
        return self.id

    # Getter pour participant_id
    def get_participant_id(self):
        return self.participant_id

    # Getter pour parcours_id
    def get_parcours_id(self):
        return self.parcours_id
