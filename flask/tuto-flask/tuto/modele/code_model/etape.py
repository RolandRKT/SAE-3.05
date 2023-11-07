class Etape:
    def __init__(self,id, nom_etape, id_photo, coordonneX, coordonneY):
        self.__id_etape = id
        self.__nom_etape = nom_etape
        self.__id_photo = id_photo
        self._coordonneX = coordonneX
        self._coordonneY = coordonneY
        
    def get_id_etape(self):
        return self.__id_etape

    def get_nom_etape(self):
        return self.__nom_etape

    def get_id_photo(self):
        return self.__id_photo

    def get_coordonneX(self):
        return self._coordonneX
    
    def get_coordonneY(self):
        return self._coordonneY