from flask import Blueprint, jsonify, request
from datetime import datetime
from alunos.models import NenhumalunoDisponivel, AlunonaoEncontrado, adicionar_aluno, listar_alunos, alterar_dados, deletar_alunos, listar_aluno


alunos_blueprint = Blueprint('alunos', __name__)


@alunos_blueprint.route(("/alunos/"), methods=['GET'])
def list_alunos():
    try:
        alunos = listar_alunos()
        return jsonify(alunos)
    except NenhumalunoDisponivel:
        return jsonify({'Message': 'Nenhum Aluno Disponivel'}), 404

@alunos_blueprint.route(("/alunos/<int:id>"), methods=['GET'])
def list_aluno(id):
    try:
        aluno = listar_aluno(id)
        return jsonify(aluno)
    except AlunonaoEncontrado:
        return jsonify({'Message': 'Aluno nao Encontrado'})
@alunos_blueprint.route(("/alunos/"), methods=['POST'])
def add_aluno():
    try:
        aluno_forms = request.json
        data_nascimento = datetime.strptime(aluno_forms['data_nascimento'], "%Y-%m-%d").date()
        aluno_forms['data_nascimento'] = data_nascimento
        ad_aluno = adicionar_aluno(aluno_forms, id)
        return jsonify(ad_aluno), 200
    except:
        pass


@alunos_blueprint.route(("/alunos/"), methods=['PUT'])
def alter_aluno():
    try:
        aluno_forms = request.json
        resultado = alterar_dados(aluno_forms)
        return jsonify(resultado), 200
    except AlunonaoEncontrado:
        return jsonify({'Message': 'Aluno nao Encontrado'})

@alunos_blueprint.route(("/alunos/<int:id>"), methods=['DELETE'])
def del_alunos(id):
    try:
        resultado = deletar_alunos(id)
        return jsonify(resultado), 200
    except:
        {'Message': 'Aluno nao encontrado'}