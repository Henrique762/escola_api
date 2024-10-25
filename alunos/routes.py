from flask import Blueprint, jsonify, request
from datetime import datetime
from alunos.models import adicionar_aluno, listar_alunos, alterar_dados, deletar_alunos, listar_aluno


alunos_blueprint = Blueprint('alunos', __name__)


@alunos_blueprint.route(("/alunos/"), methods=['GET'])
def list_alunos():
    alunos = listar_alunos()
    return jsonify(alunos)

@alunos_blueprint.route(("/alunos/<int:id>"), methods=['GET'])
def list_aluno(id):
    aluno = listar_aluno(id)
    return jsonify(aluno)

@alunos_blueprint.route(("/alunos/"), methods=['POST'])
def add_aluno():
    aluno_forms = request.json
    data_nascimento = datetime.strptime(aluno_forms['data_nascimento'], "%Y-%m-%d").date()
    aluno_forms['data_nascimento'] = data_nascimento
    adicionar_aluno(aluno_forms, id)
    return jsonify({'message': 'Aluno criado com sucesso'}), 200

@alunos_blueprint.route(("/alunos/"), methods=['PUT'])
def alter_aluno():
    aluno_forms = request.json
    resultado = alterar_dados(aluno_forms)
    return jsonify({'message': f'{resultado}'}), 200

@alunos_blueprint.route(("/alunos/<int:id>"), methods=['DELETE'])
def del_alunos(id):
    print(id)
    resultado = deletar_alunos(id)
    return jsonify(resultado), 200