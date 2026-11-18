export class MensagemContatoModel {
  constructor(
    public idMensagemContato: bigint,
    public nome: string,
    public meioContato: string,
    public assunto: string,
    public mensagem: string,
    public criadoEm: Date,
  ) {}
}
