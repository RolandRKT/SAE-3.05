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
from terminer_bd import Termine_bd

SUIVRE = Suivre_bd(cnx)
COMPOSER = Composer_bd(cnx)
PARCOURS = Parcours_bd(cnx)
IMAGE = Image_bd(cnx)
PARTICIPANT = Participant_bd(cnx)
TERMINE = Termine_bd(cnx)


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
    liste_term = liste_terminer_et_suivi(id_participant)
    boolean = False
    for parc in PARCOURS.get_all_parcours():
        for suivi in liste_term:
            print(type(parc.get_id_parc()), type(suivi.get_id_parc()))
            if parc.get_id_parc() == suivi.get_id_parc():
                boolean = True
                print(boolean)
        if not boolean:
            liste.append((parc, IMAGE.get_par_image(
                parc.get_id_photo())[0].get_img_filename()))
            print(liste)
        boolean = False
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
        if not TERMINE.get_termine_id_part(id_participant,
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
    liste_des_parcours = PARCOURS.get_all_parcours()
    liste_termine = []
    for suivi in liste_des_parcours:
        if TERMINE.get_termine_id_part(id_participant, suivi.get_id_parc()):
            parcour_courant = PARCOURS.get_par_parcours(suivi.get_id_parc())[0]
            images = IMAGE.get_par_image(parcour_courant.get_id_photo())
            monimage = images[0].get_img_filename()
            liste_termine.append((parcour_courant, monimage))
    return (liste_termine, liste_suivi)


def liste_terminer_et_suivi(id_part):
    """
    Cette fonction retourne la liste des parcours suivis et terminés par un participant.

    Parameters:
        id_part (int): L'ID du participant.

    Returns:
        list: Une liste contenant les parcours suivis et terminés par le participant.
    """
    liste_suivi = SUIVRE.get_par_suivre_participant(id_part)
    liste_termine = TERMINE.get_all_termine(id_part)

    if liste_suivi and liste_termine:
        return liste_suivi + liste_termine
    elif liste_suivi:
        return liste_suivi
    elif liste_termine:
        return liste_termine

    return []


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


def inserer_parcours_view(nom_parcours, description, id_img, duree):
    next_id_parcours = PARCOURS.get_prochain_id_parcours()
    PARCOURS.inserer_parcours(next_id_parcours, nom_parcours,
                              duree + str(':00'), description, id_img)
    return next_id_parcours


def inserer_composer_view(parcours_id, etape_id, order):
    COMPOSER.inserer_compose(parcours_id, etape_id, order)


# def supprimer_avis(id_parcours, pseudo):
#     id_participant = PARTICIPANT.get_id_participant_par_pseudo(pseudo)
#     TERMINE.supprimer_termine(id_parcours, id_participant)
#     pass


def voir_note_comm_du_parcours(id_parcours):
    """
        Récupère la note et le commentaire d'un parcours.

        Args:
            id_parcours (int): L'identifiant du parcours.

        Returns:
            list: Une liste contenant les notes et commentaires du parcours.
    """
    return TERMINE.get_note_comm(id_parcours)


def particpant_parcours_note_comm(id_parcours,id_participant):
    """
        Récupère la note et le commentaire d'un parcours.

        Args:
            id_parcours (int): L'identifiant du parcours.

        Returns:
            list: Une liste contenant les notes et commentaires du parcours.
    """
    return TERMINE.get_termine_id_part(id_participant, id_parcours)


def note_comm_parcours_participant(id_parcours, id_participant):
    """
        Récupère la note et le commentaire d'un parcours.

        Args:
            id_parcours (int): L'identifiant du parcours.
            id_participant (int): L'identifiant du participant.

        Returns:
            list: Une liste contenant les notes et commentaires du parcours.
    """
    return TERMINE.get_note_comm_parc_part(id_parcours, id_participant)


def maj_note_comm(id_parcours, id_participant, note, comm):
    """
        Met à jour la note et le commentaire d'un parcours.

        Args:
            id_parcours (int): L'identifiant du parcours.
            id_participant (int): L'identifiant du participant.
            note (int): La note attribuée au parcours.
            comm (str): Le commentaire du participant.
    """
    TERMINE.mettre_a_jour_note_comm(id_parcours, id_participant, note, comm)


def get_moyenne_note_parcours(id_parcours):
    """
        Récupère la moyenne des notes attribuées à un parcours.

        Args:
            id_parcours (int): L'identifiant du parcours.

        Returns:
            float: La moyenne des notes attribuées au parcours.
    """
    return TERMINE.get_note_moyenne(id_parcours)


def get_nb_personne_ayant_termine_noter_commenter(id_parcours):
    """
        Récupère le nombre de personne ayant terminé un parcours.

        Args:
            id_parcours (int): L'identifiant du parcours.

        Returns:
            int: Le nombre de personne ayant terminé le parcours.
    """
    return TERMINE.get_nb_personne(id_parcours)