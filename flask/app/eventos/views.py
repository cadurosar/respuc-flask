from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from . import eventos
from .forms import AddOrEditEventoForm
from .. import db
from ..models import Evento

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

		evento = Evento(nome=form.nome.data, dataevento=form.dataevento.data, descricao=form.descricao.data)

		db.session.add(evento)
		db.session.commit()

		flash('Evento criado com sucesso')
		
		#redirect pra listagem de eventos
		return redirect(url_for('eventos.lista_eventos'))

	return render_template('eventos/add_or_edit_evento.html', action="Add", add_evento=add_evento, form=form, title="Add evento")

@eventos.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_evento(id):

	"""
    Edita um evento do banco
    """
    #check_admin()
	
	evento = Evento.query.get_or_404(id)

	form = AddOrEditEventoForm(obj=evento)

	add_evento = False

	if form.validate_on_submit():
		evento.nome = form.nome.data
		evento.dataevento = form.dataevento.data
		evento.descricao = form.descricao.data

		db.session.commit()
		flash('Evento editado com sucesso')

		return redirect(url_for('eventos.lista_eventos'))

	form.nome.data = evento.nome
	form.dataevento.data = evento.dataevento
	form.descricao.data = evento.descricao

	return render_template('eventos/add_or_edit_evento.html', action="Edit", add_evento=add_evento, form=form, evento=evento, title="Edit evento")

@eventos.route('/delete/<int:id>')
@login_required
def delete_evento(id):

    """
    Deleta um evento do banco
    """	
    #check_admin()

    evento = Evento.query.get_or_404(id)

    db.session.delete(evento)
    db.session.commit()

    # redirect to the departments page
    return redirect(url_for('eventos.lista_eventos'))

    return render_template(title="Deletar evento")