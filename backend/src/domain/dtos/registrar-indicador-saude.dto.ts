import { TipoIndicadorSaude } from "../models/indicador-saude.model";

export class RegistrarIndicadorSaudeDto {
  constructor(
    public idPaciente: bigint,
    public tipo: TipoIndicadorSaude,
    public valorPrincipal: number,
    public valorSecundario: number | null,
    public unidade: string,
    public registradoEm: Date,
  ) {}
}
