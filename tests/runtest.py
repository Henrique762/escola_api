import requests
import unittest

class TestEndpoints(unittest.TestCase):
    BASE_URL = 'http://127.0.0.1:8888'

    def test_001_adicionar_aluno_page(self):
        res = requests.get(f'{self.BASE_URL}/alunos/adicionar')
        self.assertEqual(res.status_code, 200, "Falha ao carregar a página de adição de alunos")
        self.assertIn('text/html', res.headers['Content-Type'], "Esperava resposta HTML para a página de adição de alunos")

    def test_002_listar_alunos(self):
        res = requests.get(f'{self.BASE_URL}/alunos/')
        self.assertEqual(res.status_code, 200, "Falha ao listar alunos")
        self.assertIn('text/html', res.headers['Content-Type'], "Esperava resposta HTML para a lista de alunos")
    

    def test_004_adicionar_aluno(self):
        data = {
            'nome': 'João',
            'idade': 18,
            'turma_id': 1,
            'data_nascimento': '2005-01-01'
        }
        res = requests.post(f'{self.BASE_URL}/alunos/', data=data)
        self.assertIn(res.status_code, [200, 302], "Falha ao adicionar novo aluno")

    def test_005_atualizar_aluno_com_notas(self):
        aluno_id = 1
        data = {
            'nome': 'João',
            'idade': 18,
            'turma_id': 1,
            'data_nascimento': '2005-01-01',
            'nota_primeiro_semestre': 8.5,
            'nota_segundo_semestre': 9.0,
            'media_final': 8.75
        }
        res = requests.post(f'{self.BASE_URL}/alunos/editar/{aluno_id}', data=data)
        self.assertIn(res.status_code, [200, 302], "Falha ao atualizar dados do aluno com notas")

    def test_006_deletar_aluno(self):
        aluno_id = 2
        res = requests.post(f'{self.BASE_URL}/alunos/{aluno_id}', data={'_method': 'DELETE'})
        self.assertIn(res.status_code, [200, 302], "Falha ao deletar aluno")

    def test_007_listar_professores(self):
        res = requests.get(f'{self.BASE_URL}/professores')
        self.assertEqual(res.status_code, 200, "Falha ao listar professores")
        self.assertIn('text/html', res.headers['Content-Type'], "Esperava resposta HTML para a lista de professores")

    def test_008_adicionar_professor(self):
        data = {'nome': 'Ana', 'idade': 40, 'materia': 'Matemática', 'observacoes': 'Experiente'}
        res = requests.post(f'{self.BASE_URL}/professores', data=data)
        self.assertIn(res.status_code, [200, 302], "Falha ao adicionar novo professor")

    def test_009_atualizar_professor(self):
        professor_id = 1
        data = {'nome': 'José', 'idade': 45, 'materia': 'Física', 'observacoes': 'Atualizado'}
        res = requests.post(f'{self.BASE_URL}/professores/{professor_id}', data=data)
        self.assertIn(res.status_code, [200, 302], "Falha ao atualizar dados do professor")

    def test_010_deletar_professor(self):
        professor_id = 1
        res = requests.post(f'{self.BASE_URL}/professores/delete/{professor_id}', data={'_method': 'DELETE'})
        self.assertIn(res.status_code, [200, 302], "Falha ao deletar professor")

    def test_011_listar_turmas(self):
        res = requests.get(f'{self.BASE_URL}/turmas/')
        self.assertEqual(res.status_code, 200, "Falha ao listar turmas")
        self.assertIn('text/html', res.headers['Content-Type'], "Esperava resposta HTML para a lista de turmas")

    def test_012_adicionar_turma(self):
        data = {'descricao': 'Turma A', 'professor': 1, 'ativo': 'true'}
        res = requests.post(f'{self.BASE_URL}/turmas', data=data)
        self.assertIn(res.status_code, [200, 302], "Falha ao adicionar nova turma")

    def test_013_atualizar_turma(self):
        turma_id = 1
        data = {'descricao': 'Turma B', 'professor': 2, 'ativo': 'false'}
        res = requests.post(f'{self.BASE_URL}/turmas/{turma_id}', data=data)
        self.assertIn(res.status_code, [200, 302], "Falha ao atualizar dados da turma")

    def test_014_deletar_turma(self):
        turma_id = 2
        res = requests.post(f'{self.BASE_URL}/turmas/delete/{turma_id}', data={'_method': 'DELETE'})
        self.assertIn(res.status_code, [200, 302], "Falha ao deletar turma")


if __name__ == '__main__':
    unittest.main()