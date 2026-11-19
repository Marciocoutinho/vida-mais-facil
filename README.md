# Vida+Fácil

Projeto de referência técnica e pedagógica para o simulado da ocupação Aplicações Web e Mobile, desenvolvido no cenário fictício Vida+Fácil / InovaVida Digital.

O projeto será construído de forma incremental, seguindo a ordem dos módulos A, B, C, D, E e F do Projeto-Teste. As decisões serão fundamentadas no briefing, no dataset, nos conteúdos educativos, nos documentos técnicos e na matriz de requisitos e evidências do simulado.

## Estado atual

Os módulos A e B estão concluídos.

O Módulo A — Pesquisa e experiência consolidou os artefatos de pesquisa, matriz CSD, proto-personas, requisitos, casos de uso e navegação em documento Word para avaliação. A entrega passou por inspeção visual de 30 páginas e auditoria estrutural de acessibilidade, sem achados altos, médios ou baixos.

O Módulo B — UX/UI reuniu no Figma wireframes mobile de baixa fidelidade, foundations, design system com componentes reutilizáveis, o protótipo interativo dos fluxos B01–B11, as versões responsivas e o painel de evidências. As justificativas de design foram registradas como anexo da entrega. O protótipo utiliza somente dados fictícios e não possui backend.

O Módulo C — Banco de Dados e Domínio definiu e validou a base MariaDB em Docker, o DER, o diagrama de classes, o dicionário de dados, o DDL, os dados iniciais fictícios e os Models/DTOs TypeScript. A estrutura foi inspecionada por consultas SQL e pelo MySQL Workbench.

Ainda não há API ou interface executável. Os Models e DTOs do Módulo C representam a fundação de domínio para a futura API NestJS.

## Tecnologias previstas

- Next.js e TypeScript no frontend;
- Node.js e NestJS na API;
- Prisma ORM;
- MariaDB;
- Figma para wireframes, protótipo e design system;
- Vercel para publicação, no módulo correspondente.

## Documentação

- [Fontes oficiais e inventário inicial](docs/01-fontes-oficiais.md)
- [Evidências de pesquisa](docs/02-evidencias-pesquisa.md)
- [Matriz CSD](docs/03-matriz-csd.md)
- [Proto-personas](docs/04-personas.md)
- [Requisitos e regras de negócio](docs/05-requisitos.md)
- [Casos de uso](docs/06-casos-de-uso.md)
- [Mapa de navegação](docs/07-mapa-navegacao.md)
- [Checklist de evidências do Módulo A](docs/08-checklist-evidencias.md)
- [Especificação consolidada do Módulo A](docs/entregas/modulo-a/Especificacao_Modulo_A_Vida_Mais_Facil.docx)
- [Entrega do Módulo B — UX/UI](docs/entregas/modulo-b/README.md) — [Justificativas de Design](docs/entregas/modulo-b/Justificativas_de_Design.md) — [Arquivo Figma](https://www.figma.com/design/Gt2sX3sydfR12zF6HALCAS)
- [Dicionário de dados — Módulo C](docs/entregas/modulo-c/Dicionario_de_Dados.md)
- [Especificação de software — Módulo C](docs/entregas/modulo-c/Especificacao_de_Software.md)
- [Evidências — Módulo C](docs/entregas/modulo-c/Evidencias.md)
- [DER — Módulo C](docs/entregas/modulo-c/diagramas/DER_Vida_Mais_Facil.png)
- [Diagrama de classes — Módulo C](docs/entregas/modulo-c/diagramas/Diagrama_de_Classes_Vida_Mais_Facil.png)
- [DDL do banco](database/ddl/001_schema.sql)
- [Dados iniciais fictícios](database/dml/001_seed.sql)

### Entrega do Módulo B

- `01 Wireframes Mobile`: wireframes mobile dos fluxos B01–B11;
- `02 Foundations`: tokens de cor, tipografia, espaçamento, bordas e acessibilidade;
- `03 Components`: biblioteca de componentes e variantes reutilizáveis;
- `04 Prototype Mobile`: fluxos mobile B01–B11;
- `05 Responsive`: adaptações para 360 px, 768 px e 1440 px;
- `06 Evidence`: cobertura dos requisitos, fluxos, responsividade e acessibilidade.

### Entrega do Módulo C

- `01 Modelagem`: DER e diagrama de classes com cardinalidades e enums;
- `02 Banco de dados`: dicionário de dados, DDL e dados iniciais fictícios;
- `03 Ambiente local`: MariaDB em Docker, porta `3307` e verificação de saúde;
- `04 Domínio`: Models e DTOs TypeScript organizados em `backend/src/domain`;
- `05 Evidências`: consultas SQL, validação relacional e inspeção no MySQL Workbench.

## Autoria

Marcio Coutinho
