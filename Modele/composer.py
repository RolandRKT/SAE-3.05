from ..app import db
from .parcours import *
from .etape import *

class Composer(db.Model):
    id_parc = db.Column(db.Integer, db.ForeignKey("parcours.id_parc"), primary_key=True)
    id_etape = db.Column(db.Integer, db.ForeignKey("etape.id_etape"), primary_key=True)


