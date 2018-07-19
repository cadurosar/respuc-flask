from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from . import pessoas
from .forms import AddOrEditAlunoForm, AddOrEditAprendizForm, AddOrEditVoluntarioForm
from .. import db
from ..models import Usuario, Aluno, Voluntario, Aprendiz

"""
TODOS:
"""

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











"""
ALUNOS:
"""

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
        aluno.cpf_responsavel = form.cpf_responsavel.data
        aluno.telefone_responsavel = form.telefone_responsavel.data
        aluno.profissao_responsavel = form.profissao_responsavel.data
        
        db.session.commit()
        flash('Aluno editado com sucesso.')
                
        # redirect to the alunos page
        return redirect(url_for('pessoas.lista_pessoas'))

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
    form.cpf_responsavel.data = aluno.cpf_responsavel
    form.telefone_responsavel.data = aluno.telefone_responsavel
    form.profissao_responsavel.data = aluno.profissao_responsavel

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











"""
APRENDIZES:
"""

@pessoas.route('/add/aprendiz', methods=['GET', 'POST'])
@login_required
def add_aprendiz():

    """
    Adiciona um aprendiz no banco
    """
    #check_admin()

    add_aprendiz = True

    form = AddOrEditAprendizForm()
    if form.validate_on_submit():
        aprendiz = Aprendiz(nome=form.nome.data, cpf=form.cpf.data, rg=form.rg.data, naturalidade=form.naturalidade.data, email=form.email.data, data_nascimento=form.data_nascimento.data, telefone=form.telefone.data, celular=form.celular.data, rua=form.rua.data, numero=form.numero.data, complemento=form.complemento.data, bairro=form.bairro.data, cidade=form.cidade.data, uf=form.uf.data, cep=form.cep.data, trabalho=form.trabalho.data, nome_responsavel=form.nome_responsavel.data, cpf_responsavel=form.cpf_responsavel.data, telefone_responsavel=form.telefone_responsavel.data, profissao_responsavel=form.profissao_responsavel.data)

        db.session.add(aprendiz)
        db.session.commit()
        flash('Aprendiz criado com sucesso')
        # redirect to usuarios page
        return redirect(url_for('pessoas.lista_pessoas'))

    # load usuario template
    return render_template('pessoas/add_or_edit_aprendiz.html', action="Add",
                           add_aprendiz=add_aprendiz, form=form,
                           title="Add Aprendiz")


@pessoas.route('/edit/aprendiz/<string:cpf>', methods=['GET', 'POST'])
@login_required
def edit_aprendiz(cpf):
    """
    Edita um aprendiz do banco
    """
    #check_admin()

    add_aprendiz = False

    aprendiz = Aprendiz.query.get_or_404(cpf)

    form = AddOrEditAprendizForm(obj=aprendiz)

    #inicializa os campos do form com os dados do banco
    #da pra fazer isso de um jeito mais esperto, com loop; refazer

    if form.validate_on_submit():

        aprendiz.nome = form.nome.data
        aprendiz.cpf = form.cpf.data
        aprendiz.rg = form.rg.data
        aprendiz.naturalidade = form.naturalidade.data
        aprendiz.email = form.email.data
        aprendiz.data_nascimento = form.data_nascimento.data
        aprendiz.telefone = form.telefone.data
        aprendiz.celular = form.celular.data
        aprendiz.rua = form.rua.data
        aprendiz.numero = form.numero.data
        aprendiz.complemento = form.complemento.data
        aprendiz.bairro = form.bairro.data
        aprendiz.cidade = form.cidade.data
        aprendiz.uf = form.uf.data
        aprendiz.cep = form.cep.data
        aprendiz.trabalho = form.trabalho.data
        aprendiz.nome_responsavel = form.nome_responsavel.data
        aprendiz.cpf_responsavel = form.cpf_responsavel.data
        aprendiz.telefone_responsavel = form.telefone_responsavel.data
        aprendiz.profissao_responsavel = form.profissao_responsavel.data
        
        db.session.commit()
        flash('Aprendiz editado com sucesso.')

        # redirect to the aprendizes page
        return redirect(url_for('pessoas.lista_pessoas'))

    form.nome.data = aprendiz.nome
    form.cpf.data = aprendiz.cpf
    form.rg.data = aprendiz.rg
    form.naturalidade.data = aprendiz.naturalidade
    form.email.data = aprendiz.email
    form.data_nascimento.data = aprendiz.data_nascimento
    form.telefone.data = aprendiz.telefone
    form.celular.data = aprendiz.celular
    form.rua.data = aprendiz.rua
    form.numero.data = aprendiz.numero
    form.complemento.data = aprendiz.complemento
    form.bairro.data = aprendiz.bairro
    form.cidade.data = aprendiz.cidade
    form.uf.data = aprendiz.uf
    form.cep.data = aprendiz.cep
    form.trabalho.data = aprendiz.trabalho
    form.nome_responsavel.data = aprendiz.nome_responsavel
    form.cpf_responsavel.data = aprendiz.cpf_responsavel
    form.telefone_responsavel.data = aprendiz.telefone_responsavel
    form.profissao_responsavel.data = aprendiz.profissao_responsavel

    return render_template('pessoas/add_or_edit_aprendiz.html', action="Edit",
                           add_aprendiz=add_aprendiz, form=form,
                           aprendiz=aprendiz, title="Edit Aprendiz")


