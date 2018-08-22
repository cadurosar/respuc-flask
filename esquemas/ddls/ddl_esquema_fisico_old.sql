/*
	DDL antigo do esquema físico

	Projeto: RESPUC-NEAM PUC-Rio

	Descrição:
	Cria no banco de dados tabelas baseadas no DDL antigo já implementado.
*/

/* --------------------------------------------- TABELAS ---------------------------------------------- */

/*
 *  - Garante que os campos Nome, Rua, Email, Naturalidade, CEP, Rua, Bairro, Cidade, Complemento e Trabalho não recebam apenas espaços em branco.
 *  - No caso do CEP, checa-se se o comprimento da string é igual a 8.
 *  - No caso da UF, checa-se se o comprimento da string é igual a 2.
 */
DROP TABLE IF EXISTS aprendiz CASCADE;

CREATE TABLE aprendiz
(
	cpf char(11) NOT NULL,
	rg char(12) NOT NULL,
	naturalidade varchar(50) NOT NULL,
	email varchar(60) NOT NULL,
	nome varchar(70) NOT NULL,
	data_nascimento date NOT NULL,
	telefone varchar(200) NOT NULL,
	celular varchar(200) NOT NULL,
	rua varchar(100) NOT NULL,
	numero varchar(20) NOT NULL,
	complemento varchar(50) NOT NULL,
	bairro varchar(20) NOT NULL,
	cidade varchar(20) NOT NULL,
	uf char(2) NOT NULL,
	cep char(8) NOT NULL,
	trabalho varchar(20) NOT NULL,
	nome_responsavel varchar(200) NOT NULL,
	cpf_responsavel char(11) NOT NULL,
	telefone_responsavel varchar(200) NOT NULL,
	profissao_responsavel varchar(200) NOT NULL,

	CONSTRAINT aprendiz_pk PRIMARY KEY (cpf),
	CONSTRAINT aprendiz_ck_naturalidade CHECK (length(trim(naturalidade)) > 0),
	CONSTRAINT aprendiz_ck_email CHECK (length(trim(email)) > 0),
	CONSTRAINT aprendiz_ck_nome CHECK (length(trim(nome)) > 0),
	CONSTRAINT aprendiz_ck_rua CHECK (length(trim(rua)) > 0),
	CONSTRAINT aprendiz_ck_complemento CHECK (length(trim(complemento)) > 0),
	CONSTRAINT aprendiz_ck_bairro CHECK (length(trim(bairro)) > 0),
	CONSTRAINT aprendiz_ck_cidade CHECK (length(trim(cidade)) > 0),
	CONSTRAINT aprendiz_ck_cep CHECK (length(trim(cep)) = 8),
	CONSTRAINT aprendiz_ck_uf CHECK (length(trim(uf)) = 2),
	CONSTRAINT aprendiz_ck_trabalho CHECK (length(trim(trabalho)) > 0)
);

/*
 *  - Garante que os campos Nome, Rua, Email, Naturalidade, CEP, Rua, Bairro, Cidade e Complemento não recebam apenas espaços em branco.
 *  - No caso do CEP, checa-se se o comprimento da string é igual a 8.
 *  - No caso da UF, checa-se se o comprimento da string é igual a 2.
 */
DROP TABLE IF EXISTS aluno CASCADE;

CREATE TABLE aluno
(
	cpf char(11) NOT NULL,
	rg char(12) NOT NULL,
	naturalidade varchar(50) NOT NULL,
	email varchar(60) NOT NULL,
	nome varchar(70) NOT NULL,
	data_nascimento date NOT NULL,
	telefone varchar(200) NOT NULL,
	celular varchar(200) NOT NULL,
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

	CONSTRAINT aluno_pk PRIMARY KEY (cpf),
	CONSTRAINT aluno_ck_naturalidade CHECK (length(trim(naturalidade)) > 0),
	CONSTRAINT aluno_ck_email CHECK (length(trim(email)) > 0),
	CONSTRAINT aluno_ck_nome CHECK (length(trim(nome)) > 0),
	CONSTRAINT aluno_ck_rua CHECK (length(trim(rua)) > 0),
	CONSTRAINT aluno_ck_complemento CHECK (length(trim(complemento)) > 0),
	CONSTRAINT aluno_ck_bairro CHECK (length(trim(bairro)) > 0),
	CONSTRAINT aluno_ck_cidade CHECK (length(trim(cidade)) > 0),
	CONSTRAINT aluno_ck_cep CHECK (length(trim(cep)) = 8)
);

