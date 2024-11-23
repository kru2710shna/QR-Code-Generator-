from flask import Blueprint

# Initialize blueprint
routes = Blueprint("routes", __name__)

# Import routes to register them
from .auth_routes import *
from .qr_routes import *
from .dashboard_routes import *
