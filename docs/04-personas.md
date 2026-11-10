# Proto-personas do Vida+Fácil

## Objetivo

Representar os três públicos previstos nas fontes oficiais e orientar requisitos, fluxos, conteúdo e decisões de acessibilidade do Vida+Fácil.

## Limite da pesquisa

O pacote analisado não contém entrevistas ou observações com usuários. Por isso, estes perfis são **proto-personas**: composições provisórias baseadas no Projeto-Teste, briefing, rascunho, matriz CSD e dataset fictício. Os nomes são apenas rótulos de trabalho; não representam pessoas reais. Informações demográficas e comportamentais ausentes nas fontes não foram completadas por invenção.

## P01 — Rosa, pessoa idosa usuária

> Nome de trabalho fictício. Faixa etária confirmada pelas fontes: 60 anos ou mais.

### Papel e contexto

Rosa representa a pessoa idosa que usa a plataforma para acessar conteúdo educativo, marcar atendimentos e registrar indicadores básicos de saúde. As fontes colocam a inclusão digital desse público no centro do produto, mas não informam sua escolaridade, renda, ocupação, condição clínica ou familiaridade tecnológica.

### Objetivos

- encontrar orientações educativas de forma simples;
- localizar um profissional e escolher um horário disponível;
- acompanhar seus próximos atendimentos;
- registrar glicemia, pressão arterial, frequência cardíaca e peso;
- consultar o histórico desses registros em gráficos simples;
- receber confirmação clara após executar uma ação.

### Necessidades de experiência

- navegação simples, previsível e responsiva;
- linguagem direta, sem depender de jargão técnico;
- formulários com rótulos visíveis, instruções e mensagens de erro compreensíveis;
- foco de teclado perceptível e operação sem depender apenas do mouse;
- texto redimensionável, contraste suficiente e alvos de interação confortáveis;
- confirmação inequívoca de cadastro, agendamento e registro de indicador.

Os detalhes de acessibilidade acima são critérios de projeto a validar no Módulo B; as fontes confirmam a obrigação de uma interface acessível, mas não definem métricas específicas.

### Barreiras e riscos a validar

- dificuldade para interpretar campos, unidades ou mensagens ambíguas;
- abandono quando o fluxo exige dados pessoais sem explicar a finalidade;
- confusão entre informação educativa e orientação clínica individual;
- risco de erro ao registrar valores sem unidade, intervalo ou confirmação;
- dificuldade para perceber o resultado de uma ação apenas por mudança visual sutil.

### Fluxos prioritários

1. criar conta e entrar;
2. consultar o dashboard;
3. agendar atendimento;
4. registrar e consultar indicadores;
5. acessar conteúdo educativo;
6. enviar mensagem pelo contato.

### O que ainda não sabemos

- nível de letramento digital e equipamentos utilizados;
- campos obrigatórios aceitáveis no cadastro;
- necessidade de ajuda de cuidador e forma de consentimento;
- unidades, limites e mensagens adequadas para cada indicador;
- necessidade de cancelar ou reagendar atendimentos.

### Base de evidências

CSD C03 a C12; evidências E02, E03, E05, E06, B02, B03, B05, B06, B07 e R04 registradas em `02-evidencias-pesquisa.md`.

## P02 — Alex, pessoa cuidadora

> Nome de trabalho fictício. Idade, gênero, profissão e relação com o paciente não foram definidos pelas fontes.

### Papel e contexto

Alex representa cuidadores formais ou informais citados como público do Vida+Fácil. O material não descreve cadastro, permissões, vínculo com a pessoa cuidada nem ações próprias. Consequentemente, este perfil registra necessidades de pesquisa e não autoriza a implementação de acesso a dados de outra pessoa.

### Objetivos provisórios

- encontrar conteúdo educativo útil ao cuidado;
- compreender como apoiar uma pessoa idosa no uso do serviço;
- acompanhar informações somente quando houver vínculo, consentimento e autorização definidos;
- receber retorno claro sobre ações permitidas e bloqueadas.

### Necessidades de experiência

- distinguir a própria conta da conta da pessoa cuidada;
- saber quais dados pode visualizar ou alterar;
- compreender como solicitar, aceitar e revogar um vínculo;
- encontrar orientação sem assumir responsabilidade clínica;
- receber mensagens que expliquem limites de permissão sem expor dados sensíveis.

