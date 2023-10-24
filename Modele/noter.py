from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import time
from datetime import datetime

from ..app import db
from .parcours import Parcours
from .note import Note

class Noter(db.Model):
    id_parc = db.Column(db.Integer, db.ForeignKey("parcours.id_parc"), primary_key=True)
    id_note = db.Column(db.Integer, db.ForeignKey("note.id_note"), primary_key=True)
