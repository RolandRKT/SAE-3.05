
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
from suivre_bd import *
from image_bd import *
from connexion import cnx,close_cnx
from admin_bd import *
from etape_bd import *
from composer_bd import *

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from participant import *
from admin import *

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
    etape = Etape_bd(cnx)
    liste_etape = etape.get_all_etape()
    lesetapes = []
    for eta in liste_etape:
                i=Image_bd(cnx)
                images=i.get_par_image(eta.get_id_photo())
                monimage=images[0].get_img_filename()
                lesetapes.append((eta,monimage))
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("parcours_mobile.html", page_mobile=True, page_profil=False)
    else:
        return render_template("parcours.html", page_mobile=False, liste_etape = lesetapes, x = nb_etape, longueur = len(liste_etape), page_profil=False)

@app.route("/mon-profil")
def mon_profil():
    
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
    username=request.form.get("username")
    password=request.form.get("password")
    print(username,password)
    user = Participant_bd(cnx)
    adm = Admin_bd(cnx)
    liste_user=user.get_all_participant()

    print(liste_user)
    liste_admin = adm.get_all_admin()
    print(liste_admin)
    if liste_user != [] and liste_user != None:
        for part in liste_user:
            if (username==part.get_pseudo() or username==part.get_email())and password==part.get_mdp():
                print("votre connexion fonctionne")
                le_participant.set_email(part.get_email())
                le_participant.set_mdp(part.get_mdp())
                le_participant.set_pseudo(part.get_pseudo())
                le_participant.set_id(part.get_id())
                parcour=Parcours_bd(cnx)
                liste_parc=parcour.get_all_parcours()
                lesparcs=[]
                monimage=""
                for parc in liste_parc:
                    i=Image_bd(cnx)
                    images=i.get_par_image(parc.get_id_photo())
                    monimage=images[0].get_img_filename()
                    lesparcs.append((parc,monimage))
                user_agent = request.user_agent.string
                if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
                    return render_template("les_parcours_mobile.html", liste_parc=lesparcs, page_mobile=True)
                else:
                    return render_template("les_parcours.html", liste_parc=lesparcs, page_mobile=False)
    if liste_admin != [] and liste_admin != None:
        for admi in liste_admin:
            if username == admi.get_pseudo() and password == admi.get_mdp():
                administrateur.set_pseudo(admi.get_pseudo())
                administrateur.set_mdp(admi.get_mdp())
                administrateur.set_id(admi.get_id_admin())
                
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
                return redirect(url_for("accueil_admin"))
    return redirect(url_for("login"))


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
    liste_user=user.get_all_participant()
    if liste_user != [] and liste_user != None:
        for part in liste_user:
            if username==part.get_pseudo() and email==part.get_email() and password==part.get_mdp():
                print("vous etes deja inscrit")
                
                return render_template("login.html", page_mobile=False, page_login=True)
    user.inserer_participant(user.get_prochain_id_participant(),username,email,password)
    return redirect(url_for("login"))

@app.route("/login_admin")
def login_admin():
    print("hahaha")
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

@app.route("/mes-parcours/en-cours")
def mes_parcours_en_cours():
    if le_participant.get_id() == -1:
        return redirect(url_for("portails"))
    user_agent = request.user_agent.string
    user = Suivre_bd(cnx)
    parcour = Parcours_bd(cnx)
    liste_suivi = user.get_par_suivre_participant(le_participant.get_id())
    liste_parcour = list()
    i = Image_bd(cnx)
    for suivi in liste_suivi:
        parcour_courant = parcour.get_par_parcours(suivi.get_id_parc())[0]
        images = i.get_par_image(parcour_courant.get_id_photo())
        monimage = images[0].get_img_filename()
        liste_parcour.append((parcour_courant, monimage))
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("mes_parcours.html", liste_termines=None, liste_suivis=liste_parcour, page_mobile=True, page_home=False, page_profil=False, page_mes_parcours=True, onglet=1)
    else:
        return render_template("mes_parcours.html", liste_termines=None, liste_suivis=liste_parcour, page_mobile=False, page_home=False, page_profil=False, page_mes_parcours=True, onglet=1)

@app.route("/mes-parcours/terminees")
def mes_parcours_terminees():
    if le_participant.get_id() == -1:
        return redirect(url_for("portails"))
    user_agent = request.user_agent.string
    user = Suivre_bd(cnx)
    composer = Composer_bd(cnx)
    parcour = Parcours_bd(cnx)
    liste_suivi = user.get_par_suivre_participant(le_participant.get_id())
    liste_termine = list()
    i = Image_bd(cnx)
    for suivi in liste_suivi:
        print("ID Parcours: ", suivi.get_id_parc())
        print("composer:", composer.get_max_etape_composer(suivi.get_id_parc()))
        if composer.get_max_etape_composer(suivi.get_id_parc()) == user.get_num_etape_suivre(suivi.get_id_parc()):
            print("bbbbbbbbb")
            parcour_courant = parcour.get_par_parcours(suivi.get_id_parc())[0]
            images = i.get_par_image(parcour_courant.get_id_photo())
            monimage = images[0].get_img_filename()
            liste_termine.append((parcour_courant, monimage))
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("mes_parcours.html", liste_termines=liste_termine, liste_suivis=liste_suivi, page_mobile=True, page_home=False, page_profil=False, page_mes_parcours=True, onglet=2)
    else:
        return render_template("mes_parcours.html", liste_termines=liste_termine, liste_suivis=liste_suivi, page_mobile=False, page_home=False, page_profil=False, page_mes_parcours=True, onglet=2)
