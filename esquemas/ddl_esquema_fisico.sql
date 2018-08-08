/*
	DDL do esquema físico

	Projeto: RESPUC-NEAM PUC-Rio

	Descrição:
	Cria no banco de dados as tabelas apresentadas como entidades no esquema conceitual.
*/

/* --------------------------------------------- TABELAS ---------------------------------------------- */

DROP TABLE IF EXISTS pessoa CASCADE;

CREATE TABLE pessoa
(
	pk_cpf char(11) NOT NULL,
	rg char(12) NOT NULL,
	naturalidade varchar(50) NOT NULL,
	email varchar(60) NOT NULL,
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
	fk_cpf char(11) NOT NULL,
	rua varchar(100) NOT NULL,
	numero varchar(20) NOT NULL,
	complemento varchar(50) NOT NULL,
	bairro varchar(20) NOT NULL,
	cidade varchar(20) NOT NULL,
	uf char(2) NOT NULL,
	cep char(8) NOT NULL,
	nome_responsavel varchar(200) NOT NULL,
	cpf_responsavel char(11) NOT NULL,
	telefone_responsavel varchar(200) NOT NULL,
	profissao_responsavel varchar(200) NOT NULL,

	CONSTRAINT aprendiz_aluno_cpf_fk FOREIGN KEY (fk_cpf) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT aprendiz_aluno_ck_rua CHECK (length(trim(rua)) > 0),
	CONSTRAINT aprendiz_aluno_ck_complemento CHECK (length(trim(complemento)) > 0),
	CONSTRAINT aprendiz_aluno_ck_bairro CHECK (length(trim(bairro)) > 0),
	CONSTRAINT aprendiz_aluno_ck_cidade CHECK (length(trim(cidade)) > 0),
	CONSTRAINT aprendiz_aluno_ck_cep CHECK (length(trim(cep)) = 8),
	CONSTRAINT aprendiz_aluno_ck_uf CHECK (length(trim(uf)) = 2)
);


DROP TABLE IF EXISTS aprendiz CASCADE;

CREATE TABLE aprendiz
(
	fk_cpf char(11) NOT NULL,
	trabalho varchar(20) NOT NULL,

	CONSTRAINT aprendiz_cpf_fk FOREIGN KEY (fk_cpf) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT aprendiz_ck_trabalho CHECK (length(trim(trabalho)) > 0)
);


DROP TABLE IF EXISTS aluno CASCADE;

CREATE TABLE aluno
(
	fk_cpf char(11) NOT NULL,
	curso varchar(80) NOT NULL,
	nome_dificuldade varchar(80) [],
	apoio_dificuldade boolean [],

	CONSTRAINT aluno_cpf_fk FOREIGN KEY (fk_cpf) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT aluno_ck_curso CHECK (curso IN ('Administração', 'Arquitetura e Urbanismo', 'Artes Cênicas', 'Ciência da Computação', 'Ciências Biológicas', 'Ciências Econômicas', 'Ciências Sociais', 'Comunicação Social - Cinema', 'Comunicação Social - Jornalismo', 'Comunicação Social - Publicidade e Propaganda', 'Design - Comunicação Visual', 'Design - Mídia Digital', 'Design - Moda', 'Design - Projeto de Produto', 'Direito', 'Engenharia Ambiental', 'Engenharia Civil', 'Engenharia da Computação', 'Engenharia de Controle e Automação', 'Engenharia Elétrica', 'Engenharia Mecânica', 'Engenharia de Materiais e Nanotecnologia', 'Engenharia de Petróleo', 'Engenharia de Produção', 'Engenharia Química', 'Filosofia', 'Física', 'Geografia', 'História', 'Letras', 'Matemática', 'Pedagogia','Produção e Gestão de Mídias em Educação', 'Psicologia', 'Química', 'Relações Internacionais', 'Serviço Social', 'Sistemas de Informação', 'Teologia'))
);


DROP TABLE IF EXISTS funcionario CASCADE;

