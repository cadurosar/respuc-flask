from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from . import pessoas
from .forms import AddOrEditAlunoForm, AddOrEditAprendizForm, AddOrEditVoluntarioForm
from .. import db
from ..models import Usuario, Aluno, Voluntario, AprendizAluno, Pessoa, Realiza

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

    #nao é um full outer join que pega todos os atributos de todas as tabelas, fica faltando dificuldade
    alunos= db.session.query(Pessoa).join(Aluno).all()
    
    aprendizes = db.session.query(Pessoa).join(AprendizAluno).all()

    voluntarios = db.session.query(Voluntario).all()

    return render_template('pessoas/pessoas.html',
                           alunos=alunos, aprendizes=aprendizes, voluntarios=voluntarios, title="Pessoas")


"""
ALUNOS:
"""
@pessoas.route('/aluno/<string:rg_numero>/<rg_data_expedicao>/<string:rg_orgao_expedidor>', methods=['GET', 'POST'])
@login_required
def info_aluno(rg_numero, rg_data_expedicao, rg_orgao_expedidor):

    pessoa = db.session.query(Pessoa).get_or_404([rg_numero, rg_orgao_expedidor, rg_data_expedicao])

    aluno = db.session.query(Aluno).get_or_404([rg_numero, rg_orgao_expedidor, rg_data_expedicao])

    return render_template('pessoas/info_pessoa.html', pessoa=pessoa, aluno=aluno, title="Info")


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
        pessoa = Pessoa(rg_numero=form.rg_numero.data, rg_orgao_expedidor=form.rg_orgao_expedidor.data, rg_data_expedicao=form.rg_data_expedicao.data, nome=form.nome.data, sexo=form.sexo.data, email=form.email.data, data_nascimento=form.data_nascimento.data, celular=form.celular.data, rua=form.rua.data, numero=form.numero.data, complemento=form.complemento.data, bairro=form.bairro.data, cidade=form.cidade.data, uf=form.uf.data, cep=form.cep.data)

        aprendizaluno = AprendizAluno(rg_numero_pessoa=form.rg_numero.data, rg_orgao_expedidor_pessoa=form.rg_orgao_expedidor.data, rg_data_expedicao_pessoa=form.rg_data_expedicao.data, nome_responsavel=form.nome_responsavel.data, telefone_responsavel=form.telefone_responsavel.data, profissao_responsavel=form.profissao_responsavel.data, nome_instituicao=form.nome_instituicao.data, serie=form.serie.data, nivel_escolaridade=form.nivel_escolaridade.data, status_escolaridade=form.status_escolaridade.data, turno=form.turno.data)

        aluno = Aluno(rg_numero_pessoa=form.rg_numero.data, rg_orgao_expedidor_pessoa=form.rg_orgao_expedidor.data, rg_data_expedicao_pessoa=form.rg_data_expedicao.data)

        #commita pessoa primeiro para nao dar erro de violacao de fk no commit de aluno
        db.session.add(pessoa)
        db.session.commit()

        db.session.add(aprendizaluno)
        db.session.add(aluno)
        db.session.commit()
        flash('Aluno criado com sucesso')
        # redirect to usuarios page
        return redirect(url_for('pessoas.lista_pessoas'))

    # load usuario template
    return render_template('pessoas/add_or_edit_aluno.html', action="Add",
                           add_aluno=add_aluno, form=form,
                           title="Add Aluno")


@pessoas.route('/edit/aluno/<string:rg_numero>/<rg_data_expedicao>/<string:rg_orgao_expedidor>', methods=['GET', 'POST'])
@login_required
def edit_aluno(rg_numero, rg_data_expedicao, rg_orgao_expedidor):
    """
    Edita um aluno do banco
    """
    #check_admin()

    add_aluno = False

    pessoa = db.session.query(Pessoa).get_or_404([rg_numero, rg_orgao_expedidor, rg_data_expedicao])

    form = AddOrEditAlunoForm(obj=pessoa)


    if form.validate_on_submit():

        pessoa.nome = form.nome.data
        pessoa.rg_numero = form.rg_numero.data
        pessoa.rg_orgao_expedidor = form.rg_orgao_expedidor.data
        pessoa.rg_data_expedicao = form.rg_data_expedicao.data
        pessoa.email = form.email.data
        pessoa.data_nascimento = form.data_nascimento.data
        pessoa.celular = form.celular.data
        pessoa.rua = form.rua.data
        pessoa.numero = form.numero.data
        pessoa.complemento = form.complemento.data
        pessoa.bairro = form.bairro.data
        pessoa.cidade = form.cidade.data
        pessoa.uf = form.uf.data
        pessoa.cep = form.cep.data
        
        # pessoa.nome_responsavel = form.nome_responsavel.data
        # pessoa.cpf_responsavel = form.cpf_responsavel.data
        # pessoa.telefone_responsavel = form.telefone_responsavel.data
        # pessoa.profissao_responsavel = form.profissao_responsavel.data
        
        db.session.commit()
        flash('Aluno editado com sucesso.')
                
        # redirect to the alunos page
        return redirect(url_for('pessoas.lista_pessoas'))

    #inicializa os campos do form com os dados do banco
    #da pra fazer isso de um jeito mais esperto, com loop; refazer

    form.nome.data = pessoa.nome
    form.rg_numero.data = pessoa.rg_numero
    form.rg_orgao_expedidor.data = pessoa.rg_orgao_expedidor
    form.rg_data_expedicao.data = pessoa.rg_data_expedicao
    form.email.data = pessoa.email
    form.data_nascimento.data = pessoa.data_nascimento
    form.celular.data = pessoa.celular
    form.rua.data = pessoa.rua
    form.numero.data = pessoa.numero
    form.complemento.data = pessoa.complemento
    form.bairro.data = pessoa.bairro
    form.cidade.data = pessoa.cidade
    form.uf.data = pessoa.uf
    form.cep.data = pessoa.cep

    # form.nome_responsavel.data = pessoa.nome_responsavel
    # form.cpf_responsavel.data = pessoa.cpf_responsavel
    # form.telefone_responsavel.data = pessoa.telefone_responsavel
    # form.profissao_responsavel.data = pessoa.profissao_responsavel

    return render_template('pessoas/add_or_edit_aluno.html', action="Edit",
                           add_aluno=add_aluno, form=form,
                           aluno=pessoa, title="Edit Aluno")


