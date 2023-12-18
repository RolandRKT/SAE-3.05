from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))

from admin import Admin


class Admin_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_admin(self):
        try:
            query = text("select id_admin, pseudo, mdp from ADMIN")
            resultat = self.cnx.execute(query)
            admin=[]
            for id_admin, pseudo, mdp in resultat:
                admin.append(Admin(id_admin, pseudo, mdp))
            return admin
        except Exception as e:
            print("aaaaaaaaaaaaaaah")
            return None
        
    def get_par_admin(self,id_admin):
        try:
            query = text("select id_admin, pseudo, mdp from ADMIN where id_admin= "+str(id_admin))
            resultat = self.cnx.execute(query)
            admin=[]
            for id_admin, pseudo, mdp in resultat:
                admin.append(Admin(id_admin, pseudo, mdp))
            return admin
        except Exception as e:
            print("la connexion a échoué")
            print(e)
            return None

    def inserer_admin(self, idadmin, pseudo, mail, mdp):
        try:
            query = text(f"insert into ADMIN values({str(idadmin)}, '{pseudo}', '{mdp}')")
            self.cnx.execute(query)
            self.cnx.commit()
            print("Reussi")
        except Exception as e:
            print("La connexion a échoué")
            print(e)
            return None


    def get_prochain_id_admin(self):
        try:
            query = text("SELECT MAX(id_admin) as m FROM ADMIN")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("La connexion a échoué shushduz")
            print(e)
            return None
