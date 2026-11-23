import { Body, Controller, Post } from '@nestjs/common';
import { MensagensContatoService } from './mensagens-contato.service';
import { CreateMensagemContatoDto } from './dto/create-mensagem-contato.dto';

@Controller('mensagens-contato')
export class MensagensContatoController {
  constructor(
    private readonly mensagensContatoService: MensagensContatoService,
  ) {}

  @Post()
  create(@Body() createMensagemContatoDto: CreateMensagemContatoDto) {
    return this.mensagensContatoService.create(createMensagemContatoDto);
  }
}