/*
 *  - Garante que o campo Nome não receba uma string composta de apenas espaços em branco.
 *  - Garante que o número de presenças é positivo, se essa informação for definida.
 *  - Garante que a data do evento é uma data passada.
 *  - Garante que o campo Descrição não receba uma string composta de apenas espaços em branco.
 */
DROP TABLE IF EXISTS evento CASCADE;

CREATE TABLE evento
(
	nome varchar(20) NOT NULL,
	presencas integer,
	data date NOT NULL,
	descricao varchar(200),

	CONSTRAINT evento_pk PRIMARY KEY (nome, data),
	CONSTRAINT evento_ck_nome CHECK (length(trim(nome)) > 0),
	CONSTRAINT evento_ck_presencas CHECK (presencas > 0),
	CONSTRAINT evento_ck_data CHECK (isfinite(data)),
	CONSTRAINT evento_ck_descricao CHECK ((descricao IS NULL) OR (length(trim(descricao)) > 0))
);

/*
 *  - Garante que o valor recebido para CPF não é negativo ou zero.
 *  - Garante que o campo Matéria não receba uma string composta de apenas espaços em branco.
 */
DROP TABLE IF EXISTS dificuldade CASCADE;

CREATE TABLE dificuldade
(
	materia varchar(20) NOT NULL,
	cpf char(11) NOT NULL,

	CONSTRAINT dificuldade_pk PRIMARY KEY (cpf, materia),
	CONSTRAINT dificuldade_ck_cpf CHECK (CAST(cpf AS bigint) > 0),
	CONSTRAINT dificuldade_materia CHECK (length(trim(materia)) > 0)
);

/*
 *  - Garante que o valor recebido para CPF não é negativo ou zero.
 *  - Garante que o campo Matéria não receba uma string composta de apenas espaços em branco.
 */
DROP TABLE IF EXISTS apoio CASCADE;

CREATE TABLE apoio
(
	materia varchar(20) NOT NULL,
	cpf char(11) NOT NULL,

	CONSTRAINT apoio_pk PRIMARY KEY (cpf, materia),
	CONSTRAINT apoio_ck_cpf CHECK (CAST(cpf AS bigint) > 0),
	CONSTRAINT apoio_materia CHECK (length(trim(materia)) > 0)
);

/*
 *  - Garante que o campo Telefone não receba uma string composta de apenas zeros.
 */
DROP TABLE IF EXISTS escola CASCADE;

CREATE TABLE escola
(
	nome varchar(150) NOT NULL,
	telefone varchar(20) NOT NULL,

	CONSTRAINT escola_pk PRIMARY KEY (nome, telefone),
	CONSTRAINT escola_ck_telefone CHECK (CAST(telefone AS bigint) > 0)
);

/*
 */
DROP TABLE IF EXISTS voluntario CASCADE;

CREATE TABLE voluntario
(
	cpf char(11) NOT NULL,
	rg char(12) NOT NULL,
	naturalidade varchar(50) NOT NULL,
	email varchar(60) NOT NULL,
	nome varchar(70) NOT NULL,
	data_nascimento date NOT NULL,
	telefone varchar(200) NOT NULL,
	celular varchar(200) NOT NULL,
	rua varchar(100) NOT NULL,
	numero varchar(20) NOT NULL,
	complemento varchar(50) NOT NULL,
	bairro varchar(20) NOT NULL,
	cidade varchar(20) NOT NULL,
	uf char(2) NOT NULL,
	cep char(8) NOT NULL,
	matricula char(7) CONSTRAINT voluntario_pk PRIMARY KEY
);

/*
 *  - Garante que a quantidade de alunos que cursam é positivo.
 *  - Garante que o nome do curso corresponde com os nomes dos cursos oferecidos na PUC-Rio.
 */
DROP TABLE IF EXISTS curso CASCADE;

