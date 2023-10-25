class Participant:
    def __init__(self, id_participant, email, mdp):
        self.id_participant = id_participant
        self.email = email
        self.mdp = mdp

    # Getter pour id_participant
    def get_id_participant(self):
        return self.id_participant

    # Getter pour email
    def get_email(self):
        return self.email

    # Getter pour mdp
    def get_mdp(self):
        return self.mdp

    def __str__(self):
        return "id participant : " + str(self.id_participant) + " le mail : " + self.email
