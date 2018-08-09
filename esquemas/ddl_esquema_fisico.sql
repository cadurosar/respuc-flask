/*
	DDL do esquema físico

	Projeto: RESPUC-NEAM PUC-Rio

	Descrição:
	Cria no banco de dados as tabelas apresentadas como entidades no esquema conceitual versão 3.
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


/* --------------------------------------------- TABELAS ---------------------------------------------- */

DROP TABLE IF EXISTS pessoa CASCADE;

CREATE TABLE pessoa
(
	pk_cpf char(11) NOT NULL,
	rg char(12) NOT NULL,
	naturalidade varchar(50) NOT NULL,
	email varchar(60) UNIQUE NOT NULL,
	nome varchar(70) NOT NULL,
	data_nascimento date NOT NULL,
	telefone varchar(200) NOT NULL,
	celular varchar(200) NOT NULL,

	CONSTRAINT pessoa_pk PRIMARY KEY (pk_cpf),
	CONSTRAINT pessoa_ck_naturalidade CHECK (length(trim(naturalidade)) > 0),
	CONSTRAINT pessoa_ck_email CHECK (length(trim(email)) > 0),
	CONSTRAINT pessoa_ck_nome CHECK (length(trim(nome)) > 0)
);


DROP TABLE IF EXISTS aprendiz_aluno CASCADE;

CREATE TABLE aprendiz_aluno
(
	fk_cpf_pessoa char(11) NOT NULL,
	endereco endereco NOT NULL,
	nome_responsavel varchar(200) NOT NULL,
	cpf_responsavel char(11) NOT NULL,
	telefone_responsavel varchar(200) NOT NULL,
	profissao_responsavel varchar(200) NOT NULL,

	CONSTRAINT aprendiz_aluno_cpf_pessoa_fk FOREIGN KEY (fk_cpf_pessoa) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS aprendiz CASCADE;

CREATE TABLE aprendiz
(
	fk_cpf_pessoa char(11) NOT NULL,
	departamento varchar(20) NOT NULL,
	trabalho varchar(20) [] NOT NULL,

	CONSTRAINT aprendiz_cpf_pessoa_fk FOREIGN KEY (fk_cpf_pessoa) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT aprendiz_ck_departamento CHECK (length(trim(departamento)) > 0)
);


DROP TABLE IF EXISTS aluno CASCADE;

CREATE TABLE aluno
(
	fk_cpf_pessoa char(11) NOT NULL,
	curso varchar(80) NOT NULL,
	dificuldade dificuldade [],

	CONSTRAINT aluno_cpf_pessoa_fk FOREIGN KEY (fk_cpf_pessoa) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT aluno_ck_curso CHECK (curso IN ('Administração', 'Arquitetura e Urbanismo', 'Artes Cênicas', 'Ciência da Computação', 'Ciências Biológicas', 'Ciências Econômicas', 'Ciências Sociais', 'Comunicação Social - Cinema', 'Comunicação Social - Jornalismo', 'Comunicação Social - Publicidade e Propaganda', 'Design - Comunicação Visual', 'Design - Mídia Digital', 'Design - Moda', 'Design - Projeto de Produto', 'Direito', 'Engenharia Ambiental', 'Engenharia Civil', 'Engenharia da Computação', 'Engenharia de Controle e Automação', 'Engenharia Elétrica', 'Engenharia Mecânica', 'Engenharia de Materiais e Nanotecnologia', 'Engenharia de Petróleo', 'Engenharia de Produção', 'Engenharia Química', 'Filosofia', 'Física', 'Geografia', 'História', 'Letras', 'Matemática', 'Pedagogia','Produção e Gestão de Mídias em Educação', 'Psicologia', 'Química', 'Relações Internacionais', 'Serviço Social', 'Sistemas de Informação', 'Teologia'))
);


DROP TABLE IF EXISTS funcionario CASCADE;

CREATE TABLE funcionario
(
	fk_cpf_pessoa char(11) NOT NULL,
	funcao varchar(20) NOT NULL,

	CONSTRAINT funcionario_cpf_pessoa_fk FOREIGN KEY (fk_cpf_pessoa) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT funcionario_ck_funcao CHECK (length(trim(funcao)) > 0)
);


DROP TABLE IF EXISTS voluntario CASCADE;

CREATE TABLE voluntario
(
	fk_cpf_pessoa char(11) NOT NULL,
	endereco endereco NOT NULL,
	matricula_puc char(7) NOT NULL,
	curso_puc varchar(80) NOT NULL,

	CONSTRAINT voluntario_cpf_pessoa_fk FOREIGN KEY (fk_cpf_pessoa) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT voluntario_ck_matricula_puc CHECK (length(trim(matricula_puc)) = 7),
	CONSTRAINT voluntario_ck_curso_puc CHECK (length(trim(curso_puc)) > 0)
);


DROP TABLE IF EXISTS atividade CASCADE;

CREATE TABLE atividade
(
	pk_id serial NOT NULL,
	nome varchar(50) NOT NULL,
	data date NOT NULL,

	CONSTRAINT atividade_pk PRIMARY KEY (pk_id),
	CONSTRAINT atividade_ck_nome CHECK (length(trim(nome)) > 0),
	CONSTRAINT atividade_ck_data CHECK (isfinite(data))
);


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


DROP TABLE IF EXISTS evento CASCADE;

CREATE TABLE evento
(
	fk_atividade_id serial NOT NULL,
	presencas integer NOT NULL,
	descricao varchar(200) NOT NULL,

	CONSTRAINT evento_pk PRIMARY KEY (fk_atividade_id),
	CONSTRAINT evento_atividade_id_fk FOREIGN KEY (fk_atividade_id) REFERENCES atividade(pk_id) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT evento_ck_presencas CHECK (presencas > 0),
	CONSTRAINT evento_ck_descricao CHECK (length(trim(descricao)) > 0)
);


DROP TABLE IF EXISTS instituicao CASCADE;

CREATE TABLE instituicao
(
	pk_nome varchar(200) NOT NULL,
	telefone varchar(16) NOT NULL,
	email varchar(60) NOT NULL,
	vinculo varchar(200) NOT NULL,

	CONSTRAINT instituicao_pk PRIMARY KEY (pk_nome),
	CONSTRAINT instituicao_ck_nome CHECK (length(trim(pk_nome)) > 0),
	CONSTRAINT instituicao_ck_email CHECK (length(trim(email)) > 0),
	CONSTRAINT instituicao_ck_telefone CHECK (length(trim(telefone)) > 0)
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
	pk_email varchar(60) NOT NULL,
	login varchar(120) NOT NULL,
	senha_hash varchar(128) NOT NULL,
	permissao smallint NOT NULL,

	CONSTRAINT usuario_pk PRIMARY KEY (pk_email),
	CONSTRAINT usuario_email_pessoa_fk FOREIGN KEY (pk_email) REFERENCES pessoa(email) ON UPDATE CASCADE ON DELETE CASCADE
);
