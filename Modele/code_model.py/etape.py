class Etape:
    def __init__(self,id, nom_etape, id_photo, localisation):
        self.id_etape = id
        self.nom_etape = nom_etape
        self.id_photo = id_photo
        self.localisation = localisation
    
    def get_id_etape(self):
        return self.id_etape

    def get_nom_etape(self):
        return self.nom_etape

    def get_id_photo(self):
        return self.id_photo

    def get_localisation(self):
        return self.localisation