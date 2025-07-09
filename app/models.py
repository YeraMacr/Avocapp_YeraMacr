from . import db, login_manager, bcrypt
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    pesajes = db.relationship('Pesaje', backref='usuario', lazy=True)

    @property
    def password(self):
        raise AttributeError('Contraseña no legible')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Pesaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    peso = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