### Riscos a validar

- exposição indevida de dados pessoais ou de saúde;
- alteração de agendamentos ou indicadores sem autorização;
- confusão sobre quem realizou determinada ação;
- criação de um fluxo complexo que não seja exigido pelo MVP.

### Fluxos candidatos, ainda não aprovados

1. acessar conteúdo educativo;
2. solicitar ou aceitar vínculo com a pessoa cuidada;
3. consultar ou apoiar ações dentro de permissões explícitas;
4. encerrar ou revogar o vínculo.

Os fluxos 2 a 4 permanecem fora do escopo funcional até a resolução das dúvidas D01 e D02 da matriz CSD.

### O que ainda não sabemos

- quais ações são permitidas;
- se o cuidador possui conta própria;
- quem inicia e aprova o vínculo;
- como o consentimento é registrado e revogado;
- se existe diferença entre cuidador formal e informal no sistema.

### Base de evidências

CSD C03, S05, D01 e D02; evidências E02 e B02 registradas em `02-evidencias-pesquisa.md`.

## P03 — Dani, profissional de saúde

> Nome de trabalho fictício. Idade, gênero e especialidade não foram definidos como perfil único nas fontes.

### Papel e contexto

Dani representa o profissional de saúde cadastrado na plataforma. O rascunho prevê registro profissional, especialidade e disponibilidade, enquanto o agendamento depende da escolha de profissional, data e horário.

### Objetivos

- manter dados profissionais necessários ao serviço;
- informar ou consultar sua disponibilidade;
- visualizar atendimentos agendados;
- evitar conflitos de horário;
- receber feedback claro após alterar informações.

### Necessidades de experiência

- separar dados de identificação, credenciais profissionais e disponibilidade;
- visualizar agenda por data e horário;
- identificar estados do agendamento sem ambiguidade;
- receber validação de conflitos antes da confirmação;
- acessar apenas informações necessárias ao atendimento e autorizadas pelo produto.

### Barreiras e riscos a validar

- duplicidade ou sobreposição de horários;
- falta de definição sobre quem cria e edita a disponibilidade;
- coleta excessiva de dados profissionais;
- ausência de estados para cancelamento e reagendamento;
- acesso a dados de saúde sem regra de autorização definida.

### Fluxos prioritários provisórios

1. criar conta profissional e entrar;
2. consultar ou administrar disponibilidade;
3. visualizar agenda de atendimentos;
4. receber confirmação após atualizações.

### O que ainda não sabemos

- quem valida o registro profissional;
- se o profissional cria sua disponibilidade ou se ela é administrativa;
- quais dados do paciente ficam visíveis;
- quais estados e ações existem no ciclo do atendimento;
- se o profissional participa do registro ou da interpretação dos indicadores.

### Base de evidências

CSD C03, C05, C12, S02, S09, D05 e D07; evidências E02, E03, R02, R03 e R04 registradas em `02-evidencias-pesquisa.md`.

## Relação entre personas e áreas do produto

| Área | Pessoa idosa | Pessoa cuidadora | Profissional de saúde |
| --- | --- | --- | --- |
| Conteúdo educativo | Prioritária | Prevista | Não definida |
| Agendamento | Cria e consulta | A validar | Consulta; disponibilidade a validar |
| Indicadores | Registra e consulta | A validar | Acesso não definido |
| Contato | Previsto | Previsto como hipótese | Não definido |
| Gestão de vínculo | Não definida | Dúvida crítica | Não se aplica nas fontes |

## Hipóteses prioritárias para validação

1. a pessoa idosa é a persona principal do MVP;
2. os fluxos essenciais podem ser concluídos com linguagem direta e poucos passos;
3. o profissional administra a própria disponibilidade;
4. o cuidador precisa de vínculo explícito e revogável para acessar dados de outra pessoa;
5. os quatro indicadores do briefing atendem ao escopo mínimo;
6. confirmações visuais e textuais no portal são necessárias mesmo quando houver e-mail.

## Critérios para evolução destas proto-personas

- registrar a origem de cada nova informação;
- separar achado de pesquisa de decisão de produto;
- não inferir condição clínica, renda, escolaridade ou incapacidade pela idade;
- validar fluxos com participantes dos públicos representados, quando possível;
- revisar as personas quando requisitos ou dúvidas da CSD forem resolvidos.
