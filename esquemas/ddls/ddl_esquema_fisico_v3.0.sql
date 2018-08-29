/*
ESSE É O RASCUNHO DO DDL V3: TODAS AS TABEALS JA ESTAO EXPLICITADAS COM SEUS ATRIBUTOS, FALTA APENAS COLOAR EM LINGUAGEM SQL E ESCREVER AS RESTRICOES DE FK E PK.

juntei entidade pessoa, menor, aluno e voluntario em uma mesma tabela; isso some com tabelas aprendiz, menor e voluntario

coloquei um pk_matricula_neam em pessoa para servir como pk para nao precisarmos lidar com pks compostas

fusao de colunas de oriundo_de com pessoa (1:n); pk de instituicao deve estar presente na tabela pessoa

oriundo_de.escolaridade_nivel e oriundo_de.escolaridade_status juntados em escolaridade_nivel, que agora assume valores como "fundamental completo","fundamental incompleto", etc

tabela participa criada por relacionamento entre entidades ser (n:n)
tabela realiza criada por relacionamento entre entidades ser (n:n)
tabela faz criada por relacionamento entre entidades ser (n:n)
tabela cursa criada por relacionamento entre entidades ser (n:n)

fim dos comentarios */

DROP TYPE IF EXISTS tipo_pessoa CASCADE;

CREATE TYPE tipo_pessoa AS ENUM (
	'voluntario',
	'aprendiz',
	'aluno'
);

DROP TABLE IF EXISTS instituicao CASCADE;

CREATE TABLE instituicao
(
	pk_nome varchar(200) NOT NULL,
	contato_nome varchar(100),
	contato_telefone char(10),

	CONSTRAINT instituicao_pk PRIMARY KEY (pk_nome)
);

DROP TABLE IF EXISTS pessoa CASCADE;

