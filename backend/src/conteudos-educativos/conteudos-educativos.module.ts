import { Module } from '@nestjs/common';
import { ConteudosEducativosService } from './conteudos-educativos.service';
import { ConteudosEducativosController } from './conteudos-educativos.controller';
import { PrismaModule } from '../prisma/prisma.module';

@Module({
  imports: [PrismaModule],
  controllers: [ConteudosEducativosController],
  providers: [ConteudosEducativosService],
})
export class ConteudosEducativosModule {}
