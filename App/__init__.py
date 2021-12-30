import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')
    # app.config.from_pyfile('config.py', silent=True)  # another form

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Import all modules her
        from . import routes
    
        from .authentication import auth
        app.register_blueprint(auth.auth_bp)

        from .ookamanager import routes
        app.register_blueprint(routes.om_bp)

        from .ookarchyves import routes
        app.register_blueprint(routes.oa_bp)

        from .settings import params
        app.register_blueprint(params.p_bp)

        # Create Database Models
        db.create_all()

    return app