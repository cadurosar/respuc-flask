from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import CheckConstraint, Column, Date, ForeignKey, Integer, String, Table, Text, SmallInteger, ForeignKeyConstraint, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
import datetime

from app import db, login_manager

Base = declarative_base()
metadata = Base.metadata

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'

    usuario_id = db.Column(db.Integer, primary_key=True)
    senha_hash = db.Column(db.String(128))
    email = db.Column(db.String(60), index=True, unique=True)
    permissao = db.Column(db.Integer, nullable=False, default=0)

    @property
    def senha(self):
        raise AttributeError('senha is not a readable attribute.')

    @senha.setter
    def senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verify_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return '<email {}'.format(self.email)

    def get_id(self):
        return self.usuario_id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

@login_manager.user_loader
def load_user(usuario_id):
    return Usuario.query.get(usuario_id)


#abaixo codigo gerado com flask-sqlcodegen

class AtividadeFora(db.Model):
    __tablename__ = 'atividade_fora'

    dia = db.Column(db.Date, primary_key=True, nullable=False)
    horario = db.Column(db.String, primary_key=True, nullable=False)
    descricao = db.Column(db.String(200), primary_key=True, nullable=False)

    pessoa = relationship('Pessoa', secondary='aluno_faz_atividade_fora')


class ConjuntoDeAula(db.Model):
    __tablename__ = 'conjunto_de_aulas'

    materia = db.Column(db.String(100), primary_key=True, nullable=False)
    horario = db.Column(db.String, primary_key=True, nullable=False)
    matricula_puc = db.Column(db.String(7), nullable=False)
    curso_puc = db.Column(db.String(80))
    data_ini = db.Column(db.Date)
    data_fim = db.Column(db.Date)


class Evento(db.Model):
    __tablename__ = 'evento'

    nome = db.Column(db.String(200), primary_key=True, nullable=False)
    data = db.Column(db.Date, primary_key=True, nullable=False)
    descricao = db.Column(db.String(200))

    pessoa = relationship('Pessoa', secondary='participa')


class Instituicao(db.Model):
    __tablename__ = 'instituicao'

    nome = db.Column(db.String(200), primary_key=True)
    contato_telefone = db.Column(db.String(16))
    contato_nome = db.Column(db.String(200))


class Pessoa(db.Model):
    __tablename__ = 'pessoa'

    rg_numero = db.Column(db.String(12), primary_key=True, nullable=False)
    rg_orgao_expedidor = db.Column(db.String(20), primary_key=True, nullable=False)
    rg_data_expedicao = db.Column(db.Date, primary_key=True, nullable=False)
    nome = db.Column(db.String(80), nullable=False)
    sexo = db.Column(db.SmallInteger)
    data_nascimento = db.Column(db.Date)
    email = db.Column(db.String(60))
    celular = db.Column(db.String(16))
    rua = db.Column(db.String(100))
    numero = db.Column(db.String(20))
    complemento = db.Column(db.String(50))
    bairro = db.Column(db.String(20))
    cidade = db.Column(db.String(20))
    uf = db.Column(db.String(2))
    cep = db.Column(db.String(8))
    foto = db.Column(db.String(200))
    data_desligamento = db.Column(db.Date)


class Aluno(db.Model):
    __tablename__ = 'aluno'
    __table_args__ = (
        ForeignKeyConstraint(['rg_numero_pessoa', 'rg_orgao_expedidor_pessoa', 'rg_data_expedicao_pessoa'], ['pessoa.rg_numero', 'pessoa.rg_orgao_expedidor', 'pessoa.rg_data_expedicao'], ondelete='CASCADE', onupdate='CASCADE'),
    )

    rg_numero_pessoa = db.Column(db.String(12), primary_key=True, nullable=False)
    rg_orgao_expedidor_pessoa = db.Column(db.String(20), primary_key=True, nullable=False)
    rg_data_expedicao_pessoa = db.Column(db.Date, primary_key=True, nullable=False)
    dificuldade = db.Column(ARRAY(db.String(length=50)))


