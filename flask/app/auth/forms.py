from wtforms import PasswordField, StringField, SubmitField, ValidationError, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf import FlaskForm

from ..models import Usuario

class RegistrationForm(FlaskForm):
    role = SelectField('Função', choices = [('aprendiz','Aprendiz'),('aluno','Aluno')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), EqualTo('confirma_senha')])
    confirma_senha = PasswordField('Confirmar Senha')
    submit = SubmitField('Registrar')

    def validate_email(self, field):
        if Usuario.query.filter_by(email=field.data).first():
            raise ValidationError('Email já em uso.')

    def validate_username(self, field):
        if Usuario.query.filter_by(usuario_id=field.data).first():
            raise ValidationError('Nome de usuário já em uso.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')
