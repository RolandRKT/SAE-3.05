from .app import db
from flask import Flask
from  datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class Note(db.Model):
    idNote = db.Column(db.Integer, primary_key=True)
    point = db.Column(db.Integer)
    notes=relationship("Parcours", back_populates="notes")
    

class Commentaire(db.Model):
    idCommentaire = db.Column(db.Integer, primary_key=True)
    point = db.Column(db.Integer)
    lesCommentaires=relationship("Parcours", back_populates="Comm")


class AttentesTypeParcours( db.Model ):
    idAttente       = db.Column(db.Integer, primary_key=True)
    nomAttente      = db.Column(db.String(100))
    caracteristique = db.Column(db.String(100))
    description     = db.Column(db.String(100))
    lesAttentes=relationship("TypeParcours", back_populates="lesattentes")

class TypeEtape(db.Model):
    idTypeEtape = db.Column(db.Integer, primary_key=True)
    decTypeEtape= db.Column(db.String(100))
    lesType=relationship("Etape", back_populates="types")

     
class Image(db.Model):
    idPhoto = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    img_filename = db.Column(db.String())
    img_data = db.Column(db.LargeBinary)
    lesImages=relationship("Etape", back_populates="photo")

    
class TypeParcours(db.Model):
    idTypeParc = db.Column(db.Integer, primary_key=True)
    nom        = db.Column(db.String(100))
    idAttente= db.Column(db.Integer, ForeignKey("AttentesTypeParcours.idAttente"))
    lesattentes = relationship("Image", backref="AttentesTypeParcours.idAttente")
    lestype=relationship("Parcours", back_populates="typeparc")


class Etape(db.Model):
    idEtape    = db.Column(db.Integer, primary_Key=True)
    nomEtape   = db.Column(db.String(100))
    idPhoto    = db.Column(db.Integer, ForeignKey("Image.idPhoto"))
    idTypeEtape= db.Column(db.Integer, ForeignKey("TypeEtape.idTypeEtape"))
    photo = relationship("Image", backref="Image.idPhoto")
    types = relationship("TypeEtape", backref="TypeEtape.idTypeEtape")

    lesEtapes=relationship("Composer", back_populates="lesEtape")


class Parcours(db.Model):
    idParc = db.Column(db.Integer, primary_key=True)
    nomParc = db.Column(db.String(100))
    dateDebut = db.Column(db.String(100))
    dateFin = db.Column(datetime)
    
    idTypeParc=db.Column(db.Integer, ForeignKey("TypeParcours.idTypeParc"))
    typeparc = relationship("TypeParcours", backref="TypeParcours.idTypeParc")

    idCommentaire=db.Column(db.Integer, ForeignKey("Commentaire.idCommentaire"))
    Comm = relationship("Commentaire", backref="Commentaire.idCommentaire")
    
    idNote=db.Column(db.Integer, ForeignKey("Note.idNote"))
    notes = relationship("Note", backref="Note.idNote")

    lesEtapes=relationship("Composer", back_populates="lesparcours")


    def __repr__(self):
        return f"ID: {self.idParc} , nom : {self.nomParc}"


class Composer(db.Model):
    idParc = db.Column(db.Integer, ForeignKey("Parcours.idParc"), primary_key=True)
    lesparcours = relationship("Parcours", backref="Parcours.idParc")  # ok car relation 1-1
    
    idEtape = db.Column(db.Integer, ForeignKey("Etape.idEtape"), primary_key=True) # idem 
    lesEtape = relationship("Etape", backref="Etape.idEtape")


"""
def get_image(the_id):
    #return Image.query.filter(Image.id == the_id).first()
    return Image.query.get_or_404(the_id)


def get_images(params=None):
    if not params:
        return Image.query.all()
    else:
        raise Exception('Filtering not implemented yet.')


def add_image(image_dict):
    new_image = Image(name=image_dict['name'], \
                        img_filename=image_dict['img_filename'], \
                        img_data=image_dict['img_data'])
    db.session.add(new_image)
    db.session.commit()
"""