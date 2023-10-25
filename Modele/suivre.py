from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .parcours import Parcours
from .participant import Participant

Base = declarative_base()

class Suivre(Base):
    __tablename__ = "SUIVRE"
    id_parc = Column(Integer, ForeignKey("parcours.id_parc"), primary_key=True)
    id_user = Column(Integer, ForeignKey("participant.id_user"), primary_key=True)
    point = Column(Integer)
    comm = Column(String(250))

    #parcours = relationship("Parcours", backref="suivis")
    #participant = relationship("Participant", backref="suivis")

    def __init__(self, id_parc, id_user, point, comm):
        self.id_parc = id_parc
        self.id_user = id_user
        self.point = point
        self.comm = comm
