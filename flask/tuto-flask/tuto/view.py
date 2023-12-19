
from flask import jsonify, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired
from flask import request
from hashlib import sha256
from wtforms import PasswordField
from flask import request, redirect, url_for
from wtforms import FloatField
from flask import flash
from .app import app, db
import sqlalchemy
import os
import sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))
from participant_bd import *
from parcours_bd import *

from image_bd import *
from connexion import cnx,close_cnx
from admin_bd import *
from etape_bd import *
from composer_bd import *

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from participant import *

num_parcours = 1

test=Participant(-1,"","","")
@app.route("/")
def home():
    """
        Nous montre la premiere page la du lancement du site
    """
    return render_template("home.html", page_home=True)

@app.route("/portails")
def portails():
    return render_template("portails.html")

@app.route("/login")
def login():
    """
        permet de se diriger vers la page login
    """
    print("hahaha")
    user_agent = request.user_agent.string
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("login_mobile.html", page_mobile=True, page_login=True)
    else:
        return render_template("login.html", page_mobile=False, page_login=True)


@app.route("/inscription")
def inscription():
    """
        Permet de se diriger vers la page inscription
    """
    user_agent = request.user_agent.string
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("inscription_mobile.html", page_mobile=True, page_login=False)
    else:
        return render_template("inscription.html", page_mobile=False, page_login=False)

@app.route("/parcours/<int:nb_etape>")
def parcours(nb_etape):
    """
        se dirige vers la page parcours
    """
    
    # bon = False
    user_agent = request.user_agent.string
    etape = Etape_bd(cnx)
    composer =  Composer_bd(cnx)

    liste_composer = composer.get_par_parcour_composition(num_parcours)
    
    liste_etape = []
    
    for comp in liste_composer:    
        liste_etape.append(etape.get_par_id_etape(comp.get_parcours_id()))
    
    lesetapes = []

    for eta in liste_etape:
                i=Image_bd(cnx)
                images=i.get_par_image(eta.get_id_photo())
                try:
                    monimage=images[0].get_img_filename()
                    print(monimage)
                    lesetapes.append((eta,monimage))
                except:
                    lesetapes.append((eta, "image_default.jpg"))
    

    print(lesetapes)

    lesetapes_json = []

    for eta, monimage in lesetapes:
        etape_data = {
            'id': eta.get_id_etape(),
            'nom': eta.get_nom_etape(),
            'coordonneX': eta.get_coordonneX(),
            'coordonneY': eta.get_coordonneY(),
            # Ajoutez d'autres propriétés selon vos besoins
            'image': monimage,
        }
        lesetapes_json.append(etape_data)
    
    print(lesetapes_json)
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("parcours_mobile.html", page_mobile=True, etape_actu = [lesetapes[nb_etape - 1 ]], x = nb_etape, longueur = len(liste_etape), num_parcours = num_parcours)
    else:
        return render_template("parcours.html", page_mobile=False, etape_actu = [lesetapes[nb_etape - 1 ]],  x = nb_etape, longueur = len(liste_etape), num_parcours = num_parcours, lesetapes_json = lesetapes_json)

@app.route("/admin/parcours/<int:nb_etape>")
def parcours_admin(nb_etape):
    """
        se dirige vers la page parcours
    """
    user_agent = request.user_agent.string
    etape = Etape_bd(cnx)
    composer =  Composer_bd(cnx)

    liste_composer = composer.get_par_parcour_composition(num_parcours)
    
    liste_etape = []
    
    for comp in liste_composer:    
        liste_etape.append(etape.get_par_id_etape(comp.get_parcours_id()))
    
    lesetapes = []

    for eta in liste_etape:
                i=Image_bd(cnx)
                images=i.get_par_image(eta.get_id_photo())
                try:
                    monimage=images[0].get_img_filename()
                    lesetapes.append((eta,monimage))
                except:
                    lesetapes.append((eta, "image_default.jpg"))
    

    print(lesetapes)

    lesetapes_json = []

    for eta, monimage in lesetapes:
        etape_data = {
            'id': eta.get_id_etape(),
            'nom': eta.get_nom_etape(),
            'coordonneX': eta.get_coordonneX(),
            'coordonneY': eta.get_coordonneY(),
            # Ajoutez d'autres propriétés selon vos besoins
            'image': monimage,
        }
        print(etape_data)
        lesetapes_json.append(etape_data)
    
    print(lesetapes_json)
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("parcours_mobile.html", page_mobile=True, etape_actu = [lesetapes[nb_etape - 1 ]], x = nb_etape, longueur = len(liste_etape), num_parcours = num_parcours)
    else:
        return render_template("parcours_admin.html", page_mobile=False, etape_actu = [lesetapes[nb_etape - 1 ]],  x = nb_etape, longueur = len(liste_etape), num_parcours = num_parcours, lesetapes_json = lesetapes_json)


@app.route("/mon-profil")
def mon_profil():
    user_agent = request.user_agent.string
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("mon_profil.html", page_mobile=True, page_home=False)
    else:
        return render_template("mon_profil.html", page_mobile=False, page_home=False)

