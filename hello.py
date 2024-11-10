from flask import Flask, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os

TEMPLATES = "templates"
app = Flask(__name__, template_folder=TEMPLATES)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://projetweb:La!meilleure!boutique!de!velo!numero!1@localhost/my_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de SQLAlchemy et Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/ping")
def ping():
    print("ping")
    return '<a href="pong">Ping!</a>'

@app.route("/pong")
def pong():
    print("pong")
    return '<a href="ping">Pong!</a>'

