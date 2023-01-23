from flask import Flask
from config import config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

cors = CORS(resources={ r'/api|/auth/*': { 'origins': '*' } })
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize modules
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models from modules
    from .auth import models as auth_models

    # Register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
