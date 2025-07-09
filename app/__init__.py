from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from . import auth, main
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(main.main_bp)

    with app.app_context():
        db.create_all()

    return app