class Voluntario(db.Model):
    __tablename__ = 'voluntario'
    __table_args__ = (
        CheckConstraint("curso_puc = ANY (ARRAY['Administração'::bpchar, 'Arquitetura e Urbanismo'::bpchar, 'Artes Cênicas'::bpchar, 'Ciência da Computação'::bpchar, 'Ciências Biológicas'::bpchar, 'Ciências Econômicas'::bpchar, 'Ciências Sociais'::bpchar, 'Comunicação Social - Cinema'::bpchar, 'Comunicação Social - Jornalismo'::bpchar, 'Comunicação Social - Publicidade e Propaganda'::bpchar, 'Design - Comunicação Visual'::bpchar, 'Design - Mídia Digital'::bpchar, 'Design - Moda'::bpchar, 'Design - Projeto de Produto'::bpchar, 'Direito'::bpchar, 'Engenharia Ambiental'::bpchar, 'Engenharia Civil'::bpchar, 'Engenharia da Computação'::bpchar, 'Engenharia de Controle e Automação'::bpchar, 'Engenharia Elétrica'::bpchar, 'Engenharia Mecânica'::bpchar, 'Engenharia de Materiais e Nanotecnologia'::bpchar, 'Engenharia de Petróleo'::bpchar, 'Engenharia de Produção'::bpchar, 'Engenharia Química'::bpchar, 'Filosofia'::bpchar, 'Física'::bpchar, 'Geografia'::bpchar, 'História'::bpchar, 'Letras'::bpchar, 'Matemática'::bpchar, 'Pedagogia'::bpchar, 'Produção e Gestão de Mídias em Educação'::bpchar, 'Psicologia'::bpchar, 'Química'::bpchar, 'Relações Internacionais'::bpchar, 'Serviço Social'::bpchar, 'Sistemas de Informação'::bpchar, 'Teologia'::bpchar])"),
        ForeignKeyConstraint(['rg_numero_pessoa', 'rg_orgao_expedidor_pessoa', 'rg_data_expedicao_pessoa'], ['pessoa.rg_numero', 'pessoa.rg_orgao_expedidor', 'pessoa.rg_data_expedicao'], ondelete='CASCADE', onupdate='CASCADE')
    )

    rg_numero_pessoa = db.Column(db.String(12), primary_key=True, nullable=False)
    rg_orgao_expedidor_pessoa = db.Column(db.String(20), primary_key=True, nullable=False)
    rg_data_expedicao_pessoa = db.Column(db.Date, primary_key=True, nullable=False)
    matricula_puc = db.Column(db.String(7), nullable=False)
    curso_puc = db.Column(db.String(80), nullable=False)


class AlunoFazAtividadeFora(db.Model):

    __tablename__ = 'aluno_faz_atividade_fora'
    __table_args__ = (
        ForeignKeyConstraint(['dia_atividade', 'horario_atividade', 'descricao_atividade'], ['atividade_fora.dia', 'atividade_fora.horario', 'atividade_fora.descricao'], ondelete='CASCADE', onupdate='CASCADE'),
        ForeignKeyConstraint(['rg_numero_pessoa', 'rg_orgao_expedidor_pessoa', 'rg_data_expedicao_pessoa'], ['pessoa.rg_numero', 'pessoa.rg_orgao_expedidor', 'pessoa.rg_data_expedicao'], ondelete='CASCADE', onupdate='CASCADE')
    )

    rg_numero_pessoa = db.Column(db.String(12), primary_key=True, nullable=False)
    rg_orgao_expedidor_pessoa = db.Column(db.String(20), primary_key=True, nullable=False)
    rg_data_expedicao_pessoa = db.Column(db.Date, primary_key=True, nullable=False)
    dia_atividade = db.Column(db.Date, primary_key=True, nullable=False)
    horario_atividade = db.Column(db.String, primary_key=True, nullable=False)
    descricao_atividade = db.Column(db.String(200), primary_key=True, nullable=False)


