class Admin:
    def __init__(self,id_admin,pseudo, mdp):
        self.__id_admin = id_admin
        self.__pseudo=pseudo
        self.__mdp = mdp

    # Getter pour id_admin
    def get_id_admin(self):
        return self.__id_admin

    # Getter pour mdp
    def get_mdp(self):
        return self.__mdp
    
    def get_pseudo(self):
        return self.__pseudo

    def set_pseudo(self,pseudo):
        self.__pseudo=pseudo

    def set_mdp(self,mdp):
        self.__mdp=mdp
        
    def set_id(self,id):
        self.__id_admin=id