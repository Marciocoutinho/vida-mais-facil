import { Injectable, NotFoundException } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';

@Injectable()
export class ConteudosEducativosService {
  constructor(private readonly prisma: PrismaService) {}

  async findAll() {
    const conteudos = await this.prisma.conteudo_educativo.findMany({
      where: { ativo: true },
      orderBy: { publicado_em: 'desc' },
    });

    return conteudos.map((conteudo) => ({
      id: conteudo.id_conteudo.toString(),
      titulo: conteudo.titulo,
      resumo: conteudo.resumo,
      tipo: conteudo.tipo,
      url: conteudo.url,
      publicadoEm: conteudo.publicado_em,
    }));
  }

  async findOne(id: number) {
    const conteudo = await this.prisma.conteudo_educativo.findFirst({
      where: {
        id_conteudo: BigInt(id),
        ativo: true,
      },
    });

    if (!conteudo) {
      throw new NotFoundException(`Conteúdo educativo ${id} não encontrado.`);
    }

    return {
      id: conteudo.id_conteudo.toString(),
      titulo: conteudo.titulo,
      resumo: conteudo.resumo,
      tipo: conteudo.tipo,
      url: conteudo.url,
      publicadoEm: conteudo.publicado_em,
    };
  }
}
