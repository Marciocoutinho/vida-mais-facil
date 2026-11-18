# Evidências — Módulo C

## Ambiente do banco de dados

- O MariaDB foi iniciado por Docker Compose;
- O container `vida-mais-facil-db` ficou com status `healthy`;
- A porta local `3307` foi mapeada para a porta `3306` do container;
- A configuração foi validada com `docker compose config --quiet`.

## Estrutura criada

O comando `SHOW TABLES;` confirmou as nove tabelas:

- `agendamento`;
- `conteudo_educativo`;
- `disponibilidade`;
- `especialidade`;
- `indicador_saude`;
- `mensagem_contato`;
- `paciente`;
- `profissional`;
- `usuario`.

## Dados iniciais

A execução de `001_seed.sql` foi validada por consulta de contagem:

| Item                 | Quantidade |
| -------------------- | ---------: |
| Usuários             |          3 |
| Pacientes            |          1 |
| Profissionais        |          2 |
| Especialidades       |          3 |
| Disponibilidades     |          3 |
| Agendamentos         |          1 |
| Indicadores de saúde |          4 |
| Conteúdos educativos |          3 |
| Mensagens de contato |          1 |

## Consulta relacional

Foi consultado o agendamento de demonstração, confirmando o relacionamento entre as entidades:

- Paciente: Maria de Souza;
- Profissional: Dra. Ana Ribeiro;
- Especialidade: Geriatria;
- Início: 05/12/2026 às 09:00;
- Fim: 05/12/2026 às 09:30;
- Confirmação: 18/11/2026 às 10:00.

## Inspeção visual

A conexão `Vida+Fácil - MariaDB Docker` foi criada no MySQL Workbench usando `127.0.0.1:3307`. As tabelas e o registro de agendamento foram visualizados pela interface gráfica.

## Observações de segurança

- Senhas não foram registradas neste documento;
- O arquivo `.env` não deve ser versionado;
- Os dados inseridos no seed são fictícios;
- O sistema não armazena diagnósticos ou recomendações clínicas.
