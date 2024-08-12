from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.extensions import db, migrate, bcrypt, jwt
from app.routes import auth_bp, business_bp, stk_bp



def create_app(config_class=Config):
    app = Flask(__name__)
    # Enable CORS on all routes
    CORS(app)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(business_bp, url_prefix='/business')
    app.register_blueprint(stk_bp, url_prefix = '/stk_push')
    

    return app

