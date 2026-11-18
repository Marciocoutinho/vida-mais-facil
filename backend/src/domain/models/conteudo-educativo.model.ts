export enum TipoConteudoEducativo {
  ARTIGO = "ARTIGO",
  VIDEO = "VIDEO",
  GUIA = "GUIA",
}

export class ConteudoEducativoModel {
  constructor(
    public idConteudo: bigint,
    public titulo: string,
    public resumo: string,
    public tipo: TipoConteudoEducativo,
    public url: string,
    public publicadoEm: Date | null,
    public ativo: boolean,
  ) {}
}
