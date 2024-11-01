import requests
import unittest


class TestAlunoEndpoints(unittest.TestCase):

    BASE_URL = 'http://127.0.0.1:8888'

    def test_000_professor_retorna_lista(self):
        r = requests.get('http://127.0.0.1:8888/professor')
        if r.status_code == 404:
            self.fail("Você não definiu a página /professores no seu server")

        self.assertEqual(r.status_code, 200,
                         "Falha ao buscar lista de Professores")

        self.assertIn('text/html', r.headers['Content-Type'],
                      "Esperava resposta HTML para a lista de professores")
        self.assertIn('<h1>Lista de Professores</h1>', r.text,
                      "Conteúdo HTML esperado não encontrado na resposta")

    def test_001_adiciona_alunos(self):

        response_fernando = requests.post('http://127.0.0.1:8888/alunos', data={
            'nome': 'Fernando',
            'idade': 20,
            'turma_id': 1,
            'data_nascimento': '2000-01-01',
            'nota_primeiro_semestre': 7.5,
            'nota_segundo_semestre': 8.0,
            'media_final': 7.75
        })

        self.assertIn(response_fernando.status_code, [200, 302],
                      "Falha ao adicionar aluno Fernando")

        response_roberto = requests.post(f'{self.BASE_URL}/alunos', data={
            'nome': 'Roberto',
            'idade': 22,
            'turma_id': 1,
            'data_nascimento': '2000-02-01'
        })

        self.assertIn(response_roberto.status_code, [200, 302],
                      "Falha ao adicionar aluno Roberto")

        response_lista = requests.get(f'{self.BASE_URL}/alunos')

        self.assertIn('Fernando', response_lista.text,
                      "Fernando não encontrado na lista")
        self.assertIn('Roberto', response_lista.text,
                      "Roberto não encontrado na lista")

    def test_002_professor_por_id_encontrado(self):
        id_professor = 1
        res = requests.get(f'http://127.0.0.1:8888/professor/{id_professor}')

        self.assertEqual(res.status_code, 200, "Falha ao buscar professor")

        self.assertIn('<h1>Detalhes do Professor</h1>', res.text,
                      "Conteúdo HTML esperado não encontrado na resposta")

    def test_003_professor_por_id_nao_encontrado(self):
        id_professor = 999
        res = requests.get(f'http://127.0.0.1:8888/professor/{id_professor}')

        self.assertEqual(
            res.status_code, 404, "Deveria retornar 404 quando o professor não é encontrado")

        json_data = res.json()
        self.assertEqual(
            json_data['message'], 'Professor não encontrado', "Mensagem de erro inesperada.")

    def test_004_professor_deletado_com_sucesso(self):
        id_professor = 2
        res = requests.post(
            f'http://127.0.0.1:8888/professores/{id_professor}',
            data={'_method': 'DELETE'})

        self.assertEqual(res.status_code, 204, "Falha ao excluir o professor.")

        res = requests.get('http://127.0.0.1:8888/professor')
        self.assertEqual(
            res.status_code, 200, "Falha ao carregar a página de professores após redirecionamento.")

        self.assertIn('text/html', res.headers['Content-Type'],
                      "Esperava resposta HTML para a lista de professores.")
        self.assertIn('<h1>Lista de Professores</h1>', res.text,
                      "Conteúdo HTML esperado não encontrado na resposta final.")

    def test_005_adicionar_professor(self):
        res = requests.get('http://127.0.0.1:8888/professores/novo')

        if res.status_code == 404:
            self.fail(
                "Você não definiu a página /professores/novo no seu server")

        self.assertEqual(res.status_code, 200,
                         "Falha ao buscar página adicionar professor")

        self.assertIn('text/html', res.headers['Content-Type'],
                      "Esperava resposta HTML para a adicionar professor")
        self.assertIn('<h1>Adicionar Novo Professor</h1>', res.text,
                      "Conteúdo HTML esperado não encontrado na resposta")

    def test_006a_id_inexistente_no_put(self):
        id_aluno = 999
        r = requests.post(f'http://localhost:8888/alunos/{id_aluno}/atualizar',
                          data={'nome': 'bowser'})
        self.assertEqual(r.status_code, 404)
        self.assertIn('Aluno não encontrado', r.json().get('error'))

    def test_006b_id_inexistente_no_get(self):
        id_aluno = 999
        r = requests.get(f'http://localhost:8888/alunos/{id_aluno}')
        self.assertEqual(r.status_code, 404)
        json_response = r.json() if r.content else None
        self.assertIsNotNone(json_response)
        self.assertIn('message', json_response)
        self.assertEqual(json_response['message'], 'Aluno não encontrado')

    def test_006c_id_inexistente_no_delete(self):
        id_aluno = 999
        r = requests.post(f'http://localhost:8888/alunos/{id_aluno}',
                          data={'_method': 'DELETE'})
        self.assertEqual(r.status_code, 404)
        json_response = r.json() if r.content else None
        self.assertIsNotNone(json_response)
        self.assertIn('message', json_response)
        self.assertEqual(json_response['message'], 'Aluno não encontrado')

    def test_008a_post_sem_nome(self):

        r = requests.post('http://127.0.0.1:8888/alunos', data={
                          'turma_id': 1, 'data_nascimento': '2000-01-01', 'nota_primeiro_semestre': 10, 'nota_segundo_semestre': 10, 'media_final': 10})

        self.assertEqual(r.status_code, 400)

        self.assertEqual(r.json().get('error'), 'aluno sem nome')

    def test_008b_put_sem_nome(self):

        r = requests.post('http://127.0.0.1:8888/alunos', data={
            'nome': 'maximus',
            'idade': 20,
            'turma_id': 1,
            'data_nascimento': '2000-01-01',
            'nota_primeiro_semestre': 7,
            'nota_segundo_semestre': 8,
            'media_final': 7.5
        })
        self.assertEqual(r.status_code, 200)

        r = requests.post('http://127.0.0.1:8888/alunos/7/atualizar', data={
            'id': 7,
            'idade': 21,
            'turma_id': 1,
            'data_nascimento': '2000-01-01',
            'nota_primeiro_semestre': 9,
            'nota_segundo_semestre': 10,
            'media_final': 9.5
        })
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json().get('error'), 'nome é obrigatório')


if __name__ == '__main__':
    runTests()