@pessoas.route('/delete/aluno/<string:rg_numero>/<rg_data_expedicao>/<string:rg_orgao_expedidor>', methods=['GET', 'POST'])
@login_required
def delete_aluno(rg_numero, rg_data_expedicao, rg_orgao_expedidor):

    """
    Deleta um aluno do banco
    """
    #check_admin()

    pessoa = db.session.query(Pessoa).get_or_404([rg_numero, rg_orgao_expedidor, rg_data_expedicao])

    aluno = db.session.query(Aluno).get_or_404([rg_numero, rg_orgao_expedidor, rg_data_expedicao])

    db.session.delete(aluno)
    db.session.delete(pessoa)
    db.session.commit()
    flash('Aluno foi deletado com sucesso')

    # redirect to the departments page
    return redirect(url_for('pessoas.lista_pessoas'))

    return render_template(title="Deletar aluno")


"""
APRENDIZES:
"""

@pessoas.route('/aprendiz/<string:cpf>', methods=['GET', 'POST'])
@login_required
def info_aprendiz(cpf):

    aprendiz = AprendizAluno.query.get_or_404(cpf)

    return render_template('pessoas/info_pessoa.html', pessoa=aprendiz, title="Info")


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
        pessoa = Pessoa(rg_numero=form.rg_numero.data, rg_orgao_expedidor=form.rg_orgao_expedidor.data, rg_data_expedicao=form.rg_data_expedicao.data, nome=form.nome.data, sexo=form.sexo.data, email=form.email.data, data_nascimento=form.data_nascimento.data, celular=form.celular.data, rua=form.rua.data, numero=form.numero.data, complemento=form.complemento.data, bairro=form.bairro.data, cidade=form.cidade.data, uf=form.uf.data, cep=form.cep.data)

        aprendizaluno = AprendizAluno(rg_numero_pessoa=form.rg_numero.data, rg_orgao_expedidor_pessoa=form.rg_orgao_expedidor.data, rg_data_expedicao_pessoa=form.rg_data_expedicao.data, nome_responsavel=form.nome_responsavel.data, telefone_responsavel=form.telefone_responsavel.data, profissao_responsavel=form.profissao_responsavel.data, nome_instituicao=form.nome_instituicao.data, serie=form.serie.data, nivel_escolaridade=form.nivel_escolaridade.data, status_escolaridade=form.status_escolaridade.data, turno=form.turno.data)

        realiza = Realiza(rg_numero_pessoa=form.rg_numero.data, rg_orgao_expedidor_pessoa=form.rg_orgao_expedidor.data, rg_data_expedicao_pessoa=form.rg_data_expedicao.data, local=form.trabalho_local.data, descricao=form.trabalho_descricao.data, data_ini=form.trabalho_data_ini.data, data_fim=form.trabalho_data_fim.data)

        #commita pessoa primeiro pra evitar erro de fk
        db.session.add(pessoa)
        db.session.commit()

        db.session.add(aprendizaluno)
        db.session.add(realiza)
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

    aprendiz = AprendizAluno.query.get_or_404(cpf)

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

    aprendiz = AprendizAluno.query.get_or_404(cpf)
    db.session.delete(aprendiz)
    db.session.commit()
    flash('Aprendiz foi deletado com sucesso')

    # redirect to the departments page
    return redirect(url_for('pessoas.lista_pessoas'))

    return render_template(title="Deletar aprendiz")


"""
VOLUNTARIOS:
"""

@pessoas.route('/voluntario/<string:cpf>', methods=['GET', 'POST'])
@login_required
def info_voluntario(cpf):

    voluntario = Voluntario.query.get_or_404(cpf)

    return render_template('pessoas/info_pessoa.html', pessoa=voluntario, title="Info")


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
        pessoa = Pessoa(rg_numero=form.rg_numero.data, rg_orgao_expedidor=form.rg_orgao_expedidor.data, rg_data_expedicao=form.rg_data_expedicao.data, nome=form.nome.data, sexo=form.sexo.data, email=form.email.data, data_nascimento=form.data_nascimento.data, celular=form.celular.data, rua=form.rua.data, numero=form.numero.data, complemento=form.complemento.data, bairro=form.bairro.data, cidade=form.cidade.data, uf=form.uf.data, cep=form.cep.data)

        voluntario = Voluntario(rg_numero_pessoa=form.rg_numero.data, rg_orgao_expedidor_pessoa=form.rg_orgao_expedidor.data, rg_data_expedicao_pessoa=form.rg_data_expedicao.data, matricula_puc=form.matricula.data, curso_puc=form.curso.data)


        db.session.add(pessoa)
        db.session.commit()
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
    