/*
	DDL do esquema físico

	Projeto: RESPUC-NEAM PUC-Rio

	Descrição:
	Cria no banco de dados as tabelas apresentadas como entidades no esquema conceitual versão 5.
*/

/* --------------------------------------------- TABELAS ---------------------------------------------- */

/* COMO INSERIR EM PESSOA:
EX: insert into pessoa values ('111111111111', 'detran', (to_date('2017-09-01', 'YYYY-MM-DD')), 'Joao', 1, (to_date('1999-09-01', 'YYYY-MM-DD')), 'joao@gmail.com', '12345678', ('rua a', 'numero 2', 'casa 1', 'barra', 'RJ', 'RJ', '12345678'), null, null)
*/

DROP TABLE IF EXISTS pessoa CASCADE;

CREATE TABLE pessoa
(
	rg_numero char(12) NOT NULL,
	rg_orgao_expedidor char(20) NOT NULL,
	rg_data_expedicao date NOT NULL,
	nome char(80) NOT NULL,
	sexo smallint,
	data_nascimento date,
	email char(60),
	celular char(16),
	rua char(100),
	numero char(20),
	complemento char(50),
	bairro char(20),
	cidade char(20),
	uf char(2),
	cep char(8),
	foto char(200),
	data_desligamento date,

	CONSTRAINT pessoa_pk PRIMARY KEY (rg_numero, rg_orgao_expedidor, rg_data_expedicao)
);


/* ----------- */

DROP TABLE IF EXISTS instituicao CASCADE;

CREATE TABLE instituicao
(
	nome char(200) NOT NULL,
	contato_telefone char(16),
	contato_nome char(200),

	CONSTRAINT instituicao_pk PRIMARY KEY (nome)
);

/* ----------- */

DROP TABLE IF EXISTS aprendiz_aluno CASCADE;

CREATE TABLE aprendiz_aluno
(
	rg_numero_pessoa char(12) NOT NULL,
	rg_orgao_expedidor_pessoa char(20) NOT NULL,
	rg_data_expedicao_pessoa date NOT NULL,
	nome_responsavel char(80),
	telefone_responsavel char(16),
	profissao_responsavel char(60),
	nome_instituicao char(200) NOT NULL,
	serie char(10),
	nivel_escolaridade char(15),
	status_escolaridade char(10),
	turno char(5),
	local_destino char(200),
	descricao_destino char(200),
	data_destino date,


	CONSTRAINT aprendiz_aluno_pk PRIMARY KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa, nome_responsavel, nome_instituicao),
	CONSTRAINT aprendiz_aluno_pessoa FOREIGN KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa) REFERENCES pessoa(rg_numero, rg_orgao_expedidor, rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT aprendiz_aluno_instituicao FOREIGN KEY (nome_instituicao) REFERENCES instituicao(nome) ON UPDATE CASCADE ON DELETE CASCADE
);

/* ----------- */

DROP TABLE IF EXISTS voluntario CASCADE;

CREATE TABLE voluntario
(
	rg_numero_pessoa char(12) NOT NULL,
	rg_orgao_expedidor_pessoa char(20) NOT NULL,
	rg_data_expedicao_pessoa date NOT NULL,
	matricula_puc char(7) NOT NULL,
	curso_puc char(80) NOT NULL,

	CONSTRAINT voluntario_pk PRIMARY KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa),
	CONSTRAINT voluntario_fk FOREIGN KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa) REFERENCES pessoa(rg_numero, rg_orgao_expedidor, rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT voluntario_ck_curso CHECK (curso_puc IN ('Administração', 'Arquitetura e Urbanismo', 'Artes Cênicas', 'Ciência da Computação', 'Ciências Biológicas', 'Ciências Econômicas', 'Ciências Sociais', 'Comunicação Social - Cinema', 'Comunicação Social - Jornalismo', 'Comunicação Social - Publicidade e Propaganda', 'Design - Comunicação Visual', 'Design - Mídia Digital', 'Design - Moda', 'Design - Projeto de Produto', 'Direito', 'Engenharia Ambiental', 'Engenharia Civil', 'Engenharia da Computação', 'Engenharia de Controle e Automação', 'Engenharia Elétrica', 'Engenharia Mecânica', 'Engenharia de Materiais e Nanotecnologia', 'Engenharia de Petróleo', 'Engenharia de Produção', 'Engenharia Química', 'Filosofia', 'Física', 'Geografia', 'História', 'Letras', 'Matemática', 'Pedagogia','Produção e Gestão de Mídias em Educação', 'Psicologia', 'Química', 'Relações Internacionais', 'Serviço Social', 'Sistemas de Informação', 'Teologia'))
);

/* ----------- */

DROP TABLE IF EXISTS aluno CASCADE;

CREATE TABLE aluno
(
	rg_numero_pessoa char(12) NOT NULL,
	rg_orgao_expedidor_pessoa char(20) NOT NULL,
	rg_data_expedicao_pessoa date NOT NULL,
	dificuldade char(50) [] ,

	CONSTRAINT aluno_pk PRIMARY KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa),
	CONSTRAINT aluno_fk FOREIGN KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa) REFERENCES pessoa(rg_numero, rg_orgao_expedidor, rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE
);

