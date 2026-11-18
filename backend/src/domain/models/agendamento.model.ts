export class AgendamentoModel {
  constructor(
    public idAgendamento: bigint,
    public idPaciente: bigint,
    public idDisponibilidade: bigint,
    public confirmadoEm: Date,
  ) {}
}
