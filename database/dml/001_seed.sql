-- Dados iniciais fictícios do Vida+Fácil
START TRANSACTION;

-- Especialidades disponíveis
INSERT INTO especialidade (id_especialidade, nome) VALUES
  (1, 'Geriatria'),
  (2, 'Cardiologia'),
  (3, 'Clínica Geral');

-- Usuários de demonstração
-- A senha é representada por hash BCrypt de exemplo; nenhuma senha real é armazenada.
INSERT INTO usuario (
  id_usuario,
  nome,
  email,
  senha_hash,
  perfil
) VALUES
  (
    1,
    'Maria de Souza',
    'maria.souza@example.test',
    '$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy',
    'PACIENTE'
  ),
  (
    2,
    'Dra. Ana Ribeiro',
    'ana.ribeiro@example.test',
    '$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy',
    'PROFISSIONAL'
  ),
  (
    3,
    'Dr. Bruno Lima',
    'bruno.lima@example.test',
    '$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy',
    'PROFISSIONAL'
  );

-- Perfis vinculados aos usuários
INSERT INTO paciente (id_paciente, id_usuario) VALUES
  (1, 1);

INSERT INTO profissional (
  id_profissional,
  id_usuario,
  id_especialidade,
  registro_profissional
) VALUES
  (1, 2, 1, 'CRM-SP-123456'),
  (2, 3, 2, 'CRM-SP-654321');

  -- Horários futuros cadastrados pelos profissionais
INSERT INTO disponibilidade (
  id_disponibilidade,
  id_profissional,
  inicio_em,
  fim_em,
  status
) VALUES
  (1, 1, '2026-12-05 09:00:00', '2026-12-05 09:30:00', 'RESERVADA'),
  (2, 1, '2026-12-05 10:00:00', '2026-12-05 10:30:00', 'DISPONIVEL'),
  (3, 2, '2026-12-06 14:00:00', '2026-12-06 14:30:00', 'DISPONIVEL');

-- Agendamento vinculado ao horário reservado
INSERT INTO agendamento (
  id_agendamento,
  id_paciente,
  id_disponibilidade,
  confirmado_em
) VALUES
  (1, 1, 1, '2026-11-18 10:00:00');

  -- Indicadores de saúde de demonstração
INSERT INTO indicador_saude (
  id_indicador,
  id_paciente,
  tipo,
  valor_principal,
  valor_secundario,
  unidade,
  registrado_em
) VALUES
  (1, 1, 'PRESSAO_ARTERIAL', 120.00, 80.00, 'mmHg', '2026-11-15'),
  (2, 1, 'GLICEMIA', 110.00, NULL, 'mg/dL', '2026-11-16'),
  (3, 1, 'PESO', 72.50, NULL, 'kg', '2026-11-17'),
  (4, 1, 'FREQUENCIA_CARDIACA', 72.00, NULL, 'bpm', '2026-11-18');

  -- Conteúdos educativos disponíveis ao público
INSERT INTO conteudo_educativo (
  id_conteudo,
  titulo,
  resumo,
  tipo,
  url,
  publicado_em,
  ativo
) VALUES
  (
    1,
    'Como se preparar para uma consulta',
    'Orientações gerais para organizar dúvidas e informações antes de um atendimento.',
    'GUIA',
    'https://example.test/conteudos/preparo-consulta',
    '2026-11-01',
    1
  ),
  (
    2,
    'Alimentação e bem-estar',
    'Conteúdo educativo geral sobre escolhas alimentares no dia a dia.',
    'ARTIGO',
    'https://example.test/conteudos/alimentacao-bem-estar',
    '2026-11-02',
    1
  ),
  (
    3,
    'Movimento no dia a dia',
    'Vídeo educativo sobre hábitos de movimento adequados à rotina.',
    'VIDEO',
    'https://example.test/conteudos/movimento',
    '2026-11-03',
    1
  );

-- Mensagem fictícia enviada pelo formulário de contato
INSERT INTO mensagem_contato (
  id_mensagem_contato,
  nome,
  meio_contato,
  assunto,
  mensagem,
  criado_em
) VALUES
  (
    1,
    'Maria de Souza',
    'maria.souza@example.test',
    'Dúvida sobre agendamento',
    'Gostaria de confirmar como consultar meus próximos atendimentos.',
    '2026-11-18 11:00:00'
  );

COMMIT;