/* ----------- */

DROP TABLE IF EXISTS atividade_fora CASCADE;

CREATE TABLE atividade_fora
(
	dia date NOT NULL,
	horario time NOT NULL,
	descricao char(200) NOT NULL,

	CONSTRAINT atividade_fora_pk PRIMARY KEY (dia, horario, descricao)
);

/* ----------- */

DROP TABLE IF EXISTS evento CASCADE;

CREATE TABLE evento
(
	nome char(200) NOT NULL,
	data date NOT NULL,
	descricao char(200),

	CONSTRAINT evento_pk PRIMARY KEY (nome, data)
);

/* ----------- */

DROP TABLE IF EXISTS conjunto_de_aulas CASCADE;

CREATE TABLE conjunto_de_aulas
(
	materia char(100) NOT NULL,
	horario time NOT NULL,
	matricula_puc char(7) NOT NULL,
	curso_puc char(80),
	data_ini date,
	data_fim date,

	CONSTRAINT conjunto_de_aulas_pk PRIMARY KEY(materia, horario)
);


/* ----------- */

DROP TABLE IF EXISTS realiza CASCADE;

CREATE TABLE realiza
(
	rg_numero_pessoa char(12) NOT NULL,
	rg_orgao_expedidor_pessoa char(20) NOT NULL,
	rg_data_expedicao_pessoa date NOT NULL,
	local char(200) NOT NULL,
	descricao char(200) NOT NULL,
	data_ini date,
	data_fim date,

	CONSTRAINT realiza_pk PRIMARY KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa, local, descricao),
	CONSTRAINT realiza_pessoa_fk FOREIGN KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa) REFERENCES pessoa(rg_numero, rg_orgao_expedidor, rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE
);


/* ----------- */

DROP TABLE IF EXISTS cursa CASCADE;

CREATE TABLE cursa
(
	rg_numero_pessoa char(12) NOT NULL,
	rg_orgao_expedidor_pessoa char(20) NOT NULL,
	rg_data_expedicao_pessoa date NOT NULL,
	materia char(200),
	horario time,
	data_ini date,
	data_fim date,

	CONSTRAINT cursa_pk PRIMARY KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa, materia, horario),
	CONSTRAINT cursa_pessoa_fk FOREIGN KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa) REFERENCES pessoa(rg_numero, rg_orgao_expedidor, rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT cursa_conjunto_de_aulas_fk FOREIGN KEY (materia, horario) REFERENCES conjunto_de_aulas(materia, horario) ON UPDATE CASCADE ON DELETE CASCADE
);


/* ----------- */

DROP TABLE IF EXISTS participa CASCADE;

CREATE TABLE participa
(
	rg_numero_pessoa char(12) NOT NULL,
	rg_orgao_expedidor_pessoa char(20) NOT NULL,
	rg_data_expedicao_pessoa date NOT NULL,
	evento_nome char(200),
	evento_data date,

	CONSTRAINT participa_pk PRIMARY KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa, evento_nome, evento_data),
	CONSTRAINT participa_rg_pessoa_fk FOREIGN KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa) REFERENCES pessoa(rg_numero, rg_orgao_expedidor, rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT participa_evento_fk FOREIGN KEY (evento_nome, evento_data) REFERENCES evento(nome, data) ON UPDATE CASCADE ON DELETE CASCADE
);

/* ----------- */

DROP TABLE IF EXISTS aluno_faz_atividade_fora CASCADE;

CREATE TABLE aluno_faz_atividade_fora
(
	rg_numero_pessoa char(12) NOT NULL,
	rg_orgao_expedidor_pessoa char(20) NOT NULL,
	rg_data_expedicao_pessoa date NOT NULL,
	dia_atividade date,
	horario_atividade time,
	descricao_atividade char(200),

	CONSTRAINT aluno_faz_atividade_fora_pk PRIMARY KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa, dia_atividade, horario_atividade, descricao_atividade),
	CONSTRAINT aluno_faz_atividade_fora_fk1 FOREIGN KEY (rg_numero_pessoa, rg_orgao_expedidor_pessoa, rg_data_expedicao_pessoa) REFERENCES pessoa(rg_numero, rg_orgao_expedidor, rg_data_expedicao) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT aluno_faz_atividade_fora_fk2 FOREIGN KEY (dia_atividade, horario_atividade, descricao_atividade) REFERENCES atividade_fora(dia, horario, descricao) ON UPDATE CASCADE ON DELETE CASCADE
);

/* --------------------------------------------- USUARIO ---------------------------------------------- */

DROP TABLE IF EXISTS usuario CASCADE;

CREATE TABLE usuario
(
	usuario_id serial NOT NULL,
	email char(60) UNIQUE NOT NULL,
	senha_hash char(128) NOT NULL,
	permissao smallint NOT NULL DEFAULT 0,

	CONSTRAINT usuario_pk PRIMARY KEY (usuario_id, email)
);