CREATE TABLE curso
(
	nome varchar(80) NOT NULL,
	coord varchar(50) NOT NULL,
	depto varchar(30) NOT NULL,
	qtd_alunos integer NOT NULL,

	CONSTRAINT curso_pk PRIMARY KEY (nome),
	CONSTRAINT curso_ck_nome CHECK (nome IN ('Administração', 'Arquitetura e Urbanismo', 'Artes Cênicas', 'Ciência da Computação', 'Ciências Biológicas', 'Ciências Econômicas', 'Ciências Sociais', 'Comunicação Social - Cinema', 'Comunicação Social - Jornalismo', 'Comunicação Social - Publicidade e Propaganda', 'Design - Comunicação Visual', 'Design - Mídia Digital', 'Design - Moda', 'Design - Projeto de Produto', 'Direito', 'Engenharia Ambiental', 'Engenharia Civil', 'Engenharia da Computação', 'Engenharia de Controle e Automação', 'Engenharia Elétrica', 'Engenharia Mecânica', 'Engenharia de Materiais e Nanotecnologia', 'Engenharia de Petróleo', 'Engenharia de Produção', 'Engenharia Química', 'Filosofia', 'Física', 'Geografia', 'História', 'Letras', 'Matemática', 'Pedagogia','Produção e Gestão de Mídias em Educação', 'Psicologia', 'Química', 'Relações Internacionais', 'Serviço Social', 'Sistemas de Informação', 'Teologia')),
	CONSTRAINT curso_ck_qtd_alunos CHECK (qtd_alunos > 0)
);

/*
 *  - Garante que o número do CPF é positivo.
 *  - Garante que o campo Estágio não receba uma string composta de apenas espaços em branco.
 */
DROP TABLE IF EXISTS estagio CASCADE;

CREATE TABLE estagio
(
	cpf char(11) NOT NULL,
	estagio varchar(50) NOT NULL,

	CONSTRAINT estagio_pk PRIMARY KEY (cpf, estagio),
	CONSTRAINT estagio_ck_cpf CHECK (CAST(cpf AS bigint) > 0),
	CONSTRAINT estagio_ck_estagio CHECK (length(trim(estagio)) > 0)
);

/*
 *  - Garante que o número do CPF é positivo.
 *  - Garante que o campo Trabalho não receba uma string composta de apenas espaços em branco.
 */
DROP TABLE IF EXISTS trabalho CASCADE;

CREATE TABLE trabalho
(
	cpf char(11) NOT NULL,
	trabalho varchar(50) NOT NULL,

	CONSTRAINT trabalho_pk PRIMARY KEY (cpf, trabalho),
	CONSTRAINT trabalho_ck_cpf CHECK (CAST(cpf AS bigint) > 0),
	CONSTRAINT trabalho_ck_trabalho CHECK (length(trim(trabalho)) > 0)
);

/*
 *  - Garante que o número do CPFF é positivo.
 *  - Garante que o campo Trabalho não receba uma string composta de apenas espaços em branco.
 */
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

/*
 *  - Garante que o campo Nome não receba uma string composta de apenas espaços em branco.
 */
DROP TABLE IF EXISTS atividade CASCADE;

CREATE TABLE atividade
(
	nome varchar(50) NOT NULL,

	CONSTRAINT atividade_pk PRIMARY KEY (nome),
	CONSTRAINT atividade_ck_nome CHECK (length(trim(nome)) > 0)
);

/*
 *  - Garante que os campos Naturalidade, Email e Nome não recebam uma string composta de apenas espaços em branco.
 */
DROP TABLE IF EXISTS funcionario CASCADE;

CREATE TABLE funcionario
(
	cpf char(11) NOT NULL,
	rg char(12) NOT NULL,
	naturalidade varchar(50) NOT NULL,
	email varchar(60) NOT NULL,
	nome varchar(70) NOT NULL,
	data_nascimento date NOT NULL,
	telefone varchar(200) NOT NULL,
	celular varchar(200) NOT NULL,
	funcao varchar(200) NOT NULL,

	CONSTRAINT funcionario_pk PRIMARY KEY (cpf),
	CONSTRAINT funcionario_ck_naturalidade CHECK (length(trim(Naturalidade)) > 0),
	CONSTRAINT funcionario_ck_email CHECK (length(trim(Email)) > 0),
	CONSTRAINT funcionario_ck_nome CHECK (length(trim(Nome)) > 0)
);

