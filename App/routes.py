from flask import current_app as app, request, json, render_template, redirect, url_for
from flask_login import current_user, login_required, logout_user
from werkzeug.exceptions import HTTPException

from .ooka_tools import get_year

 # index ookamy
@app.route("/")
def home():
    # Template completement independant
    return render_template('index.html', d=get_year())


# liste des modules
@app.route("/news")
@login_required
def news():
    return render_template('news.html', menu_active='News')


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

