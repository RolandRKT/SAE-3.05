from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text, Date, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import func
import time
from datetime import datetime

from .app import db
from flask import Flask


class Client(db.Model):
    id_client = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    email = db.Column(db.String)
    id_client_type = db.Column(db.Integer,
                               db.ForeignKey("clientType.id_client_type"))

    type = relationship("Client_type", back_ref="client")
    les_parc = relationship("Parcours", back_populates="client")


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
    id_parc = db.Column(db.Integer, ForeignKey("Parcours.id_parc"))
    les_comm = relationship("Parcours", backref="Parcours.id_parc")


class AttentesTypeParcours(db.Model):
    id_attente = db.Column(db.Integer, primary_key=True)
    nom_attente = db.Column(db.String(100))
    caracteristique = db.Column(db.String(100))
    description = db.Column(db.String(100))
    les_attentes = relationship("TypeParcours", back_populates="les_attentes")


class TypeEtape(db.Model):
    id_type_etape = db.Column(db.Integer, primary_key=True)
    dec_type_etape = db.Column(db.String(100))
    les_type = relationship("Etape", back_populates="types")


class Image(db.Model):
    id_photo = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    img_filename = db.Column(db.String())
    img_data = db.Column(db.LargeBinary)
    les_images = relationship("Etape", back_populates="photo")


class TypeParcours(db.Model):
    id_type_parc = db.Column(db.Integer, primary_key=True)
    nom_type_parc = db.Column(db.String(100))
    id_attente = db.Column(db.Integer,
                           ForeignKey("AttentesTypeParcours.id_attente"))
    les_attentes = relationship("Image",
                                backref="AttentesTypeParcours.id_attente")
    les_type = relationship("Parcours", back_populates="typeparc")


class Etape(db.Model):
    id_etape = db.Column(db.Integer, primary_Key=True)
    nom_etape = db.Column(db.String(100))
    id_photo = db.Column(db.Integer, ForeignKey("Image.id_photo"))
    id_type_etape = db.Column(db.Integer,
                              ForeignKey("TypeEtape.id_type_etape"))
    photo = relationship("Image", backref="Image.id_photo")
    types = relationship("TypeEtape", backref="TypeEtape.id_type_etape")

    les_etapes = relationship("Composer", back_populates="les_etapes")


class Parcours(db.Model):
    id_parc = db.Column(db.Integer, primary_key=True)
    nom_parc = db.Column(db.String(100))
    date_debut = db.Column(db.String(100))
    date_fin = db.Column(datetime)

    id_type_parc = db.Column(db.Integer,
                             ForeignKey("TypeParcours.id_type_parc"))
    type_parc = relationship("TypeParcours",
                             backref="TypeParcours.id_type_parc")

    les_commentaires = relationship("Commentaire", back_populates="les_comm")
    les_notes = relationship("Noter", back_populates="les_parcours")
    les_etapes = relationship("Composer", back_populates="les_parc")
    client = relationship("Client", backref="les_parc")

    def __repr__(self):
        return f"ID: {self.id_parc} , nom : {self.nom_parc}"


class Composer(db.Model):
    id_parc = db.Column(db.Integer,
                        ForeignKey("Parcours.id_parc"),
                        primary_key=True)
    les_parc = relationship("Parcours",
                            backref="Parcours.id_parc")  # ok car relation 1-1

    id_etape = db.Column(db.Integer,
                         ForeignKey("Etape.id_etape"),
                         primary_key=True)  # idem
    les_etapes = relationship("Etape", backref="Etape.id_etape")


class Noter(db.Model):
    id_parc = db.Column(db.Integer,
                        ForeignKey("Parcours.id_parc"),
                        primary_key=True)
    les_parcours = relationship(
        "Parcours", backref="Parcours.id_parc")  # ok car relation 1-1

    id_note = db.Column(db.Integer, ForeignKey("Note.id_note"))
    notes = relationship("Note", backref="Note.id_note")


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
