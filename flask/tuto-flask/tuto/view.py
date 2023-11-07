
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


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    print("hahaha")
    user_agent = request.user_agent.string
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("login_mobile.html", page_mobile=True, page_login=True)
    else:
        return render_template("login.html", page_mobile=False, page_login=True)


@app.route("/inscription")
def inscription():
    user_agent = request.user_agent.string
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("inscription_mobile.html", page_mobile=True, page_login=False)
    else:
        return render_template("inscription.html", page_mobile=False, page_login=False)

@app.route("/parcours")
def parcours():
    return render_template("parcours.html")

@app.route("/login", methods=["GET", "POST"])
def connecter():
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
