from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
api_bp = Blueprint('api', __name__)
api = Api(api_bp)


def create_app(config_class=Config):
    """Initialise app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(api_bp, url_prefix='/api')

    return app

from flask_backend import models
from flask_backend import resources