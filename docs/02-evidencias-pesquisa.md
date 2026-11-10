# Evidências de pesquisa do Vida+Fácil

## Objetivo

Este documento registra os fatos extraídos das fontes fornecidas para o simulado. Ele separa informações confirmadas, materiais de apoio, limitações dos dados e divergências que exigem decisão.

As fontes foram lidas sem alteração. Os textos abaixo são sínteses, não transcrições integrais.

## Fontes analisadas

| ID | Fonte | Localização utilizada | Papel |
| --- | --- | --- | --- |
| F-PT | `PT- Tecnologias Web.docx` | Seções `Contexto Geral` e `MÓDULO A` | Define o cenário, o escopo geral e as entregas oficiais do módulo. |
| F-MR | `Matriz_Requisitos_e_Evidencias_Vida_Mais_Facil.xlsx` | Abas `Roteiro`, `Matriz` e `Fontes` | Organiza a adaptação de treinamento, os requisitos e as evidências esperadas. |
| F-BR | `Briefing INFORMAÇÕES.docx` | Seções `Público-Alvo` e `Funcionalidades Esperadas (MVP)` | Detalha público, missão e capacidades esperadas. |
| F-RB | `Rascunho Briefing.docx` | Seção `Cenários e fluxos principais esperados` | Detalha cadastro, agendamento, indicadores e feedback. |
| F-DS | `Dados_Iniciais_Vida+Facil - Sugestão.xlsx` | Abas `usuarios`, `agendamentos` e `indicadores` | Oferece dados fictícios para demonstração, com limitações de qualidade. |
| F-TC | `Textos competição.docx` | Seções da landing page | Fornece textos promocionais e depoimentos fictícios. |
| F-CE | Pasta `TEXTOS` | Dois DOCX de conteúdo e `Textos Gerais.txt` | Fornece conteúdo educativo e textos institucionais sugeridos. |
| F-TT | `Timetable_Aplições Web e Mobile_2025_VF.docx` | Tabela do dia 18/09/2025 | Confirma a duração oficial de 4 horas para o Módulo A. |

## Evidências confirmadas no Projeto-Teste

| ID | Evidência | Origem | Consequência para o projeto |
| --- | --- | --- | --- |
| E01 | A startup fictícia se chama InovaVida Digital e a plataforma se chama Vida+Fácil. | F-PT, `Contexto Geral` | Manter esses nomes em toda a documentação e na futura interface. |
| E02 | Os públicos declarados são profissionais de saúde, cuidadores e pacientes da terceira idade. | F-PT, `Contexto Geral` | Investigar necessidades e fluxos dos três públicos. |
| E03 | O portal deve oferecer conteúdo educativo, agendamento de atendimentos e registro básico de indicadores de saúde pelo paciente. | F-PT, `Contexto Geral` | Tratar essas três capacidades como escopo essencial do MVP. |
| E04 | Glicemia e pressão são exemplos explícitos de indicadores. | F-PT, `Contexto Geral` | O briefing amplia o conjunto esperado para quatro indicadores. |
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

## Evidências do briefing

| ID | Evidência | Origem | Consequência para o projeto |
| --- | --- | --- | --- |
| B01 | O foco declarado é a inclusão digital de pessoas idosas e o vínculo entre pacientes, cuidadores e profissionais. | F-BR | Priorizar linguagem simples, autonomia e acessibilidade. |
| B02 | O público inclui pessoas idosas 60+, cuidadores formais e informais e profissionais de diferentes especialidades. | F-BR | Representar os três grupos sem inventar permissões ainda não definidas. |
| B03 | O conteúdo educativo pode incluir artigos e vídeos sobre saúde, nutrição, exercícios e prevenção. | F-BR | Planejar conteúdo encontrável e apresentado de forma acessível. |
| B04 | O agendamento prevê integração com a agenda profissional e confirmação por e-mail. | F-BR | Modelar disponibilidade antes do agendamento; a integração de e-mail depende do ambiente permitido. |
| B05 | O registro manual esperado inclui glicemia, pressão arterial, frequência cardíaca e peso. | F-BR | Considerar esses quatro indicadores como conjunto funcional do MVP. |
| B06 | O histórico deve oferecer gráficos simples. | F-BR | Prever consulta histórica e visualização compreensível, sem interpretação clínica automática. |
| B07 | O MVP inclui formulário de contato e lembretes por e-mail sobre consultas e medicamentos. | F-BR | O contato é requisito; lembretes de medicamentos permanecem pendentes por falta de fluxo e dados correspondentes. |

## Detalhamentos do rascunho de apoio

| ID | Detalhamento | Origem | Tratamento |
| --- | --- | --- | --- |
| R01 | Há cadastros separados para paciente e profissional, com campos pessoais e profissionais. | F-RB | Validar campos obrigatórios e minimizar dados pessoais antes da especificação. |
| R02 | O profissional informa especialidade, registro e disponibilidade. | F-RB | Separar perfil profissional de horários disponíveis. |
| R03 | O paciente filtra profissionais, consulta horários livres e conclui o agendamento. | F-RB | Usar essa sequência no caso de uso e no mapa de navegação. |
| R04 | Ações de criar, editar ou excluir precisam de feedback visual curto e claro. | F-RB | Registrar como requisito de usabilidade e critério de aceite. |
| R05 | O fluxo solicita no mínimo três indicadores, observações gerais e consulta posterior. | F-RB | O briefing oficial lista quatro indicadores; a expressão sobre observações ainda precisa de esclarecimento. |
| R06 | A tela de indicadores deve permitir criar, visualizar, editar e excluir registros. | F-RB | Tratar como CRUD esperado, sujeito a regras de autorização e auditoria. |

