class Suivre:
    def __init__(self, id_parc, id_user, point, comm):
        self.id_parc = id_parc
        self.id_user = id_user
        self.point = point
        self.comm = comm

    # Getter pour id_parc
    def get_id_parc(self):
        return self.id_parc

    # Getter pour id_user
    def get_id_user(self):
        return self.id_user

    # Getter pour point
    def get_point(self):
        return self.point

    # Getter pour comm
    def get_comm(self):
        return self.comm
