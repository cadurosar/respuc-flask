from wtforms import StringField, SubmitField, ValidationError, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class AddOrEditEventoForm(FlaskForm):

	"""
	Form para adição/edição de um aluno
	"""

	nome = StringField('Nome do evento', validators=[DataRequired()])
	data = DateField('Data do evento', format='%Y-%m-%d', validators=[DataRequired()])
	descricao = TextAreaField('Descrição do evento', validators=[DataRequired()])

	submit = SubmitField('Confirmar')