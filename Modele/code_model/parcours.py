class Parcours:

    def __init__(self, id, nom_parc, date_debut, date_fin, description, id_photo):
        self.__id_parc = id
        self.__nom_parc = nom_parc
        self.__date_debut = date_debut
        self.__date_fin = date_fin
        self.__description = description
        self.__id_photo = id_photo

    # Getter pour id_parc
    def get_id_parc(self):
        return self.__id_parc

    # Getter pour nom_parc
    def get_nom_parc(self):
        return self.__nom_parc

    # Getter pour date_debut
    def get_date_debut(self):
        return self.__date_debut

    # Getter pour date_fin
    def get_date_fin(self):
        return self.__date_fin

    # Getter pour description
    def get_description(self):
        return self.__description

    # Getter pour id_photo
    def get_id_photo(self):
        return self.__id_photo
