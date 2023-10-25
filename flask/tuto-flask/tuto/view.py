from .app import app, db
from flask import jsonify, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired
from flask import request
from hashlib import sha256
from wtforms import PasswordField
from flask import request, redirect, url_for
from wtforms import FloatField
from flask import flash

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/create-account")
def createaccount():
    return render_template("inscription.html")

@app.route("/home_mobile")
def home_mobile():
    return render_template("home_mobile.html")

@app.route("/login_mobile")
def login_mobile():
    return render_template("login_mobile.html")

@app.route("/inscription_mobile")
def inscription_mobile():
    return render_template("inscription_mobile.html")

# Nouvelle route pour effectuer la redirection
@app.route("/redirect_home_mobile")
def redirect_home_mobile():
    return redirect(url_for("home_mobile"))
