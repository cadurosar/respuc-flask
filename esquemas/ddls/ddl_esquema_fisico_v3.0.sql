//juntei entidade pessoa, menor, aluno e voluntario em uma mesma tabela; isso some com tabelas aprendiz, menor e voluntario
//coloquei um pk_matricula_neam em pessoa para servir como pk para nao precisarmos lidar com pks compostas
//fusao de colunas de oriundo de com pessoa (1:n)
//oriundo_de.escolaridade_nivel e oriundo_de.escolaridade_status juntados em escolaridade_nivel, que agora assume valores como "fundamental completo","fundamental incompleto", etc

pessoa:
nome
email
celular
foto
desligamento_data
desigamento_motivo
sexo
data_nascimento
identificador_tipo
identificador_numero
identificador_complemento
endereco_numero
endereco_rua
endereco_complemento
endereco_bairro
endereco_cep
endereco_uf
endereco_cidade
pk_matricula_neam

tipo (voluntario aprendiz ou aluno)

nome_responsavel
telefone_resposnavel
profissao_resposnsavel

curso_puc //pdoe ser null
matriula_puc //unique e pode ser null

dificudladess []
serie
escolaridade_nivel
escolaridade_turno

participa:
fk_matricula_neam_pessoa
fk_data_evento
fk_nome_evento


evento:
pk_data
pk_nome
descricao


trabalho:
pk_local_puc
pk_funcao


realiza:
fk_matricula_neam
fk_local_puc_trabalho
fk_funcao_trabalho
data_ini
data_fim


instituicao:
pk_nome
contato_nome
contato_telefone


atividade fora:
pk_atividade_nome
atividade_local


faz:
fk_matricula_neam_pessoa
fk_local_atividade_fora
hora_ini
hora_fim
dia_semana
frequencia //pode ser mudado ao longo do tempo; pode ser null


atividades neam:
pk_nome_atividade_neam //era a descricao
hora_ini


cursa:
fk_nome_atividade_neam
fk_matricula_neam_pessoa
nota
data_ini
data_fim


aula_reforco:
pk_materia


da:
fk_matricula_neam_pessoa
fk_materia_aula_reforco
hora_ini
data


recebe:
fk_matricula_neam_pessoa_aluno
fk_matricula_neam_pessoa_voluntario