from flask import Flask
from flask_cors import CORS

from .config import Config
from flask_jwt_extended import JWTManager
from .utils.db import db


def create_app():
    app = Flask(__name__)
    # CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
    CORS(app)

    app.config.from_object(Config)

    # Set the path to store uploaded files (event images)
    app.config['UPLOAD_FOLDER'] = 'D:/GitHub/Other Projects/ArenaSync/frontend/public/assets/event_img/'

    db.init_app(app)
    jwt = JWTManager(app)

    with app.app_context():
        from .models import Admin, Player, Event, EventRegistration
        db.create_all()  # Create database tables for our data models

        from .routes.user_routes import user_blueprint
        from .routes.admin_routes import admin_blueprint
        from .routes.event_routes import event_blueprint

        app.register_blueprint(user_blueprint, url_prefix='/user')
        app.register_blueprint(admin_blueprint, url_prefix='/admin')
        app.register_blueprint(event_blueprint, url_prefix='/event')

    return app
