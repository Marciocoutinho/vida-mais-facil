import { Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';
import { CreateMensagemContatoDto } from './dto/create-mensagem-contato.dto';

@Injectable()
export class MensagensContatoService {
  constructor(private readonly prisma: PrismaService) {}

  async create(createMensagemContatoDto: CreateMensagemContatoDto) {
    const registro = await this.prisma.mensagem_contato.create({
      data: {
        nome: createMensagemContatoDto.nome.trim(),
        meio_contato: createMensagemContatoDto.meioContato.trim(),
        assunto: createMensagemContatoDto.assunto.trim(),
        mensagem: createMensagemContatoDto.mensagem.trim(),
      },
    });

    return {
      id: registro.id_mensagem_contato.toString(),
      mensagem: 'Mensagem recebida com sucesso.',
      criadoEm: registro.criado_em,
    };
  }
}
