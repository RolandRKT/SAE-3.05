class Parcours:

    def __init__(self, id, nom_parc, date_debut, date_fin, description, id_photo):
        self.id_parc = id
        self.nom_parc = nom_parc
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.description = description
        self.id_photo = id_photo

    # Getter pour id_parc
    def get_id_parc(self):
        return self.id_parc

    # Getter pour nom_parc
    def get_nom_parc(self):
        return self.nom_parc

    # Getter pour date_debut
    def get_date_debut(self):
        return self.date_debut

    # Getter pour date_fin
    def get_date_fin(self):
        return self.date_fin

    # Getter pour description
    def get_description(self):
        return self.description

    # Getter pour id_photo
    def get_id_photo(self):
        return self.id_photo
