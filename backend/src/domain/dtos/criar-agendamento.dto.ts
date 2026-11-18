export class CriarAgendamentoDto {
  constructor(
    public idPaciente: bigint,
    public idDisponibilidade: bigint,
  ) {}
}
