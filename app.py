from flask import jsonify, request
from config import app,db
from datetime import datetime
from professores.models import adicionar_professor
from alunos.models import adicionar_aluno, listar_alunos, alterar_dados, deletar_alunos
from turmas.models import adicionar_turma

with app.app_context():
    db.create_all()

@app.route("/professores", methods=['GET'])
def add_professor():
    adicionar_professor()
    return jsonify({'message': 'Professor criado com sucesso'}), 200
@app.route("/turmas", methods=['POST'])
def add_turma():
    turma_forms = request.json
    print(turma_forms)
    adicionar_turma(turma_forms)
    return jsonify({'message': 'Turma criada com sucesso'}), 200


### ALUNOS ROUTES

@app.route(("/alunos"), methods=['GET'])
def list_alunos():
    alunos = listar_alunos()
    return jsonify(alunos)

@app.route(("/alunos"), methods=['POST'])
def add_aluno():
    aluno_forms = request.json
    data_nascimento = datetime.strptime(aluno_forms['data_nascimento'], "%Y-%m-%d").date()
    aluno_forms['data_nascimento'] = data_nascimento
    print(aluno_forms)
    adicionar_aluno(aluno_forms)
    return jsonify({'message': 'Aluno criado com sucesso'}), 200

@app.route(("/alunos"), methods=['PUT'])
def alter_aluno():
    aluno_forms = request.json
    resultado = alterar_dados(aluno_forms)
    return jsonify({'message': f'{resultado}'}), 200

@app.route(("/alunos"), methods=['DELETE'])
def del_alunos():
    aluno_forms = request.json
    resultado = deletar_alunos(aluno_forms)
    return jsonify({'message':{
        f'{resultado}'}}), 200

app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])