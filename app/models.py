from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model, UserMixin):
    """Model for storing user information."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Password hashing
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"

class QRCode(db.Model):
    """Model for storing QR code information."""
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text, nullable=False)  # The data encoded in the QR code
    hashed_key = db.Column(db.String(128), nullable=True)  # Secure key for private QR codes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Optional link to the user
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship to link user to QR codes
    user = db.relationship('User', backref=db.backref('qrcodes', lazy=True))

    def __repr__(self):
        return f"<QRCode {self.id}>"
