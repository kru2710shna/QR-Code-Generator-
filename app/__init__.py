from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Configure LoginManager
    login_manager.login_view = 'auth.login'
    login_manager.login_message = "Please log in to access this page."
    login_manager.login_message_category = "info"

    # Register blueprints
    from app.routes.auth_routes import auth_routes
    from app.routes.qr_routes import qr_routes
    from app.routes.dashboard_routes import dashboard_routes
    
    app.register_blueprint(auth_routes, url_prefix='/auth')
    app.register_blueprint(qr_routes, url_prefix='/qr')
    app.register_blueprint(dashboard_routes, url_prefix='/dashboard')

    return app
