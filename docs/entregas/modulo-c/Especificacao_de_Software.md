# Especificação de Software — Vida+Fácil — Módulo C

## 1. Objetivo

Definir a base de dados e a abstração de domínio do Vida+Fácil para apoiar o cadastro de usuários, perfis de pacientes e profissionais, disponibilidades, agendamentos, indicadores de saúde, conteúdo educativo e mensagens de contato.

## 2. Escopo de domínio

O modelo contempla:

- Usuários com perfil de paciente ou profissional;
- Especialidades e registros profissionais;
- Horários disponibilizados por profissionais;
- Agendamentos de pacientes;
- Registros manuais de glicemia, pressão arterial, frequência cardíaca e peso;
- Conteúdos educativos públicos;
- Mensagens enviadas pelo formulário de contato.

O sistema não realiza diagnóstico, interpretação clínica ou recomendação médica.

## 3. Tecnologias e execução

- Banco de dados: MariaDB 12, executado em Docker;
- Persistência: tabelas InnoDB, chaves primárias, estrangeiras, `UNIQUE` e `CHECK`;
- Linguagem de domínio: TypeScript;
- Organização: Models e DTOs em `backend/src/domain`;
- Administração e consulta visual: MySQL Workbench.

## 4. Diagramas

### Diagrama Entidade-Relacionamento

O DER descreve a estrutura relacional do banco de dados, suas entidades, chaves e cardinalidades.

- [Arquivo editável](diagramas/DER_Vida_Mais_Facil.drawio)
- [Imagem PNG](diagramas/DER_Vida_Mais_Facil.png)

### Diagrama de classes

O diagrama de classes representa os Models TypeScript, seus atributos, enums e relacionamentos de domínio.

- [Arquivo editável](diagramas/Diagrama_de_Classes_Vida_Mais_Facil.drawio)
- [Imagem PNG](diagramas/Diagrama_de_Classes_Vida_Mais_Facil.png)

## 5. Artefatos de dados

- [Dicionário de dados](Dicionario_de_Dados.md);
- DDL: `database/ddl/001_schema.sql`;
- Dados iniciais fictícios: `database/dml/001_seed.sql`;
- Configuração local do banco: `docker-compose.yml` e `.env.example`.

O DDL cria nove tabelas: `usuario`, `paciente`, `profissional`,
`especialidade`, `disponibilidade`, `agendamento`, `indicador_saude`,
`conteudo_educativo` e `mensagem_contato`.

## 6. Regras de domínio relevantes

- O e-mail de `usuario` é único;
- O campo `perfil` define se a conta é de paciente ou profissional; a aplicação deve criar somente o perfil correspondente;
- Cada profissional possui uma especialidade e um registro profissional único;
- Uma disponibilidade pertence a um profissional e não pode terminar antes ou no mesmo instante em que começa;
- Uma disponibilidade pode originar, no máximo, um agendamento;
- Indicadores de saúde aceitam somente os tipos e unidades previstos;
- Para pressão arterial, `valor_secundario` é obrigatório; para os demais indicadores, ele permanece vazio;
- Conteúdos só devem ser devolvidos ao público quando estiverem ativos;
- Mensagens de contato podem ser enviadas sem vínculo com usuário autenticado.

## 7. Models e DTOs

Os Models TypeScript representam as entidades persistidas e os tipos de domínio em:

```text
backend/src/domain/models
```

Os DTOs definem dados de entrada e saída da futura API em:

```text
backend/src/domain/dtos
```

A separação evita a exposição de dados sensíveis. Por exemplo, `UsuarioRespostaDto` não possui `senha` nem `senhaHash`.

## 8. Validação realizada

A execução foi validada localmente com Docker e MariaDB:

- `docker compose config --quiet`;
- `docker compose up -d`;
- `docker compose ps`, com o serviço saudável;
- execução de `001_schema.sql`;
- execução de `001_seed.sql`;
- consulta das nove tabelas criadas;
- consulta de contagem dos registros iniciais;
- consulta relacional de agendamento entre paciente, profissional, especialidade e disponibilidade;
- inspeção visual das tabelas e do agendamento pelo MySQL Workbench.