CREATE TABLE pessoa
(
	nome varchar(100) NOT NULL,
	email varchar(50) UNIQUE,
	celular char(50),
	foto char(200),
	desligamento_data date,
	desligamento_motivo varchar(100),
	sexo char(1),	/* M, F ou O */
	data_nascimento date,
	identificador_tipo smallint NOT NULL,	/* certidao, rg ou cpf */
	identificador_numero varchar(32) NOT NULL,
	identificador_complemento char(2),
	endereco_numero smallint,
	endereco_rua varchar(100),
	endereco_complemento varchar(50),
	endereco_bairro varchar(20),
	endereco_cidade varchar(20),
	endereco_uf char(2),
	endereco_cep char(8),
	pk_matricula_neam serial NOT NULL,
	tipo tipo_pessoa NOT NULL,		/* voluntário, aprendiz ou aluno */
	nome_responsavel varchar(100) [] NOT NULL,
	telefone_responsavel char(10) [],
	profissao_responsavel varchar(50) [],
	curso_puc varchar(50),
	matricula_puc char(7) UNIQUE,
	dificuldade varchar(50) [],
	serie varchar(10),
	escolaridade_nivel varchar(30),
	escolaridade_turno varchar(10),
	nome_instituicao varchar(200),

	CONSTRAINT pessoa_pk PRIMARY KEY (pk_matricula_neam),
	CONSTRAINT nome_instituicao_fk FOREIGN KEY (nome_instituicao) REFERENCES instituicao(pk_nome) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS evento CASCADE;

CREATE TABLE evento
(
	pk_data date NOT NULL,
	pk_nome char(100) NOT NULL,
	descricao varchar(200),

	CONSTRAINT evento_pk PRIMARY KEY (pk_data, pk_nome)
);

DROP TABLE IF EXISTS participa CASCADE;

CREATE TABLE participa
(
	pk_matricula_neam_pessoa serial NOT NULL,
	pk_data_evento date NOT NULL,
	pk_nome_evento varchar(100) NOT NULL,

	CONSTRAINT participa_pk PRIMARY KEY (pk_matricula_neam_pessoa, pk_data_evento, pk_nome_evento),
	CONSTRAINT participa_pessoa_fk FOREIGN KEY (pk_matricula_neam_pessoa) REFERENCES pessoa(pk_matricula_neam) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT participa_evento_fk FOREIGN KEY (pk_data_evento, pk_nome_evento) REFERENCES evento(pk_data, pk_nome) ON UPDATE CASCADE ON DELETE CASCADE

);

DROP TABLE IF EXISTS trabalho CASCADE;

CREATE TABLE trabalho
(
	pk_local_puc varchar(50) NOT NULL,
	pk_funcao varchar(50) NOT NULL,

	CONSTRAINT trabalho_pk PRIMARY KEY (pk_local_puc, pk_funcao)
);


DROP TABLE IF EXISTS realiza CASCADE;

CREATE TABLE realiza
(
	pk_matricula_neam_pessoa serial NOT NULL,
	pk_local_puc_trabalho varchar(50) NOT NULL,
	pk_funcao_trabalho varchar(50) NOT NULL,
	data_ini date NOT NULL,
	data_fim date,

	CONSTRAINT realiza_pk PRIMARY KEY (pk_matricula_neam_pessoa, pk_local_puc_trabalho, pk_funcao_trabalho),
	CONSTRAINT realiza_pessoa_fk FOREIGN KEY (pk_matricula_neam_pessoa) REFERENCES pessoa(pk_matricula_neam) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT realiza_trabalho_fk FOREIGN KEY (pk_local_puc_trabalho, pk_funcao_trabalho) REFERENCES trabalho(pk_local_puc, pk_funcao) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS atividade_fora CASCADE;

CREATE TABLE atividade_fora 
(
	pk_atividade_nome varchar(100) NOT NULL,
	atividade_local varchar(100),

	CONSTRAINT atividade_fora_pk PRIMARY KEY (pk_atividade_nome)
);

DROP TABLE IF EXISTS faz CASCADE;

CREATE TABLE faz
(
	pk_matricula_neam_pessoa serial NOT NULL,
	pk_nome_atividade_fora varchar(100) NOT NULL,
	hora_ini time,
	hora_fim time,
	dia_semana varchar(15),
	frequencia char(4),

	CONSTRAINT faz_pk PRIMARY KEY (pk_matricula_neam_pessoa, pk_nome_atividade_fora),
	CONSTRAINT faz_pessoa_fk FOREIGN KEY (pk_matricula_neam_pessoa) REFERENCES pessoa(pk_matricula_neam) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT faz_atividade_fora_fk FOREIGN KEY (pk_nome_atividade_fora) REFERENCES atividade_fora(pk_atividade_nome) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS atividade_neam CASCADE;

CREATE TABLE atividade_neam
(
	pk_nome_atividade_neam varchar(100) NOT NULL,
	hora_ini time,

	CONSTRAINT atividade_neam_pk PRIMARY KEY (pk_nome_atividade_neam)
);

DROP TABLE IF EXISTS cursa CASCADE;

CREATE TABLE cursa
(
	pk_matricula_neam_pessoa serial NOT NULL,
	pk_nome_atividade_neam varchar(100) NOT NULL,
	nota real,
	data_ini date,
	data_fim date,

	CONSTRAINT cursa_pk PRIMARY KEY (pk_matricula_neam_pessoa),
	CONSTRAINT cursa_pessoa_fk FOREIGN KEY (pk_matricula_neam_pessoa) REFERENCES pessoa(pk_matricula_neam) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT cursa_atividade_neam_fk FOREIGN KEY (pk_nome_atividade_neam) REFERENCES atividade_neam(pk_nome_atividade_neam) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS aula_reforco CASCADE;

CREATE TABLE aula_reforco
(
	pk_materia varchar(20) NOT NULL,
	pk_matricula_neam_pessoa serial NOT NULL,
	pk_matricula_puc_pessoa char(7) UNIQUE NOT NULL,
	hora_ini time,
	data date,

	CONSTRAINT aula_reforco_pk PRIMARY KEY (pk_materia, pk_matricula_neam_pessoa, pk_matricula_puc_pessoa),
	CONSTRAINT aula_reforco_matricula_neam_fk FOREIGN KEY (pk_matricula_neam_pessoa) REFERENCES pessoa(pk_matricula_neam) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT aula_reforco_matricula_puc_fk FOREIGN KEY (pk_matricula_puc_pessoa) REFERENCES pessoa(matricula_puc) ON UPDATE CASCADE ON DELETE CASCADE
);


/* trigger  para conferir se atributos "escolaridade_nivel", "escolaridade_turno", "nome_responsavel", "telefone_resposnavel" e "profissao_resposnsavel" nao sao null quando o tipo==aprendiz ou aluno */
CREATE OR REPLACE FUNCTION verifica_requisitos_aprendiz_aluno() RETURNS trigger as $tg_requisitos_aprendiz_aluno$
	BEGIN

		IF (NEW.tipo == 'aprendiz' OR NEW.tipo == 'aluno') THEN
	
			IF NEW.escolaridade_nivel IS NULL OR NEW.escolaridade_turno IS NULL OR NEW.nome_responsavel IS NULL OR NEW.telefone_responsavel IS NULL OR NEW.profissao_responsavel IS NULL THEN
				RAISE EXCEPTION 'Um aprendiz ou aluno deve possuir os dados de escolaridade e do seu responsável completos.';
				RETURN NULL;
			END IF;
		END IF;

		RETURN NEW;
	END;
$tg_requisitos_aprendiz_aluno$ LANGUAGE plpgsql;

CREATE TRIGGER tg_requisitos_aprendiz_aluno BEFORE INSERT OR UPDATE ON pessoa FOR EACH ROW EXECUTE PROCEDURE verifica_requisitos_aprendiz_aluno();


/* trigger para conferir se atributos "matriula_puc" e "curso_puc" não sao null quando tipo==voluntario */
CREATE OR REPLACE FUNCTION verifica_requisitos_voluntario() RETURNS trigger as $tg_requisitos_voluntario$
	BEGIN

		IF (NEW.tipo == 'voluntario') THEN

			IF NEW.matriula_puc IS NULL OR NEW.curso_puc IS NULL THEN
				RAISE EXCEPTION 'Um voluntário deve possuir os dados de matrícula e curso na PUC.';
				RETURN NULL;
			END IF;
		END IF;

		RETURN NEW;
	END;
$tg_requisitos_voluntario$ LANGUAGE plpgsql;

CREATE TRIGGER tg_requisitos_voluntario BEFORE INSERT OR UPDATE ON pessoa FOR EACH ROW EXECUTE PROCEDURE verifica_requisitos_voluntario();

/* --------------------------------------------- USUARIO ---------------------------------------------- */

DROP TABLE IF EXISTS usuario CASCADE;

CREATE TABLE usuario
(
	usuario_id serial NOT NULL,
	email varchar(60) UNIQUE NOT NULL,
	senha_hash varchar(128) NOT NULL,
	permissao integer NOT NULL DEFAULT 0,
	
	CONSTRAINT usuario_pk PRIMARY KEY (email)
);