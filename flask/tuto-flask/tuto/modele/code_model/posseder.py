class Posseder:
    def __init__(self, id_etape,id_interet):
        self.__id_etape=id_etape
        self.__id_interet=id_interet
    
    def get_id_etape(self):
        return self.__id_etape

    def get_id_interet(self):
        return self.__id_interet