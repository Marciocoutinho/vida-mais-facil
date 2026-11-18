import { PerfilUsuario } from "../models/usuario.model";

export class UsuarioRespostaDto {
  constructor(
    public idUsuario: bigint,
    public nome: string,
    public email: string,
    public perfil: PerfilUsuario,
    public criadoEm: Date,
  ) {}
}
