import os
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# ajouter le .env et lier les os.getenv machin chose 'postgresql://USER:PASSWORD@HOST/DATABASE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + str(os.getenv('USER')) + ':' + str(os.getenv('PWD')) + '@' + str(os.getenv('HOST')) + '/' + str(os.getenv('DATABASE'))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)