export class CriarDisponibilidadeDto {
  constructor(
    public idProfissional: bigint,
    public inicioEm: Date,
    public fimEm: Date,
  ) {}
}
