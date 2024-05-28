from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from newpinterest.models import Usuario
from werkzeug.security import generate_password_hash, check_password_hash


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first() #filtra-se pela variável (não se usa get)
        if not usuario:
            raise ValidationError("Usuário não encontrado, crie uma conta.")

    '''def validate_senha(self, senha):
        # validate_email will ensure that self.usuario is set
        if self.usuario and not check_password_hash(self.usuario.senha, senha.data):
            raise ValidationError("Senha incorreta")'''


class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first() #filtra-se pela variável (não se usa get)
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar.")
        
    def validate_confirmacao_senha(self, confirmacao_senha):
        if confirmacao_senha.data != self.senha.data:
            raise ValidationError("As senhas não correspondem.")


class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Eviar Foto")