from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import time
from datetime import datetime

from ..app import db
from .image import Image



class Etape(db.Model):
    id_etape = db.Column(db.Integer, primary_key=True)
    nom_etape = db.Column(db.String(100))
    id_photo = db.Column(db.Integer, db.ForeignKey("image.id_photo"))
    localisation = db.Column(db.String(200))