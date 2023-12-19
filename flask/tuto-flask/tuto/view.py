"""
    Ce fichier va nous permettre de faire les redirection vers
    d'autres pages aprés une action.
"""
import os
import sys
from flask import jsonify, render_template, url_for, redirect, request, redirect, url_for

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))
from participant_bd import Participant_bd
from connexion import cnx
from admin_bd import Admin_bd

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from participant import *
from admin import *

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, ''))
from models import les_parcour_suivi, les_parcours_terminer,lister_etape_du_parcours, lister_les_parcours, inserer_le_participant

le_participant = Participant(-1, "", "", "")
administrateur = Admin(-1, "", "")

PARTICIPANT = Participant_bd(cnx)
ADMIN = Admin_bd(cnx)

from .app import app


@app.route("/")
def home():
    """
        Nous montre la premiere page la du lancement du site
    """
    return render_template("home.html", page_home=True)


@app.route("/portails")
def portails():
    """
        Cette fonction va nous diriger vers la pages des portails.
    """
    le_participant.set_all(-1, "", "", "")
    administrateur.set_all(-1, "", "")
    user_agent = request.user_agent.string
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("portail_mobile.html")
    return render_template("portails.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    """
        permet de se diriger vers la page login
    """
    user_agent = request.user_agent.string
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("login_mobile.html",
                               page_mobile=True,
                               page_login=True)
    return render_template("login.html",
                               page_mobile=False,
                               page_login=True)


@app.route("/les-parcours")
def les_parcours():
    """
        Cette fonction nous permet de nous diriger vers la page qui
        liste les parcours
    """
    if le_participant.get_id() == -1:
        return redirect(url_for("portails"))
    user_agent = request.user_agent.string
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("les_parcours_mobile.html",
                               liste_parc=lister_les_parcours(),
                               page_mobile=True)
    return render_template("les_parcours.html",
                               liste_parc=lister_les_parcours(),
                               page_mobile=False)


@app.route("/inscription")
def inscription():
    """
        Permet de se diriger vers la page inscription
    """
    user_agent = request.user_agent.string
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("inscription_mobile.html",
                               page_mobile=True,
                               page_login=False)
    return render_template("inscription.html",
                               page_mobile=False,
                               page_login=False)


@app.route("/parcours/<int:nb_etape>")
def parcours(nb_etape):
    """
        se dirige vers la page parcours
    """
    if le_participant.get_id() == -1:
        return redirect(url_for("portails"))
    user_agent = request.user_agent.string
    ma_liste = lister_etape_du_parcours()
    lesetapes, liste_etape = ma_liste[0], ma_liste[1]
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("parcours_mobile.html",
                               page_mobile=True,
                               page_profil=False)
    return render_template("parcours.html",
                               page_mobile=False,
                               liste_etape=lesetapes,
                               x=nb_etape,
                               longueur=len(liste_etape),
                               page_profil=False)


@app.route("/mon-profil")
def mon_profil():
    """
        se dirige vers la page mon profil
    """
    user_agent = request.user_agent.string
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        if le_participant.get_id() == -1:
            return redirect(url_for("portails"))
        return render_template("mon_profil.html",
                               page_mobile=True,
                               page_home=False,
                               participant=le_participant,
                               page_profil=True)
    if le_participant.get_id() == -1:
        return redirect(url_for("portails"))
    return render_template("mon_profil.html",
                               page_mobile=False,
                               page_home=False,
                               participant=le_participant,
                               page_profil=True)


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
    liste_user = PARTICIPANT.get_all_participant()
    if liste_user:
        found_user = next(
            (part for part in liste_user
             if (username == part.get_pseudo() or username == part.get_email())
             and password == part.get_mdp()), None)
        if found_user:
            le_participant.set_all(found_user.get_id(),
                                   found_user.get_pseudo(),
                                   found_user.get_email(),
                                   found_user.get_mdp())
            return redirect(url_for("les_parcours"))
    return redirect(url_for("login"))


@app.route("/accueil_admin", methods=["POST"])
def connecter_admin():
    """
        recupere les champs entrer dans la page de connexion et verifie
        si l'admin à déja un compte.
        Si il a un compte on le dirige vers la page des parcours
        Sinon on le redirige sur la page connexion
    """
    username = request.form.get("username")
    password = request.form.get("password")
    liste_admin = ADMIN.get_all_admin()
    if liste_admin != [] and liste_admin is not None:
        for admi in liste_admin:
            if username == admi.get_pseudo() and password == admi.get_mdp():
                administrateur.set_all(admi.get_id(), admi.get_pseudo(),
                                       admi.get_mdp())
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
        liste_user = PARTICIPANT.get_all_participant()

        for part in liste_user:
            if username == part.get_pseudo() or email == part.get_email():
                return jsonify({"error": "exists"})
        inserer_le_participant(username, email, password)
        le_participant.set_all(PARTICIPANT.get_prochain_id_participant() - 1,
                               username, email, password)
        return jsonify({"success": "registered"})

    return render_template("login.html", page_mobile=False, page_login=True)


@app.route("/login_admin")
def login_admin():
    """
        Cette fonction permet de nous diriger vers la page login.
    """
    user_agent = request.user_agent.string
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("login_admin_mobile.html", page_mobile=True)
    return render_template("login_admin.html", page_mobile=False)


@app.route("/accueil_admin")
def accueil_admin():
    """
        Cette fonction nous dirige vers la page accueil admin.
    """
    if administrateur.get_id() == -1:
        return redirect(url_for("portails"))
    user_agent = request.user_agent.string
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("accueil_admin.html", page_mobile=True)
    return render_template("accueil_admin.html", page_mobile=False)


@app.route("/mes-parcours/en-cours")
def mes_parcours_en_cours():
    """
        Cette focntion va nous permettre d'afficher
        les differents parcours que l'utilisateur est en-train de faire.
    """
    if le_participant.get_id() == -1:
        return redirect(url_for("portails"))
    user_agent = request.user_agent.string

    liste_parcour = les_parcour_suivi(le_participant.get_id())
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("mes_parcours.html",
                               liste_termines=None,
                               liste_suivis=liste_parcour,
                               page_mobile=True,
                               page_home=False,
                               page_profil=False,
                               page_mes_parcours=True,
                               onglet=1)
    return render_template("mes_parcours.html",
                               liste_termines=None,
                               liste_suivis=liste_parcour,
                               page_mobile=False,
                               page_home=False,
                               page_profil=False,
                               page_mes_parcours=True,
                               onglet=1)


@app.route("/mes-parcours/terminees")
def mes_parcours_terminees():
    """
       Cette focntion va nous permettre d'afficher
       les differents parcours que l'utilisateur a terminer.
    """
    if le_participant.get_id() == -1:
        return redirect(url_for("portails"))
    user_agent = request.user_agent.string
    liste_termine = les_parcours_terminer(le_participant.get_id())[0]
    liste_suivi = les_parcours_terminer(le_participant.get_id())[1]
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("mes_parcours.html",
                               liste_termines=liste_termine,
                               liste_suivis=liste_suivi,
                               page_mobile=True,
                               page_home=False,
                               page_profil=False,
                               page_mes_parcours=True,
                               onglet=2)
    return render_template("mes_parcours.html",
                           liste_termines=liste_termine,
                           liste_suivis=liste_suivi,
                           page_mobile=False,
                           page_home=False,
                           page_profil=False,
                           page_mes_parcours=True,
                           onglet=2)


@app.route("/redirect")
def redirection():
    return redirect(url_for('les_parcours'))

@app.route('/gerer-compte')
def gerer_compte():
    """
        Cette methode va nous permettre de nous diriger vers la page gerer compte
    """
    liste_participant = PARTICIPANT.get_all_participant()
    return render_template("gerer_compte.html",
                           liste_part=liste_participant,
                           adm=PARTICIPANT)


@app.route('/suppression-participant/<pseudo>', methods=['POST', 'DELETE'])
def suppression_participant(pseudo):
    """
        Cette fonction va nous permettre de supprimer un participant
        et de nous rediriger vers la page gerer compte
    """
    ADMIN.delete_part(pseudo)
    return redirect(url_for("gerer_compte"))
