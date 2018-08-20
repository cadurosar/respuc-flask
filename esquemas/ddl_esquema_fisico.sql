/*
	DDL do esquema físico

	Projeto: RESPUC-NEAM PUC-Rio

	Descrição:
	Cria no banco de dados as tabelas apresentadas como entidades no esquema conceitual versão 5.
*/

/* ---------------------------------------------- TIPOS ----------------------------------------------- */

DROP TYPE IF EXISTS endereco CASCADE;

CREATE TYPE endereco AS
(
	rua varchar(100),
	numero varchar(20),
	complemento varchar(50),
	bairro varchar(20),
	cidade varchar(20),
	uf char(2),
	cep char(8)
);


DROP TYPE IF EXISTS dificuldade CASCADE;

CREATE TYPE dificuldade AS
(
	nome varchar(80),
	apoio boolean
);


DROP TYPE IF EXISTS responsavel CASCADE;

CREATE TYPE responsavel AS
(
	nome varchar(80),
	celular varchar(200),
	profissao varchar(200)
);


/* --------------------------------------------- TABELAS ---------------------------------------------- */

DROP TABLE IF EXISTS pessoa CASCADE;

CREATE TABLE pessoa
(
	pk_rg_numero char(12) NOT NULL,
	pk_rg_orgao_expedidor varchar(20) NOT NULL,
	pk_rg_data_expedicao date NOT NULL,
	nome varchar(80) NOT NULL,
	sexo smallint NOT NULL,
	data_nascimento date NOT NULL,
	email varchar(60) UNIQUE NOT NULL,
	celular varchar(200) NOT NULL,
	endereco endereco NOT NULL,
	foto varchar(200) NOT NULL,
	data_desligamento date,

	CONSTRAINT pessoa_pk PRIMARY KEY (pk_rg, pk_rg_numero, pk_rg_data_expedicao),
	CONSTRAINT pessoa_ck_rg_numero_pk CHECK (length(trim(pk_rg_numero)) > 0),
	CONSTRAINT pessoa_ck_rg_orgao_expedidor_pk CHECK (length(trim(pk_rg_orgao_expedidor)) > 0),
	CONSTRAINT pessoa_ck_rg_data_expedicao_pk CHECK (length(trim(pk_rg_data_expedicao)) > 0),
	CONSTRAINT pessoa_ck_nome CHECK (length(trim(nome)) > 0),
	CONSTRAINT pessoa_ck_email CHECK (length(trim(email)) > 0),
	CONSTRAINT pessoa_ck_sexo CHECK (sexo >= 0),
	CONSTRAINT pessoa_ck_data_nascimento CHECK (isfinite(data_nascimento))
);


DROP TABLE IF EXISTS aprendiz_aluno CASCADE;

