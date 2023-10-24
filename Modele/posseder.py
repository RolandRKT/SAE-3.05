from ..app import db
from .user import *
from .parcours import *


class Posseder(db.Model):
    id_user = db.Column(db.Integer, db.ForeignKey("user.id_user"), primary_key = True)
    id_parc = db.Column(db.Integer, db.ForeignKey("parcours.id_parc"), primary_key = True)


