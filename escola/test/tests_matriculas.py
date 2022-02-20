from rest_framework.test import APITestCase
from escola.models import Matricula, Aluno, Curso
from django.urls import reverse
from rest_framework import status


class MatriculasTestCase(APITestCase):

  def setUp(self):
    self.list_url = reverse('Matriculas-list')

    self.aluno_1 = Aluno.objects.create(
        nome='Aluno 1',
        rg='501184077',
        cpf='95637601070',
        data_nascimento='1996-07-16'
      )
    self.aluno_2 = Aluno.objects.create(
      nome='Aluno 2',
      rg='424930274',
      cpf='01652673059',
      data_nascimento='1996-07-16'
    )

    self.curso_1 = Curso.objects.create(
      codigo_curso='CTT1',
      descricao='Curso teste 1',
      nivel='B'
    )
    self.curso_2 = Curso.objects.create(
      codigo_curso='CTT2',
      descricao='Curso teste 2',
      nivel='A'
    )

    self.matricula_1 = Matricula.objects.create(
      aluno=self.aluno_1,
      curso=self.curso_2,
      periodo='M'
    )
    self.matricula_2 = Matricula.objects.create(
      aluno=self.aluno_2,
      curso=self.curso_1,
      periodo='N'
    )

  def test_requisicao_get_lista_Matriculas(self):
    """Garante que conseguimos retornar uma lista de matriculas"""
    response = self.client.get(self.list_url)
    self.assertEquals(response.status_code, status.HTTP_200_OK)


  def test_post_cria_matricula_de_aluno(self):
    """Garante que um aluno será matriculado em um curso"""
    data = {
      'aluno': self.aluno_1.pk,
      'curso': self.curso_2.pk,
      'periodo': 'M'
    }

    response = self.client.post(self.list_url, data)
    self.assertEquals(response.status_code, status.HTTP_201_CREATED)

  
  def test_put_altera_matricula(self):
    """Garate que a matricula de um aluno será alterada"""
    data = {
      'aluno': self.aluno_1.pk,
      'curso': self.curso_2.pk,
      'periodo': 'V'
    }

    response = self.client.put('/matriculas/1/', data)
    self.assertEquals(response.status_code, status.HTTP_200_OK)

  def test_matricula_nao_pode_ser_deletada(self):
    """Garante que uma matricula deletada ao enviar uma requisição DELETE"""
    response = self.client.delete('/matriculas/1/')
    self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

  
  def test_lista_matriculas_aluno(self):
    """Garante que podemos retornar as matriculas de um aluno"""
    response = self.client.get('/alunos/1/matriculas/')
    self.assertEquals(response.status_code, status.HTTP_200_OK)

  def test_lista_alunos_matriculados_em_um_curso(self):
    """Garante que podemos retornar os alunos matriculados em um curso"""
    response = self.client.get('/cursos/1/matriculas/')
    self.assertEquals(response.status_code, status.HTTP_200_OK)