CREATE TABLE funcionario
(
	fk_cpf char(11) NOT NULL,
	funcao varchar(200) NOT NULL,

	CONSTRAINT funcionario_cpf_fk FOREIGN KEY (fk_cpf) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS voluntario CASCADE;

CREATE TABLE voluntario
(
	fk_cpf char(11) NOT NULL,
	rua varchar(100) NOT NULL,
	numero varchar(20) NOT NULL,
	complemento varchar(50) NOT NULL,
	bairro varchar(20) NOT NULL,
	cidade varchar(20) NOT NULL,
	uf char(2) NOT NULL,
	cep char(8) NOT NULL,
	matricula_puc char(7) NOT NULL,
	curso_puc varchar(80) NOT NULL,

	CONSTRAINT voluntario_cpf_fk FOREIGN KEY (fk_cpf) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS evento CASCADE;

CREATE TABLE evento
(
	pk_nome varchar(20) NOT NULL,
	pk_data date NOT NULL,
	pk_presencas integer NOT NULL,
	pk_descricao varchar(200) NOT NULL,

	CONSTRAINT evento_pk PRIMARY KEY (pk_nome, pk_data, pk_presencas, pk_descricao),
	CONSTRAINT evento_ck_nome CHECK (length(trim(pk_nome)) > 0),
	CONSTRAINT evento_ck_presencas CHECK (pk_presencas > 0),
	CONSTRAINT evento_ck_data CHECK (isfinite(pk_data)),
	CONSTRAINT evento_ck_descricao CHECK (length(trim(pk_descricao)) > 0)
);


DROP TABLE IF EXISTS escola CASCADE;

CREATE TABLE escola
(
	pk_nome varchar(150) NOT NULL,
	telefone varchar(20),

	CONSTRAINT escola_pk PRIMARY KEY (pk_nome),
	CONSTRAINT escola_ck_telefone CHECK (CAST(telefone AS bigint) > 0)
);


DROP TABLE IF EXISTS atividade CASCADE;

CREATE TABLE atividade
(
	pk_nome varchar(50) NOT NULL,
	data date NOT NULL,

	CONSTRAINT atividade_pk PRIMARY KEY (pk_nome),
	CONSTRAINT atividade_ck_nome CHECK (length(trim(pk_nome)) > 0),
	CONSTRAINT atividade_ck_data CHECK (isfinite(data))
);


DROP TABLE IF EXISTS projeto CASCADE;

CREATE TABLE projeto
(
	fk_atividade varchar(50) NOT NULL,
	id_projeto integer NOT NULL,
	presenca integer NOT NULL,

	CONSTRAINT projeto_pk PRIMARY KEY (fk_atividade),
	CONSTRAINT projeto_atividade_fk FOREIGN KEY (fk_atividade) REFERENCES atividade(pk_nome) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS estagio CASCADE;

CREATE TABLE estagio
(
	fk_atividade varchar(50) NOT NULL,
	conteudo varchar(200) NOT NULL,

	CONSTRAINT estagio_pk PRIMARY KEY (fk_atividade),
	CONSTRAINT estagio_atividade_fk FOREIGN KEY (fk_atividade) REFERENCES atividade(pk_nome) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT estagio_ck_conteudo CHECK (length(trim(conteudo)) > 0)
);


DROP TABLE IF EXISTS aula CASCADE;

CREATE TABLE aula
(
	fk_atividade varchar(50) NOT NULL,
	id_projeto integer NOT NULL,
	presenca integer NOT NULL,

	CONSTRAINT aula_pk PRIMARY KEY (fk_atividade),
	CONSTRAINT aula_atividade_fk FOREIGN KEY (fk_atividade) REFERENCES atividade(pk_nome) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS instituicao CASCADE;

CREATE TABLE instituicao
(
	nome varchar(1024) NOT NULL,
	telefone varchar(16) NOT NULL,
	celular varchar(16) NOT NULL,
	email varchar(1024) NOT NULL,
	vinculo varchar(1024) NOT NULL,
	nome_responsavel varchar(1024) NOT NULL,
	email_responsavel char(1024) NOT NULL,
	telefone_responsavel varchar(16) NOT NULL,

	CONSTRAINT instituicao_pk PRIMARY KEY (nome)
);


DROP TABLE IF EXISTS aluno_aprendiz_atividade CASCADE;

CREATE TABLE aluno_aprendiz_atividade
(
	cpf char(11) NOT NULL,
	atividade varchar(50) NOT NULL,

	CONSTRAINT aluno_aprendiz_atividade_pk PRIMARY KEY (cpf, atividade),
	CONSTRAINT aluno_aprendiz_atividade_cpf_fk FOREIGN KEY (cpf) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT aluno_aprendiz_atividade_atividade_fk FOREIGN KEY (atividade) REFERENCES atividade(pk_nome) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS pessoa_evento CASCADE;

CREATE TABLE pessoa_evento
(
	fk_cpf char(11) NOT NULL,
	fk_nome varchar(20) NOT NULL,
	fk_data date NOT NULL,
	fk_presencas integer NOT NULL,
	fk_descricao varchar(200) NOT NULL,

	CONSTRAINT pessoa_evento_pk PRIMARY KEY (fk_cpf, fk_nome, fk_data, fk_presencas, fk_descricao),
	CONSTRAINT pessoa_evento_cpf_fk FOREIGN KEY (fk_cpf) REFERENCES pessoa(pk_cpf) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT pessoa_evento_nome_data_presencas_descricao_fk FOREIGN KEY (fk_nome, fk_data, fk_presencas, fk_descricao) REFERENCES evento(pk_nome, pk_data, pk_presencas, pk_descricao) ON UPDATE CASCADE ON DELETE CASCADE
);


/* --------------------------------------------- USUARIO ---------------------------------------------- */

DROP TABLE IF EXISTS usuario CASCADE;

CREATE TABLE usuario
(
	email varchar(60) NOT NULL,
	login varchar(120) NOT NULL,
	senha_hash varchar(128) NOT NULL,
	tipo integer NOT NULL,
	permissao varchar(60) [] NOT NULL,

	CONSTRAINT usuario_pk PRIMARY KEY (email)
);
