export enum TipoIndicadorSaude {
  GLICEMIA = "GLICEMIA",
  PRESSAO_ARTERIAL = "PRESSAO_ARTERIAL",
  FREQUENCIA_CARDIACA = "FREQUENCIA_CARDIACA",
  PESO = "PESO",
}

export class IndicadorSaudeModel {
  constructor(
    public idIndicador: bigint,
    public idPaciente: bigint,
    public tipo: TipoIndicadorSaude,
    public valorPrincipal: number,
    public valorSecundario: number | null,
    public unidade: string,
    public registradoEm: Date,
    public criadoEm: Date,
  ) {}
}
