from wtforms import PasswordField, StringField, SubmitField, ValidationError, BooleanField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, EqualTo, Optional
from flask_wtf import FlaskForm

from ..models import Usuario

class AddOrEditAlunoForm(FlaskForm):

	"""
	Form para adição/edição de um aluno
	"""

	nome = StringField('Nome', validators=[DataRequired()])
	cpf = IntegerField('CPF (somente números)', validators=[DataRequired()])
	rg = IntegerField('RG (somente números)', validators=[DataRequired()])
	naturalidade = StringField('Naturalidade', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	data_nascimento = DateField('Data de nascimento', format='%Y-%m-%d', validators=[DataRequired()])
	telefone = IntegerField('Telefone', validators=[DataRequired()])
	celular = IntegerField('Celular', validators=[DataRequired()])
	rua = StringField('Rua', validators=[DataRequired()])
	numero = IntegerField('Número', validators=[DataRequired()])
	complemento = StringField('Complemento', validators=[DataRequired()])
	bairro = StringField('Bairro', validators=[DataRequired()])
	cidade = StringField('Cidade', validators=[DataRequired()])
	uf = SelectField('UF', choices=[('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'), ('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'), ('MG','MG'), ('PA','PA'), ('PB','PB'), ('PR','PR'), ('PE','PE'), ('PI','PI'), ('RJ','RJ'), ('RN','RN'), ('RS','RS'), ('RO','RO'), ('RR','RR'), ('SC','SC'), ('SP','SP'), ('SE','SE'), ('TO', 'TO')], validators=[DataRequired()])
	cep = StringField('CEP', validators=[DataRequired()])
	nome_responsavel = StringField('Nome do responsável', validators=[DataRequired()])
	cpf_responsavel = StringField('CPF do responsável', validators=[DataRequired()])
	telefone_responsavel = StringField('Telefone do responsável', validators=[DataRequired()])
	profissao_responsavel = StringField('Profissão do responsável', validators=[DataRequired()])

	submit = SubmitField('Confirmar')

class AddOrEditAprendizForm(FlaskForm):

	"""
	Form para adição/edição de um aprendiz
	"""

	nome = StringField('Nome', validators=[DataRequired()])
	cpf = IntegerField('CPF (somente números)', validators=[DataRequired()])
	rg = IntegerField('RG (somente números)', validators=[DataRequired()])
	naturalidade = StringField('Naturalidade', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	data_nascimento = DateField('Data de nascimento', format='%Y-%m-%d', validators=[DataRequired()])
	telefone = IntegerField('Telefone', validators=[DataRequired()])
	celular = IntegerField('Celular', validators=[DataRequired()])
	rua = StringField('Rua', validators=[DataRequired()])
	numero = IntegerField('Número', validators=[DataRequired()])
	complemento = StringField('Complemento', validators=[DataRequired()])
	bairro = StringField('Bairro', validators=[DataRequired()])
	cidade = StringField('Cidade', validators=[DataRequired()])
	uf = SelectField('UF', choices=[('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'), ('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'), ('MG','MG'), ('PA','PA'), ('PB','PB'), ('PR','PR'), ('PE','PE'), ('PI','PI'), ('RJ','RJ'), ('RN','RN'), ('RS','RS'), ('RO','RO'), ('RR','RR'), ('SC','SC'), ('SP','SP'), ('SE','SE'), ('TO', 'TO')], validators=[DataRequired()])
	cep = StringField('CEP', validators=[DataRequired()])
	trabalho = StringField('Trabalho', validators=[DataRequired()])
	nome_responsavel = StringField('Nome do responsável', validators=[DataRequired()])
	cpf_responsavel = StringField('CPF do responsável', validators=[DataRequired()])
	telefone_responsavel = StringField('Telefone do responsável', validators=[DataRequired()])
	profissao_responsavel = StringField('Profissão do responsável', validators=[DataRequired()])

	submit = SubmitField('Confirmar')

class AddOrEditVoluntarioForm(FlaskForm):

	"""
	Form para adição/edição de um voluntario
	"""

	nome = StringField('Nome', validators=[DataRequired()])
	cpf = IntegerField('CPF (somente números)', validators=[DataRequired()])
	rg = IntegerField('RG (somente números)', validators=[DataRequired()])
	naturalidade = StringField('Naturalidade', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	data_nascimento = DateField('Data de nascimento', format='%Y-%m-%d', validators=[DataRequired()])
	telefone = IntegerField('Telefone', validators=[DataRequired()])
	celular = IntegerField('Celular', validators=[DataRequired()])
	rua = StringField('Rua', validators=[DataRequired()])
	numero = IntegerField('Número', validators=[DataRequired()])
	complemento = StringField('Complemento', validators=[DataRequired()])
	bairro = StringField('Bairro', validators=[DataRequired()])
	cidade = StringField('Cidade', validators=[DataRequired()])
	uf = SelectField('UF', choices=[('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'), ('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'), ('MG','MG'), ('PA','PA'), ('PB','PB'), ('PR','PR'), ('PE','PE'), ('PI','PI'), ('RJ','RJ'), ('RN','RN'), ('RS','RS'), ('RO','RO'), ('RR','RR'), ('SC','SC'), ('SP','SP'), ('SE','SE'), ('TO', 'TO')], validators=[DataRequired()])
	cep = StringField('CEP', validators=[DataRequired()])
	matricula = StringField('Matrícula', validators=[DataRequired()])

	submit = SubmitField('Confirmar')
