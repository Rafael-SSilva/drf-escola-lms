from rest_framework.test import APITestCase
from escola.models import Aluno
from django.urls import reverse
from rest_framework import status


class AlunosTestCase(APITestCase):

  def setUp(self):
    self.list_url = reverse('Alunos-list')
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

  def test_requisicao_get_lista_alunos(self):
    """garante que conseguimos retornar uma lista de alunos"""
    response = self.client.get(self.list_url)
    self.assertEquals(response.status_code, status.HTTP_200_OK)


  def test_post_cria_novo_aluno(self):
    """Garate que um aluno será criado ao enviar uma requisição POST"""
    data = {
      'nome': 'Aluno 3',
      'rg': '130967919',
      'cpf': '97494831037',
      'data_nascimento': '1980-04-21'
    }

    response = self.client.post(self.list_url, data)
    self.assertEquals(response.status_code, status.HTTP_201_CREATED)

  
  def test_put_altera_aluno_existente(self):
    """Garate que os dados de um aluno será alterado ao enviar um PUT com os novos dados"""
    data = {
      'nome': 'Aluno 1',
      'rg': '130967919',
      'cpf': '97494831037',
      'data_nascimento': '1980-04-21'
    }

    response = self.client.put('/alunos/1/', data)
    self.assertEquals(response.status_code, status.HTTP_200_OK)

  def test_delete_nao_exclui_aluno(self):
    """Garante que um aluno não será deleteado ao enviar uma requisição DELETE"""
    response = self.client.delete('/alunos/1/')
    self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
  