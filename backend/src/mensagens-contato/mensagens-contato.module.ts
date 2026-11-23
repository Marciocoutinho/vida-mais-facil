import { Module } from '@nestjs/common';
import { MensagensContatoService } from './mensagens-contato.service';
import { MensagensContatoController } from './mensagens-contato.controller';
import { PrismaModule } from '../prisma/prisma.module';

@Module({
  imports: [PrismaModule],
  controllers: [MensagensContatoController],
  providers: [MensagensContatoService],
})
export class MensagensContatoModule {}
