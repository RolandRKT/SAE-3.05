from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import declarative_base


from ..app import db
from .connexion import cnx
base =declarative_base

class Participant( base ):
    __tablename__="PARTICPANT"
    id_participant = Column(Integer, primary_key = True)
    email   = Column(String)
    mdp     = Column(String)
    
    def __init__(self, id_participant,email,mdp):
        self.id_participant=id_participant
        self.email=email
        self.mdp = mdp
    
    def __str__(self):
        return str("id participant : "+self.id_participant +" le mail : "+self.email)