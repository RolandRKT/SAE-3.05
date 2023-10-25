from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .image import Image

Base = declarative_base()

class Etape(Base):
    __tablename__ = "ETAPE"
    id_etape = Column(Integer, primary_key=True)
    nom_etape = Column(String)
    id_photo = Column(Integer, ForeignKey("IMAGE.id_photo"))
    localisation = Column(String)

    #image = relationship("Image", back_populates="etapes")

    def __init__(self, nom_etape, id_photo, localisation):
        self.nom_etape = nom_etape
        self.id_photo = id_photo
        self.localisation = localisation
