/*
	DDL do esquema físico 

	Feito em: 22/08/2018

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

	CONSTRAINT pessoa_pk PRIMARY KEY (pk_rg_numero, pk_rg_orgao_expedidor, pk_rg_data_expedicao),
	CONSTRAINT pessoa_ck_sexo CHECK (sexo >= 0),
	CONSTRAINT pessoa_ck_data_nascimento CHECK (isfinite(data_nascimento))
);

/* ----------- */

DROP TABLE IF EXISTS aprendiz_aluno CASCADE;

CREATE TABLE aprendiz_aluno
(
	fk_rg_numero_pessoa char(12) NOT NULL,
	fk_rg_orgao_expedidor_pessoa varchar(20) NOT NULL,
	fk_rg_data_expedicao_pessoa date NOT NULL,
	responsavel responsavel [],

	CONSTRAINT aprendiz_aluno_fk FOREIGN KEY (fk_rg_numero_pessoa, fk_rg_orgao_expedidor_pessoa, fk_rg_data_expedicao_pessoa) REFERENCES pessoa(pk_rg_numero, pk_rg_orgao_expedidor, pk_rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE
);

/* ----------- */

DROP TABLE IF EXISTS voluntario CASCADE;

CREATE TABLE voluntario
(
	fk_rg_numero_pessoa char(12) NOT NULL,
	fk_rg_orgao_expedidor_pessoa varchar(20) NOT NULL,
	fk_rg_data_expedicao_pessoa date NOT NULL,
	matricula_puc char(7) UNIQUE NOT NULL,
	curso_puc varchar(80) NOT NULL,

	CONSTRAINT voluntario_fk FOREIGN KEY (fk_rg_numero_pessoa, fk_rg_orgao_expedidor_pessoa, fk_rg_data_expedicao_pessoa) REFERENCES pessoa(pk_rg_numero, pk_rg_orgao_expedidor, pk_rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT voluntario_ck_curso CHECK (curso_puc IN ('Administração', 'Arquitetura e Urbanismo', 'Artes Cênicas', 'Ciência da Computação', 'Ciências Biológicas', 'Ciências Econômicas', 'Ciências Sociais', 'Comunicação Social - Cinema', 'Comunicação Social - Jornalismo', 'Comunicação Social - Publicidade e Propaganda', 'Design - Comunicação Visual', 'Design - Mídia Digital', 'Design - Moda', 'Design - Projeto de Produto', 'Direito', 'Engenharia Ambiental', 'Engenharia Civil', 'Engenharia da Computação', 'Engenharia de Controle e Automação', 'Engenharia Elétrica', 'Engenharia Mecânica', 'Engenharia de Materiais e Nanotecnologia', 'Engenharia de Petróleo', 'Engenharia de Produção', 'Engenharia Química', 'Filosofia', 'Física', 'Geografia', 'História', 'Letras', 'Matemática', 'Pedagogia','Produção e Gestão de Mídias em Educação', 'Psicologia', 'Química', 'Relações Internacionais', 'Serviço Social', 'Sistemas de Informação', 'Teologia'))
);

/* ----------- */

DROP TABLE IF EXISTS aluno CASCADE;

CREATE TABLE aluno
(
	fk_rg_numero_pessoa char(12) NOT NULL,
	fk_rg_orgao_expedidor_pessoa varchar(20) NOT NULL,
	fk_rg_data_expedicao_pessoa date NOT NULL,
	dificuldade dificuldade [],

	CONSTRAINT aluno_fk FOREIGN KEY (fk_rg_numero_pessoa, fk_rg_orgao_expedidor_pessoa, fk_rg_data_expedicao_pessoa) REFERENCES pessoa(pk_rg_numero, pk_rg_orgao_expedidor, pk_rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE
);

/* ----------- */

DROP TABLE IF EXISTS atividade_fora CASCADE;

CREATE TABLE atividade_fora
(
	pk_dia date NOT NULL,
	pk_horario time NOT NULL,
	pk_descricao varchar(200) NOT NULL,

	CONSTRAINT atividade_fora_pk PRIMARY KEY (pk_dia, pk_horario, pk_descricao)
);

/* ----------- */

DROP TABLE IF EXISTS instituicao CASCADE;

CREATE TABLE instituicao
(
	pk_nome varchar(200) NOT NULL,
	contato_telefone varchar(16) NOT NULL,
	contato_nome varchar(200) NOT NULL,

	CONSTRAINT instituicao_pk PRIMARY KEY (pk_nome)
);

/* ----------- */

DROP TABLE IF EXISTS trabalho CASCADE;

CREATE TABLE trabalho
(
	pk_local varchar(200) NOT NULL,
	pk_descricao varchar(200) NOT NULL,

	CONSTRAINT trabalho_pk PRIMARY KEY (pk_local, pk_descricao)
);

/* ----------- */

DROP TABLE IF EXISTS realiza CASCADE;

CREATE TABLE realiza
(
	fk_rg_numero_pessoa char(12) NOT NULL,
	fk_rg_orgao_expedidor_pessoa varchar(20) NOT NULL,
	fk_rg_data_expedicao_pessoa date NOT NULL,
	fk_local varchar(200) NOT NULL,
	fk_descricao varchar(200) NOT NULL,
	data_ini date NOT NULL,
	data_fim date NOT NULL,

	CONSTRAINT realiza_pk PRIMARY KEY (fk_rg_numero_pessoa, fk_rg_orgao_expedidor_pessoa, fk_rg_data_expedicao_pessoa, fk_local, fk_descricao),
	CONSTRAINT realiza_pessoa_fk FOREIGN KEY (fk_rg_numero_pessoa, fk_rg_orgao_expedidor_pessoa, fk_rg_data_expedicao_pessoa) REFERENCES pessoa(pk_rg_numero, pk_rg_orgao_expedidor, pk_rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT realiza_trabalho_fk FOREIGN KEY (fk_local, fk_descricao) REFERENCES trabalho(pk_local, pk_descricao) ON UPDATE CASCADE ON DELETE CASCADE
);

/* ----------- */

DROP TABLE IF EXISTS evento CASCADE;

CREATE TABLE evento
(
	pk_nome varchar(200) NOT NULL,
	pk_data date NOT NULL,
	descricao varchar(200) NOT NULL,

	CONSTRAINT evento_pk PRIMARY KEY (pk_nome, pk_data),
	CONSTRAINT evento_ck_data_pk CHECK (isfinite(pk_data))
);

/* ----------- */

DROP TABLE IF EXISTS aula CASCADE;

CREATE TABLE aula
(
	pk_materia varchar(200) NOT NULL,
	pk_horario varchar(200) NOT NULL,

	CONSTRAINT aula_pk PRIMARY KEY (pk_materia, pk_horario)
);

/* ----------- */

DROP TABLE IF EXISTS cursa CASCADE;

CREATE TABLE cursa
(
	fk_rg_numero_pessoa char(12) NOT NULL,
	fk_rg_orgao_expedidor_pessoa varchar(20) NOT NULL,
	fk_rg_data_expedicao_pessoa date NOT NULL,
	fk_materia varchar(200) NOT NULL,
	fk_horario varchar(200) NOT NULL,
	data_ini date NOT NULL,
	data_fim date NOT NULL,

	CONSTRAINT cursa_pk PRIMARY KEY (fk_rg_numero_pessoa, fk_rg_orgao_expedidor_pessoa, fk_rg_data_expedicao_pessoa, fk_materia, fk_horario),
	CONSTRAINT cursa_pessoa_fk FOREIGN KEY (fk_rg_numero_pessoa, fk_rg_orgao_expedidor_pessoa, fk_rg_data_expedicao_pessoa) REFERENCES pessoa(pk_rg_numero, pk_rg_orgao_expedidor, pk_rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT cursa_aula_fk FOREIGN KEY (fk_materia, fk_horario) REFERENCES aula(pk_materia, pk_horario) ON UPDATE CASCADE ON DELETE CASCADE
);

/* ----------- */

DROP TABLE IF EXISTS leciona CASCADE;

CREATE TABLE leciona
(
	fk_rg_numero_pessoa char(12) NOT NULL,
	fk_rg_orgao_expedidor_pessoa varchar(20) NOT NULL,
	fk_rg_data_expedicao_pessoa date NOT NULL,
	fk_materia varchar(200) NOT NULL,
	fk_horario varchar(200) NOT NULL,
	data_ini date NOT NULL,
	data_fim date NOT NULL,

	CONSTRAINT leciona_pk PRIMARY KEY (fk_rg_numero_pessoa, fk_rg_orgao_expedidor_pessoa, fk_rg_data_expedicao_pessoa, fk_materia, fk_horario),
	CONSTRAINT leciona_pessoa_fk FOREIGN KEY (fk_rg_numero_pessoa, fk_rg_orgao_expedidor_pessoa, fk_rg_data_expedicao_pessoa) REFERENCES pessoa(pk_rg_numero, pk_rg_orgao_expedidor, pk_rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT leciona_aula_fk FOREIGN KEY (fk_materia, fk_horario) REFERENCES aula(pk_materia, pk_horario) ON UPDATE CASCADE ON DELETE CASCADE
);

/* ----------- */

DROP TABLE IF EXISTS participa CASCADE;

CREATE TABLE participa
(
	fk_rg_numero char(12) NOT NULL,
	fk_rg_orgao_expedidor varchar(20) NOT NULL,
	fk_rg_data_expedicao date NOT NULL,
	fk_evento_nome varchar(200) NOT NULL,
	fk_evento_data date NOT NULL,

	CONSTRAINT participa_pk PRIMARY KEY (fk_rg_numero, fk_rg_orgao_expedidor, fk_rg_data_expedicao, fk_evento_nome, fk_evento_data),
	CONSTRAINT participa_rg_pessoa_fk FOREIGN KEY (fk_rg_numero, fk_rg_orgao_expedidor, fk_rg_data_expedicao) REFERENCES pessoa(pk_rg_numero, pk_rg_orgao_expedidor, pk_rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT participa_evento_fk FOREIGN KEY (fk_evento_nome, fk_evento_data) REFERENCES evento(pk_nome, pk_data) ON UPDATE CASCADE ON DELETE CASCADE
);

/* ----------- */

DROP TABLE IF EXISTS oriundo_de CASCADE;

CREATE TABLE oriundo_de
(
	fk_rg_numero char(12) NOT NULL,
	fk_rg_orgao_expedidor varchar(20) NOT NULL,
	fk_rg_data_expedicao date NOT NULL,
	fk_nome_instituicao varchar(200) NOT NULL,

	CONSTRAINT oriundo_de_pk PRIMARY KEY (fk_rg_numero, fk_rg_orgao_expedidor, fk_rg_data_expedicao, fk_nome_instituicao),
	CONSTRAINT oriundo_de_cpf_pessoa_fk FOREIGN KEY (fk_rg_numero, fk_rg_orgao_expedidor, fk_rg_data_expedicao) REFERENCES pessoa(pk_rg_numero, pk_rg_orgao_expedidor, pk_rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE,
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

/* ----------- */