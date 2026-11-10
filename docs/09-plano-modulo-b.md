# Plano do Módulo B

## Objetivo

Estruturar o design do Vida+Fácil com foco em acessibilidade, usabilidade e experiência da pessoa usuária, produzindo wireframes de baixa fidelidade, protótipo navegável de alta fidelidade, style guide e justificativas de design.

## Duração e fonte de verdade

- duração oficial adotada: 4 horas;
- referência principal: Módulo B do Projeto-Teste;
- requisitos de avaliação: REQ-07 a REQ-10 da matriz;
- base funcional: requisitos, casos de uso e mapa de navegação produzidos no Módulo A;
- ferramenta prevista: Figma;
- abordagem: mobile-first, com evidências de adaptação responsiva.

O roteiro adaptado de treinamento reserva duas horas para este módulo. Essa duração não substitui as quatro horas definidas no Projeto-Teste.

## Decisões de escopo

### Fluxo principal

O fluxo principal será o agendamento de atendimento pela pessoa paciente:

`Entrar → Dashboard → Filtrar profissionais e horários → Escolher horário → Revisar → Confirmar → Ver confirmação → Consultar atendimentos`

### Fluxo secundário

O fluxo secundário será o registro e a consulta de indicadores:

`Entrar → Dashboard → Indicadores → Novo registro → Validar dados → Confirmar → Ver listagem → Consultar histórico`

### Limites

Não serão prototipados como funcionalidades aprovadas:

- área privada da pessoa cuidadora;
- vínculo, consentimento e acesso delegado;
- medicamentos e lembretes;
- cancelamento e reagendamento;
- área administrativa;
- interpretação clínica dos indicadores;
- administração da disponibilidade profissional enquanto o ator responsável não for confirmado.

## Inventário de telas

| ID | Tela ou estado | Rota de referência | Finalidade | Requisitos principais |
| --- | --- | --- | --- | --- |
| B01 | Início | `/` | Apresentar o Vida+Fácil e oferecer acesso a conteúdo, cadastro e entrada. | RF-01, RF-02, RNF-01 a RNF-03 |
| B02 | Entrar | `/login` | Autenticar a pessoa e direcioná-la para a área compatível com seu perfil. | RF-05, RNF-03 a RNF-05 |
| B03 | Dashboard da pessoa paciente | `/paciente` | Resumir próximos atendimentos, indicadores recentes e acessos essenciais. | RF-06, RNF-01 a RNF-03 |
| B04 | Filtros de atendimento | `/paciente/agendamentos/novo` | Filtrar opções por especialidade e data, com orientação quando não houver resultado. | RF-07, RNF-01 a RNF-03 |
| B05 | Seleção de profissional e horário | `/paciente/agendamentos/novo` | Exibir opções compatíveis e permitir a escolha de um horário disponível. | RF-07, RF-08, RN-03 |
| B06 | Revisão do agendamento | `/paciente/agendamentos/novo` | Apresentar profissional, especialidade, data e horário antes da confirmação. | RF-08, RN-03, RN-04 |
| B07 | Confirmação do agendamento | `/paciente/agendamentos/novo` | Informar que o agendamento foi concluído ou explicar conflito e próxima ação. | RF-08, RF-14, RN-06 |
| B08 | Atendimentos | `/paciente/agendamentos` | Listar somente os atendimentos relacionados à pessoa autenticada. | RF-09, RNF-05 |
| B09 | Indicadores | `/paciente/indicadores` | Listar os registros da pessoa paciente e oferecer ações de criação, edição, exclusão e histórico. | RF-11, RF-12, RN-05, RNF-07 |
| B10 | Novo indicador | `/paciente/indicadores/novo` | Registrar tipo, valor, unidade e data com validação compreensível. | RF-11, RNF-01, RNF-03, RNF-07 |
| B11 | Histórico do indicador | `/paciente/indicadores/historico` | Apresentar série temporal e gráfico simples sem diagnóstico automático. | RF-12, RNF-08 |

## Conexões do protótipo

### Agendamento

`B02 → B03 → B04 → B05 → B06 → B07 → B08`

