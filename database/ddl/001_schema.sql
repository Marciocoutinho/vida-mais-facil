-- Banco de dados do Vida+Fácil
CREATE DATABASE IF NOT EXISTS vida_mais_facil
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE vida_mais_facil;

-- Conta de acesso ao sistema
CREATE TABLE usuario (
  id_usuario BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  nome VARCHAR(120) NOT NULL,
  email VARCHAR(254) NOT NULL,
  senha_hash VARCHAR(255) NOT NULL,
  perfil ENUM('PACIENTE', 'PROFISSIONAL') NOT NULL,
  criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT pk_usuario PRIMARY KEY (id_usuario),
  CONSTRAINT uq_usuario_email UNIQUE (email)
) ENGINE=InnoDB;

-- Especialidades dos profissionais
CREATE TABLE especialidade (
  id_especialidade BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,

  CONSTRAINT pk_especialidade PRIMARY KEY (id_especialidade),
  CONSTRAINT uq_especialidade_nome UNIQUE (nome)
) ENGINE=InnoDB;

-- Perfil de pessoa paciente
CREATE TABLE paciente (
  id_paciente BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_usuario BIGINT UNSIGNED NOT NULL,

  CONSTRAINT pk_paciente PRIMARY KEY (id_paciente),
  CONSTRAINT uq_paciente_usuario UNIQUE (id_usuario),
  CONSTRAINT fk_paciente_usuario
    FOREIGN KEY (id_usuario)
    REFERENCES usuario (id_usuario)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Perfil de profissional de saúde
CREATE TABLE profissional (
  id_profissional BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_usuario BIGINT UNSIGNED NOT NULL,
  id_especialidade BIGINT UNSIGNED NOT NULL,
  registro_profissional VARCHAR(40) NOT NULL,

  CONSTRAINT pk_profissional PRIMARY KEY (id_profissional),
  CONSTRAINT uq_profissional_usuario UNIQUE (id_usuario),
  CONSTRAINT uq_profissional_registro UNIQUE (registro_profissional),
  CONSTRAINT fk_profissional_usuario
    FOREIGN KEY (id_usuario)
    REFERENCES usuario (id_usuario)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT fk_profissional_especialidade
    FOREIGN KEY (id_especialidade)
    REFERENCES especialidade (id_especialidade)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Horários oferecidos pelos profissionais
CREATE TABLE disponibilidade (
  id_disponibilidade BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_profissional BIGINT UNSIGNED NOT NULL,
  inicio_em DATETIME NOT NULL,
  fim_em DATETIME NOT NULL,
  status ENUM('DISPONIVEL', 'RESERVADA', 'INATIVA')
    NOT NULL DEFAULT 'DISPONIVEL',
  criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT pk_disponibilidade PRIMARY KEY (id_disponibilidade),
  CONSTRAINT uq_disponibilidade_profissional_inicio
    UNIQUE (id_profissional, inicio_em),
  CONSTRAINT chk_disponibilidade_periodo
    CHECK (fim_em > inicio_em),
  CONSTRAINT fk_disponibilidade_profissional
    FOREIGN KEY (id_profissional)
    REFERENCES profissional (id_profissional)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Agendamentos confirmados pelas pessoas pacientes
CREATE TABLE agendamento (
  id_agendamento BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_paciente BIGINT UNSIGNED NOT NULL,
  id_disponibilidade BIGINT UNSIGNED NOT NULL,
  confirmado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT pk_agendamento PRIMARY KEY (id_agendamento),
  CONSTRAINT uq_agendamento_disponibilidade UNIQUE (id_disponibilidade),
  CONSTRAINT fk_agendamento_paciente
    FOREIGN KEY (id_paciente)
    REFERENCES paciente (id_paciente)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT fk_agendamento_disponibilidade
    FOREIGN KEY (id_disponibilidade)
    REFERENCES disponibilidade (id_disponibilidade)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Registros manuais de indicadores de saúde
CREATE TABLE indicador_saude (
  id_indicador BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_paciente BIGINT UNSIGNED NOT NULL,
  tipo ENUM(
    'GLICEMIA',
    'PRESSAO_ARTERIAL',
    'FREQUENCIA_CARDIACA',
    'PESO'
  ) NOT NULL,
  valor_principal DECIMAL(10,2) NOT NULL,
  valor_secundario DECIMAL(10,2) NULL,
  unidade VARCHAR(20) NOT NULL,
  registrado_em DATE NOT NULL,
  criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT pk_indicador_saude PRIMARY KEY (id_indicador),
  CONSTRAINT chk_indicador_valor_principal
    CHECK (valor_principal >= 0),
  CONSTRAINT chk_indicador_valor_secundario
    CHECK (valor_secundario IS NULL OR valor_secundario >= 0),
  CONSTRAINT chk_indicador_pressao
    CHECK (
      (tipo = 'PRESSAO_ARTERIAL' AND valor_secundario IS NOT NULL)
      OR
      (tipo <> 'PRESSAO_ARTERIAL' AND valor_secundario IS NULL)
    ),
  CONSTRAINT chk_indicador_unidade
    CHECK (
      (tipo = 'GLICEMIA' AND unidade = 'mg/dL')
      OR (tipo = 'PRESSAO_ARTERIAL' AND unidade = 'mmHg')
      OR (tipo = 'FREQUENCIA_CARDIACA' AND unidade = 'bpm')
      OR (tipo = 'PESO' AND unidade = 'kg')
    ),
  CONSTRAINT fk_indicador_paciente
    FOREIGN KEY (id_paciente)
    REFERENCES paciente (id_paciente)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Conteúdos educativos disponíveis ao público
CREATE TABLE conteudo_educativo (
  id_conteudo BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  titulo VARCHAR(180) NOT NULL,
  resumo TEXT NOT NULL,
  tipo ENUM('ARTIGO', 'VIDEO', 'GUIA') NOT NULL,
  url VARCHAR(2048) NOT NULL,
  publicado_em DATE NULL,
  ativo TINYINT(1) NOT NULL DEFAULT 1,

  CONSTRAINT pk_conteudo_educativo PRIMARY KEY (id_conteudo),
  CONSTRAINT chk_conteudo_ativo CHECK (ativo IN (0, 1))
) ENGINE=InnoDB;

-- Mensagens enviadas pelo formulário de contato
CREATE TABLE mensagem_contato (
  id_mensagem_contato BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  nome VARCHAR(120) NOT NULL,
  meio_contato VARCHAR(254) NOT NULL,
  assunto VARCHAR(150) NOT NULL,
  mensagem TEXT NOT NULL,
  criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT pk_mensagem_contato PRIMARY KEY (id_mensagem_contato)
) ENGINE=InnoDB;