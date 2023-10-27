class Suivre:
    def __init__(self, id_parc, id_user, point, comm,numero_etape):
        self.__id_parc = id_parc
        self.__id_user = id_user
        self.__point = point
        self.__comm = comm
        self.__num_etape=numero_etape

    # Getter pour id_parc
    def get_id_parc(self):
        return self.__id_parc

    # Getter pour id_user
    def get_id_user(self):
        return self.__id_user

    # Getter pour point
    def get_point(self):
        return self.__point

    # Getter pour comm
    def get_comm(self):
        return self.__comm

    def get_numero(self):
        return self.__num_etape