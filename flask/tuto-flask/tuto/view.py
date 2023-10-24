from .app import app, db
from flask import jsonify, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField ,HiddenField
from wtforms.validators import DataRequired
from flask import request
from hashlib import sha256
from wtforms import PasswordField
from flask import request, redirect, url_for
from wtforms import FloatField
from flask import flash

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/create-account")
def createaccount():
    return render_template("inscription.html")
