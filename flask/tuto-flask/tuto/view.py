"""
    Ce fichier va nous permettre de faire les redirection vers
    d'autres pages aprés une action.
"""
from io import BytesIO
import os
import sys
from tkinter import Canvas
from flask import jsonify, render_template, send_file, url_for, redirect, request
from flask import request
from werkzeug.utils import secure_filename
from .app import app
from flask import jsonify, render_template, url_for, redirect, request, redirect, url_for
from flask_mail import Mail, Message

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))

from participant_bd import Participant_bd
from parcours_bd import Parcours_bd
from image_bd import Image_bd
from connexion import cnx
from admin_bd import Admin_bd
from etape_bd import Etape_bd
from composer_bd import Composer_bd
from suivre_bd import Suivre_bd
from terminer_bd import Termine_bd

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')

sys.path.append(os.path.join(ROOT, './'))
from app import mail

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, './'))
from message import msg_forget_password, msg_inscription

sys.path.append(os.path.join(ROOT, 'modele/bd/'))

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, ''))

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from models import les_parcour_suivi, les_parcours_terminer, inserer_parcours_view, lister_les_parcours, inserer_le_participant, inserer_composer_view
from participant import *
from admin import *

UPLOAD_FOLDER = './tuto/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

le_participant = Participant(-1, "", "", "")
administrateur = Admin(-1, "", "")

PARTICIPANT = Participant_bd(cnx)
ADMIN = Admin_bd(cnx)
TERMINE = Termine_bd(cnx)
PARCOURS = Parcours_bd(cnx)
ETAPE = Etape_bd(cnx)
COMPOSER = Composer_bd(cnx)
SUIVRE = Suivre_bd(cnx)
IMAGE = Image_bd(cnx)
TERMINER = Termine_bd(cnx)
TERMINE = Termine_bd(cnx)

from .app import app

