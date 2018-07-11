from wtforms import PasswordField, StringField, SubmitField, ValidationError, BooleanField, DateField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Optional
from flask_wtf import FlaskForm

from ..models import Usuario

class AddAluno():

"""
Form para adição de uma pessoa
"""

	nome = StringField('Nome', validators=[DataRequired()])
	cpf = IntegerField('CPF (somente números)', validators=[DataRequired()])
	rg = IntegerField('RG (somente números)', validators=[DataRequired()])
	naturalidade = StringField('Naturalidade', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	data_nascimento = Datefield('Data de nascimento', validators=[DataRequired()])
	telefone = IntegerField('Telefone', validators=[DataRequired()])
	celular = IntegerField('Celular', validators=[DataRequired()])
	rua - StringField('Rua', validators=[DataRequired()])
	numero = IntegerField('Número', validators=[DataRequired()])
	complemento = StringField('Complemento', validator=[DataRequired()])
	bairro = StringField('Bairro', validators=[DataRequired()])
	cidade = StringField('Cidade', validators=[DataRequired()])
	uf = StringField('UF', validators=[DataRequired()])
	cep = StringField('CEP', validators=[DataRequired()])
	nome_responsavel = StringField('Nome do responsável', validators=[DataRequired()])
	cpf_responsavel = StringField('CPF do responsável', validators=[DataRequired()])
	telefone_responsavel = StringField('Telefone do responsável', validators=[DataRequired()])
	profissao_responsavel = StringField('Profissão do responsável', validators=[DataRequired()])
