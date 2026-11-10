# Requisitos do Vida+Fácil

## Objetivo

Transformar as evidências do Módulo A em comportamentos verificáveis para orientar design, implementação e avaliação do MVP.

## Convenções

### Prioridade

- **Obrigatório:** necessário para atender ao escopo essencial documentado.
- **Desejável:** melhora a entrega, mas depende do tempo após os obrigatórios.
- **Condicional:** só entra no MVP após a resolução de uma dúvida ou confirmação de infraestrutura.

### Estado

- **Confirmado:** sustentado diretamente pelo Projeto-Teste ou briefing.
- **Refinado:** detalhado pelo rascunho ou por decisão técnica necessária para tornar o requisito testável.
- **A validar:** depende de hipótese ou regra de negócio ainda não confirmada.

## Requisitos funcionais

| ID | Prioridade | Estado | Requisito | Critérios de aceite | Origem |
| --- | --- | --- | --- | --- | --- |
| RF-01 | Obrigatório | Confirmado | Apresentar página inicial com identidade do Vida+Fácil e acesso às áreas essenciais. | A página identifica o produto e oferece caminhos perceptíveis para conteúdo, cadastro e login. | E01, E05 |
| RF-02 | Obrigatório | Confirmado | Permitir consultar conteúdo educativo. | A pessoa consegue localizar e abrir ao menos um conteúdo; o conteúdo é identificado como informativo, sem diagnóstico personalizado. | E03, B03, C04 |
| RF-03 | Obrigatório | Refinado | Permitir o cadastro de paciente com os dados mínimos necessários. | Campos obrigatórios são identificados; dados inválidos geram mensagem junto ao campo; a senha não é exibida nem armazenada em texto simples. | R01, S10, DS04 |
| RF-04 | Obrigatório | Refinado | Permitir o cadastro de profissional com dados pessoais, especialidade e registro profissional. | O perfil profissional é distinguido do paciente; especialidade e registro são validados como obrigatórios; disponibilidade não é armazenada como texto livre no perfil. | R01, R02 |
| RF-05 | Obrigatório | Confirmado | Permitir autenticação e encerramento de sessão. | Credenciais válidas iniciam uma sessão; credenciais inválidas recebem mensagem sem revelar qual campo está cadastrado; sair encerra o acesso autenticado. | E05, R01 |
| RF-06 | Obrigatório | Confirmado | Disponibilizar dashboard para a pessoa paciente. | Após entrar, a pessoa visualiza um resumo e acessos diretos para agendamento, indicadores e conteúdo. A ordem dos blocos será validada no wireframe. | E05, S03 |
| RF-07 | Obrigatório | Refinado | Permitir buscar profissionais e horários disponíveis por especialidade, data e horário. | A busca apresenta somente opções compatíveis com os filtros e informa quando não há resultado. | R03, S09 |
| RF-08 | Obrigatório | Confirmado | Permitir que a pessoa paciente agende um atendimento em horário disponível. | O resumo apresenta profissional, especialidade, data e horário; a confirmação cria um único agendamento; conflito de horário impede a operação e orienta nova escolha. | E03, B04, R03 |
| RF-09 | Obrigatório | Refinado | Permitir que paciente e profissional consultem seus próprios atendimentos. | Cada perfil visualiza apenas atendimentos relacionados à sua conta, ordenados por data e horário. | B04, DS02 |
| RF-10 | Obrigatório | A validar | Permitir manter horários de disponibilidade profissional. | Horários futuros podem ser criados e removidos; um horário agendado não pode ser removido silenciosamente. O ator responsável por essa gestão ainda precisa ser confirmado. | R02, S02, D05 |
| RF-11 | Obrigatório | Confirmado | Permitir que a pessoa paciente registre indicadores manualmente. | É possível registrar glicemia, pressão arterial, frequência cardíaca ou peso com data, valor e unidade coerentes; erros são explicados antes do envio. | E03, B05, C06, C07 |
| RF-12 | Obrigatório | Refinado | Permitir consultar, editar e excluir os próprios registros de indicadores. | A listagem exibe tipo, valor, unidade e data; edição e exclusão exigem confirmação apropriada; o histórico apresenta gráfico simples por tipo de indicador. | B06, R06 |
| RF-13 | Obrigatório | Confirmado | Disponibilizar formulário de contato. | Nome, meio de contato, assunto e mensagem possuem validação; o envio apresenta confirmação ou erro; o destino real será definido antes da implementação. | B07, S08 |
| RF-14 | Condicional | A validar | Confirmar agendamento por e-mail. | Quando houver serviço de e-mail aprovado, uma confirmação é enviada sem expor dados sensíveis desnecessários; sem o serviço, a confirmação permanece disponível no portal. | B04, S04, D11 |

## Requisitos não funcionais

