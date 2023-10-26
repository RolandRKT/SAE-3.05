__package__ = "Modele"

import sqlalchemy
#pip install mysql-connector-python

def ouvrir_connexion(user, passwd, host, database):
    try:
        # Create an engine for interacting with the database server
        engine = sqlalchemy.create_engine(f"mysql+mysqlconnector://{user}:{passwd}@{host}/{database}")
        
        # Create a connection
        cnx = engine.connect()
        print("Connexion réussie")
        return cnx
    except Exception as err:
        print(err)
        raise err


cnx = ouvrir_connexion("dahouede","dahouede","servinfo-maria","DBdahouede")

def get_cnx():
    return cnx

#import sqlalchemy
#
#def ouvrir_connexion():
#    try:
#        # Utilisez le mot de passe échappé dans la chaîne de connexion.
#        engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:root_password@localhost/test')
#        
#        
#        # Créez une connexion.
#        cnx = engine.connect()
#        print("Connexion réussie")
#        return cnx
#    except Exception as err:
#        print(err)
#        raise err
#
#cnx = ouvrir_connexion()
#