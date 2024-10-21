from flask import jsonify, request
from config import app,db
from professores.models import adicionar_professor
from turmas.models import adicionar_turma

with app.app_context():
    db.create_all()

@app.route("/professores", methods=['GET'])
def add_professor():
    adicionar_professor()
    return jsonify({'message': 'Professor criado com sucesso'})
@app.route("/turmas", methods=['POST'])
def add_turma():
    try:
        turma_forms = request.json
        if not isinstance(turma_forms['descricao'], str) and not isinstance(turma_forms['professor'], str) and not isinstance(turma_forms['ativo'], bool):
            raise FormsError('Erro no Formulário')
    except FormsError:
        return jsonify({'message': 'Formulário Incorreto'})
    return turma_forms

app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])