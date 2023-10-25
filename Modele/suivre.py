from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import time
from datetime import datetime

from ..app import db
from .parcours import *
from .participant import *

class suivre(db.Model):
    id_parc = db.Column(db.Integer, db.ForeignKey("parcours.id_parc"), primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("participant.id_user"), primary_key=True)
    point = db.Column(db.Integer)
    comm = db.Column(db.String(250))
    
def get_suivre_parcours_id(id_parc):
    return get_parcours_id(id_parc)

def get_suivre_participant_id(id_user):
    return get_participant_id(id_user)
    