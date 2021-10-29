import os
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import db_test

app = Flask(__name__)
# ajouter le .env et lier les os.getenv machin chose 'postgresql://USER:PASSWORD@HOST/DATABASE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + str(os.getenv('USER')) + ':' + str(os.getenv('PWD')) + '@' + str(os.getenv('HOST')) + '/' + str(os.getenv('DATABASE'))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = MyDatabase()

@app.route("/")
def index():
    coucou = db.query('SELECT * FROM users;')

    return coucou


if __name__ == "__main__":
    app.run(debug=True)