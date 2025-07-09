import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'clave-super-secreta'  # Cambiar en producción
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'pesajes.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False