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
from suivre_bd import *



def lister_les_parcours() -> list:
    """
        Cette methode va nous permettre de retourner une liste de tuple avec le premier
        element qui est le parcours et le second qui est son images.
        Args:
            return (list): une lsite de tuple
    """
    parcour=Parcours_bd(cnx)
    liste_parc=parcour.get_all_parcours()
    lesparcs=[]
    monimage=""
    for parc in liste_parc:
        i=Image_bd(cnx)
        images=i.get_par_image(parc.get_id_photo())
        monimage=images[0].get_img_filename()
        lesparcs.append((parc,monimage))
    return lesparcs

def lister_etape_du_parcours():
    etape = Etape_bd(cnx)
    liste_etape = etape.get_all_etape()
    lesetapes = []
    for eta in liste_etape:
        i=Image_bd(cnx)
        images=i.get_par_image(eta.get_id_photo())
        monimage=images[0].get_img_filename()
        lesetapes.append((eta,monimage))
    return (lesetapes,liste_etape)
