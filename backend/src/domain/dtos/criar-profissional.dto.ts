export class CriarProfissionalDto {
  constructor(
    public idUsuario: bigint,
    public idEspecialidade: bigint,
    public registroProfissional: string,
  ) {}
}