@pessoas.route('/delete/aprendiz/<string:cpf>', methods=['GET', 'POST'])
@login_required
def delete_aprendiz(cpf):

    """
    Deleta um aprendiz do banco
    """
    #check_admin()

    aprendiz = Aprendiz.query.get_or_404(cpf)
    db.session.delete(aprendiz)
    db.session.commit()
    flash('Aprendiz foi deletado com sucesso')

    # redirect to the departments page
    return redirect(url_for('pessoas.lista_pessoas'))

    return render_template(title="Deletar aprendiz")











"""
VOLUNTARIOS:
"""

@pessoas.route('/add/voluntario', methods=['GET', 'POST'])
@login_required
def add_voluntario():

    """
    Adiciona um voluntario no banco
    """
    #check_admin()

    add_voluntario = True

    form = AddOrEditVoluntarioForm()
    if form.validate_on_submit():
        voluntario = Voluntario(nome=form.nome.data, cpf=form.cpf.data, rg=form.rg.data, naturalidade=form.naturalidade.data, email=form.email.data, data_nascimento=form.data_nascimento.data, telefone=form.telefone.data, celular=form.celular.data, rua=form.rua.data, numero=form.numero.data, complemento=form.complemento.data, bairro=form.bairro.data, cidade=form.cidade.data, uf=form.uf.data, cep=form.cep.data, matricula=form.matricula.data)

        db.session.add(voluntario)
        db.session.commit()
        flash('Voluntario criado com sucesso')
        # redirect to usuarios page
        return redirect(url_for('pessoas.lista_pessoas'))

    # load usuario template
    return render_template('pessoas/add_or_edit_voluntario.html', action="Add",
                           add_voluntario=add_voluntario, form=form,
                           title="Add Voluntario")


@pessoas.route('/edit/voluntario/<string:cpf>', methods=['GET', 'POST'])
@login_required
def edit_voluntario(cpf):
    """
    Edita um voluntario do banco
    """
    #check_admin()

    add_voluntario = False

    voluntario = Voluntario.query.get_or_404(cpf)

    form = AddOrEditVoluntarioForm(obj=voluntario)

    #inicializa os campos do form com os dados do banco
    #da pra fazer isso de um jeito mais esperto, com loop; refazer

    if form.validate_on_submit():

        voluntario.nome = form.nome.data
        voluntario.cpf = form.cpf.data
        voluntario.rg = form.rg.data
        voluntario.naturalidade = form.naturalidade.data
        voluntario.email = form.email.data
        voluntario.data_nascimento = form.data_nascimento.data
        voluntario.telefone = form.telefone.data
        voluntario.celular = form.celular.data
        voluntario.rua = form.rua.data
        voluntario.numero = form.numero.data
        voluntario.complemento = form.complemento.data
        voluntario.bairro = form.bairro.data
        voluntario.cidade = form.cidade.data
        voluntario.uf = form.uf.data
        voluntario.cep = form.cep.data
        voluntario.matricula = form.matricula.data
        
        db.session.commit()
        flash('Voluntario editado com sucesso.')

        # redirect to the voluntarios page
        return redirect(url_for('pessoas.lista_pessoas'))

    form.nome.data = voluntario.nome
    form.cpf.data = voluntario.cpf
    form.rg.data = voluntario.rg
    form.naturalidade.data = voluntario.naturalidade
    form.email.data = voluntario.email
    form.data_nascimento.data = voluntario.data_nascimento
    form.telefone.data = voluntario.telefone
    form.celular.data = voluntario.celular
    form.rua.data = voluntario.rua
    form.numero.data = voluntario.numero
    form.complemento.data = voluntario.complemento
    form.bairro.data = voluntario.bairro
    form.cidade.data = voluntario.cidade
    form.uf.data = voluntario.uf
    form.cep.data = voluntario.cep
    form.matricula.data = voluntario.matricula

    return render_template('pessoas/add_or_edit_voluntario.html', action="Edit",
                           add_voluntario=add_voluntario, form=form,
                           voluntario=voluntario, title="Edit Voluntario")


@pessoas.route('/delete/voluntario/<string:cpf>', methods=['GET', 'POST'])
@login_required
def delete_voluntario(cpf):

    """
    Deleta um voluntario do banco
    """
    #check_admin()

    voluntario = Voluntario.query.get_or_404(cpf)
    db.session.delete(voluntario)
    db.session.commit()
    flash('Voluntario foi deletado com sucesso')

    # redirect to the departments page
    return redirect(url_for('pessoas.lista_pessoas'))

    return render_template(title="Deletar voluntario")
