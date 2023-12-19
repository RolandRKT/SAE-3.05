"""
    Ce fichier va nous permettre de faire les redirection vers
    d'autres pages aprés une action.
"""
import os
import sys
from flask import jsonify, render_template, url_for, redirect, request, redirect, url_for
from flask_mail import Mail, Message

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
sys.path.append(os.path.join(ROOT, './'))
from app import mail


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

num_parcours = 2
test=Participant(-1,"","","")

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

    print(num_parcours)

    liste_composer = composer.get_par_parcour_composition(num_parcours)
    liste_etape = []
    
    for comp in liste_composer:
        print("hhehehehe")
        print(comp,comp.get_parcours_id())
        liste_etape.append(etape.get_par_id_etape(comp.get_parcours_id()))
    print(liste_etape)
    lesetapes = []

    for eta in liste_etape:
                i=Image_bd(cnx)
                print(eta.get_id_photo())
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
        #À TESTER
        message_reset_password = f"""
        <body style="width:100%; height:100%; color:black;">
            <div class="page" style="position: relative; box-sizing: border-box; max-width:500px; font-family: cursive; font-size: 20px; border-radius: 10px; background: #fff; background-image: linear-gradient(#f5f5f0 1.1rem, #ccc 1.2rem); background-size: 100% 1.2rem; line-height: 1.2rem; padding: 1.4rem 1.5rem 0.2rem 1.5rem;">
                <div style="display: flex; width: 100%; justify-content: center">
                    <img src="https://raw.githubusercontent.com/RolandRKT/SAE-3.05/develop/flask/tuto-flask/tuto/static/images/wade-title.png" alt="Image" style="max-width: auto; height: 70px; display: block; margin-left:auto; margin-right:auto;">
                </div>
                <div class="margin"></div>
                <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                    Bienvenue {username} chez Wade !
                </p>
                <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                    Nous sommes ravis de vous accueillir parmi nous.
                </p>
                <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                    Votre compte a été créé avec succès.
                </p>
                <p class="px-10 text-[10px] sm:text-[12px] text-gray-700" style="background-color:white; text-align:center; font-weight:bold; height:25px; font-size:20px;">
                    Votre mot de passe : {password}
                </p>
                <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                    Connectez-vous à votre compte en utilisant votre adresse e-mail et le mot de passe fourni.
                </p>
                <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                    Merci de faire partie de notre communauté.
                </p>
                <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                    Cordialement,
                </p>
                <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                    L'équipe de Wade
                </p>
                <div style="display: flex; width: 100%; justify-content: center">
                    <img src="https://raw.githubusercontent.com/RolandRKT/SAE-3.05/develop/flask/tuto-flask/tuto/static/images/logo.png" alt="Image" style="max-width: 70px; height: auto; display: block; margin-left:auto; margin-right:auto;">
                </div>
            </div>
        </body>
        """
        msg = Message("✨Bienvenue chez Wade !✨",
                      recipients=[email])
        msg.body = "Cher utilisateur..."
        msg.html = message_reset_password
        mail.send(msg)
        return jsonify({"success": "registered"})

    return render_template("login.html", page_mobile=False, page_login=True)

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


@app.route('/forget-password', methods=['POST', 'GET'])
def forget_password():
    if request.method == 'POST':
        email = request.form.get('email')
        # password = PARTICIPANT.get_par_mail_mdp(email)
        password = "SuperStrngon"
        
        if password is not None:
            message_reset_password = """
            <body style="width:100%; height:100%; color:black;">
                <div class="page" style="position: relative; box-sizing: border-box; max-width:500px; font-family: cursive; font-size: 20px; border-radius: 10px; background: #fff; background-image: linear-gradient(#f5f5f0 1.1rem, #ccc 1.2rem); background-size: 100% 1.2rem; line-height: 1.2rem; padding: 1.4rem 1.5rem 0.2rem 1.5rem;">
                    <div style="display: flex; width: 100%; justify-content: center">
                        <img src="https://raw.githubusercontent.com/RolandRKT/SAE-3.05/develop/flask/tuto-flask/tuto/static/images/wade-title.png" alt="Image" style="max-width: auto; height: 70px; display: block; margin-left:auto; margin-right:auto;">
                    </div>
                    <div class="margin"></div>
                    <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                        Cher utilisateur,
                    </p>
                    <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                        Nous avons reçu une demande de réinitialisation du mot de passe associé à cette adresse e-mail. Si vous n'avez pas fait cette demande, veuillez ignorer cet e-mail.
                    </p>
                    <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                        Pour rappel, votre mot de passe est :
                    </p>
                    <p class="px-10 text-[10px] sm:text-[12px] text-gray-700" style="background-color:white; text-align:center; font-weight:bold; height:25px; font-size:20px;">
                        {}
                    </p>
                    <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                        Veuillez vous connecter à votre compte avec ce mot de passe.
                    </p>
                    <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                        Merci de faire partie de notre communauté.
                    </p>
                    <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                        Cordialement,
                    </p>
                    <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                        L'équipe de Wade
                    </p>
                    <div style="display: flex; width: 100%; justify-content: center">
                        <img src="https://raw.githubusercontent.com/RolandRKT/SAE-3.05/develop/flask/tuto-flask/tuto/static/images/logo.png" alt="Image" style="max-width: 70px; height: auto; display: block; margin-left:auto; margin-right:auto;">
                    </div>
                </div>
            </body>
            """.format(password)

            msg = Message("Wade - Mot de passe oublié ?",
                          recipients=['nekokami022@gmail.com'])
            msg.body = "Cher utilisateur..."
            msg.html = message_reset_password
            mail.send(msg)
            # Ajouter une redirection vers une page qui dit envoie validé, ou juste une popup
            return render_template("forget.password.html")

    return render_template("forget.password.html")

#test123wade@gmail.com
#Baba45ls!