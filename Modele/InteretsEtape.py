from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import time
from datetime import datetime

from ..app import db

class InteretsEtape(db.Model):
    id_interet_etape = db.Column(db.Integer, primary_key=True)
    nom_interet = db.Column(db.String(100))
    descritpion = db.Column(db.String(200))


def get_interts_etape_id(id_interet_etape):
    return InteretsEtape.query.get(id_interet_etape)

def get_interts_etape():
    return InteretsEtape.query.all()
                                   
                                   