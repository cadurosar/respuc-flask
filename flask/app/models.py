from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import ARRAY, Column, Date, Enum, Float, ForeignKey, ForeignKeyConstraint, Integer, SmallInteger, String, Table, Time, text
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

# ---

class AtividadeFora(db.Model):
    __tablename__ = 'atividade_fora'

    pk_atividade_nome = db.Column(db.String(100), primary_key=True)
    atividade_local = db.Column(db.String(100))


class AtividadeNeam(db.Model):
    __tablename__ = 'atividade_neam'

    pk_nome_atividade_neam = db.Column(db.String(100), primary_key=True)
    hora_ini = db.Column(db.Time)


class Evento(db.Model):
    __tablename__ = 'evento'

    pk_nome = db.Column(db.String(200), primary_key=True, nullable=False)
    pk_data = db.Column(db.Date, primary_key=True, nullable=False)
    descricao = db.Column(db.String(200))

    pessoa = relationship('Pessoa', secondary='participa')


class Instituicao(db.Model):
    __tablename__ = 'instituicao'

    pk_nome = db.Column(db.String(200), primary_key=True)
    contato_nome = db.Column(db.String(100))
    contato_telefone = db.Column(db.CHAR(10))


class Trabalho(db.Model):
    __tablename__ = 'trabalho'

    pk_local_puc = db.Column(db.String(50), primary_key=True, nullable=False)
    pk_funcao = db.Column(db.String(50), primary_key=True, nullable=False)


class Pessoa(db.Model):
    __tablename__ = 'pessoa'

    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True)
    celular = db.Column(db.CHAR(50))
    foto = db.Column(db.CHAR(200))
    desligamento_data = db.Column(db.Date)
    desligamento_motivo = db.Column(db.String(100))
    sexo = db.Column(db.CHAR(1))
    data_nascimento = db.Column(db.Date)
    identificador_tipo = db.Column(db.SmallInteger, nullable=False)
    identificador_numero = db.Column(db.String(32), nullable=False)
    identificador_complemento = db.Column(db.CHAR(2))
    endereco_numero = db.Column(db.SmallInteger)
    endereco_rua = db.Column(db.String(100))
    endereco_complemento = db.Column(db.String(50))
    endereco_bairro = db.Column(db.String(20))
    endereco_cidade = db.Column(db.String(20))
    endereco_uf = db.Column(db.CHAR(2))
    endereco_cep = db.Column(db.CHAR(8))
    pk_matricula_neam = db.Column(db.Integer, primary_key=True, server_default=text("nextval('pessoa_pk_matricula_neam_seq'::regclass)"))
    tipo = db.Column(Enum('voluntario', 'aprendiz', 'aluno', name='tipo_pessoa'), nullable=False)
    nome_responsavel = db.Column(ARRAY(db.String(length=100)), nullable=False)
    telefone_responsavel = db.Column(ARRAY(db.CHAR(length=10)))
    profissao_responsavel = db.Column(ARRAY(db.String(length=50)))
    curso_puc = db.Column(db.String(50))
    matricula_puc = db.Column(db.CHAR(7), unique=True)
    dificuldade = db.Column(ARRAY(db.String(length=50)))
    serie = db.Column(db.String(10))
    escolaridade_nivel = db.Column(db.String(30))
    escolaridade_turno = db.Column(db.String(10))
    nome_instituicao = db.Column(ForeignKey('instituicao.pk_nome', ondelete='CASCADE', onupdate='CASCADE'))

    instituicao = relationship('Instituicao')


class Cursa(Pessoa):
    __tablename__ = 'cursa'

    pk_matricula_neam_pessoa = db.Column(ForeignKey('pessoa.pk_matricula_neam', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, server_default=text("nextval('cursa_pk_matricula_neam_pessoa_seq'::regclass)"))
    pk_nome_atividade_neam = db.Column(ForeignKey('atividade_neam.pk_nome_atividade_neam', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    nota = db.Column(db.Float)
    data_ini = db.Column(db.Date)
    data_fim = db.Column(db.Date)

    atividade_neam = relationship('AtividadeNeam')


class AulaReforco(db.Model):
    __tablename__ = 'aula_reforco'

    pk_materia = db.Column(db.String(20), primary_key=True, nullable=False)
    pk_matricula_neam_pessoa = db.Column(ForeignKey('pessoa.pk_matricula_neam', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, server_default=text("nextval('aula_reforco_pk_matricula_neam_pessoa_seq'::regclass)"))
    pk_matricula_puc_pessoa = db.Column(ForeignKey('pessoa.matricula_puc', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, unique=True)
    hora_ini = db.Column(db.Time)
    data = db.Column(db.Date)

    pessoa = relationship('Pessoa', primaryjoin='AulaReforco.pk_matricula_neam_pessoa == Pessoa.pk_matricula_neam')
    pessoa1 = relationship('Pessoa', uselist=False, primaryjoin='AulaReforco.pk_matricula_puc_pessoa == Pessoa.matricula_puc')


class Faz(db.Model):
    __tablename__ = 'faz'

    pk_matricula_neam_pessoa = db.Column(ForeignKey('pessoa.pk_matricula_neam', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, server_default=text("nextval('faz_pk_matricula_neam_pessoa_seq'::regclass)"))
    pk_nome_atividade_fora = db.Column(ForeignKey('atividade_fora.pk_atividade_nome', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    hora_ini = db.Column(db.Time)
    hora_fim = db.Column(db.Time)
    dia_semana = db.Column(db.String(15))
    frequencia = db.Column(db.CHAR(4))

    pessoa = relationship('Pessoa')
    atividade_fora = relationship('AtividadeFora')


t_participa = Table(
    'participa', metadata,
    db.Column('pk_matricula_neam_pessoa', ForeignKey('pessoa.pk_matricula_neam', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, server_default=text("nextval('participa_pk_matricula_neam_pessoa_seq'::regclass)")),
    db.Column('pk_data_evento', db.Date, primary_key=True, nullable=False),
    db.Column('pk_nome_evento', db.String(100), primary_key=True, nullable=False),
    ForeignKeyConstraint(['pk_data_evento', 'pk_nome_evento'], ['evento.pk_data', 'evento.pk_nome'], ondelete='CASCADE', onupdate='CASCADE')
)


class Realiza(db.Model):
    __tablename__ = 'realiza'
    __table_args__ = (
        ForeignKeyConstraint(['pk_local_puc_trabalho', 'pk_funcao_trabalho'], ['trabalho.pk_local_puc', 'trabalho.pk_funcao'], ondelete='CASCADE', onupdate='CASCADE'),
    )

    pk_matricula_neam_pessoa = db.Column(ForeignKey('pessoa.pk_matricula_neam', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, server_default=text("nextval('realiza_pk_matricula_neam_pessoa_seq'::regclass)"))
    pk_local_puc_trabalho = db.Column(db.String(50), primary_key=True, nullable=False)
    pk_funcao_trabalho = db.Column(db.String(50), primary_key=True, nullable=False)
    data_ini = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date)

    trabalho = relationship('Trabalho')
    pessoa = relationship('Pessoa')
