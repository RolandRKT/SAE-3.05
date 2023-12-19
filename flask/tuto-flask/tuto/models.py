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
PARTICIPANT=Participant_bd(cnx)



def lister_les_parcours() -> list:
    """
        Retourne une liste de tuples contenant chaque parcours et son image associée.

        Returns:
            List[Tuple[Parcours, str]]:
                Une liste de tuples où chaque tuple contient un objet Parcours et le nom de son image associée.
    """
    return [(parc, IMAGE.get_par_image(parc.get_id_photo())[0].get_img_filename()) for parc in PARCOURS.get_all_parcours()]

def inserer_le_participant(user,mail,paw):
    """
        Cette va nous permettre d'appeler la fonction que l'admin utilise pour
        inserer un utilisateur.
    """
    PARTICIPANT.inserer_participant(PARTICIPANT.get_prochain_id_participant(), user, mail, paw)

def les_parcour_suivi(id):
    """
        Récupère la liste des parcours actuellement suivis par un utilisateur.

        Args:
            id (int): L'identifiant unique de l'utilisateur.

        Returns:
            List[Tuple[Parcours, str]]:
                Une liste de tuples où chaque tuple contient un parcours en cours et le nom de son image associée.
    """
    liste_suivi = SUIVRE.get_par_suivre_participant(id)
    liste_parcour = list()    
    for suivi in liste_suivi:
        if COMPOSER.get_max_etape_composer(suivi.get_id_parc()) != SUIVRE.get_num_etape_suivre(suivi.get_id_parc()):
            parcour_courant = PARCOURS.get_par_parcours(suivi.get_id_parc())[0]
            images = IMAGE.get_par_image(parcour_courant.get_id_photo())
            monimage = images[0].get_img_filename()
            liste_parcour.append((parcour_courant, monimage))
    return liste_parcour

def les_parcours_terminer(id):
    """
    Récupère les parcours terminés par un utilisateur.

    Args:
        id (int): L'identifiant de l'utilisateur.

    Returns:
        Tuple[List[Tuple[Parcours, str]], List[Suivi]]:
            - Une liste de tuples où chaque tuple contient un parcours terminé et le nom de son image associée.
            - Une liste des objets Suivi représentant le suivi de chaque parcours par l'utilisateur.
    """
    liste_suivi = SUIVRE.get_par_suivre_participant(id)
    liste_termine = list()
    for suivi in liste_suivi:
        if COMPOSER.get_max_etape_composer(suivi.get_id_parc()) == SUIVRE.get_num_etape_suivre(suivi.get_id_parc()):
            parcour_courant = PARCOURS.get_par_parcours(suivi.get_id_parc())[0]
            images = IMAGE.get_par_image(parcour_courant.get_id_photo())
            monimage = images[0].get_img_filename()
            liste_termine.append((parcour_courant, monimage))
    return (liste_termine,liste_suivi)


def lister_etape_du_parcours():
    etape = Etape_bd(cnx)
    liste_etape = etape.get_all_etape()
    lesetapes = []
    for eta in liste_etape:
        images=IMAGE.get_par_image(eta.get_id_photo())
        monimage=images[0].get_img_filename()
        lesetapes.append((eta,monimage))
    return (lesetapes,liste_etape)