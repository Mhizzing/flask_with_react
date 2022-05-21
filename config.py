import os
from dotenv import load_dotenv



basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """
    Base config class.
    """

    # Default settings
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = False
    WTF_CSRF_ENABLED = True

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'simply-unbreakable'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI', default="sqlite:///" + os.path.join(basedir, 'prod.db'))