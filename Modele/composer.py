from ..app import db
from .parcours import *
from .etape import *

class Composer(db.Model):
    id_parc = db.Column(db.Integer, db.ForeignKey("parcours.id_parc"), primary_key=True)
    id_etape = db.Column(db.Integer, db.ForeignKey("etape.id_etape"), primary_key=True)


def get_composer_parc_id(id_parc):
    return get_parcours_id(id_parc)

def get_composer_etape_id(id_etape):
    return get_etape_id(id_etape)
