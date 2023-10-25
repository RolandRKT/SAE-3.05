from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import time
from datetime import datetime

from ..app import db

class Parcours(db.Model):
    id_parc = db.Column(db.Integer, primary_key=True)
    nom_parc = db.Column(db.String(100))
    date_debut = db.Column(db.String(100))
    date_fin = db.Column(db.DateTime)
    desription = db.Column(db.String)
    id_photo = db.Column(db.Integer, db.ForeignKey("image.id_photo"))

    def __repr__(self):
        return f"ID: {self.id_parc} , nom : {self.nom_parc}"

    
def get_parcours_id(id_parc):
    return Parcours.query.get(id_parc)

def get_parcours():
    return Parcours.query.all()