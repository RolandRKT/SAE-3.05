
from flask import jsonify, render_template, url_for, redirect
from flask import request
from flask import request, redirect, url_for
from .app import app
import os
import sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))
from participant_bd import *
from parcours_bd import *

from image_bd import *
from connexion import cnx
from admin_bd import *
from etape_bd import *

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from participant import *
from admin import *


ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, ''))
from models import *

le_participant=Participant(-1,"","","")
administrateur = Admin(-1, "", "")
@app.route("/")
def home():
    """
        Nous montre la premiere page la du lancement du site
    """
    return render_template("home.html", page_home=True)

@app.route("/portails")
def portails():
    le_participant.set_email("")
    le_participant.set_mdp("")
    le_participant.set_pseudo("")
    le_participant.set_id(-1)
    administrateur.set_pseudo("")
    administrateur.set_mdp("")
    administrateur.set_id(-1)
    return render_template("portails.html")

@app.route("/login", methods=['GET','POST'])
def login():
    """
        permet de se diriger vers la page login
    """
    user_agent = request.user_agent.string
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("login_mobile.html", page_mobile=True, page_login=True)
    else:
        return render_template("login.html", page_mobile=False, page_login=True)
    
@app.route("/les-parcours")
def les_parcours():
    if le_participant.get_id() == -1:
        return redirect(url_for("portails"))
    return render_template("les_parcours.html", liste_parc=lister_les_parcours())


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
    if le_participant.get_id() == -1:
        return redirect(url_for("portails"))
    user_agent = request.user_agent.string
    ma_liste=lister_etape_du_parcours()
    lesetapes,liste_etape=ma_liste[0],ma_liste[1]
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("parcours_mobile.html", page_mobile=True, page_profil=False)
    else:
        return render_template("parcours.html", page_mobile=False, liste_etape = lesetapes, x = nb_etape, longueur = len(liste_etape), page_profil=False)

@app.route("/mon-profil")
def mon_profil():
    """
        se dirige vers la page mon profil
    """
    user_agent = request.user_agent.string
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        if le_participant.get_id() == -1:
            return redirect(url_for("portails"))
        return render_template("mon_profil.html", page_mobile=True, page_home=False, participant=le_participant, page_profil=True)
    else:
        if le_participant.get_id() == -1:
            return redirect(url_for("portails"))
        return render_template("mon_profil.html", page_mobile=False, page_home=False, participant=le_participant,page_profil=True)

@app.route("/les-parcours", methods=["GET", "POST"])
def connecter():
    """
        recupere les champs entrer dans la page de connexion et verifie 
        si l'utilisateur à déja un compte.
        Si il a un compte on le dirige vers la page des parcours
        Sinon on le redirige sur la page connexion
    """
    username = request.form.get("username")
    password = request.form.get("password")
    user = Participant_bd(cnx)
    liste_user = user.get_all_participant()
    if liste_user:
        found_user = next((part for part in liste_user if (username == part.get_pseudo() or username == part.get_email()) and password == part.get_mdp()), None)

        if found_user:
            le_participant.set_all(found_user.get_id(), found_user.get_pseudo(), found_user.get_email(), found_user.get_mdp())

            parcour = Parcours_bd(cnx)
            liste_parc = parcour.get_all_parcours()

            lesparcs = [(parc, Image_bd(cnx).get_par_image(parc.get_id_photo())[0].get_img_filename()) for parc in liste_parc]
            user_agent = request.user_agent.string
            if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
                return render_template("les_parcours_mobile.html", liste_parc=lesparcs, page_mobile=True)
            else:
                return render_template("les_parcours.html", liste_parc=lesparcs, page_mobile=False)
    return redirect(url_for("les_parcours"))
    
    
    
    
@app.route("/accueil_admin", methods=["POST"])
def connecter_admin():
    """
        recupere les champs entrer dans la page de connexion et verifie 
        si l'admin à déja un compte.
        Si il a un compte on le dirige vers la page des parcours
        Sinon on le redirige sur la page connexion
    """
    username=request.form.get("username")
    password=request.form.get("password")
    adm = Admin_bd(cnx)
    liste_admin = adm.get_all_admin()
    if liste_admin != [] and liste_admin != None:
        for admi in liste_admin:
            if username == admi.get_pseudo() and password == admi.get_mdp():
                administrateur.set_all(admi.get_id(),admi.get_pseudo(),admi.get_mdp())
                return redirect(url_for("accueil_admin"))
    return redirect(url_for("login_admin"))

@app.route("/inscription", methods=["GET", "POST"])
def inscrire():
    """
    Permet d'inscrire les utilisateur qui n'ont pas de compte
    """
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        user = Participant_bd(cnx)
        liste_user = user.get_all_participant()

        for part in liste_user:
            if username == part.get_pseudo() or email == part.get_email():
                return jsonify({"error": "exists"})

        user.inserer_participant(user.get_prochain_id_participant(), username, email, password)
        le_participant.set_all(user.get_prochain_id_participant()-1,username,email,password)
        return jsonify({"success": "registered"})

    return render_template("login.html", page_mobile=False, page_login=True) 

@app.route("/login_admin")
def login_admin():
    user_agent = request.user_agent.string
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("login_admin.html", page_mobile = True)
    else:
        return render_template("login_admin.html", page_mobile = False)

@app.route("/accueil_admin")
def accueil_admin():
    if administrateur.get_id() == -1:
        return redirect(url_for("portails"))
    user_agent = request.user_agent.string
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("accueil_admin.html", page_mobile = True)
    else:
        return render_template("accueil_admin.html", page_mobile = False)

@app.route("/redirect")
def redirection():
    return redirect(url_for('les_parcours'))

@app.route('/gerer-compte')
def gerer_compte():
    adm = Participant_bd(cnx)
    liste_participant = adm.get_all_participant()
    return render_template("gerer_compte.html", liste_part=liste_participant, adm=adm)

@app.route('/suppression-participant/<pseudo>', methods=['POST', 'DELETE'])
def suppression_participant(pseudo):
    adm = Admin_bd(cnx)
    adm.delete_part(pseudo)
    return redirect(url_for("gerer_compte"))
