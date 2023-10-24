import os.path
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE8LOCAL']=True
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = "bcc090e2-26b2-4c16-84ab-e766cc644320"

def mkpath(path):
    return (os.path.normpath(os.path.join(os.path.dirname(__file__),path)))

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)