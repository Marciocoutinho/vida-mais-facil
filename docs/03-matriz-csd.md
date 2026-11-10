# Matriz CSD do Vida+Fácil

## Objetivo

A matriz CSD separa certezas, suposições e dúvidas para impedir que uma decisão de produto seja apresentada como fato. Cada item aponta para as evidências registradas em `02-evidencias-pesquisa.md`.

## Certezas

| ID | Certeza | Evidência | Consequência |
| --- | --- | --- | --- |
| C01 | O produto se chama Vida+Fácil e pertence ao cenário fictício da InovaVida Digital. | E01 | Usar esses nomes em todos os artefatos. |
| C02 | O produto é uma plataforma web. | B01 e F-BR | Não planejar aplicativo móvel nativo no MVP. |
| C03 | Os públicos são pessoas idosas 60+, cuidadores e profissionais de saúde. | E02 e B02 | Representar os três grupos na pesquisa e nos fluxos. |
| C04 | O MVP inclui conteúdo educativo. | E03 e B03 | Prever acesso a artigos, vídeos ou materiais equivalentes. |
| C05 | O MVP inclui agendamento de atendimentos. | E03 e R03 | Representar escolha de profissional e horário livre. |
| C06 | O paciente registra indicadores de saúde manualmente. | E03 e B05 | Criar fluxo simples de registro pelo paciente. |
| C07 | Glicemia, pressão arterial, frequência cardíaca e peso formam o conjunto esperado no briefing. | B05 | Projetar esses quatro indicadores, sem ampliar pelo dataset. |
| C08 | O histórico deve apresentar gráficos simples. | B06 | Prever visualização histórica acessível e sem diagnóstico. |
| C09 | O MVP inclui formulário de contato. | B07 | Representar o envio e o retorno ao usuário. |
| C10 | A interface deve ser acessível e responsiva. | E06 e B01 | Tratar acessibilidade e responsividade desde os requisitos. |
| C11 | As telas mínimas incluem início, registro, login, dashboard do cliente e agendamento. | E05 | Cobrir essas telas no mapa de navegação e no protótipo. |
| C12 | Ações de criação, edição e exclusão devem apresentar feedback curto e claro. | R04 | Definir estados de sucesso e erro nos critérios de aceite. |
| C13 | O Módulo A tem duração oficial de 4 horas. | D01 resolvida | Usar 4 horas como referência; 2 horas pertence ao roteiro adaptado. |
| C14 | O Módulo A entrega personas, CSD, requisitos, casos de uso e navegação. | E08, E09 e M02 a M05 | Não encerrar o módulo sem esses artefatos. |
| C15 | O dataset é fictício e contém problemas de qualidade e segurança. | DS01 a DS04 | Não copiá-lo diretamente para produção nem para o modelo físico. |

## Suposições a validar

| ID | Suposição | Base | Como validar |
| --- | --- | --- | --- |
| S01 | A pessoa idosa será a persona principal. | O foco declarado é inclusão digital de pessoas idosas. | Comparar prioridade dos fluxos e confirmar com o instrutor. |
| S02 | O profissional administrará sua própria disponibilidade. | O rascunho inclui disponibilidade no cadastro profissional. | Definir caso de uso e regra de autorização. |
| S03 | O dashboard priorizará próximo atendimento, indicadores recentes e conteúdo. | As fontes citam esses três eixos, mas não definem hierarquia. | Validar no wireframe do Módulo B. |
| S04 | A confirmação de agendamento poderá ser exibida no portal quando o envio real de e-mail não estiver disponível. | A matriz condiciona o canal ao ambiente permitido. | Confirmar infraestrutura e critério de avaliação. |
| S05 | O cuidador poderá apoiar uma pessoa idosa vinculada. | O cuidador é público oficial, mas não possui fluxo definido. | Obter regra de vínculo, consentimento e permissões. |
| S06 | Os quatro indicadores do briefing serão suficientes para o MVP. | O rascunho exige no mínimo três; o briefing lista quatro. | Confirmar na especificação e na ficha de avaliação. |
| S07 | O gráfico usará uma série temporal simples para cada indicador. | O briefing pede gráficos simples. | Validar legibilidade e utilidade no protótipo. |
| S08 | O formulário de contato persistirá uma mensagem ou simulará envio com confirmação. | O destino não é definido. | Confirmar ambiente e necessidade de persistência. |
| S09 | O profissional será filtrado por especialidade, data e horário. | O rascunho descreve esses filtros. | Validar necessidade e custo no fluxo principal. |
| S10 | O cadastro coletará somente dados essenciais para o MVP. | O rascunho lista CPF e endereço completo, mas não justifica cada campo. | Aplicar minimização de dados na especificação. |

## Dúvidas

| ID | Dúvida | Impacto | Próxima ação |
| --- | --- | --- | --- |
| D01 | Quais ações o cuidador pode realizar e para quem? | Afeta personas, autorização, telas e banco. | Solicitar decisão de produto antes dos módulos C e D. |
| D02 | Como funciona o vínculo e o consentimento entre cuidador e paciente? | Pode expor dados pessoais e de saúde indevidamente. | Definir regra explícita e testes de autorização. |
| D03 | O lembrete de medicamentos pertence ao MVP? | Exigiria medicamento, horário, prescrição e canal de envio. | Manter fora do modelo até obter regra completa. |
| D04 | Quais campos pessoais são realmente obrigatórios no cadastro? | Afeta privacidade, formulário e banco. | Revisar CPF, endereço e telefone pela necessidade do fluxo. |
| D05 | Qual é a regra para cancelar ou reagendar? | Afeta agenda, estados e disponibilidade. | Consultar ficha ou registrar decisão de produto. |
| D06 | O que significa “observações ou sintomas” e a que registro pertence? | Afeta estrutura e risco de armazenar informação sensível sem contexto. | Esclarecer antes da modelagem. |
| D07 | Quais unidades e validações cada indicador utiliza? | Afeta formulário, histórico, API e banco. | Derivar das fontes técnicas ou definir com revisão qualificada. |
| D08 | Mapa de navegação e jornada do cliente são ambos obrigatórios? | Afeta tempo e evidências do Módulo A. | Consultar a ficha oficial de avaliação. |
| D09 | Qual contato institucional fictício deve aparecer no produto? | As fontes apresentam dados diferentes. | Escolher dados canônicos antes do Módulo E. |
| D10 | Quem revisa e aprova o conteúdo educativo? | Os textos não apresentam referências clínicas. | Tratar como conteúdo demonstrativo até revisão. |
| D11 | O e-mail será real, simulado ou substituído por feedback no portal? | Afeta infraestrutura, testes e publicação. | Confirmar ambiente disponível. |
| D12 | Entrevistas e observações serão fornecidas separadamente? | Sem elas, as personas não podem alegar validação com usuários. | Manter personas como composições provisórias e registrar a lacuna. |

## Critério de uso

- Certezas podem orientar requisitos, desde que preservem o sentido da fonte.
- Suposições precisam de validação antes de virarem regra de negócio definitiva.
- Dúvidas devem permanecer visíveis na especificação e não podem ser preenchidas por invenção.
