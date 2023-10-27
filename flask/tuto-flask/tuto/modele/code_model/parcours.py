class Parcours:

    def __init__(self, id, nom_parc, duree, description, id_photo):
        self.__id_parc = id
        self.__nom_parc = nom_parc
        self.__duree=duree
        self.__description = description
        self.__id_photo = id_photo

    # Getter pour id_parc
    def get_id_parc(self):
        return self.__id_parc

    # Getter pour nom_parc
    def get_nom_parc(self):
        return self.__nom_parc

    # Getter pour duree
    def get_duree(self):
        return self.__duree

    # Getter pour description
    def get_description(self):
        return self.__description

    # Getter pour id_photo
    def get_id_photo(self):
        return self.__id_photo
