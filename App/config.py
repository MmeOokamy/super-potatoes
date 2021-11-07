from os import environ, path
from .ooka_tools import get_env_variable

basedir = path.abspath(path.dirname(__file__))

class Config:
    """Set Flask configuration from environment variables."""

    FLASK_APP = get_env_variable('FLASK_APP')
    FLASK_ENV = get_env_variable('FLASK_ENV')
    SECRET_KEY = get_env_variable('SK')


    # Static Assets
    STATIC_FOLDER = get_env_variable('App/static')
    TEMPLATES_FOLDER = get_env_variable('App/templates')
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False