- ausência de resultados retorna a B04 com orientação para ajustar os filtros;
- conflito de horário retorna a B05 sem criar agendamento;
- falha de e-mail mantém B07 como confirmação válida no portal;
- B08 oferece retorno ao dashboard e início de um novo agendamento.

### Indicadores

`B02 → B03 → B09 → B10 → B09 → B11`

- erro de validação mantém os dados seguros em B10 e associa a explicação ao campo;
- sucesso retorna a B09 com confirmação textual;
- edição utiliza a mesma estrutura de formulário de B10;
- exclusão exige confirmação e retorna a B09;
- B11 oferece retorno perceptível à listagem.

## Estados obrigatórios

Os wireframes e o protótipo devem representar, por tela ou por variante de componente:

- carregamento;
- ausência de resultados ou registros;
- erro de preenchimento associado ao campo;
- erro geral de processamento;
- sucesso com mensagem textual;
- controle desabilitado com motivo perceptível;
- foco visível;
- horário indisponível;
- conflito durante a confirmação do agendamento;
- confirmação antes de excluir um indicador.

## Conteúdo mínimo por tela

- título principal único e descritivo;
- navegação compatível com o estado de autenticação;
- rótulos visíveis nos campos;
- instruções antes de entradas com formato específico;
- ação principal identificável;
- retorno ou cancelamento sem perda inesperada de dados;
- mensagens que não dependem somente de cor;
- indicação de carregamento, vazio, sucesso ou erro quando aplicável.

## Acessibilidade e responsividade

- contraste mínimo de 4,5:1 para texto normal e 3:1 para texto grande;
- estrutura mobile-first utilizável a partir de 320 px de largura CSS;
- texto e operações essenciais preservados com ampliação de 200%;
- ordem de leitura e navegação coerente;
- foco e estado atual representados visualmente;
- controles com nomes e rótulos compreensíveis;
- erros próximos aos campos e resumidos quando necessário;
- gráficos acompanhados de informação textual e sem classificação clínica automática.

O protótipo será construído primeiro em largura mobile. Para demonstrar adaptação responsiva, serão criadas variações desktop das telas B01, B03, B04 e B09. As demais telas usarão as mesmas regras documentadas de grade, conteúdo e componentes.

## Organização prevista no Figma

1. `00 Escopo` — objetivo, fontes, fluxos e exclusões;
2. `01 Wireframes Mobile` — telas B01 a B11 em baixa fidelidade;
3. `02 Foundations` — cores, tipografia, espaçamento e grade;
4. `03 Components` — componentes e estados;
5. `04 Prototype Mobile` — telas de alta fidelidade e conexões;
6. `05 Responsive` — variações desktop selecionadas;
7. `06 Evidence` — contraste, acessibilidade e checklist.

## Critérios de conclusão da atividade de design

- todas as telas do inventário possuem wireframe;
- os dois fluxos podem ser percorridos sem ligação quebrada;
- os estados críticos estão visíveis;
- cada tela está ligada aos requisitos correspondentes;
- componentes equivalentes usam o mesmo padrão;
- cores de texto e controles possuem contraste verificado;
- variações responsivas preservam conteúdo e ações;
- as exclusões e decisões pendentes continuam identificadas.

## Distribuição das quatro horas

| Período | Atividade |
| --- | --- |
| 00:00–00:25 | Fluxos, inventário de telas e organização do arquivo |
| 00:25–01:10 | Wireframes mobile |
| 01:10–01:55 | Foundations e componentes essenciais |
| 01:55–03:10 | Telas de alta fidelidade e protótipo navegável |
| 03:10–03:35 | Responsividade e verificação de acessibilidade |
| 03:35–04:00 | Teste, evidências, justificativas e documentação |

## Resultado esperado do Módulo B

- wireframes digitais do fluxo principal e do fluxo secundário;
- protótipo mobile navegável de alta fidelidade;
- style guide e biblioteca mínima de componentes;
- evidências de contraste e adaptação responsiva;
- justificativas de design ligadas aos requisitos e às proto-personas;
- checklist e link do Figma registrados no repositório.
