class Interet_etape:

    def __init__(self, id_interet, nom_interet, description_interet):
        self.__id_interet = id_interet
        self.__nom_interet = nom_interet
        self.__description_interet = description_interet

    # getter id interet
    def get_id_interet(self):
        return self.__id_interet
    
    # getter nom interet
    def get_nom_interet(self):
        return self.__nom_interet
    
    # gettet description interet
    def get_description_interet(self):
        return self.__description_interet