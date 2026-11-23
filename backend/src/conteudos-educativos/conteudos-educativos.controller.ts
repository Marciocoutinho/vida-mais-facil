import { Controller, Get, Param, ParseIntPipe } from '@nestjs/common';
import { ConteudosEducativosService } from './conteudos-educativos.service';

@Controller('conteudos-educativos')
export class ConteudosEducativosController {
  constructor(
    private readonly conteudosEducativosService: ConteudosEducativosService,
  ) {}

  @Get()
  findAll() {
    return this.conteudosEducativosService.findAll();
  }

  @Get(':id')
  findOne(@Param('id', ParseIntPipe) id: number) {
    return this.conteudosEducativosService.findOne(id);
  }
}
