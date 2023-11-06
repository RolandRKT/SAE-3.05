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
    user_agent = request.user_agent.string
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("login_mobile.html", page_mobile=True, page_login=True)
    else:
        return render_template("login.html", page_mobile=False, page_login=True)

@app.route("/inscription")
def inscription():
    user_agent = request.user_agent.string
    if any(keyword in user_agent for keyword in ["Mobi", "Android", "iPhone", "iPad"]):
        return render_template("inscription_mobile.html", page_mobile=True, page_login=False)
    else:
        return render_template("inscription.html", page_mobile=False, page_login=False)

@app.route("/parcours")
def parcours():
    return render_template("parcours.html")
