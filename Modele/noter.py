from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import time
from datetime import datetime

from ..app import db
from .parcours import *
from .user import *

class posseder(db.Model):
    id_parc = db.Column(db.Integer, db.ForeignKey("parcours.id_parc"), primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id_user"), primary_key=True)
    point = db.Column(db.Integer)
    comm = db.Column(db.String(250))