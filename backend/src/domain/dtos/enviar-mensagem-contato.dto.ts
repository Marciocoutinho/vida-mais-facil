export class EnviarMensagemContatoDto {
  constructor(
    public nome: string,
    public meioContato: string,
    public assunto: string,
    public mensagem: string,
  ) {}
}
