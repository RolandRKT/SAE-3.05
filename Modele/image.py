from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Image(Base):
    __tablename__ = "IMAGE"
    id_photo = Column(Integer, primary_key=True)
    name = Column(String)
    img_filename = Column(String)
    img_data = Column(LargeBinary)

    def __init__(self, name, img_filename, img_data):
        self.name = name
        self.img_filename = img_filename
        self.img_data = img_data
    
