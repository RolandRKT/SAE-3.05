"""
    Ce fichier va nous permettre de faire le lien avec la bd
"""
import os
import sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))
from participant_bd import Participant_bd
from parcours_bd import Parcours_bd
from image_bd import Image_bd
from connexion import cnx
from etape_bd import Etape_bd
from suivre_bd import Suivre_bd
from composer_bd import Composer_bd

SUIVRE = Suivre_bd(cnx)
COMPOSER = Composer_bd(cnx)
PARCOURS = Parcours_bd(cnx)
IMAGE = Image_bd(cnx)
PARTICIPANT = Participant_bd(cnx)


def lister_les_parcours(id_participant) -> list:
    """
        Retourne une liste de tuples contenant chaque parcours et son image associée.
        Args:
        Param: id_participant : l'id du participant
        Returns:
            List[Tuple[Parcours, str]]:
                Une liste de tuples où chaque tuple contient un objet Parcours et
                le nom de son image associée.
    """
    liste = []
    liste_term=liste_terminer_et_suivi(id_participant)
    boolean=False
    for parc in PARCOURS.get_all_parcours():
        for suivi in liste_term:
            print(type(parc.get_id_parc()),type(suivi.get_id_parc()))
            if parc.get_id_parc() == suivi.get_id_parc():
                boolean=True
                print(boolean)
        if not boolean:
            liste.append((parc,IMAGE.get_par_image(parc.get_id_photo())[0].get_img_filename()))
            print(liste)
        boolean=False
    return liste
            


def inserer_le_participant(user, mail, paw):
    """
        Cette va nous permettre d'appeler la fonction que l'admin utilise pour
        inserer un utilisateur.
    """
    PARTICIPANT.inserer_participant(PARTICIPANT.get_prochain_id_participant(),
                                    user, mail, paw)


def les_parcour_suivi(id_participant):
    """
        Récupère la liste des parcours actuellement suivis par un utilisateur.

        Args:
            id_participant (int): L'identifiant unique de l'utilisateur.

        Returns:
            List[Tuple[Parcours, str]]:
                Une liste de tuples où chaque tuple contient un
                parcours en cours et le nom de son image associée.
    """
    liste_suivi = SUIVRE.get_par_suivre_participant(id_participant)
    liste_parcour = []
    for suivi in liste_suivi:
        if COMPOSER.get_max_etape_composer(
                suivi.get_id_parc()) != SUIVRE.get_num_etape_suivre(
                    suivi.get_id_parc()):
            parcour_courant = PARCOURS.get_par_parcours(suivi.get_id_parc())[0]
            images = IMAGE.get_par_image(parcour_courant.get_id_photo())
            monimage = images[0].get_img_filename()
            liste_parcour.append((parcour_courant, monimage))
    return liste_parcour


def les_parcours_terminer(id_participant):
    """
    Récupère les parcours terminés par un utilisateur.

    Args:
        id (int): L'identifiant de l'utilisateur.

    Returns:
        Tuple[List[Tuple[Parcours, str]], List[Suivi]]:
            - Une liste de tuples où chaque tuple contient
            un parcours terminé et le nom de son image associée.
            - Une liste des objets Suivi représentant
            le suivi de chaque parcours par l'utilisateur.
    """
    liste_suivi = SUIVRE.get_par_suivre_participant(id_participant)
    liste_termine = []
    for suivi in liste_suivi:
        if COMPOSER.get_max_etape_composer(
                suivi.get_id_parc()) == SUIVRE.get_num_etape_suivre(
                    suivi.get_id_parc()):
            parcour_courant = PARCOURS.get_par_parcours(suivi.get_id_parc())[0]
            images = IMAGE.get_par_image(parcour_courant.get_id_photo())
            monimage = images[0].get_img_filename()
            liste_termine.append((parcour_courant, monimage))
    return (liste_termine, liste_suivi)


def liste_terminer_et_suivi(id_part):
    """
        Cette fonction 
    """
    liste_suivi = SUIVRE.get_par_suivre_participant(id_part)
    liste_termine = []
    for suivi in liste_suivi:
        liste_termine.append(suivi)
    return liste_termine



def lister_etape_du_parcours():
    """
        Methode permettant de je sais pas
    """
    etape = Etape_bd(cnx)
    liste_etape = etape.get_all_etape()
    lesetapes = []
    for eta in liste_etape:
        images = IMAGE.get_par_image(eta.get_id_photo())
        monimage = images[0].get_img_filename()
        lesetapes.append((eta, monimage))
    return (lesetapes, liste_etape)


def inserer_parcours_view( nom_parcours, description, id_img, duree='00:06:00'):
    parcours = Parcours_bd(cnx)
    next_id_parcours = parcours.get_prochain_id_parcours()
    parcours.inserer_parcours(next_id_parcours, nom_parcours, duree, description, id_img)