class AprendizAluno(db.Model):
    __tablename__ = 'aprendiz_aluno'
    __table_args__ = (
        ForeignKeyConstraint(['rg_numero_pessoa', 'rg_orgao_expedidor_pessoa', 'rg_data_expedicao_pessoa'], ['pessoa.rg_numero', 'pessoa.rg_orgao_expedidor', 'pessoa.rg_data_expedicao'], ondelete='CASCADE', onupdate='CASCADE'),
    )

    rg_numero_pessoa = db.Column(db.String(12), primary_key=True, nullable=False)
    rg_orgao_expedidor_pessoa = db.Column(db.String(20), primary_key=True, nullable=False)
    rg_data_expedicao_pessoa = db.Column(db.Date, primary_key=True, nullable=False)
    nome_responsavel = db.Column(db.String(80), primary_key=True, nullable=False)
    telefone_responsavel = db.Column(db.String(16))
    profissao_responsavel = db.Column(db.String(60))
    nome_instituicao = db.Column(ForeignKey('instituicao.nome', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    serie = db.Column(db.String(10))
    nivel_escolaridade = db.Column(db.String(15))
    status_escolaridade = db.Column(db.String(10))
    turno = db.Column(db.String(5))
    local_destino = db.Column(db.String(200))
    descricao_destino = db.Column(db.String(200))
    data_destino = db.Column(db.Date)

    instituicao = relationship('Instituicao')
    pessoa = relationship('Pessoa')


class Cursa(db.Model):
    __tablename__ = 'cursa'
    __table_args__ = (
        ForeignKeyConstraint(['materia', 'horario'], ['conjunto_de_aulas.materia', 'conjunto_de_aulas.horario'], ondelete='CASCADE', onupdate='CASCADE'),
        ForeignKeyConstraint(['rg_numero_pessoa', 'rg_orgao_expedidor_pessoa', 'rg_data_expedicao_pessoa'], ['pessoa.rg_numero', 'pessoa.rg_orgao_expedidor', 'pessoa.rg_data_expedicao'], ondelete='CASCADE', onupdate='CASCADE')
    )

    rg_numero_pessoa = db.Column(db.String(12), primary_key=True, nullable=False)
    rg_orgao_expedidor_pessoa = db.Column(db.String(20), primary_key=True, nullable=False)
    rg_data_expedicao_pessoa = db.Column(db.Date, primary_key=True, nullable=False)
    materia = db.Column(db.String(200), primary_key=True, nullable=False)
    horario = db.Column(db.String, primary_key=True, nullable=False)
    data_ini = db.Column(db.Date)
    data_fim = db.Column(db.Date)

    conjunto_de_aula = relationship('ConjuntoDeAula')
    pessoa = relationship('Pessoa')


class Participa(db.Model):
    __tablename__ = 'participa'
    __table_args__ = (
        ForeignKeyConstraint(['evento_nome', 'evento_data'], ['evento.nome', 'evento.data'], ondelete='CASCADE', onupdate='CASCADE'),
        ForeignKeyConstraint(['rg_numero_pessoa', 'rg_orgao_expedidor_pessoa', 'rg_data_expedicao_pessoa'], ['pessoa.rg_numero', 'pessoa.rg_orgao_expedidor', 'pessoa.rg_data_expedicao'], ondelete='CASCADE', onupdate='CASCADE')
    )

    rg_numero_pessoa = db.Column(db.String(12), primary_key=True, nullable=False)
    rg_orgao_expedidor_pessoa = db.Column(db.String(20), primary_key=True, nullable=False)
    rg_data_expedicao_pessoa = db.Column(db.Date, primary_key=True, nullable=False)
    evento_nome = db.Column(db.String(200), primary_key=True, nullable=False)
    evento_data = db.Column(db.Date, primary_key=True, nullable=False)


# t_participa = Table(
#     'participa', metadata,
#     db.Column('rg_numero_pessoa', db.String(12), primary_key=True, nullable=False),
#     db.Column('rg_orgao_expedidor_pessoa', db.String(20), primary_key=True, nullable=False),
#     db.Column('rg_data_expedicao_pessoa', db.Date, primary_key=True, nullable=False),
#     db.Column('evento_nome', db.String(200), primary_key=True, nullable=False),
#     db.Column('evento_data', db.Date, primary_key=True, nullable=False),
#     ForeignKeyConstraint(['evento_nome', 'evento_data'], ['evento.nome', 'evento.data'], ondelete='CASCADE', onupdate='CASCADE'),
#     ForeignKeyConstraint(['rg_numero_pessoa', 'rg_orgao_expedidor_pessoa', 'rg_data_expedicao_pessoa'], ['pessoa.rg_numero', 'pessoa.rg_orgao_expedidor', 'pessoa.rg_data_expedicao'], ondelete='CASCADE', onupdate='CASCADE')
# )



class Realiza(db.Model):
    __tablename__ = 'realiza'
    __table_args__ = (
        ForeignKeyConstraint(['rg_numero_pessoa', 'rg_orgao_expedidor_pessoa', 'rg_data_expedicao_pessoa'], ['pessoa.rg_numero', 'pessoa.rg_orgao_expedidor', 'pessoa.rg_data_expedicao'], ondelete='CASCADE', onupdate='CASCADE'),
    )

    rg_numero_pessoa = db.Column(db.String(12), primary_key=True, nullable=False)
    rg_orgao_expedidor_pessoa = db.Column(db.String(20), primary_key=True, nullable=False)
    rg_data_expedicao_pessoa = db.Column(db.Date, primary_key=True, nullable=False)
    local = db.Column(db.String(200), primary_key=True, nullable=False)
    descricao = db.Column(db.String(200), primary_key=True, nullable=False)
    data_ini = db.Column(db.Date)
    data_fim = db.Column(db.Date)

    pessoa = relationship('Pessoa')
