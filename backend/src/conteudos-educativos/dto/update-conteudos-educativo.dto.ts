import { PartialType } from '@nestjs/mapped-types';
import { CreateConteudosEducativoDto } from './create-conteudos-educativo.dto';

export class UpdateConteudosEducativoDto extends PartialType(CreateConteudosEducativoDto) {}
