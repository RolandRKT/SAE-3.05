from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .parcours import Parcours
from .participant import Participant

Base = declarative_base()


class Composer(Base):
    __tablename__ = "COMPOSER"
    id = Column(Integer, primary_key=True)
    participant_id = Column(Integer, ForeignKey("PARTICIPANT.id_participant"))
    parcours_id = Column(Integer, ForeignKey("PARCOURS.id_parc"))
    
    participant = relationship("Participant")
    parcours = relationship("Parcours")
