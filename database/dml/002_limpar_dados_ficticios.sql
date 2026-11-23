USE vida_mais_facil;

START TRANSACTION;

DELETE FROM agendamento;
DELETE FROM indicador_saude;
DELETE FROM disponibilidade;
DELETE FROM profissional;
DELETE FROM paciente;
DELETE FROM mensagem_contato;
DELETE FROM conteudo_educativo;
DELETE FROM usuario;
DELETE FROM especialidade;

COMMIT;