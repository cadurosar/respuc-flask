from wtforms import PasswordField, StringField, SubmitField, ValidationError, BooleanField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, EqualTo, Optional
from flask_wtf import FlaskForm

from ..models import Usuario

class AddOrEditAlunoForm(FlaskForm):

	"""
	Form para adição/edição de um aluno
	"""

	#para pessoas e alunoaprendiz
	rg_numero = IntegerField('RG (somente números)', validators=[DataRequired()])
	rg_orgao_expedidor = StringField('Orgão expedidor (RG)', validators=[DataRequired()])
	rg_data_expedicao = DateField('Data de expedição', format='%Y-%m-%d', validators=[DataRequired()])

	#para pessoa
	nome = StringField('Nome', validators=[DataRequired()])
	sexo = IntegerField('Sexo',validators=[DataRequired()])
	data_nascimento = DateField('Data de nascimento', format='%Y-%m-%d', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	celular = IntegerField('Celular', validators=[DataRequired()])
	rua = StringField('Rua', validators=[DataRequired()])
	numero = IntegerField('Número', validators=[DataRequired()])
	complemento = StringField('Complemento', validators=[DataRequired()])
	bairro = StringField('Bairro', validators=[DataRequired()])
	cidade = StringField('Cidade', validators=[DataRequired()])
	uf = SelectField('UF', choices=[('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'), ('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'), ('MG','MG'), ('PA','PA'), ('PB','PB'), ('PR','PR'), ('PE','PE'), ('PI','PI'), ('RJ','RJ'), ('RN','RN'), ('RS','RS'), ('RO','RO'), ('RR','RR'), ('SC','SC'), ('SP','SP'), ('SE','SE'), ('TO', 'TO')], validators=[DataRequired()])
	cep = StringField('CEP', validators=[DataRequired()])

    # para alunos e aprendizes:
	nome_responsavel = StringField('Nome do responsável', validators=[DataRequired()])
	telefone_responsavel = StringField('Telefone do responsável', validators=[DataRequired()])
	profissao_responsavel = StringField('Profissão do responsável', validators=[DataRequired()])

	nome_instituicao = StringField('Nome da instituicao de origem', validators=[DataRequired()])
    
	serie = StringField('Série/Ano', validators=[DataRequired()])
	nivel_escolaridade = SelectField('Nível de escolaridade', choices=[('Fundamental','Fundamental'), ('Médio','Médio'), ('Técnico', 'Técnico')])
	status_escolaridade = SelectField('Status', choices=[('Cursando','Cursando'),('Concluído','Concluído')])
	turno = SelectField('Turno', choices=[('Manhã','Manhã'),('Noite','Noite')])

	submit = SubmitField('Confirmar')

class AddOrEditAprendizForm(FlaskForm):

	"""
	Form para adição/edição de um aprendiz
	"""
	#para realiza, pessoas e alunoaprendiz
	rg_numero = IntegerField('RG (somente números)', validators=[DataRequired()])
	rg_orgao_expedidor = StringField('Orgão expedidor (RG)', validators=[DataRequired()])
	rg_data_expedicao = DateField('Data de expedição', format='%Y-%m-%d', validators=[DataRequired()])

	#para pessoa
	nome = StringField('Nome', validators=[DataRequired()])
	sexo = IntegerField('Sexo',validators=[DataRequired()])
	data_nascimento = DateField('Data de nascimento', format='%Y-%m-%d', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	celular = IntegerField('Celular', validators=[DataRequired()])
	rua = StringField('Rua', validators=[DataRequired()])
	numero = IntegerField('Número', validators=[DataRequired()])
	complemento = StringField('Complemento', validators=[DataRequired()])
	bairro = StringField('Bairro', validators=[DataRequired()])
	cidade = StringField('Cidade', validators=[DataRequired()])
	uf = SelectField('UF', choices=[('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'), ('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'), ('MG','MG'), ('PA','PA'), ('PB','PB'), ('PR','PR'), ('PE','PE'), ('PI','PI'), ('RJ','RJ'), ('RN','RN'), ('RS','RS'), ('RO','RO'), ('RR','RR'), ('SC','SC'), ('SP','SP'), ('SE','SE'), ('TO', 'TO')], validators=[DataRequired()])
	cep = StringField('CEP', validators=[DataRequired()])

    #para alunoaprendiz:
	nome_responsavel = StringField('Nome do responsável', validators=[DataRequired()])
	telefone_responsavel = StringField('Telefone do responsável', validators=[DataRequired()])
	profissao_responsavel = StringField('Profissão do responsável', validators=[DataRequired()])

	nome_instituicao = StringField('Nome da instituicao de origem', validators=[DataRequired()])
    
	serie = StringField('Série/Ano', validators=[DataRequired()])
	nivel_escolaridade = SelectField('Nível de escolaridade', choices=[('Fundamental','Fundamental'), ('Médio','Médio'), ('Técnico', 'Técnico')])
	status_escolaridade = SelectField('Status', choices=[('Cursando','Cursando'),('Concluído','Concluído')])
	turno = SelectField('Turno', choices=[('Manhã','Manhã'),('Noite','Noite')])

	#para realiza
	trabalho_local = StringField('Local de trabalho', validators=[DataRequired()])
	trabalho_descricao = StringField('Descrição do trabalho', validators=[DataRequired()])
	trabalho_data_ini = DateField('Data de inicio do trabalho', format='%Y-%m-%d', validators=[DataRequired()])
	trabalho_data_fim = DateField('Data de inicio do trabalho', format='%Y-%m-%d', validators=[DataRequired()])

	submit = SubmitField('Confirmar')

class AddOrEditVoluntarioForm(FlaskForm):

	"""
	Form para adição/edição de um voluntario
	"""
	#para pessoa e voluntario
	rg_numero = IntegerField('RG (somente números)', validators=[DataRequired()])
	rg_orgao_expedidor = StringField('Orgão expedidor (RG)', validators=[DataRequired()])
	rg_data_expedicao = DateField('Data de expedição', format='%Y-%m-%d', validators=[DataRequired()])

	#para pessoa
	nome = StringField('Nome', validators=[DataRequired()])
	sexo = IntegerField('Sexo',validators=[DataRequired()])
	data_nascimento = DateField('Data de nascimento', format='%Y-%m-%d', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	celular = IntegerField('Celular', validators=[DataRequired()])
	rua = StringField('Rua', validators=[DataRequired()])
	numero = IntegerField('Número', validators=[DataRequired()])
	complemento = StringField('Complemento', validators=[DataRequired()])
	bairro = StringField('Bairro', validators=[DataRequired()])
	cidade = StringField('Cidade', validators=[DataRequired()])
	uf = SelectField('UF', choices=[('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'), ('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'), ('MG','MG'), ('PA','PA'), ('PB','PB'), ('PR','PR'), ('PE','PE'), ('PI','PI'), ('RJ','RJ'), ('RN','RN'), ('RS','RS'), ('RO','RO'), ('RR','RR'), ('SC','SC'), ('SP','SP'), ('SE','SE'), ('TO', 'TO')], validators=[DataRequired()])
	cep = StringField('CEP', validators=[DataRequired()])
	
	#para voluntario
	matricula = StringField('Matrícula', validators=[DataRequired()])
	curso = SelectField('Cruso', choices=[('Administração','Administração'), ('Arquitetura e Urbanismo','Arquitetura e Urbanismo')])

	submit = SubmitField('Confirmar')
