from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from turmas.models import adicionar_turma, listar_turma, listar_turmas, atualizar_turma, excluir_turma
from datetime import datetime
from professores.professores_models import listar_professores, listar_professor
from alunos.models import listar_alunos, deletar_alunos

turmas_blueprint = Blueprint('turmas', __name__)

@turmas_blueprint.route('/', methods=['GET'])
def getIndex():
  return render_template('index.html')

@turmas_blueprint.route('/turmas/', methods=['GET'])
def get_turmas():
  turmas = listar_turmas()
  for turma in turmas:
    nomeProfessor = listar_professor(turma['professor'])['nome']
    turma['nomeProfessor'] = nomeProfessor
  return render_template('turmas/turmas.html', turmas=turmas)

@turmas_blueprint.route('/turmas/adicionar', methods=['GET'])
def adicionar_turmas_page():
    professores = listar_professores() 
    return render_template('turmas/turmas_adicionar.html', professores=professores)

@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turmas():
    descricao = request.form['descricao']
    professor = request.form['professor']
    ativo = request.form['ativo']
    if request.form['ativo'] == 'true':
        ativo = True
    else:
        ativo = False

    nova_turma = {'descricao': descricao, 
                    'professor': professor, 
                      'ativo': ativo }
    adicionar_turma(nova_turma)
    return redirect(url_for('turmas.get_turmas'))

@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['PUT', 'POST'])
def update_turma(id_turma):
        try:
            turma = listar_turma(id_turma)
            if(turma):
              descricao = request.form['descricao']
              professor = request.form['professor']
              if request.form['ativo'] == 'true':
                  ativo = True
              else:
                  ativo = False
              turma['descricao'] = descricao
              turma['professor'] = professor
              turma['ativo'] = ativo
              atualizar_turma(id_turma, turma)
              return redirect(url_for('turmas.get_turmas'))
            else:
               return redirect(url_for('turmas.get_turmas')) 
        except:
            return jsonify({'message': 'Turma não encontrada'}), 404

@turmas_blueprint.route('/turmas/delete/<int:id_turma>', methods=['DELETE','POST'])
def delete_turma(id_turma):
        try:
            alunos = listar_alunos()
            for aluno in alunos:
                  if int(aluno['turma']) == int(id_turma):
                      deletar_alunos(aluno['id'])
            excluir_turma(id_turma)
            return redirect(url_for('turmas.get_turmas'))
        except:
            return jsonify({'message': 'Turma não encontrada'}), 404

@turmas_blueprint.route('/turmas/editar/<int:id_turma>', methods=['GET'])
def get_turma_id(id_turma):
        try:
          turma = listar_turma(id_turma)
          nomeProfessor = listar_professor(turma['professor'])['nome']
          turma['nomeProfessor'] = nomeProfessor
          professores = listar_professores()
          if turma:
            return render_template('turmas/turmas_editar.html', turma=turma, professores=professores)
          else:
            return redirect(url_for('turmas.get_turmas'))
        except:
            return jsonify({'message': 'Turma não encontrada'}), 404