| ID | Prioridade | Estado | Requisito | Critérios de verificação | Origem |
| --- | --- | --- | --- | --- | --- |
| RNF-01 | Obrigatório | Refinado | A interface deve seguir uma referência de acessibilidade equivalente ao nível AA da WCAG 2.2. | Fluxos essenciais funcionam por teclado; foco é visível; controles têm nome acessível; mensagens de erro são associadas aos campos; contraste e estrutura semântica passam por auditoria. | E06, C10, P01 |
| RNF-02 | Obrigatório | Confirmado | A interface deve ser responsiva. | Conteúdo e operações essenciais funcionam a partir de 320 px de largura CSS e com ampliação de 200%, sem perda de informação ou rolagem horizontal injustificada. | E06, C10 |
| RNF-03 | Obrigatório | Refinado | A linguagem e a interação devem ser simples e consistentes. | Rótulos permanecem visíveis; instruções evitam jargão; ações equivalentes usam os mesmos termos; sucesso e erro não dependem somente de cor. | B01, R04, P01 |
| RNF-04 | Obrigatório | Refinado | Credenciais e sessões devem ser protegidas. | Senhas usam hash apropriado com salt; rotas privadas exigem autenticação; encerramento de sessão invalida o acesso; segredos não entram no repositório. | DS04 |
| RNF-05 | Obrigatório | Refinado | O acesso deve respeitar o perfil e a propriedade dos dados. | Paciente não acessa registros de outro paciente; profissional acessa somente o necessário ao fluxo aprovado; cuidador não recebe acesso delegado antes de regra explícita. | D01, D02, P02 |
| RNF-06 | Obrigatório | Refinado | A coleta de dados deve ser minimizada. | Cada campo pessoal possui finalidade documentada; campos sem necessidade para o MVP não são obrigatórios; dados sensíveis não aparecem em logs ou mensagens de erro. | S10, D04 |
| RNF-07 | Obrigatório | Refinado | Indicadores devem preservar integridade de tipo, valor, unidade e data. | Valor numérico e unidade são armazenados separadamente; o tipo determina unidades aceitas; registros inválidos são rejeitados na interface e na API. | DS03, D07 |
| RNF-08 | Obrigatório | Refinado | Conteúdo e gráficos não devem emitir diagnóstico ou recomendação clínica automática. | A interface distingue informação educativa de orientação individual; gráficos descrevem o histórico sem classificar valores como diagnóstico. | B06, D10 |
| RNF-09 | Desejável | Refinado | O código deve ser verificável e manutenível. | TypeScript em modo estrito; regras centrais cobertas por testes automatizados; lint e testes executados antes de cada entrega técnica. | Decisão técnica do projeto |
| RNF-10 | Desejável | Refinado | Falhas devem ser observáveis sem expor informação sensível. | Erros técnicos recebem identificador rastreável; logs não contêm senha, token, mensagem de contato completa ou valores clínicos sem necessidade. | Decisão técnica do projeto |

## Regras de negócio

| ID | Regra | Estado | Consequência |
| --- | --- | --- | --- |
| RN-01 | Cada conta possui um perfil autorizado; paciente e profissional têm cadastros distintos. | Refinada | O perfil controla rotas e ações disponíveis. |
| RN-02 | O conjunto essencial de indicadores é glicemia, pressão arterial, frequência cardíaca e peso. | Confirmada | Tipos adicionais do dataset não ampliam automaticamente o MVP. |
| RN-03 | Um agendamento só pode utilizar horário disponível e futuro. | Refinada | API e banco precisam validar disponibilidade no momento da confirmação. |
| RN-04 | O mesmo horário de um profissional não pode receber dois agendamentos ativos. | Refinada | A garantia deve existir também no banco para evitar concorrência. |
| RN-05 | O paciente só gerencia seus próprios registros de indicadores. | Refinada | Consultas e mutações devem verificar propriedade no servidor. |
| RN-06 | Toda criação, edição ou exclusão apresenta retorno curto e claro. | Confirmada | A interface deve prever estados de processamento, sucesso e erro. |
| RN-07 | Cuidador não acessa dados de outra pessoa até que vínculo, consentimento e permissões sejam definidos. | Pendente | Nenhuma autorização de cuidador será inferida durante a implementação. |
| RN-08 | Conteúdo fornecido é demonstrativo e não substitui avaliação profissional. | Refinada | O produto não interpreta valores nem prescreve conduta. |

## Fora do escopo até decisão explícita

- aplicativo móvel nativo;
- lembretes e cadastro de medicamentos;
- acesso delegado para cuidadores;
- cancelamento ou reagendamento de atendimento;
- interpretação clínica automática de indicadores;
- novos tipos de indicador sugeridos apenas pelo dataset;
- integração de e-mail real sem serviço e credenciais aprovados;
- dados institucionais de contato enquanto houver divergência entre as fontes.

## Rastreabilidade resumida

| Área | Requisitos | Persona principal | CSD |
| --- | --- | --- | --- |
| Conteúdo | RF-01, RF-02, RNF-08 | P01; P02 provisoriamente | C04, D10 |
| Conta e acesso | RF-03 a RF-05, RNF-04 a RNF-06 | P01, P03 | C03, S10, D04 |
| Dashboard | RF-06 | P01 | C11, S03 |
| Agendamento | RF-07 a RF-10, RF-14 | P01, P03 | C05, S02, S04, S09, D05, D11 |
| Indicadores | RF-11, RF-12, RNF-07, RN-02, RN-05 | P01 | C06 a C08, D06, D07 |
| Contato | RF-13 | P01; P02 provisoriamente | C09, S08, D09 |
| Acessibilidade | RNF-01 a RNF-03 | Todos, com prioridade para P01 | C10 |

## Pendências que impedem requisitos definitivos

1. definir ações, vínculo, consentimento e permissões do cuidador;
2. confirmar quem administra a disponibilidade profissional;
3. definir cancelamento e reagendamento;
4. aprovar campos pessoais obrigatórios e suas finalidades;
5. definir unidades e validações dos quatro indicadores com revisão qualificada;
6. decidir se e-mail será real, simulado ou substituído por confirmação no portal;
7. esclarecer se observações ou sintomas pertencem a algum registro do MVP.
