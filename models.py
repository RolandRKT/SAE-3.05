from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text, Date, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import func
import time
from datetime import date

from .app import db
from flask import Flask


class Client(db.Model):
    id_client = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String)
    email = db.Column(db.String)
    id_client_type = db.Column(db.Integer, db.ForeignKey("clientType.id_client_type"))

    type = db.relationship("client_type", back_ref="client")

    
class ClientType(db.Model):
    id_client_type = db.Column(db.Integer, primary_key = True)
    nom_type = db.Column(db.String)


if __name__ == '__main__':
    db.create_all()