@app.route("/les-parcours", methods=["GET", "POST"])
def connecter():
    """
        recupere les champs entrer dans la page de connexion et verifie 
        si l'utilisateur à déja un compte.
        Si il a un compte on le dirige vers la page des parcours
        Sinon on le redirige sur la page connexion
    """
    username=request.form.get("username")
    password=request.form.get("password")
    print(username,password)
    user = Participant_bd(cnx)
    adm = Admin_bd(cnx)
    liste_user=user.get_all_participant()
    liste_admin = adm.get_all_admin()
    for part in liste_user:
        if (username==part.get_pseudo() or username==part.get_email())and password==part.get_mdp():
            print("votre connexion fonctionne")
            test.set_email(part.get_email())
            test.set_mdp(part.get_mdp())
            test.set_pseudo(part.get_pseudo())
            parcour=Parcours_bd(cnx)
            liste_parc=parcour.get_all_parcours()
            lesparcs=[]
            monimage=""
            for parc in liste_parc:
                i=Image_bd(cnx)
                images=i.get_par_image(parc.get_id_photo())
                monimage=images[0].get_img_filename()
                lesparcs.append((parc,monimage))

            return render_template("les_parcours.html", liste_parc=lesparcs)

    for admi in liste_admin:
        if username == admi.get_pseudo() and password == admi.get_mdp():
            print("votre connexion fonctionne")
            parcour=Parcours_bd(cnx)
            liste_parc=parcour.get_all_parcours()
            lesparcs=[]
            monimage=""
            for parc in liste_parc:
                i=Image_bd(cnx)
                images=i.get_par_image(parc.get_id_photo())
                monimage=images[0].get_img_filename()
                lesparcs.append((parc,monimage))
            return render_template("les_parcours.html", liste_parc=lesparcs)
        
    close_cnx()
    return render_template("login.html", page_mobile=False, page_login=True)

@app.route("/inscription",methods=["GET", "POST"])
def inscrire():
    """
        Permet d'inscrire les utilisateur qui n'ont pas de compte
    """
    username=request.form.get("username")
    email=request.form.get("email")
    password=request.form.get("password")
    print(username)
    user = Participant_bd(cnx)
    print("test")
    liste_user=user.get_all_participant()
    print(liste_user)
    for part in liste_user:
        if username==part.get_pseudo() and email==part.get_email() and password==part.get_mdp():
            print("vous etes deja inscrit")
            cnx.close()
            return render_template("login.html", page_mobile=False, page_login=True)
    user.inserer_participant(user.get_prochain_id_participant(),username,email,password)
    print("vous etes inscrit")
    cnx.close()
    return render_template("login.html", page_mobile=False, page_login=True)

@app.route("/les_parcours")
def search():
    """
        Permet de chercher avec le titre des parcours et affiche le resultat
    """
    search_query = request.args.get("query")
    user =Parcours_bd(cnx)
    liste_parc=user.get_all_parcours()
    lesparcs=[]
    monimage=""
    for parc in liste_parc:
        if search_query!="" :
            if search_query in parc.get_nom_parc():
                i=Image_bd(cnx)
                images=i.get_par_image(parc.get_id_photo())
                monimage=images[0].get_img_filename()
                lesparcs.append((parc,monimage))
        else:
            i=Image_bd(cnx)
            images=i.get_par_image(parc.get_id_photo())
            monimage=images[0].get_img_filename()
            lesparcs.append((parc,monimage))
    return render_template("les_parcours.html", liste_parc=lesparcs)





@app.route('/get_etapes_parcours', methods=['POST'])
def get_etapes_parcours_route():
    # Récupérez l'identifiant du parcours depuis la requête
    parcours_id = request.json['parcours_id']

    composer =  Composer_bd(cnx)

    
    # Appelez la fonction Python
    etapes = composer.get_par_parcour_composition(parcours_id)

    # Renvoyez les résultats au format JSON
    return jsonify(etapes=etapes)



etape = Etape_bd(cnx)  # Assurez-vous de créer une instance appropriée de votre classe

@app.route('/api/inserer_etape', methods=['POST'])
def inserer_etape():
    print("Route /api/inserer_etape appelée")
    data = request.json
    idetape = data.get('idetape')
    nometape = data.get('nometape')
    idimage = data.get('idimage')
    coordX = data.get('coordX')
    coordY = data.get('coordY')

    etape.inserer_etape(idetape, nometape, idimage, coordX, coordY)

    return jsonify(success=True, message='Étape insérée avec succès')

@app.route('/api/get_prochain_id', methods=['GET'])
def get_prochain_id():
    prochain_id = etape.get_prochain_id_etape()

    return jsonify(prochain_id = prochain_id)

composer = Composer_bd(cnx)

@app.route('/api/get_prochain_numero', methods=['GET'])
def get_prochain_numero():
    idparc = request.args.get('idparc')
    print(idparc, "loupe")
    prochain_num = composer.get_prochain_numero_composer(idparc)
    print()
    actu_id = etape.get_prochain_id_etape()
    print(actu_id)
    return jsonify(prochain_num=prochain_num, actu_id = actu_id - 1)

@app.route('/api/inserer_composer', methods=['POST'])
def inserer_composer():
    print("Route /api/inserer_composer appelée")
    data = request.json
    idetape = data.get('idetape')
    idparc = data.get('idparc')
    numero = data.get('numero')

    print(f'idetape: {idetape}, idparc: {idparc}, numero: {numero}')

    composer.inserer_compose(idparc, idetape, numero)

    return jsonify(success=True, message='Composer insérée avec succès')



if __name__ == '__main__':
    app.run(debug=True)