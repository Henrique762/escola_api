import requests
import unittest

class TestEndpoints(unittest.TestCase):
    BASE_URL = 'http://127.0.0.1:8888'

    def test_001_listar_professores(self):
        res = requests.get(f'{self.BASE_URL}/professores')
        self.assertEqual(res.status_code, 200, "Falha ao listar professores")
        self.assertIn('text/html', res.headers['Content-Type'], "Esperava resposta HTML para a lista de professores")

    def test_002_adicionar_professor(self):
        data = {'nome': 'Ana', 'idade': 40, 'materia': 'Matemática', 'observacoes': 'Experiente'}
        res = requests.post(f'{self.BASE_URL}/professores', data=data)
        self.assertIn(res.status_code, [200, 302], "Falha ao adicionar novo professor")

    def test_003_atualizar_professor(self):
        professor_id = 1
        data = {'nome': 'José', 'idade': 45, 'materia': 'Física', 'observacoes': 'Atualizado'}
        res = requests.post(f'{self.BASE_URL}/professores/{professor_id}', data=data)
        self.assertIn(res.status_code, [200, 302], "Falha ao atualizar dados do professor")

    def test_004_listar_turmas(self):
        res = requests.get(f'{self.BASE_URL}/turmas/')
        self.assertEqual(res.status_code, 200, "Falha ao listar turmas")
        self.assertIn('text/html', res.headers['Content-Type'], "Esperava resposta HTML para a lista de turmas")

    def test_005_listar_alunos(self):
        res = requests.get(f'{self.BASE_URL}/alunos/')
        self.assertEqual(res.status_code, 200, "Falha ao listar alunos")
        self.assertIn('text/html', res.headers['Content-Type'], "Esperava resposta HTML para a lista de alunos")




if __name__ == '__main__':
    unittest.main()
