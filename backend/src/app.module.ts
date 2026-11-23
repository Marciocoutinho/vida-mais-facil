import { Module } from '@nestjs/common';
import { ConteudosEducativosModule } from './conteudos-educativos/conteudos-educativos.module';
import { PrismaModule } from './prisma/prisma.module';
import { MensagensContatoModule } from './mensagens-contato/mensagens-contato.module';

@Module({
  imports: [PrismaModule, ConteudosEducativosModule, MensagensContatoModule],
})
export class AppModule {}
