from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from . import eventos
from .forms import AddOrEditEventoForm
from .. import db
from ..models import Evento, t_participa

"""
EVENTOS
"""

@eventos.route('/', methods=['GET', 'POST'])
@login_required
def lista_eventos():
    
    """
    Lista todos os eventos
    """
    #check_admin()

    eventos = Evento.query.all()

    return render_template('eventos/eventos.html', eventos=eventos, title="Eventos")

@eventos.route('/add', methods=['GET','POST'])
@login_required
def add_evento():

	form = AddOrEditEventoForm()

	add_evento = True

	if form.validate_on_submit():

		evento = Evento(pk_nome=form.nome.data, pk_data=form.data.data, descricao=form.descricao.data)

		db.session.add(evento)
		db.session.commit()

		flash('Evento criado com sucesso')
		
		#redirect pra listagem de eventos
		return redirect(url_for('eventos.lista_eventos'))

	return render_template('eventos/add_or_edit_evento.html', action="Add", add_evento=add_evento, form=form, title="Add evento")

@eventos.route('/edit/<string:nome>/<data>', methods=['GET', 'POST'])
@login_required
def edit_evento(nome, data):

	"""
    Edita um evento do banco
    """
    #check_admin()
	
	evento = Evento.query.get_or_404([nome, data])

	form = AddOrEditEventoForm(obj=evento)

	add_evento = False

	if form.validate_on_submit():
		evento.pk_nome = form.nome.data
		evento.pk_data = form.data.data
		evento.descricao = form.descricao.data

		db.session.commit()
		flash('Evento editado com sucesso')

		return redirect(url_for('eventos.lista_eventos'))

	form.nome.data = evento.pk_nome
	form.data.data = evento.pk_data
	form.descricao.data = evento.descricao

	return render_template('eventos/add_or_edit_evento.html', action="Edit", add_evento=add_evento, form=form, evento=evento, title="Edit evento")

@eventos.route('/delete/<string:nome>/<data>')
@login_required
def delete_evento(nome, data):

    """
    Deleta um evento do banco
    """	
    #check_admin()

    evento = Evento.query.get_or_404([nome, data])

    db.session.delete(evento)
    db.session.commit()

    # redirect to the departments page
    return redirect(url_for('eventos.lista_eventos'))

    return render_template(title="Deletar evento")

@eventos.route('/<string:nome>/<data>', methods=['GET', 'POST'])
@login_required
def info_evento(nome, data):

    evento = Evento.query.get_or_404([nome, data])

    participantes = db.session.query(t_participa.c.pk_matricula_neam_pessoa).filter(t_participa.c.pk_nome_evento == nome, t_participa.c.pk_data_evento == data).all()

    return render_template('eventos/info_evento.html', evento=evento, participantes=participantes, title="Info")