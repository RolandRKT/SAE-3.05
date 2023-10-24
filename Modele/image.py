from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import time
from datetime import datetime

from ..app import db


class Image(db.Model):
    id_photo = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    img_filename = db.Column(db.String())
    img_data = db.Column(db.LargeBinary)

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