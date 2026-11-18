import { PerfilUsuario } from "../models/usuario.model";

export class CriarUsuarioDto {
  constructor(
    public nome: string,
    public email: string,
    public senha: string,
    public perfil: PerfilUsuario,
  ) {}
}
