from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import time
from datetime import datetime

from .app import db


class User(db.Model):
    id_user = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String)
    mdp = db.Column(db.String)

class Admin(User):
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

class Client(User):
    id_client = db.Column(db.Integer, db.ForeignKey("user.id_user"), primary_key=True)
    nom = db.Column(db.String)
    id_client_type = db.Column(db.Integer, db.ForeignKey("clientType.id_client_type"))

    types = relationship("ClientType", backref="client")
    les_parcours = relationship("Parcours", back_populates="client")


class ClientType(db.Model):
    id_client_type = db.Column(db.Integer, primary_key=True)
    nom_type = db.Column(db.String)


class Note(db.Model):
    id_note = db.Column(db.Integer, primary_key=True)
    point = db.Column(db.Integer)
    notes = relationship("Noter", back_populates="notes")


class Commentaire(db.Model):
    id_commentaire = db.Column(db.Integer, primary_key=True)
    point = db.Column(db.Integer)
    id_parc = db.Column(db.Integer, db.ForeignKey("Parcours.id_parc"))
    les_comm = relationship("Parcours", back_populates="les_commentaires")


class AttentesTypeParcours(db.Model):
    id_attente = db.Column(db.Integer, primary_key=True)
    nom_attente = db.Column(db.String(100))
    caracteristique = db.Column(db.String(100))
    description = db.Column(db.String(100))
    les_attentes = relationship("TypeParcours", back_populates="attentes")


class TypeEtape(db.Model):
    id_type_etape = db.Column(db.Integer, primary_key=True)
    dec_type_etape = db.Column(db.String(100))
    types = relationship("Etape", back_populates="type_etape")


class Image(db.Model):
    id_photo = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    img_filename = db.Column(db.String())
    img_data = db.Column(db.LargeBinary)
    les_images = relationship("Etape", back_populates="photo")


class TypeParcours(db.Model):
    id_type_parc = db.Column(db.Integer, primary_key=True)
    nom_type_parc = db.Column(db.String(100))
    id_attente = db.Column(db.Integer, db.ForeignKey("AttentesTypeParcours.id_attente"))
    attentes = relationship("AttentesTypeParcours", back_populates="les_type")
    les_type = relationship("Parcours", back_populates="type_parc")


class Etape(db.Model):
    id_etape = db.Column(db.Integer, primary_key=True)
    nom_etape = db.Column(db.String(100))
    id_photo = db.Column(db.Integer, db.ForeignKey("Image.id_photo"))
    id_type_etape = db.Column(db.Integer, db.ForeignKey("TypeEtape.id_type_etape"))
    photo = relationship("Image", backref="photo")
    type_etape = relationship("TypeEtape", back_populates="les_etapes")


class Parcours(db.Model):
    id_parc = db.Column(db.Integer, primary_key=True)
    nom_parc = db.Column(db.String(100))
    date_debut = db.Column(db.String(100))
    date_fin = db.Column(db.DateTime)

    id_type_parc = db.Column(db.Integer, db.ForeignKey("TypeParcours.id_type_parc"))
    type_parc = relationship("TypeParcours", back_populates="les_parcours")
    les_commentaires = relationship("Commentaire", back_populates="les_comm")
    les_notes = relationship("Noter", back_populates="les_parcours")
    les_etapes = relationship("Composer", back_populates="les_parc")
    client = relationship("Client", backref="les_parcours")

    def __repr__(self):
        return f"ID: {self.id_parc} , nom : {self.nom_parc}"


class Composer(db.Model):
    id_parc = db.Column(db.Integer, db.ForeignKey("Parcours.id_parc"), primary_key=True)
    id_etape = db.Column(db.Integer, db.ForeignKey("Etape.id_etape"), primary_key=True)
    les_parc = relationship("Parcours", backref="composer")
    les_etapes = relationship("Etape", backref="composer")


class Noter(db.Model):
    id_parc = db.Column(db.Integer, db.ForeignKey("Parcours.id_parc"), primary_key=True)
    id_note = db.Column(db.Integer, db.ForeignKey("Note.id_note"), primary_key=True)
    les_parcours = relationship("Parcours", backref="noter")
    notes = relationship("Note", backref="noter")


"""
def get_image(the_id):
    #return Image.query.filter(Image.id == the_id).first()
    return Image.query.get_or_404(the_id)


def get_images(params=None):
    if not params:
        return Image.query.all()
    else:
        raise Exception('Filtering not implemented yet.')


def add_image(image_dict):
    new_image = Image(name=image_dict['name'], \
                        img_filename=image_dict['img_filename'], \
                        img_data=image_dict['img_data'])
    db.session.add(new_image)
    db.session.commit()
"""
if __name__ == '__main__':
    db.create_all()
