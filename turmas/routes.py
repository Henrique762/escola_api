from flask import Blueprint, jsonify, request
from turmas.models import adicionar_turmas, listar_turmas, alterar_dados_turma, deletar_turmas, adicionar_turma
from datetime import datetime

turmas_blueprint = Blueprint('turmas', __name__)


@turmas_blueprint.route(("/turmas/"), methods=['GET'])
def list_turmas():
    turmas = listar_turmas()
    return jsonify(turmas)

@turmas_blueprint.route(("/turmas/<int:id>"), methods=['GET'])
def list_turmas(id):
    turmas = listar_turmas()
    return jsonify(turmas)

@turmas_blueprint.route(("/turmas/"), methods=['POST'])
def add_turma():
    turma_forms = request.json
    data_inicio = datetime.strptime(turma_forms['data_inicio'], "%Y-%m-%d").date()
    turma_forms['data_inicio'] = data_inicio
    adicionar_turma(turma_forms, id)
    return jsonify({'message': 'Turma criada com sucesso'}), 200

@turmas_blueprint.route("/turmas/", methods=['PUT'])
def alter_turma():
    turma_forms = request.json
    resultado = alterar_dados_turma(turma_forms)
    return jsonify({'message': f'{resultado}'}), 200

@turmas_blueprint.route(("/turmas/<int:id>"), methods=['DELETE'])
def del_turmas(id):
    print(id)
    resultado = deletar_turmas(id)
    return jsonify(resultado), 200