CREATE TABLE aprendiz_aluno
(
	fk_rg_numero_pessoa char(12) NOT NULL,
	fk_rg_orgao_expedidor_pessoa varchar(20) NOT NULL,
	fk_rg_data_expedicao_pessoa date NOT NULL,
	responsavel responsavel [],

	CONSTRAINT aprendiz_aluno_fk FOREIGN KEY (fk_rg_numero_pessoa, fk_rg_orgao_expedidor_pessoa, fk_rg_data_expedicao_pessoa) REFERENCES pessoa(pk_rg_numero, pk_rg_orgao_expedidor, pk_rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS voluntario CASCADE;

CREATE TABLE voluntario
(
	fk_rg_numero_pessoa char(12) NOT NULL,
	fk_rg_orgao_expedidor_pessoa varchar(20) NOT NULL,
	fk_rg_data_expedicao_pessoa date NOT NULL,
	matricula_puc char(7) UNIQUE NOT NULL,
	curso_puc varchar(80) NOT NULL,

	CONSTRAINT voluntario_fk FOREIGN KEY (fk_rg_numero_pessoa, fk_rg_orgao_expedidor_pessoa, fk_rg_data_expedicao_pessoa) REFERENCES pessoa(pk_rg_numero, pk_rg_orgao_expedidor, pk_rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT voluntario_ck_matricula_puc CHECK (length(trim(matricula_puc)) = 7),
	CONSTRAINT voluntario_ck_curso CHECK (curso_puc IN ('Administração', 'Arquitetura e Urbanismo', 'Artes Cênicas', 'Ciência da Computação', 'Ciências Biológicas', 'Ciências Econômicas', 'Ciências Sociais', 'Comunicação Social - Cinema', 'Comunicação Social - Jornalismo', 'Comunicação Social - Publicidade e Propaganda', 'Design - Comunicação Visual', 'Design - Mídia Digital', 'Design - Moda', 'Design - Projeto de Produto', 'Direito', 'Engenharia Ambiental', 'Engenharia Civil', 'Engenharia da Computação', 'Engenharia de Controle e Automação', 'Engenharia Elétrica', 'Engenharia Mecânica', 'Engenharia de Materiais e Nanotecnologia', 'Engenharia de Petróleo', 'Engenharia de Produção', 'Engenharia Química', 'Filosofia', 'Física', 'Geografia', 'História', 'Letras', 'Matemática', 'Pedagogia','Produção e Gestão de Mídias em Educação', 'Psicologia', 'Química', 'Relações Internacionais', 'Serviço Social', 'Sistemas de Informação', 'Teologia'))
)


DROP TABLE IF EXISTS aluno CASCADE;

CREATE TABLE aluno
(
	fk_rg_numero_pessoa char(12) NOT NULL,
	fk_rg_orgao_expedidor_pessoa varchar(20) NOT NULL,
	fk_rg_data_expedicao_pessoa date NOT NULL,
	dificuldade dificuldade [],

	CONSTRAINT aluno_fk FOREIGN KEY (fk_rg_numero_pessoa, fk_rg_orgao_expedidor_pessoa, fk_rg_data_expedicao_pessoa) REFERENCES pessoa(pk_rg_numero, pk_rg_orgao_expedidor, pk_rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS atividade_fora CASCADE;

CREATE TABLE atividade_fora
(
	pk_dia date NOT NULL,
	pk_horario time NOT NULL,
	pk_descricao varchar(200) NOT NULL,

	CONSTRAINT atividade_fora_pk PRIMARY KEY (pk_dia, pk_horario, pk_descricao)
);


DROP TABLE IF EXISTS instituicao CASCADE;

CREATE TABLE instituicao
(
	pk_nome varchar(200) NOT NULL,
	contato_telefone varchar(16) NOT NULL,
	contato_nome varchar(200) NOT NULL,

	CONSTRAINT instituicao_pk PRIMARY KEY (pk_nome),
	CONSTRAINT instituicao_ck_nome_pk CHECK (length(trim(pk_nome)) > 0),
	CONSTRAINT instituicao_ck_contato_telefone CHECK (length(trim(contato_telefone)) > 0),
	CONSTRAINT instituicao_ck_contato_nome CHECK (length(trim(contato_nome)) > 0)
);


DROP TABLE IF EXISTS trabalho CASCADE;

CREATE TABLE trabalho
(
	pk_local varchar(200) NOT NULL,
	pk_descricao varchar(200) NOT NULL,

	CONSTRAINT atividade_pk PRIMARY KEY (pk_local, pk_descricao),
	CONSTRAINT atividade_ck_nome_pk CHECK (length(trim(pk_local)) > 0),
	CONSTRAINT atividade_ck_nome_pk CHECK (length(trim(pk_descricao)) > 0)
);


DROP TABLE IF EXISTS evento CASCADE;

CREATE TABLE evento
(
	pk_nome varchar(200) NOT NULL,
	pk_data date NOT NULL,
	descricao varchar(200) NOT NULL,

	CONSTRAINT evento_pk PRIMARY KEY (pk_nome, pk_data),
	CONSTRAINT evento_ck_nome_pk CHECK (length(trim(pk_nome)) > 0),
	CONSTRAINT evento_ck_data_pk CHECK (isfinite(pk_data)),
	CONSTRAINT evento_ck_descricao CHECK (length(trim(descricao)) > 0)
);


----------------------------------------------------------------------


DROP TABLE IF EXISTS projeto CASCADE;

CREATE TABLE projeto
(
	fk_atividade_id serial NOT NULL,
	presencas integer NOT NULL,
	descricao varchar(200) NOT NULL,

	CONSTRAINT projeto_pk PRIMARY KEY (fk_atividade_id),
	CONSTRAINT projeto_atividade_id_fk FOREIGN KEY (fk_atividade_id) REFERENCES atividade(pk_id) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT projeto_ck_presencas CHECK (presencas > 0),
	CONSTRAINT projeto_ck_descricao CHECK (length(trim(descricao)) > 0)
);


DROP TABLE IF EXISTS estagio CASCADE;

CREATE TABLE estagio
(
	fk_atividade_id serial NOT NULL,
	local varchar(200) NOT NULL,
	carga_horaria integer NOT NULL,

	CONSTRAINT estagio_pk PRIMARY KEY (fk_atividade_id),
	CONSTRAINT estagio_atividade_id_fk FOREIGN KEY (fk_atividade_id) REFERENCES atividade(pk_id) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT estagio_ck_local CHECK (length(trim(local)) > 0),
	CONSTRAINT projeto_ck_carga_horaria CHECK (carga_horaria > 0)
);


DROP TABLE IF EXISTS aula CASCADE;

CREATE TABLE aula
(
	fk_atividade_id serial NOT NULL,
	conteudo varchar(200) NOT NULL,

	CONSTRAINT aula_pk PRIMARY KEY (fk_atividade_id),
	CONSTRAINT aula_atividade_id_fk FOREIGN KEY (fk_atividade_id) REFERENCES atividade(pk_id) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT aula_ck_conteudo CHECK (length(trim(conteudo)) > 0)
);


DROP TABLE IF EXISTS participa CASCADE;

CREATE TABLE participa
(
	fk_cpf_pessoa char(11) NOT NULL,
	fk_atividade_id serial NOT NULL,

	CONSTRAINT participa_pk PRIMARY KEY (fk_cpf_pessoa, fk_atividade_id),
	CONSTRAINT participa_cpf_pessoa_fk FOREIGN KEY (fk_cpf_pessoa) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT participa_atividade_id_fk FOREIGN KEY (fk_atividade_id) REFERENCES atividade(pk_id) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS oriundo_de CASCADE;

CREATE TABLE oriundo_de
(
	fk_cpf_pessoa char(11) NOT NULL,
	fk_nome_instituicao varchar(200) NOT NULL,

	CONSTRAINT oriundo_de_pk PRIMARY KEY (fk_cpf_pessoa, fk_nome_instituicao),
	CONSTRAINT oriundo_de_cpf_pessoa_fk FOREIGN KEY (fk_cpf_pessoa) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT oriundo_de_nome_instituicao_fk FOREIGN KEY (fk_nome_instituicao) REFERENCES instituicao(pk_nome) ON UPDATE CASCADE ON DELETE CASCADE
);


/* --------------------------------------------- USUARIO ---------------------------------------------- */

DROP TABLE IF EXISTS usuario CASCADE;

CREATE TABLE usuario
(
	pk_email varchar(60) UNIQUE NOT NULL,
	login varchar(120) NOT NULL,
	senha_hash varchar(128) NOT NULL,
	permissao smallint NOT NULL,

	CONSTRAINT usuario_pk PRIMARY KEY (pk_email),
	CONSTRAINT usuario_email_pessoa_fk FOREIGN KEY (pk_email) REFERENCES pessoa(email) ON UPDATE CASCADE ON DELETE CASCADE
);
