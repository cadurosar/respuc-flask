from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

from app import db, login_manager

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'

    usuario_id = db.Column(db.Integer, primary_key=True)
    senha_hash = db.Column(db.String(128))
    email = db.Column(db.String(60), index=True, unique=True)
    role = db.Column(db.String(5), nullable=False)
    confirmado = db.Column(db.Boolean, nullable=False, default=False)

    @property
    def senha(self):
        raise AttributeError('senha is not a readable attribute.')

    @senha.setter
    def senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verify_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return '<email {}'.format(self.email)

    def get_id(self):
        return self.usuario_id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

@login_manager.user_loader
def load_user(usuario_id):
    return Usuario.query.get(usuario_id)