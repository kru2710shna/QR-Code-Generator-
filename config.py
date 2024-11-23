import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '12hdud9d7bjdd7gdkdod64bdjdi'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///instance/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
