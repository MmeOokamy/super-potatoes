import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from .config import Config

db = SQLAlchemy()


def init_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        from .authentication import auth
        app.register_blueprint(authentication.auth.bp)

        from .ookamanager import main
        app.register_blueprint(ookamanager.main.bp)

        from .ookarchyves import main
        app.register_blueprint(ookarchyves.main.bp)

        from .settings import params
        app.register_blueprint(settings.params.bp)

        return app


# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     # a simple page
#     @app.route('/')
#     def index():
#         return render_template('index.html')
#     app.add_url_rule('/', endpoint='index')


#     # menu test page
#     @app.route('/connect')
#     def connect():
#         module_name = "Connection"
        

#         return render_template('auth/login.html')
    
#     from .authentication import auth
#     app.register_blueprint(authentication.auth.bp)

#     from .ookamanager import main
#     app.register_blueprint(ookamanager.main.bp)

#     from .ookarchyves import main
#     app.register_blueprint(ookarchyves.main.bp)

#     from .settings import params
#     app.register_blueprint(settings.params.bp)
    
#     return app