/*
 *  - Garante que o CPF corresponde ao CPF de um aluno.
 *  - Garante que o nome da atividade corresponde a uma atividade cadastrada.
 */
DROP TABLE IF EXISTS aluno_atividade CASCADE;

CREATE TABLE aluno_atividade
(
	cpf char(11) NOT NULL,
	atividade varchar(50) NOT NULL,
	CONSTRAINT aluno_atividade_pk PRIMARY KEY (cpf, atividade),
	CONSTRAINT aluno_atividade_cpf_fk FOREIGN KEY (cpf) REFERENCES aluno(cpf) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT aluno_atividade_atividade_fk FOREIGN KEY (atividade) REFERENCES atividade(nome) ON UPDATE CASCADE ON DELETE CASCADE
);

/*
 *  - Garante que o CPF corresponde ao CPF de um aprendiz.
 *  - Garante que o nome da atividade corresponde a uma atividade cadastrada.
 */
DROP TABLE IF EXISTS aprendiz_atividade CASCADE;

CREATE TABLE aprendiz_atividade
(
	cpf char(11) NOT NULL,
	atividade varchar(50) NOT NULL,
	CONSTRAINT aprendiz_atividade_pk PRIMARY KEY (cpf, atividade),
	CONSTRAINT aprendiz_atividade_cpf_fk FOREIGN KEY (cpf) REFERENCES aprendiz(cpf) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT aprendiz_atividade_atividade_fk FOREIGN KEY (atividade) REFERENCES atividade(nome) ON UPDATE CASCADE ON DELETE CASCADE
);

/* ---------------------------------------------- VISÕES ---------------------------------------------- */

CREATE OR REPLACE VIEW alunos_e_aprendizes AS
(
	SELECT
		subquery.cpf,
		subquery.nome,
		subquery.tipo
	FROM
		(SELECT
			aluno.cpf,
			aluno.nome,
			'aluno' AS tipo
		FROM aluno
		UNION ALL
		SELECT
			aprendiz.cpf,
			aprendiz.nome
			'aprendiz' AS tipo
		FROM aprendiz) AS subquery
	ORDER BY subquery.nome, subquery.tipo, subquery.cpf
);

CREATE OR REPLACE VIEW cpf_atividade AS
(
	SELECT
		subquery.atividade,
		subquery.cpf,
		subquery.tipo
	FROM
		(SELECT
			aluno_atividade.cpf,
			aluno_atividade.atividade,
			'aluno' AS tipo
		FROM aluno_atividade
		UNION ALL
		SELECT
			aprendiz_atividade.cpf,
			aprendiz_atividade.atividade
			'aprendiz' AS tipo
		FROM aprendiz_atividade) AS subquery
	ORDER BY subquery.atividade, subquery.cpf, subquery.tipo
);

CREATE OR REPLACE VIEW pessoa_atividade AS
(
	SELECT
		alunos_e_aprendizes.cpf,
		alunos_e_aprendizes.tipo,
		alunos_e_aprendizes.nome,
		cpf_atividade.atividade
	FROM
		alunos_e_aprendizes
	NATURAL JOIN
		cpf_atividade
);

/* --------------------------------------------- FUNÇÕES ---------------------------------------------- */

/*

CREATE OR REPLACE FUNCTION remove_acento(text)
RETURNS text AS
$BODY$
SELECT TRANSLATE($1,'áàãâäÁÀÃÂÄéèêëÉÈÊËíìîïÍÌÎÏóòõôöÓÒÕÔÖúùûüÚÙÛÜñÑçÇÿýÝ','aaaaaAAAAAeeeeEEEEiiiiIIIIoooooOOOOOuuuuUUUUnNcCyyY')
$BODY$
LANGUAGE sql IMMUTABLE STRICT
COST 100;
ALTER FUNCTION remove_acento(text)
OWNER TO app;
COMMENT ON FUNCTION remove_acento(text) IS 'Remove letras com acentuação';

*/
