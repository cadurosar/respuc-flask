from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from . import pessoas
from .forms import AddOrEditAlunoForm
from .. import db
from ..models import Usuario, Aluno, Voluntario, Aprendiz

@pessoas.route('/', methods=['GET', 'POST'])
@login_required
def lista_pessoas():
    """
    Lista todas as pessoas (alunos, aprendizes e voluntarios)
    """
    #check_admin()

    alunos = Aluno.query.all()

    aprendizes = Aprendiz.query.all()

    voluntarios = Voluntario.query.all()

    return render_template('pessoas/pessoas.html',
                           alunos=alunos, aprendizes=aprendizes, voluntarios=voluntarios, title="Pessoas")


@pessoas.route('/add/aluno', methods=['GET', 'POST'])
@login_required
def add_aluno():

    """
    Adiciona um aluno no banco
    """
    #check_admin()

    add_aluno = True

    form = AddOrEditAlunoForm()
    if form.validate_on_submit():
        aluno = Aluno(nome=form.nome.data, cpf=form.cpf.data, rg=form.rg.data, naturalidade=form.naturalidade.data, email=form.email.data, data_nascimento=form.data_nascimento.data, telefone=form.telefone.data, celular=form.celular.data, rua=form.rua.data, numero=form.numero.data, complemento=form.complemento.data, bairro=form.bairro.data, cidade=form.cidade.data, uf=form.uf.data, cep=form.cep.data, nome_responsavel=form.nome_responsavel.data, cpf_responsavel=form.cpf_responsavel.data, telefone_responsavel=form.telefone_responsavel.data, profissao_responsavel=form.profissao_responsavel.data)

        db.session.add(aluno)
        db.session.commit()
        flash('Aluno criado com sucesso')
        # redirect to usuarios page
        return redirect(url_for('pessoas.lista_pessoas'))

    # load usuario template
    return render_template('pessoas/add_or_edit_aluno.html', action="Add",
                           add_aluno=add_aluno, form=form,
                           title="Add Aluno")


@pessoas.route('/edit/aluno/<string:cpf>', methods=['GET', 'POST'])
@login_required
def edit_aluno(cpf):
    """
    Edita um aluno do banco
    """
    #check_admin()

    add_aluno = False

    aluno = Aluno.query.get_or_404(cpf)

    form = AddOrEditAlunoForm(obj=aluno)

    #inicializa os campos do form com os dados do banco
    #da pra fazer isso de um jeito mais esperto, com loop; refazer

    form.nome.data = aluno.nome
    form.cpf.data = aluno.cpf
    form.rg.data = aluno.rg
    form.naturalidade.data = aluno.naturalidade
    form.email.data = aluno.email
    form.data_nascimento.data = aluno.data_nascimento
    form.telefone.data = aluno.telefone
    form.celular.data = aluno.celular
    form.rua.data = aluno.rua
    form.numero.data = aluno.numero
    form.complemento.data = aluno.complemento
    form.bairro.data = aluno.bairro
    form.cidade.data = aluno.cidade
    form.uf.data = aluno.uf
    form.cep.data = aluno.cep
    form.nome_responsavel.data = aluno.nome_responsavel
    form.cpf_responsavel = aluno.cpf_responsavel
    form.telefone_responsavel = aluno.telefone_responsavel
    form.profissao_responsavel = aluno.profissao_responsavel

    if form.validate_on_submit():

        aluno.nome = form.nome.data
        aluno.cpf = form.cpf.data
        aluno.rg = form.rg.data
        aluno.naturalidade = form.naturalidade.data
        aluno.email = form.email.data
        aluno.data_nascimento = form.data_nascimento.data
        aluno.telefone = form.telefone.data
        aluno.celular = form.celular.data
        aluno.rua = form.rua.data
        aluno.numero = form.numero.data
        aluno.complemento = form.complemento.data
        aluno.bairro = form.bairro.data
        aluno.cidade = form.cidade.data
        aluno.uf = form.uf.data
        aluno.cep = form.cep.data
        aluno.nome_responsavel = form.nome_responsavel.data
        aluno.cpf_responsavel = form.cpf_responsavel
        aluno.telefone_responsavel = form.telefone_responsavel
        aluno.profissao_responsavel = form.profissao_responsavel
        
        db.session.commit()
        flash('Aluno editado com sucesso.')

        # redirect to the alunos page
        return redirect(url_for('pessoas.lista_pessoas'))

    return render_template('pessoas/add_or_edit_aluno.html', action="Edit",
                           add_aluno=add_aluno, form=form,
                           aluno=aluno, title="Edit Aluno")


@pessoas.route('/delete/aluno/<string:cpf>', methods=['GET', 'POST'])
@login_required
def delete_aluno(cpf):

    """
    Deleta um aluno do banco
    """
    #check_admin()

    aluno = Aluno.query.get_or_404(cpf)
    db.session.delete(aluno)
    db.session.commit()
    flash('Aluno foi deletado com sucesso')

    # redirect to the departments page
    return redirect(url_for('pessoas.lista_pessoas'))

    return render_template(title="Deletar aluno")


