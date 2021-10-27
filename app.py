from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# ajouter le .env et lier les os.getenv machin chose
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://USER:PASSWORD@HOST/DATABASE'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

@app.route("/")
def index():
    return 'hello'


if __name__ == "__main__":
    app.run(debug=True)