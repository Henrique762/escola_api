from flask import Blueprint, jsonify, request, render_template, url_for, redirect
from datetime import datetime
from alunos.models import NenhumalunoDisponivel, AlunonaoEncontrado, adicionar_aluno, listar_alunos, alterar_dados, deletar_alunos, listar_aluno
from turmas.models import listar_turmas

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos/adicionar', methods=['GET'])
def adicionar_alunos_page():
    turmas = listar_turmas()
    return render_template('alunos/alunos_adicionar.html', turmas=turmas)


@alunos_blueprint.route(("/alunos/"), methods=['GET'])
def list_alunos():
    try:
        alunos = listar_alunos()
        return render_template('alunos/alunos.html', alunos=alunos)
    except NenhumalunoDisponivel:
        return render_template('alunos/alunos.html'), 404

@alunos_blueprint.route(("/alunos/<int:id>"), methods=['GET'])
def list_aluno(id):
    try:
        aluno = listar_aluno(id)
        turmas = listar_turmas()
        return render_template('alunos/alunos_editar.html', aluno=aluno, turmas=turmas)
    except AlunonaoEncontrado:
        return render_template('alunos/alunos.html', alunos=aluno)
    
@alunos_blueprint.route(("/alunos/"), methods=['POST'])
def add_aluno():
    try:
        aluno_forms = request.form
        print(aluno_forms)
        adicionar_aluno(aluno_forms)
        return redirect(url_for('alunos.list_alunos'))
    except Exception as e:
        return jsonify({'Message': 'Erro ao Adicionar o Aluno'})


@alunos_blueprint.route(("/alunos/editar<int:id>"), methods=['PUT', 'POST'])
def alter_aluno(id):
    try:
        aluno = listar_aluno(id)
        aluno_forms = request.form
        alterar_dados(aluno_forms, id)
        return redirect(url_for('alunos.list_alunos'))
    except AlunonaoEncontrado:
        return render_template('alunos/alunos.html', alunos=aluno)

@alunos_blueprint.route(("/alunos/<int:id>"), methods=['DELETE', 'POST'])
def del_alunos(id):
    try:
        resultado = deletar_alunos(id)
        return redirect(url_for('alunos.list_alunos'))
    except:
        {'Message': 'Aluno nao encontrado'}