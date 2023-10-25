from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import time
from datetime import datetime

from ..app import db


class Participant(db.Model):
    id_user = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String)
    mdp = db.Column(db.String)