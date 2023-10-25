from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .image import Image

Base = declarative_base()

class Parcours(Base):
    __tablename__ = "PARCOURS"
    id_parc = Column(Integer, primary_key=True)
    nom_parc = Column(String(100))
    date_debut = Column(String(100))
    date_fin = Column(DateTime)
    description = Column(String)
    id_photo = Column(Integer, ForeignKey("IMAGE.id_photo"))

    #image = relationship("Image", backref="parcours")

    def __init__(self, nom_parc, date_debut, date_fin, description, id_photo):
        self.nom_parc = nom_parc
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.description = description
        self.id_photo = id_photo