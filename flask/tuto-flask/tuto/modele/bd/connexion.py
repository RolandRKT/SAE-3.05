"""
    Ouverture connexion.
"""
import sqlalchemy
#pip install mysql-connector-python


def ouvrir_connexion(user, passwd, host, database):
    """
        Cette class va nous permettre d'ouvrir la connexion à la bd.
    """
    try:
        # Create an engine for interacting with the database server
        engine = sqlalchemy.create_engine(
            f"mysql+mysqlconnector://{user}:{passwd}@{host}/{database}")

        # Create a connection
        cnx = engine.connect()
        print("Connexion réussie")
        return cnx
    except Exception as err:
        print("le serveur n'est pas connecter")
        return err


cnx = ouvrir_connexion("rakotomalala", "rakotomalala", "servinfo-maria",
                      "DBrakotomalala")

# cnx = ouvrir_connexion("dahouede", "dahouede", "servinfo-maria",
#                       "DBdahouede")

# cnx = ouvrir_connexion("rakotomalala", "rakotomalala", "localhost",
#                          "DBrakotomalala")


def close_cnx():
    cnx.close()
