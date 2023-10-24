from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import time
from datetime import datetime

from ..app import db

from .parcours import *

class Commentaire(db.Model):
    id_commentaire = db.Column(db.Integer, primary_key=True)
    point = db.Column(db.Integer)
    id_parc = db.Column(db.Integer, db.ForeignKey("parcours.id_parc"))
    