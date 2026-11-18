# Dicionário de dados do Vida+Fácil

## USUARIO

| Campo      | Tipo MariaDB                     | Regra                               |
| ---------- | -------------------------------- | ----------------------------------- |
| id_usuario | BIGINT UNSIGNED                  | PK, AUTO_INCREMENT, NOT NULL        |
| nome       | VARCHAR(120)                     | NOT NULL                            |
| email      | VARCHAR(254)                     | NOT NULL, UNIQUE                    |
| senha_hash | VARCHAR(255)                     | NOT NULL                            |
| perfil     | ENUM('PACIENTE', 'PROFISSIONAL') | NOT NULL                            |
| criado_em  | DATETIME                         | NOT NULL, DEFAULT CURRENT_TIMESTAMP |

## PACIENTE

| Campo       | Tipo MariaDB    | Regra                                      |
| ----------- | --------------- | ------------------------------------------ |
| id_paciente | BIGINT UNSIGNED | PK, AUTO_INCREMENT, NOT NULL               |
| id_usuario  | BIGINT UNSIGNED | FK → USUARIO(id_usuario), NOT NULL, UNIQUE |

## ESPECIALIDADE

| Campo            | Tipo MariaDB    | Regra                        |
| ---------------- | --------------- | ---------------------------- |
| id_especialidade | BIGINT UNSIGNED | PK, AUTO_INCREMENT, NOT NULL |
| nome             | VARCHAR(100)    | NOT NULL, UNIQUE             |

## PROFISSIONAL

| Campo                 | Tipo MariaDB    | Regra                                          |
| --------------------- | --------------- | ---------------------------------------------- |
| id_profissional       | BIGINT UNSIGNED | PK, AUTO_INCREMENT, NOT NULL                   |
| id_usuario            | BIGINT UNSIGNED | FK → USUARIO(id_usuario), NOT NULL, UNIQUE     |
| id_especialidade      | BIGINT UNSIGNED | FK → ESPECIALIDADE(id_especialidade), NOT NULL |
| registro_profissional | VARCHAR(40)     | NOT NULL, UNIQUE                               |

## DISPONIBILIDADE

| Campo              | Tipo MariaDB                               | Regra                                        |
| ------------------ | ------------------------------------------ | -------------------------------------------- |
| id_disponibilidade | BIGINT UNSIGNED                            | PK, AUTO_INCREMENT, NOT NULL                 |
| id_profissional    | BIGINT UNSIGNED                            | FK → PROFISSIONAL(id_profissional), NOT NULL |
| inicio_em          | DATETIME                                   | NOT NULL                                     |
| fim_em             | DATETIME                                   | NOT NULL, CHECK (fim_em > inicio_em)         |
| status             | ENUM('DISPONIVEL', 'RESERVADA', 'INATIVA') | NOT NULL, DEFAULT 'DISPONIVEL'               |
| criado_em          | DATETIME                                   | NOT NULL, DEFAULT CURRENT_TIMESTAMP          |

**Restrição adicional:** `UNIQUE(id_profissional, inicio_em)`

## AGENDAMENTO

| Campo              | Tipo MariaDB    | Regra                                                      |
| ------------------ | --------------- | ---------------------------------------------------------- |
| id_agendamento     | BIGINT UNSIGNED | PK, AUTO_INCREMENT, NOT NULL                               |
| id_paciente        | BIGINT UNSIGNED | FK → PACIENTE(id_paciente), NOT NULL                       |
| id_disponibilidade | BIGINT UNSIGNED | FK → DISPONIBILIDADE(id_disponibilidade), NOT NULL, UNIQUE |
| confirmado_em      | DATETIME        | NOT NULL, DEFAULT CURRENT_TIMESTAMP                        |

## INDICADOR_SAUDE

| Campo            | Tipo MariaDB                                                        | Regra                                           |
| ---------------- | ------------------------------------------------------------------- | ----------------------------------------------- |
| id_indicador     | BIGINT UNSIGNED                                                     | PK, AUTO_INCREMENT, NOT NULL                    |
| id_paciente      | BIGINT UNSIGNED                                                     | FK → PACIENTE(id_paciente), NOT NULL            |
| tipo             | ENUM('GLICEMIA', 'PRESSAO_ARTERIAL', 'FREQUENCIA_CARDIACA', 'PESO') | NOT NULL                                        |
| valor_principal  | DECIMAL(10,2)                                                       | NOT NULL                                        |
| valor_secundario | DECIMAL(10,2)                                                       | NULL, obrigatório somente para PRESSAO_ARTERIAL |
| unidade          | VARCHAR(20)                                                         | NOT NULL                                        |
| registrado_em    | DATE                                                                | NOT NULL                                        |
| criado_em        | DATETIME                                                            | NOT NULL, DEFAULT CURRENT_TIMESTAMP             |

**Restrições adicionais:**

- Para `PRESSAO_ARTERIAL`, `valor_secundario` é obrigatório.
- Para os demais tipos, `valor_secundario` deve permanecer vazio.
- Unidades aceitas: `mg/dL` para glicemia, `mmHg` para pressão arterial, `bpm` para frequência cardíaca e `kg` para peso.
- Não serão armazenadas interpretações, diagnósticos ou recomendações clínicas.

## CONTEUDO_EDUCATIVO

| Campo        | Tipo MariaDB                    | Regra                        |
| ------------ | ------------------------------- | ---------------------------- |
| id_conteudo  | BIGINT UNSIGNED                 | PK, AUTO_INCREMENT, NOT NULL |
| titulo       | VARCHAR(180)                    | NOT NULL                     |
| resumo       | TEXT                            | NOT NULL                     |
| tipo         | ENUM('ARTIGO', 'VIDEO', 'GUIA') | NOT NULL                     |
| url          | VARCHAR(2048)                   | NOT NULL                     |
| publicado_em | DATE                            | NULL                         |
| ativo        | TINYINT(1)                      | NOT NULL, DEFAULT 1          |

## MENSAGEM_CONTATO

| Campo               | Tipo MariaDB    | Regra                               |
| ------------------- | --------------- | ----------------------------------- |
| id_mensagem_contato | BIGINT UNSIGNED | PK, AUTO_INCREMENT, NOT NULL        |
| nome                | VARCHAR(120)    | NOT NULL                            |
| meio_contato        | VARCHAR(254)    | NOT NULL                            |
| assunto             | VARCHAR(150)    | NOT NULL                            |
| mensagem            | TEXT            | NOT NULL                            |
| criado_em           | DATETIME        | NOT NULL, DEFAULT CURRENT_TIMESTAMP |

**Regras adicionais:**

- `ativo = 1` indica conteúdo disponível ao público.
- A URL deve ser validada pela aplicação antes do armazenamento.
- `MENSAGEM_CONTATO` não possui vínculo obrigatório com `USUARIO`, pois o formulário pode ser enviado sem login.
- Mensagens de contato não devem ser expostas em logs técnicos.
