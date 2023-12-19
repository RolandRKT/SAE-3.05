import os.path
import sys

from flask import Flask, jsonify
from flask_bootstrap import Bootstrap
from flask_mail import Mail

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))

from connexion import cnx,close_cnx
from composer_bd import *
from etape_bd import *


app = Flask(__name__)
app.config['BOOTSTRAP_SERVE8LOCAL']=True

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465  # or your mail server's port
app.config['MAIL_USERNAME'] = 'test123wade@gmail.com'
app.config['MAIL_PASSWORD'] = 'Baba45ls!'
app.config['MAIL_DEFAULT_SENDER'] = 'test123wade@gmail.com'
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = "bcc090e2-26b2-4c16-84ab-e766cc644320"

def mkpath(path):
    return (os.path.normpath(os.path.join(os.path.dirname(__file__),path)))

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///'+mkpath('../myapp.db'))
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
    composer =  Composer_bd(cnx)

    liste_composer = composer.get_par_parcour_composition(1)
    
    liste_etape = []
    
    for comp in liste_composer:    
        liste_etape.append(etape.get_par_id_etape(comp.get_parcours_id()).to_dict())
    
    return jsonify({'resultat': liste_etape})

                
                
if __name__ == '__main__':
    app.run(debug=True)