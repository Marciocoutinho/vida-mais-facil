# Evidências do Projeto-Teste e da matriz

## Objetivo

Este documento registra os fatos extraídos do Projeto-Teste e da matriz de requisitos do simulado. Ele separa informações confirmadas, refinamentos do guia de treinamento e divergências que exigem decisão.

As fontes foram lidas sem alteração. Os textos abaixo são sínteses, não transcrições integrais.

## Fontes analisadas

| ID | Fonte | Localização utilizada | Papel |
| --- | --- | --- | --- |
| F-PT | `PT- Tecnologias Web.docx` | Seções `Contexto Geral` e `MÓDULO A` | Define o cenário, o escopo geral e as entregas oficiais do módulo. |
| F-MR | `Matriz_Requisitos_e_Evidencias_Vida_Mais_Facil.xlsx` | Abas `Roteiro`, `Matriz` e `Fontes` | Organiza a adaptação de treinamento, os requisitos e as evidências esperadas. |

## Evidências confirmadas no Projeto-Teste

| ID | Evidência | Origem | Consequência para o projeto |
| --- | --- | --- | --- |
| E01 | A startup fictícia se chama InovaVida Digital e a plataforma se chama Vida+Fácil. | F-PT, `Contexto Geral` | Manter esses nomes em toda a documentação e na futura interface. |
| E02 | Os públicos declarados são profissionais de saúde, cuidadores e pacientes da terceira idade. | F-PT, `Contexto Geral` | Investigar necessidades e fluxos dos três públicos. |
| E03 | O portal deve oferecer conteúdo educativo, agendamento de atendimentos e registro básico de indicadores de saúde pelo paciente. | F-PT, `Contexto Geral` | Tratar essas três capacidades como escopo essencial do MVP. |
| E04 | Glicemia e pressão são exemplos explícitos de indicadores. | F-PT, `Contexto Geral` | Verificar no briefing e no dataset quais campos e unidades estão disponíveis. |
| E05 | As telas esperadas são página inicial, registro, login, dashboard do cliente e agendamento. | F-PT, `Contexto Geral` | Representar essas telas no mapa de navegação e no Módulo B. |
| E06 | A interface deve ser acessível e responsiva. | F-PT, `Contexto Geral` | Considerar acessibilidade e responsividade desde os requisitos. |
| E07 | O objetivo do Módulo A é identificar perfis de usuários e necessidades com base nos dados fornecidos. | F-PT, `MÓDULO A` | Personas e requisitos devem ser rastreáveis às fontes. |
| E08 | O Módulo A prevê leitura de entrevistas e observações, matriz CSD, personas, mapa de navegação e requisitos funcionais e não funcionais. | F-PT, `MÓDULO A` | Produzir todos esses artefatos antes de iniciar o design. |
| E09 | A especificação do módulo deve incluir personas, matriz CSD, requisitos, diagrama de casos de uso e mapa de navegação ou jornada do cliente. | F-PT, `MÓDULO A` | Usar a especificação como entrega consolidada do módulo. |
| E10 | O README deve evoluir durante todo o projeto. | F-PT, `MÓDULO A` | Atualizar o README ao encerrar cada atividade relevante. |

## Confirmações e refinamentos da matriz

| ID | Registro da matriz | Células | Interpretação |
| --- | --- | --- | --- |
| M01 | Interpretar briefing, dataset, textos e recursos visuais antes do desenvolvimento. | `Matriz!A5:I5` | Confirma que a pesquisa antecede implementação e design. |
| M02 | Definir personas para paciente, cuidador e profissional de saúde. | `Matriz!A6:I6` | Refina os três perfis que deverão ser representados. |
| M03 | Elaborar matriz CSD baseada nas evidências do cenário. | `Matriz!A7:I7` | Impede preencher a CSD apenas com opiniões da equipe. |
| M04 | Registrar requisitos funcionais e não funcionais com prioridade. | `Matriz!A8:I8` | Acrescenta prioridade como campo obrigatório da especificação. |
| M05 | Representar casos de uso e mapa de navegação ou jornada do cliente. | `Matriz!A9:I9` | Confirma os artefatos visuais, mas mantém ambiguidade sobre mapa ou jornada. |
| M06 | Manter README com contexto, tecnologias, instalação, execução, uso e links. | `Matriz!A10:I10` | O README será completado progressivamente, conforme esses elementos existirem. |

## Situação do Módulo A na matriz

Os seis requisitos do Módulo A, `REQ-01` a `REQ-06`, estão marcados como `Não iniciado` na fonte. O repositório não alterará a planilha original. O acompanhamento das entregas será feito nos documentos do projeto e nos commits.

## Divergências e dúvidas

| ID | Divergência ou dúvida | Evidências | Estado |
| --- | --- | --- | --- |
| D01 | O Projeto-Teste reserva 4 horas para o Módulo A, enquanto o roteiro adaptado reserva 2 horas, das 08h00 às 10h00 de 24/11/2026. | F-PT, `MÓDULO A`; F-MR, `Roteiro!A5:D6` | Pendente de decisão do instrutor. |
| D02 | A expressão `mapa de navegação/jornada do cliente` não esclarece se os dois artefatos são obrigatórios ou se um deles é suficiente. | F-PT, entrega do Módulo A; F-MR, `Matriz!A9:I9` | Consultar a ficha de avaliação ou adotar apenas o que for confirmado. |
| D03 | A matriz se identifica como adaptação de treinamento e declara que não substitui a ficha de avaliação com dois avaliadores. | F-MR, `Roteiro!A2:A3` e `Roteiro!A22:A23` | Não tratar a matriz como ficha oficial de pontuação. |

## Limites desta análise

- A análise ainda não valida regras detalhadas de cadastro, disponibilidade, agendamento ou indicadores.
- A análise ainda não autoriza CRUD completo, gráficos, notificações ou atuação do cuidador em nome do paciente.
- Esses pontos dependem do briefing, do rascunho de apoio, do dataset e da ficha de avaliação aplicável.

## Próxima fonte

O próximo documento a analisar é `Briefing INFORMAÇÕES.docx`. A leitura deverá confirmar necessidades, dores, fluxos e limites do MVP antes da criação de personas e da matriz CSD.
