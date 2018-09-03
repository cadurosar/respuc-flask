from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from . import pessoas
from .forms import AddOrEditPessoaForm
from .. import db
from ..models import Usuario, Pessoa, Realiza

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

    alunos = db.session.query(Pessoa).filter(Pessoa.tipo == 'aluno').all()
    
    aprendizes = db.session.query(Pessoa).filter(Pessoa.tipo == 'aprendiz').all()

    voluntarios = db.session.query(Pessoa).filter(Pessoa.tipo == 'voluntario').all()

    return render_template('pessoas/pessoas.html',
                           alunos=alunos, aprendizes=aprendizes, voluntarios=voluntarios, title="Pessoas")


"""
ALUNOS:
"""
@pessoas.route('/<string:pk_matricula_neam>', methods=['GET', 'POST'])
@login_required
def info_pessoa(pk_matricula_neam):

    pessoa = db.session.query(Pessoa).get_or_404(pk_matricula_neam)

    return render_template('pessoas/info_pessoa.html', pessoa=pessoa, title="Info")


@pessoas.route('/add/<string:tipo>', methods=['GET', 'POST'])
@login_required
def add_pessoa(tipo):

    """
    Adiciona um aluno no banco
    """
    #check_admin()

    add_aluno = True

    form = AddOrEditPessoaForm()

    if form.validate_on_submit():
        pessoa = Pessoa(nome=form.nome.data, email=form.email.data, celular=form.celular.data, foto=form.foto.data, sexo=form.sexo.data, data_nascimento=form.data_nascimento.data, identificador_tipo=form.identificador_tipo.data, identificador_numero=form.identificador_numero.data, identificador_complemento=form.identificador_complemento.data, endereco_numero=form.endereco_numero.data, endereco_rua=form.endereco_rua.data, endereco_complemento=form.endereco_complemento.data, endereco_bairro=form.endereco_bairro.data, endereco_cidade=form.endereco_cidade.data, endereco_uf=form.endereco_uf.data, endereco_cep=form.endereco_cep.data, tipo=tipo, nome_responsavel= '{"'+form.nome_responsavel.data+'"}', telefone_responsavel='{"'+form.telefone_responsavel.data+'"}', profissao_responsavel='{"'+form.profissao_responsavel.data+'"}', curso_puc=form.curso_puc.data, matricula_puc=form.matricula_puc.data, dificuldade='{"'+form.dificuldade.data+'"}', serie=form.serie.data, escolaridade_nivel=form.escolaridade_nivel.data, escolaridade_turno=form.escolaridade_turno.data, nome_instituicao=form.nome_instituicao.data)

        db.session.add(pessoa)
        db.session.commit()

        flash( pessoa.tipo+' criado com sucesso')
        # redirect to usuarios page
        return redirect(url_for('pessoas.lista_pessoas'))

    # load usuario template
    return render_template('pessoas/add_or_edit_pessoa.html', action="Add",
                           add_aluno=add_aluno, tipo=tipo, form=form,
                           title="Add Aluno")


@pessoas.route('/edit/<string:pk_matricula_neam>', methods=['GET', 'POST'])
@login_required
def edit_pessoa(pk_matricula_neam):
    """
    Edita um aluno do banco
    """
    #check_admin()

    add_aluno = False

    pessoa = db.session.query(Pessoa).get_or_404(pk_matricula_neam)

    form = AddOrEditPessoaForm(obj=pessoa)


    if form.validate_on_submit():

        pessoa.nome = form.nome.data
        pessoa.email = form.email.data
        pessoa.celular = form.celular.data
        pessoa.foto = form.foto.data
        pessoa.sexo = form.sexo.data
        pessoa.data_nascimento = form.data_nascimento.data
        pessoa.identificador_tipo = form.identificador_tipo.data
        pessoa.identificador_numero = form.identificador_numero.data
        pessoa.identificador_complemento = form.identificador_complemento.data
        pessoa.endereco_numero = form.endereco_numero.data
        pessoa.endereco_rua = form.endereco_rua.data
        pessoa.endereco_complemento = form.endereco_complemento.data
        pessoa.endereco_bairro = form.endereco_bairro.data
        pessoa.endereco_uf = form.endereco_uf.data
        pessoa.endereco_cep = form.endereco_cep.data
        pessoa.nome_responsavel = '{"'+ form.nome_responsavel.data+'"}'
        pessoa.telefone_responsavel = '{"' + form.telefone_responsavel.data +'"}'
        pessoa.profissao_responsavel =  '{"' + form.profissao_responsavel.data +'"}'
        pessoa.curso_puc = form.curso_puc.data
        pessoa.matricula_puc = form.matricula_puc.data
        pessoa.dificuldade =  '{"' + form.dificuldade.data +'"}'
        pessoa.serie = form.serie.data
        pessoa.escolaridade_nivel = form.escolaridade_nivel.data
        pessoa.escolaridade_turno = form.escolaridade_turno.data
        pessoa.nome_instituicao = form.nome_instituicao.data
        
        db.session.commit()
        flash('%s editado com sucesso.' % pessoa.tipo)
                
        # redirect to the alunos page
        return redirect(url_for('pessoas.lista_pessoas'))

    #inicializa os campos do form com os dados do banco
    #da pra fazer isso de um jeito mais esperto, com loop; refazer

    form.nome.data = pessoa.nome
    form.email.data = pessoa.email
    form.celular.data = pessoa.celular
    form.foto.data = pessoa.foto
    form.sexo.data = pessoa.sexo
    form.data_nascimento.data = pessoa.data_nascimento
    form.identificador_tipo.data = pessoa.identificador_tipo
    form.identificador_numero.data = pessoa.identificador_numero
    form.identificador_complemento.data = pessoa.identificador_complemento
    form.endereco_numero.data = pessoa.endereco_numero
    form.endereco_rua.data = pessoa.endereco_rua
    form.endereco_complemento.data = pessoa.endereco_complemento
    form.endereco_bairro.data = pessoa.endereco_bairro
    form.endereco_cidade.data = pessoa.endereco_cidade
    form.endereco_uf.data = pessoa.endereco_uf
    form.endereco_cep.data = pessoa.endereco_cep
    form.nome_responsavel.data = pessoa.nome_responsavel[0]
    form.telefone_responsavel.data = pessoa.telefone_responsavel[0]
    form.profissao_responsavel.data = pessoa.profissao_responsavel[0]
    form.curso_puc.data = pessoa.curso_puc
    form.matricula_puc.data = pessoa.matricula_puc
    form.dificuldade.data = pessoa.dificuldade[0]
    form.serie.data = pessoa.serie
    form.escolaridade_nivel.data = pessoa.escolaridade_nivel
    form.escolaridade_turno.data = pessoa.escolaridade_turno
    form.nome_instituicao.data = pessoa.nome_instituicao

    return render_template('pessoas/add_or_edit_pessoa.html', action="Edit",
                           add_aluno=add_aluno, form=form,
                           pessoa=pessoa,tipo=pessoa.tipo, title="Edit Aluno")


@pessoas.route('/delete/<string:pk_matricula_neam>', methods=['GET', 'POST'])
@login_required
def delete_pessoa(pk_matricula_neam):

    """
    Deleta um aluno do banco
    """
    #check_admin()

    pessoa = db.session.query(Pessoa).get_or_404(pk_matricula_neam)

    tipo = pessoa.tipo

    db.session.delete(pessoa)
    db.session.commit()
    flash('%s foi deletado com sucesso' % tipo)

    # redirect to the departments page
    return redirect(url_for('pessoas.lista_pessoas'))

    return render_template(title="Deletar aluno")


