from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import BigInteger, Boolean, CheckConstraint, Column, Date, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
import datetime

from app import db, login_manager

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'

    usuario_id = db.Column(db.Integer, primary_key=True)
    senha_hash = db.Column(db.String(128))
    email = db.Column(db.String(60), index=True, unique=True)
    role = db.Column(db.String(5), nullable=False)
    confirmado = db.Column(db.Boolean, nullable=False, default=False)

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

class Aluno(db.Model):
    __tablename__ = 'aluno'
    __table_args__ = (
        db.CheckConstraint('length(btrim((bairro)::text)) > 0'),
        db.CheckConstraint('length(btrim((cep)::text)) = 8'),
        db.CheckConstraint('length(btrim((cidade)::text)) > 0'),
        db.CheckConstraint('length(btrim((complemento)::text)) > 0'),
        db.CheckConstraint('length(btrim((email)::text)) > 0'),
        db.CheckConstraint('length(btrim((naturalidade)::text)) > 0'),
        db.CheckConstraint('length(btrim((nome)::text)) > 0'),
        db.CheckConstraint('length(btrim((rua)::text)) > 0')
    )

    cpf = db.Column(db.String(11), primary_key=True)
    rg = db.Column(db.String(12), nullable=False)
    naturalidade = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    nome = db.Column(db.String(70), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    telefone = db.Column(db.String(200), nullable=False)
    celular = db.Column(db.String(200), nullable=False)
    rua = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    complemento = db.Column(db.String(50), nullable=False)
    bairro = db.Column(db.String(20), nullable=False)
    cidade = db.Column(db.String(20), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    nome_responsavel = db.Column(db.String(200), nullable=False)
    cpf_responsavel = db.Column(db.String(200), nullable=False)
    telefone_responsavel = db.Column(db.String(200), nullable=False)
    profissao_responsavel = db.Column(db.String(200), nullable=False)


aluno_atividade_table = db.Table(
    'aluno_atividade',
    db.Column('cpf', db.ForeignKey('aluno.cpf', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
    db.Column('atividade', db.ForeignKey('atividade.nome', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
)


alunos_e_aprendizes_table = db.Table(
    'alunos_e_aprendizes',
    db.Column('cpf', db.String(11)),
    db.Column('nome', db.String(70)),
    db.Column('tipo', db.Text)
)


class Apoio(db.Model):
    __tablename__ = 'apoio'
    __table_args__ = (
        db.CheckConstraint('cpf > 0'),
        db.CheckConstraint('length(btrim((materia)::text)) > 0')
    )

    materia = db.Column(db.String(20), primary_key=True, nullable=False)
    cpf = db.Column(db.BigInteger, primary_key=True, nullable=False)


class Aprendiz(db.Model):
    __tablename__ = 'aprendiz'
    __table_args__ = (
        db.CheckConstraint('length(btrim((bairro)::text)) > 0'),
        db.CheckConstraint('length(btrim((cep)::text)) = 8'),
        db.CheckConstraint('length(btrim((cidade)::text)) > 0'),
        db.CheckConstraint('length(btrim((complemento)::text)) > 0'),
        db.CheckConstraint('length(btrim((email)::text)) > 0'),
        db.CheckConstraint('length(btrim((naturalidade)::text)) > 0'),
        db.CheckConstraint('length(btrim((nome)::text)) > 0'),
        db.CheckConstraint('length(btrim((rua)::text)) > 0'),
        db.CheckConstraint('length(btrim((trabalho)::text)) > 0'),
        db.CheckConstraint('length(btrim((uf)::text)) = 2')
    )

    cpf = db.Column(db.String(11), primary_key=True)
    rg = db.Column(db.String(12), nullable=False)
    naturalidade = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    nome = db.Column(db.String(70), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    telefone = db.Column(db.String(200), nullable=False)
    celular = db.Column(db.String(200), nullable=False)
    rua = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    complemento = db.Column(db.String(50), nullable=False)
    bairro = db.Column(db.String(20), nullable=False)
    cidade = db.Column(db.String(20), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    trabalho = db.Column(db.String(20), nullable=False)
    nome_responsavel = db.Column(db.String(200), nullable=False)
    cpf_responsavel = db.Column(db.String(200), nullable=False)
    telefone_responsavel = db.Column(db.String(200), nullable=False)
    profissao_responsavel = db.Column(db.String(200), nullable=False)


aprendiz_atividade_table = db.Table(
    'aprendiz_atividade',
    db.Column('cpf', db.ForeignKey('aprendiz.cpf', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
    db.Column('atividade', db.ForeignKey('atividade.nome', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
)


class Atividade(db.Model):
    __tablename__ = 'atividade'
    __table_args__ = (
        db.CheckConstraint('length(btrim((nome)::text)) > 0'),
    )

    nome = db.Column(db.String(50), primary_key=True)

    aluno = db.relationship('Aluno', secondary='aluno_atividade', backref='atividades')
    aprendiz = db.relationship('Aprendiz', secondary='aprendiz_atividade', backref='atividades')


cpf_atividade_table = db.Table(
    'cpf_atividade',
    db.Column('atividade', db.String(50)),
    db.Column('cpf', db.String(11)),
    db.Column('tipo', db.Text)
)


class Curso(db.Model):
    __tablename__ = 'curso'
    __table_args__ = (
        db.CheckConstraint("(nome)::text = ANY ((ARRAY['Administração'::character varying, 'Arquitetura e Urbanismo'::character varying, 'Artes Cênicas'::character varying, 'Ciência da Computação'::character varying, 'Ciências Biológicas'::character varying, 'Ciências Econômicas'::character varying, 'Ciências Sociais'::character varying, 'Comunicação Social - Cinema'::character varying, 'Comunicação Social - Jornalismo'::character varying, 'Comunicação Social - Publicidade e Propaganda'::character varying, 'Design - Comunicação Visual'::character varying, 'Design - Mídia Digital'::character varying, 'Design - Moda'::character varying, 'Design - Projeto de Produto'::character varying, 'Direito'::character varying, 'Engenharia Ambiental'::character varying, 'Engenharia Civil'::character varying, 'Engenharia da Computação'::character varying, 'Engenharia de Controle e Automação'::character varying, 'Engenharia Elétrica'::character varying, 'Engenharia Mecânica'::character varying, 'Engenharia de Materiais e Nanotecnologia'::character varying, 'Engenharia de Petróleo'::character varying, 'Engenharia de Produção'::character varying, 'Engenharia Química'::character varying, 'Filosofia'::character varying, 'Física'::character varying, 'Geografia'::character varying, 'História'::character varying, 'Letras'::character varying, 'Matemática'::character varying, 'Pedagogia'::character varying, 'Produção e Gestão de Mídias em Educação'::character varying, 'Psicologia'::character varying, 'Química'::character varying, 'Relações Internacionais'::character varying, 'Serviço Social'::character varying, 'Sistemas de Informação'::character varying, 'Teologia'::character varying])::text[])"),
        db.CheckConstraint('qtd_alunos > 0')
    )

    nome = db.Column(db.String(80), primary_key=True)
    coord = db.Column(db.String(50), nullable=False)
    depto = db.Column(db.String(30))
    qtd_alunos = db.Column(db.Integer, nullable=False)


class Dificuldade(db.Model):
    __tablename__ = 'dificuldade'
    __table_args__ = (
        db.CheckConstraint('cpf > 0'),
        db.CheckConstraint('length(btrim((materia)::text)) > 0')
    )

    materia = db.Column(db.String(20), primary_key=True, nullable=False)
    cpf = db.Column(db.BigInteger, primary_key=True, nullable=False)


class Escola(db.Model):
    __tablename__ = 'escola'
    __table_args__ = (
        db.CheckConstraint('telefone > 0'),
    )

    nome = db.Column(db.String(150), primary_key=True)
    telefone = db.Column(db.BigInteger, nullable=False)


class Estagio(db.Model):
    __tablename__ = 'estagio'
    __table_args__ = (
        db.CheckConstraint('cpf > 0'),
        db.CheckConstraint('length(btrim((estagio)::text)) > 0')
    )

    cpf = db.Column(db.BigInteger, primary_key=True, nullable=False)
    estagio = db.Column(db.String(50), primary_key=True, nullable=False)


class Evento(db.Model):
    __tablename__ = 'evento'
    __table_args__ = (
        db.CheckConstraint('(descricao IS NULL) OR (length(btrim((descricao)::text)) > 0)'),
        db.CheckConstraint('length(btrim((nome)::text)) > 0'),
        db.CheckConstraint('presencas > 0'),
        db.CheckConstraint('sfinite(dataevento')
    )

    nome = db.Column(db.String(20), primary_key=True, nullable=False)
    presencas = db.Column(db.Integer)
    dataevento = db.Column(db.Date, primary_key=True, nullable=False)
    descricao = db.Column(db.String(200))


class Funcionario(db.Model):
    __tablename__ = 'funcionario'
    __table_args__ = (
        db.CheckConstraint('length(btrim((email)::text)) > 0'),
        db.CheckConstraint('length(btrim((naturalidade)::text)) > 0'),
        db.CheckConstraint('length(btrim((nome)::text)) > 0')
    )

    cpf = db.Column(db.String(11), primary_key=True)
    rg = db.Column(db.String(12), nullable=False)
    naturalidade = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    nome = db.Column(db.String(70), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    telefone = db.Column(db.String(200), nullable=False)
    celular = db.Column(db.String(200), nullable=False)
    funcao = db.Column(db.String(200), nullable=False)


class Instituicao(db.Model):
    __tablename__ = 'instituicao'

    nome = db.Column(db.String(1024), primary_key=True)
    telefone = db.Column(db.String(16), nullable=False)
    celular = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(1024), nullable=False)
    vinculo = db.Column(db.String(1024), nullable=False)
    nome_responsavel = db.Column(db.String(1024), nullable=False)
    email_responsavel = db.Column(db.String(1024), nullable=False)
    telefone_responsavel = db.Column(db.String(16), nullable=False)


pessoa_atividade_table = db.Table(
    'pessoa_atividade',
    db.Column('cpf', db.String(11)),
    db.Column('tipo', db.Text),
    db.Column('nome', db.String(70)),
    db.Column('atividade', db.String(50))
)


class Trabalho(db.Model):
    __tablename__ = 'trabalho'
    __table_args__ = (
        db.CheckConstraint('cpf > 0'),
        db.CheckConstraint('length(btrim((trabalho)::text)) > 0')
    )

    cpf = db.Column(db.BigInteger, primary_key=True, nullable=False)
    trabalho = db.Column(db.String(50), primary_key=True, nullable=False)


class Voluntario(db.Model):
    __tablename__ = 'voluntario'

    cpf = db.Column(db.String(11), primary_key=True)
    rg = db.Column(db.String(12), nullable=False)
    naturalidade = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    nome = db.Column(db.String(70), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    telefone = db.Column(db.String(200), nullable=False)
    celular = db.Column(db.String(200), nullable=False)
    rua = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    complemento = db.Column(db.String(50), nullable=False)
    bairro = db.Column(db.String(20), nullable=False)
    cidade = db.Column(db.String(20), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    matricula = db.Column(db.String(7), nullable=False, unique=True)