## Auditoria do dataset sugerido

| ID | Constatação | Células | Consequência |
| --- | --- | --- | --- |
| DS01 | A aba `usuarios` contém dez registros e distingue apenas `medico` e `cliente`. | `usuarios!A1:N11` | O dataset não define cuidador nem vínculo entre cuidador e paciente. |
| DS02 | A aba `agendamentos` contém dez registros com paciente, profissional, data e horário. | `agendamentos!A1:E11` | Não há disponibilidade separada, estado do agendamento ou rastreabilidade. |
| DS03 | A aba `indicadores` contém dez registros e nove tipos distintos, com valores e unidades misturados em texto. | `indicadores!A1:E11` | Não usar a estrutura diretamente no banco; normalizar tipos, valores e unidades no Módulo C. |
| DS04 | As senhas aparecem em texto simples e alguns campos são incoerentes com o perfil ou com o público 60+. | `usuarios!A1:N11` | Usar os dados apenas como exemplo fictício; nunca copiar senhas nem assumir qualidade de produção. |

O dataset sugere exemplos adicionais, como IMC, temperatura, saturação, colesterol e triglicerídeos. Esses exemplos não ampliam automaticamente o escopo essencial definido pelo briefing.

## Conteúdo fornecido

- A versão simples contém dez chamadas educativas curtas.
- A versão ampliada contém três artigos sobre atividade física, pressão arterial e alimentação na terceira idade.
- `Textos competição.docx` descreve a landing page, cards e depoimentos fictícios; esses depoimentos não são entrevistas de pesquisa.
- `Textos Gerais.txt` oferece missão, visão, valores e mensagens institucionais.
- Os textos educativos não apresentam referências clínicas; serão tratados como conteúdo demonstrativo fornecido, sem gerar diagnóstico ou recomendação personalizada.

## Situação do Módulo A na matriz

Os seis requisitos do Módulo A, `REQ-01` a `REQ-06`, estão marcados como `Não iniciado` na fonte. O repositório não alterará a planilha original. O acompanhamento das entregas será feito nos documentos do projeto e nos commits.

## Divergências e dúvidas

| ID | Divergência ou dúvida | Evidências | Estado |
| --- | --- | --- | --- |
| D01 | O Projeto-Teste e o timetable reservam 4 horas para o Módulo A, enquanto o roteiro adaptado reserva 2 horas. | F-PT, `MÓDULO A`; F-TT; F-MR, `Roteiro!A5:D6` | Resolvido: usar 4 horas como referência oficial e 2 horas apenas como adaptação de treinamento. |
| D02 | A expressão `mapa de navegação/jornada do cliente` não esclarece se os dois artefatos são obrigatórios ou se um deles é suficiente. | F-PT, entrega do Módulo A; F-MR, `Matriz!A9:I9` | Consultar a ficha de avaliação ou adotar apenas o que for confirmado. |
| D03 | A matriz se identifica como adaptação de treinamento e declara que não substitui a ficha de avaliação com dois avaliadores. | F-MR, `Roteiro!A2:A3` e `Roteiro!A22:A23` | Não tratar a matriz como ficha oficial de pontuação. |
| D04 | O cuidador é público oficial, mas não possui fluxo, permissões ou dados próprios nas fontes analisadas. | F-PT, F-BR, F-RB e F-DS | Criar persona baseada no papel declarado, sem inventar autorização funcional. |
| D05 | O briefing pede lembretes de medicamentos, mas não define cadastro de medicamentos, prescrição ou posologia. | F-BR | Não modelar medicamento até obter regra explícita; manter a dúvida na CSD. |
| D06 | O briefing e os textos promocionais apresentam contatos diferentes. | F-BR e F-TC | Não publicar telefone, endereço ou e-mail até definir dados demonstrativos canônicos. |

## Lacunas de pesquisa

- O pacote não contém arquivos separados de entrevistas ou relatórios de observação.
- Os depoimentos da landing page são conteúdo promocional fictício e não substituem entrevistas.
- As personas deverão ser composições provisórias baseadas no público e nos fluxos documentados, com essa limitação explícita.
- Não há regra para acesso do cuidador, compartilhamento de indicadores, cancelamento ou reagendamento.

## Limites desta análise

- A pesquisa descreve o produto, mas não fornece orientação clínica validada.
- Nenhum valor do dataset deve ser interpretado como faixa saudável, diagnóstico ou conduta.
- CRUD, e-mail e gráficos continuam sujeitos a segurança, autorização e critérios de aceite que serão definidos na especificação.

## Próxima etapa

A próxima etapa será transformar as evidências em matriz CSD e personas provisórias, mantendo as lacunas de pesquisa visíveis.
