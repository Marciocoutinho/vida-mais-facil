import { INestApplication } from '@nestjs/common';
import { Test, TestingModule } from '@nestjs/testing';
import request from 'supertest';
import { App } from 'supertest/types';
import { configureApp } from './../src/app.config';
import { AppModule } from './../src/app.module';

describe('ConteudosEducativosController (e2e)', () => {
  let app: INestApplication<App>;

  beforeAll(async () => {
    const moduleFixture: TestingModule = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();

    app = moduleFixture.createNestApplication();
    configureApp(app);
    await app.init();
  });

  afterAll(async () => {
    await app.close();
  });

  it('/conteudos-educativos (GET)', () => {
    return request(app.getHttpServer())
      .get('/conteudos-educativos')
      .expect(200)
      .expect((response) => {
        expect(response.body).toEqual(expect.any(Array));
        expect(response.body.length).toBeGreaterThan(0);
        expect(response.body[0]).toEqual(
          expect.objectContaining({
            id: expect.any(String),
            titulo: expect.any(String),
            resumo: expect.any(String),
            tipo: expect.any(String),
            url: expect.any(String),
          }),
        );
      });
  });

  it('/conteudos-educativos/999 (GET)', () => {
    return request(app.getHttpServer())
      .get('/conteudos-educativos/999')
      .expect(404)
      .expect((response) => {
        expect(response.body.message).toBe(
          'Conteúdo educativo 999 não encontrado.',
        );
      });
  });

  it('/mensagens-contato (POST) rejects invalid data', () => {
    return request(app.getHttpServer())
      .post('/mensagens-contato')
      .send({
        nome: '   ',
        meioContato: 'teste',
        assunto: '   ',
        mensagem: '   ',
        campoExtra: 'não permitido',
      })
      .expect(400)
      .expect((response) => {
        expect(response.body.message).toEqual(
          expect.arrayContaining([
            'property campoExtra should not exist',
            'nome should not be empty',
            'assunto should not be empty',
            'mensagem should not be empty',
          ]),
        );
      });
  });
});
