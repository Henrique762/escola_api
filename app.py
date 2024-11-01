from flask import jsonify, request
from config import app,db
from alunos.routes import  alunos_blueprint
from datetime import datetime
from professores.models import adicionar_professor
from alunos.models import adicionar_aluno, listar_alunos, alterar_dados, deletar_alunos, listar_aluno
from turmas.models import adicionar_turma
from turmas.routes import  turmas_blueprint

app.register_blueprint(alunos_blueprint)
app.register_blueprint(turmas_blueprint)

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

app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])

