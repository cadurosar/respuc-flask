from ..base_form import EnemBaseForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from ..models import Usuario

class RegistrationForm(EnemBaseForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    usuario_id = StringField('Usuário', validators=[DataRequired(), Length(max=10, message ='Tamanho máximo: 10 caracteres.')])
    nome = StringField('Nome', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), EqualTo('confirma_senha')])
    confirma_senha = PasswordField('Confirmar Senha')
    e_coordenador = BooleanField('Você é um coordenador?', validators=[])
    e_professor = BooleanField('Você é um professor?', validators=[])
    submit = SubmitField('Registrar')

    def validate_email(self, field):
        if Usuario.query.filter_by(email=field.data).first():
            raise ValidationError('Email já em uso.')

    def validate_username(self, field):
        if Employee.query.filter_by(usuario_id=field.data).first():
            raise ValidationError('Nome de usuário já em uso.')

class LoginForm(EnemBaseForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')
