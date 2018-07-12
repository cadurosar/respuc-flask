from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from . import pessoas
from .forms import AddAlunoForm
from .. import db
from ..models import Usuario

@pessoas.route('/', methods=['GET', 'POST'])
@login_required
def list_pessoas():
    """
    List all usuarios
    """
    #check_admin()

    alunos = Usuario.query.filter_by(role="aluno").all()

    aprendizes = Usuario.query.filter_by(role="aprendiz").all()

    voluntarios = Usuario.query.filter_by(role="voluntario").all()

    return render_template('pessoas/pessoas.html',
                           alunos=alunos, aprendizes=aprendizes, voluntarios=voluntarios, title="Pessoas")


@pessoas.route('/add', methods=['GET', 'POST'])
@login_required
def add_aluno():

    """
    Add a usuario to the database
    """
    #check_admin()

    add_aluno = True

    form = AddAlunoForm()
    if form.validate_on_submit():
        aluno = Aluno(nome=form.aluno.nome, cpf=form.aluno.cpf, rg=form.aluno.rg, naturalidade=form.aluno.naturalidade, email=form.email.data, data_nascimento=form.aluno.data_nascimento, telefone=form.aluno.telefone, celular=form.aluno.celular, rua=form.aluno.rua, numero=form.aluno.numero, complemento=form.aluno.complemento, bairro=form.aluno.bairro, cidade=form.aluno.cidade, uf=form.aluno.uf, cep=form.aluno.cep, nome_responsavel=form.aluno.nome_reponsavel, cpf_responsavel=form.aluno.cpf_responsavel, telefone_responsavel=form.aluno.telefone_responsavel, profissao_responsavel=form.aluno.profissao_responsavel)

        db.session.add(aluno)
        db.session.commit()
        flash('Aluno criado com sucesso')
        # redirect to usuarios page
        return redirect(url_for('pessoas.list_pessoas'))

    # load usuario template
    return render_template('pessoas/add_aluno.html', action="Add",
                           add_aluno=add_aluno, form=form,
                           title="Add Aluno")


@pessoas.route('/usuarios/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_usuario(id):
    """
    Edit a usuario
    """
    #check_admin()

    add_usuario = False

    usuario = Usuario.query.get_or_404(id)
    form = EditUsuarioForm(obj=usuario)
    if form.validate_on_submit():
        usuario.nome = form.nome.data
        usuario.email = form.email.data
        usuario.e_admin = form.e_admin.data

        if form.senha.data:
            usuario.senha = form.senha.data
        
        db.session.commit()
        flash('Usuário editado com sucesso.')

        # redirect to the usuarios page
        return redirect(url_for('admin.list_usuarios'))

    form.email.data = usuario.email
    form.nome.data = usuario.nome
    form.e_admin.data = usuario.e_admin
    return render_template('admin/usuarios/usuario.html', action="Edit",
                           add_usuario=add_usuario, form=form,
                           usuario=usuario, title="Edit Usuario")
