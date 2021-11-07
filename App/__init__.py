import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)
        

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        from . import routes
    
        # from .authentication import auth
        # app.register_blueprint(authentication.auth.bp)

        # from .ookamanager import main
        # app.register_blueprint(ookamanager.main.bp)

        # from .ookarchyves import main
        # app.register_blueprint(ookarchyves.main.bp)

        # from .settings import params
        # app.register_blueprint(settings.params.bp)
        
    return app