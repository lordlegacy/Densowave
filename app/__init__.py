from flask import Flask
from app.config import Config
from app.extensions import db, migrate, bcrypt, jwt
from app.routes import auth_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
