import os.path
import sys

from flask import Flask, jsonify
from flask_mail import Mail

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))

from connexion import cnx
from composer_bd import *
from etape_bd import *

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'wade.contact.assistance@gmail.com'
app.config['MAIL_PASSWORD'] = 'jjyp pyth gaka dsos'
app.config['MAIL_DEFAULT_SENDER'] = ('Wade',
                                     'wade.contact.assistance@gmail.com')
app.config['MAIL_DEBUG'] = True
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)

app.config['SECRET_KEY'] = "bcc090e2-26b2-4c16-84ab-e766cc644320"


def mkpath(path):
    return (os.path.normpath(os.path.join(os.path.dirname(__file__), path)))


from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///' + mkpath('../myapp.db'))
db = SQLAlchemy(app)


@app.route('/appel-fonction-python', methods=['GET'])
def appel_fonction_python():
    # instance = Composer_bd(cnx)
    # composer = instance.get_par_parcour_composition(1)
    # print()
    # print(etapes)
    # print()
    # resultat = []
    # for comp in composer:
    #     resultat.append(comp.to_dict())

    # return jsonify({'resultat': resultat})

    etape = Etape_bd(cnx)
    composer = Composer_bd(cnx)

    liste_composer = composer.get_par_parcour_composition(1)

    liste_etape = []

    for comp in liste_composer:
        liste_etape.append(
            etape.get_par_id_etape(comp.get_parcours_id()).to_dict())

    return jsonify({'resultat': liste_etape})


if __name__ == '__main__':
    app.run(debug=True)
