from newpinterest import database, login_manager
from datetime import datetime, timezone
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario)) #usa-se get quando é busca é feita pelo id do usuário


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True)

class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png") #não é a imagem em si, mas o nome do arquivo que contém a imagem
    data_criacao = database.Column(database.DateTime, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)