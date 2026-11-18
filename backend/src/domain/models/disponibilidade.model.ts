export enum StatusDisponibilidade {
  DISPONIVEL = "DISPONIVEL",
  RESERVADA = "RESERVADA",
  INATIVA = "INATIVA",
}

export class DisponibilidadeModel {
  constructor(
    public idDisponibilidade: bigint,
    public idProfissional: bigint,
    public inicioEm: Date,
    public fimEm: Date,
    public status: StatusDisponibilidade,
    public criadoEm: Date,
  ) {}
}
