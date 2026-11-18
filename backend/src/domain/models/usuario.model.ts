export enum PerfilUsuario {
  PACIENTE = "PACIENTE",
  PROFISSIONAL = "PROFISSIONAL",
}

export class UsuarioModel {
  constructor(
    public idUsuario: bigint,
    public nome: string,
    public email: string,
    public senhaHash: string,
    public perfil: PerfilUsuario,
    public criadoEm: Date,
  ) {}
}
