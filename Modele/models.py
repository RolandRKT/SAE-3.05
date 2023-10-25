from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import time
from datetime import datetime

from app import db


class User(db.Model):
    id_user = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String)
    mdp = db.Column(db.String)

class Parcours(db.Model):
    id_parc = db.Column(db.Integer, primary_key=True)
    nom_parc = db.Column(db.String(100))
    date_debut = db.Column(db.String(100))
    date_fin = db.Column(db.DateTime)
    desription = db.Column(db.String)
    id_photo = db.Column(db.Integer, db.ForeignKey("image.id_photo"))

    def __repr__(self):
        return f"ID: {self.id_parc} , nom : {self.nom_parc}"

class Posseder(db.Model):
    id_user = db.Column(db.Integer, db.ForeignKey("user.id_user"), primary_key = True)
    id_parc = db.Column(db.Integer, db.ForeignKey("parcours.id_parc"), primary_key = True)


class Image(db.Model):
    id_photo = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    img_filename = db.Column(db.String())
    img_data = db.Column(db.LargeBinary)

class Etape(db.Model):
    id_etape = db.Column(db.Integer, primary_key=True)
    nom_etape = db.Column(db.String(100))
    id_photo = db.Column(db.Integer, db.ForeignKey("image.id_photo"))
    localisation = db.Column(db.String(200))

class Composer(db.Model):
    id_parc = db.Column(db.Integer, db.ForeignKey("parcours.id_parc"), primary_key=True)
    id_etape = db.Column(db.Integer, db.ForeignKey("etape.id_etape"), primary_key=True)


class Note(db.Model):
    id_note = db.Column(db.Integer, primary_key=True)
    point = db.Column(db.Integer)


class Commentaire(db.Model):
    id_commentaire = db.Column(db.Integer, primary_key=True)
    point = db.Column(db.Integer)
    id_parc = db.Column(db.Integer, db.ForeignKey("parcours.id_parc"))


class Noter(db.Model):
    id_parc = db.Column(db.Integer, db.ForeignKey("parcours.id_parc"), primary_key=True)
    id_note = db.Column(db.Integer, db.ForeignKey("note.id_note"), primary_key=True)

