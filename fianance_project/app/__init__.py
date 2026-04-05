from flask import Flask
from app.extensions import db, migrate, jwt, bcrypt
from config import DevelopmentConfig
from app.routes import api_v1

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    from app.model.user import User
    from app.model.fianancial_record import Frecord

    app.register_blueprint(api_v1)

    return app