num_parcours = 2


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
    return render_template("login.html", page_mobile=False, page_login=True)


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
                               liste_parc=lister_les_parcours(
                                   le_participant.get_id()),
                               page_mobile=True)
    return render_template("les_parcours.html",
                           liste_parc=lister_les_parcours(
                               le_participant.get_id()),
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


@app.route("/get_parcours/<int:num>")
def changement_parcours(num):
    """
        Permet de se diriger vers la page parcours
    """
    global num_parcours
    num_parcours = num
    nb_etape = SUIVRE.get_num_etape_suivre(num_parcours,
                                           le_participant.get_id())
    if nb_etape is None:
        nb_etape = 1
    return redirect(url_for("parcours", nb_etape=nb_etape))


@app.route("/debut/<int:num>")
def debut(num):
    """
        Permet de se diriger vers la page parcours
    """
    global num_parcours
    num_parcours = num
    return redirect(url_for("parcours", nb_etape=0))


@app.route("/parcours/<int:nb_etape>")
def parcours(nb_etape):
    """
        se dirige vers la page parcours
    """
    if nb_etape == 0:
        val = 1
    else:
        val = nb_etape
        SUIVRE.update_numero_etape(le_participant.get_id(), num_parcours,
                                   nb_etape)
    user_agent = request.user_agent.string

    liste_composer = COMPOSER.get_par_parcour_composition(num_parcours)
    liste_etape = []
    for comp in liste_composer:
        liste_etape.append(ETAPE.get_par_id_etape(comp.get_parcours_id()))

    lesetapes = []

    for eta in liste_etape:
        images = IMAGE.get_par_image(eta.get_id_photo())
        try:
            monimage = images[0].get_img_filename()
            lesetapes.append((eta, monimage))
        except:
            lesetapes.append((eta, "image_default.jpg"))
    lesetapes_json = []

    for eta, monimage in lesetapes:
        etape_data = {
            'id': eta.get_id_etape(),
            'nom': eta.get_nom_etape(),
            'coordonneX': eta.get_coordonneX(),
            'coordonneY': eta.get_coordonneY(),
            'image': monimage,
        }
        lesetapes_json.append(etape_data)

    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("parcours_mobile.html",
                               page_mobile=True,
                               etape_actu=[lesetapes[val - 1]],
                               x=nb_etape,
                               longueur=len(liste_etape),
                               num_parcours=num_parcours,
                               lesetapes_json=lesetapes_json)
    else:
        return render_template("parcours.html",
                               page_mobile=False,
                               etape_actu=[lesetapes[val - 1]],
                               x=nb_etape,
                               longueur=len(liste_etape),
                               num_parcours=num_parcours,
                               lesetapes_json=lesetapes_json)


@app.route("/admin/parcours/<int:nb>")
def parcours_admin(nb):
    """
        se dirige vers la page parcours
    """
    user_agent = request.user_agent.string
    liste_composer = COMPOSER.get_par_parcour_composition(nb)
    liste_etape = []

    for comp in liste_composer:
        liste_etape.append(ETAPE.get_par_id_etape(comp.get_parcours_id()))
    lesetapes = []

    for eta in liste_etape:
        images = IMAGE.get_par_image(eta.get_id_photo())
        try:
            monimage = images[0].get_img_filename()
            lesetapes.append((eta, monimage))
        except:
            lesetapes.append((eta, "image_default.jpg"))

    lesetapes_json = []

    for eta, monimage in lesetapes:
        etape_data = {
            'id': eta.get_id_etape(),
            'nom': eta.get_nom_etape(),
            'coordonneX': eta.get_coordonneX(),
            'coordonneY': eta.get_coordonneY(),
            'image': monimage,
        }
        lesetapes_json.append(etape_data)

    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        print("Pas encore implémenter")
        return None
    else:
        return render_template("parcours_admin.html",
                               page_mobile=False,
                               etape_actu=[lesetapes[0]],
                               longueur=len(liste_etape),
                               num_parcours=nb,
                               lesetapes_json=lesetapes_json)


@app.route("/admin_inserer/parcours")
def parcours_admin_inserer():
    """
        se dirige vers la page parcours
    """
    user_agent = request.user_agent.string

    liste_composer = COMPOSER.get_par_parcour_composition(num_parcours)
    liste_etape = []

    for comp in liste_composer:
        liste_etape.append(ETAPE.get_par_id_etape(comp.get_parcours_id()))
    lesetapes = []

    for eta in liste_etape:
        images = IMAGE.get_par_image(eta.get_id_photo())
        try:
            monimage = images[0].get_img_filename()
            lesetapes.append((eta, monimage))
        except:
            lesetapes.append((eta, "image_default.jpg"))

    lesetapes_json = []

    for eta, monimage in lesetapes:
        etape_data = {
            'id': eta.get_id_etape(),
            'nom': eta.get_nom_etape(),
            'coordonneX': eta.get_coordonneX(),
            'coordonneY': eta.get_coordonneY(),
            'image': monimage,
        }
        lesetapes_json.append(etape_data)

    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        print("Pas encore implémenter")
        return None
    else:
        return render_template("parcours_inserer_etape.html",
                               page_mobile=False,
                               etape_actu=[lesetapes[0]],
                               longueur=len(liste_etape),
                               num_parcours=num_parcours,
                               lesetapes_json=lesetapes_json)


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
        return render_template("mon_profil_mobile.html",
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
        msg = Message("✨Bienvenue chez Wade !✨", recipients=[email])
        msg.body = "Cher utilisateur..."
        msg.html = msg_inscription(username, password)
        mail.send(msg)
        return jsonify({"success": "registered"})

    return render_template("login.html", page_mobile=False, page_login=True)


@app.route('/get_etapes_parcours', methods=['POST'])
def get_etapes_parcours_route():
    # Récupérez l'identifiant du parcours depuis la requête
    parcours_id = request.json['parcours_id']

    etapes = COMPOSER.get_par_parcour_composition(parcours_id)

    return jsonify(etapes=etapes)


@app.route('/api/inserer_etape', methods=['POST'])
def inserer_etape():
    data = request.json
    idetape = data.get('idetape')
    nometape = data.get('nometape')
    idimage = data.get('idimage')
    coordX = data.get('coordX')
    coordY = data.get('coordY')

    ETAPE.inserer_etape(idetape, nometape, idimage, coordX, coordY, None)

    return jsonify(success=True, message='Étape insérée avec succès')


@app.route('/api/get_prochain_id', methods=['GET'])
def get_prochain_id():
    prochain_id = ETAPE.get_prochain_id_etape()
    return jsonify(prochain_id=prochain_id)


@app.route('/api/get_prochain_numero', methods=['GET'])
def get_prochain_numero():
    idparc = request.args.get('idparc')
    prochain_num = COMPOSER.get_prochain_numero_composer(idparc)
    actu_id = ETAPE.get_prochain_id_etape()
    return jsonify(prochain_num=prochain_num, actu_id=actu_id - 1)


@app.route('/api/inserer_composer', methods=['POST'])
def inserer_composer():
    data = request.json
    idetape = data.get('idetape')
    idparc = data.get('idparc')
    numero = data.get('numero')
    COMPOSER.inserer_compose(idparc, idetape, numero)

    return jsonify(success=True, message='Composer insérée avec succès')


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
        return render_template("accueil_admin.html",
                               page_mobile=True,
                               page_accueil_admin=True)
    return render_template("accueil_admin.html",
                           page_mobile=False,
                           page_accueil_admin=True)


@app.route("/mes-parcours/en-cours")
def mes_parcours_en_cours():
    """
        Cette fonction va nous permettre d'afficher
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
                               onglet=1,
                               en_cours=True)
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
       Cette fonction va nous permettre d'afficher
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
                               onglet=2,
                               en_cours=False)
    return render_template("mes_parcours.html",
                           liste_termines=liste_termine,
                           liste_suivis=liste_suivi,
                           page_mobile=False,
                           page_home=False,
                           page_profil=False,
                           page_mes_parcours=True,
                           onglet=2)


@app.route("/creation_parcours")
def creation_parcours():
    liste_etape = ETAPE.get_all_etape()

    user_agent = request.user_agent.string
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("creation_parcours.html",
                               liste=liste_etape,
                               page_mobile=True)
    else:
        return render_template("creation_parcours.html",
                               liste=liste_etape,
                               page_mobile=False)


@app.route("/creation_parcours", methods=['GET', 'POST'])
def creer_parcours():
    if request.method == 'POST':
        # Traitement des autres champs
        nom_parcours = request.form.get('nom_parcours')
        description = request.form.get('textarea')
        duree = request.form.get('duree')

        ordered_etapes = request.form.get('orderedEtapes')
        ordered_etapes_ids = [
            int(etape_id) for etape_id in ordered_etapes.split(',') if etape_id
        ]

        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        # Traitement de l'image téléchargée
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '':
                # Générez un nom de fichier unique
                filename = secure_filename(image.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                print("Chemin du fichier :", filepath)
                image.save(filepath)
                next_id = IMAGE.get_prochain_id_image()
                # Enregistrez le nom du fichier dans la base de données ou utilisez comme nécessaire
                IMAGE.inserer_image(next_id, filename + str("'"),
                                    str(filename) + str(next_id),
                                    str(filename))

                # Insertion du parcours
                parcours_id = inserer_parcours_view(nom_parcours, description,
                                                    next_id, str(duree))

                for order, etape_id in enumerate(ordered_etapes_ids, start=1):
                    inserer_composer_view(parcours_id, etape_id, order)

                return redirect(url_for("accueil_admin"))
        return redirect(url_for("creation_parcours"))


@app.route("/redirect")
def redirection():
    return redirect(url_for('les_parcours'))


@app.route('/gerer-compte')
def gerer_compte():
    """
        Cette methode va nous permettre de nous diriger vers la page gerer compte
    """
    liste_participant = PARTICIPANT.get_all_participant()
    user_agent = request.user_agent.string
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("gerer_compte.html",
                               liste_part=liste_participant,
                               adm=PARTICIPANT,
                               page_mobile=True)
    else:
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


@app.route('/supprimer_etape_parcours<int:num_etape>/<int:num_parcours>',
           methods=['GET'])
def supprimer_etape_parcours(num_etape, num_parcours):
    """
    Cette fonction permet de supprimer une étape d'un parcours et redirige vers la
    page du parcours.
    """
    COMPOSER.supprimer_etape_parcours(num_parcours, num_etape)
    return redirect(url_for("parcours_admin", nb=num_parcours))


@app.route('/forget-password', methods=['POST', 'GET'])
def forget_password():
    """
    Cette fonction gère la réinitialisation du mot de passe en cas d'oubli.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = PARTICIPANT.get_par_mail_mdp(email)
        if password is not None:
            msg = Message("Wade - Mot de passe oublié ?", recipients=[email])
            msg.body = "Cher utilisateur..."
            msg.html = msg_forget_password(password)
            mail.send(msg)
            return redirect(url_for("login"))
    return render_template("forget.password.html")


@app.route('/gestion_parcours')
def gerer_parcours():
    """
    Cette fonction redirige vers la page de gestion des parcours.
    """
    les_parcours = PARCOURS.get_all_parcours()
    les_etapes = ETAPE.get_all_etape()
    return render_template("gerer_parcours.html",
                           liste_parc=les_parcours,
                           liste_etape=les_etapes)


@app.route("/avis")
def avis():
    """
        Cette fonction permet de nous diriger vers la page avis.
    """
    user_agent = request.user_agent.string
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("avis.html", page_mobile=True, avis=True)
    return render_template("avis.html", page_mobile=False, avis=True)


@app.route('/les_parcours', methods=['POST'])
def les_parcours2():
    """
    Cette fonction gère la notation des parcours par les participants.
    """
    participant = le_participant.get_id()
    radio = int(request.form.get('star-radio'))
    textarea = request.form.get('textarea')
    TERMINE.inserer_termine(num_parcours, participant, radio, textarea)
    return redirect(url_for("les_parcours"))


@app.route('/suppression-parcours/<id_parc>', methods=['POST', 'DELETE'])
def suppression_parcours(id_parc):
    """
        Cette fonction va nous permettre de supprimer un parcours
        et de nous rediriger vers la page gerer parcours
    """
    PARCOURS.delete_parcours(int(id_parc))
    return redirect(url_for("gerer_parcours"))


@app.route('/suppression-etape/<id_etp>', methods=['POST', 'DELETE'])
def suppression_etape(id_etp):
    """
        Cette fonction va nous permettre de supprimer une étape
        et de nous rediriger vers la page gerer parcours
    """
    ETAPE.supprimer_toutes_les_etapes_composer(PARCOURS, id_etp)
    return redirect(url_for("gerer_parcours"))


@app.route('/commencer')
def commencer():
    """
    Cette fonction gère le début d'un parcours pour un participant.
    """
    SUIVRE.inserer_suivre(le_participant.get_id(), num_parcours, 1)
    return redirect(url_for('parcours', nb_etape=1))


@app.route('/validation-etape', methods=['POST', 'GET'])
def validation():
    """
    Cette fonction gère la validation lors de la création d'une étape.
    """
    query = request.args
    editable = query.get('editable', False)
    if editable:
        id_etape = query.get('id_etape')
        return render_template("validation_etape.html",
                               id_etape=id_etape,
                               nom_etape=query['nom_etape'],
                               coord_x=query['coord_x'],
                               coord_y=query['coord_y'],
                               editable=editable)

    return render_template("validation_etape.html",
                           nom_etape=query['nom_etape'],
                           coord_x=query['coord_x'],
                           coord_y=query['coord_y'],
                           editable=editable)


@app.route('/inserer_etape_bd', methods=['POST'])
def inserer_etape_bd():
    """
    Cette fonction insère une étape dans la base de données.
    """
    if request.method == "POST":
        nom_etape = request.form.get("nom_etape")
        desc = request.form.get("description")
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '':
                filename = secure_filename(image.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                print("Chemin du fichier :", filepath)
                image.save(filepath)
                next_id = IMAGE.get_prochain_id_image()
                IMAGE.inserer_image(next_id, filename + str("'"),
                                    str(filename) + str(next_id),
                                    str(filename))

        ETAPE.update(nom_etape, desc, IMAGE.get_prochain_id_image() - 1)

    return redirect(url_for('accueil_admin'))


@app.route('/edit_parcours', methods=['POST'])
def edit_parcours():
    """
    Cette fonction permet d'éditer les détails d'un parcours.
    """
    if request.method == "POST":
        nom_etape = request.form.get('nom_etape')
        desc = request.form.get('description')
        id_etape = request.form.get('id_etape')
        ETAPE.update_par_id(id_etape, nom_etape, desc)

    return redirect(url_for('accueil_admin'))


@app.route('/avis/<int:id_parc>', methods=['GET', 'POST'])
def avis_parcours(id_parc):
    """
    Cette fonction affiche les avis pour un parcours spécifique.
    """
    liste_avis = TERMINER.get_note_comm(id_parc)
    user_agent = request.user_agent.string
    if any(keyword in user_agent
           for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("page_avis_admin.html",
                               liste=liste_avis,
                               page_mobile=True)
    else:
        return render_template("page_avis_admin.html",
                               liste=liste_avis,
                               page_mobile=False)


@app.route("/redirect-admin")
def redirection_admin():
    """
    Cette fonction redirige vers la page d'accueil de l'administrateur.
    """
    return redirect(url_for('accueil_admin'))
