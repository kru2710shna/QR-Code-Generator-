from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file
from flask_login import login_required, current_user
from app.models import QRCode
from app import db
import qrcode
import os

qr_routes = Blueprint("qr", __name__)

@qr_routes.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.get("data")
        secure = "secure" in request.form

        qr = qrcode.QRCode(box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        file_path = f"static/qr_codes/{data}.png"
        img.save(file_path)

        new_qr = QRCode(data=data, secure=secure, file_path=file_path, user_id=current_user.id if current_user.is_authenticated else None)
        db.session.add(new_qr)
        db.session.commit()

        flash("QR Code generated successfully!", "success")
        return redirect(url_for("qr.index"))
    return render_template("index.html")

@qr_routes.route("/view-secure", methods=["GET", "POST"])
def view_secure():
    if request.method == "POST":
        key = request.form.get("key")
        qr_code = QRCode.query.filter_by(hashed_key=key).first()

        if qr_code:
            return send_file(qr_code.file_path, as_attachment=True)
        else:
            flash("Invalid security key.", "danger")
    return render_template("secure_view.html")
