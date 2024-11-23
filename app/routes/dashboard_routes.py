from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard_routes = Blueprint("dashboard", __name__)

@dashboard_routes.route("/dashboard")
@login_required
def dashboard():
    user_qrcodes = current_user.qrcodes  # Assuming relationship is set up in User model
    return render_template("dashboard.html", qrcodes=user_qrcodes)
