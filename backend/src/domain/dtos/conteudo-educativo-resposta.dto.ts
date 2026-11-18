import { TipoConteudoEducativo } from "../models/conteudo-educativo.model";

export class ConteudoEducativoRespostaDto {
  constructor(
    public idConteudo: bigint,
    public titulo: string,
    public resumo: string,
    public tipo: TipoConteudoEducativo,
    public url: string,
    public publicadoEm: Date | null,
  ) {}
}
