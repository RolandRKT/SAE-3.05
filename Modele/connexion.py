import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


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


cnx = ouvrir_connexion("dahoude","dahoude","servinfo-maria","DBdahoude")


