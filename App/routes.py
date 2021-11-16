from datetime import datetime as dt
from werkzeug.exceptions import HTTPException
from flask import current_app as app, request, json, render_template, redirect, url_for
from flask_login import current_user, login_required, logout_user

from .ooka_tools import get_year

 # index ookamy
@app.route("/")
def home():
    # Template completement independant
    return render_template('index.html', d=get_year())


# liste des modules
@app.route("/modules")
def module():
    return render_template('modules.html', menu_active='Modules')


@app.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('home'))

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('error/404.html'), 404

@app.errorhandler(500)
def page_not_found(error):
    return render_template('error/500.html'), 500

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

# @app.route("/connect", methods=['GET', 'POST'])  # formulaire de login authentification.auth | template auth.login
# def login():
#     # GET => affiche le form
#     # POST => envoie les données
#     if request.method == 'POST':
#         # username = request.form['username']
#         # password = request.form['password']
#         return redirect(url_for('module'))


#     return render_template('auth/login.html')



# enregistrement de compte qui ne sera pas mis en place
# Il y aura juste 2 comptes : visitor et ookamy
# @app.route("/register", methods=['GET', 'POST'])  # formulaire de login authentification.auth | template auth.login
# def register():
#     return render_template('auth/register.html')

#
#



#
#

# @app.route("/ookarchyves")  # index de ookarchyves
# def ookarchyves_index():
#     return render_template('module/ookarchyves/main.html')

# @app.route("/ookarchyves/ftheme", methods=['GET', 'POST'])  # formulaire d'ajout de theme + liste des themes deja existant avec possibilité de supprimer une theme vide d'article
# def ookarchyves_form_add_theme():
#     return render_template('module/ookarchyves/fTheme.html')

# @app.route("/ookarchyves/farticle", methods=['GET', 'POST'])  #
# def ookarchyves_form_add_article():
#     return render_template('module/ookarchyves/fArticle.html')

# @app.route("/ookarchyves/article")  # voir l'article avec la possibilité de naviger vers suppression de l'article ou la modification
# def ookarchyves_article():
#     return render_template('module/ookarchyves/article.html')

#
#

# @app.route("/modules/ookamanager")  # index du kanban
# def moddule():
#     return render_template('module/ookamanager/main.html')


# @app.route("/chemin/url")
# def nomvariable():
#     return render_template('dossier/fichier.html')
