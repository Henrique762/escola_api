from flask import jsonify, request
from config import app,db
from alunos.routes import  alunos_blueprint
from datetime import datetime
from professores.professores_models import adicionar_professor
from alunos.models import adicionar_aluno, listar_alunos, alterar_dados, deletar_alunos, listar_aluno
from turmas.models import adicionar_turma
from professores.professores_routes import professores_blueprint
from turmas.routes import  turmas_blueprint

app.register_blueprint(alunos_blueprint)
app.register_blueprint(professores_blueprint)
app.register_blueprint(turmas_blueprint)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])