from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from turmas.models import adicionar_turma, listar_turma, listar_turmas, atualizar_turma, excluir_turma
from datetime import datetime

turmas_blueprint = Blueprint('turmas', __name__)


@turmas_blueprint.route('/', methods=['GET'])
def getIndex():
  return render_template('index.html')

@turmas_blueprint.route('/turmas', methods=['GET'])
def get_professores():
  turmas = listar_turmas()
  return render_template('turmas/turmas.html', turmas=turmas)

@turmas_blueprint.route('/turmas/adicionar', methods=['GET'])
def adicionar_turmas_page():
    return render_template('turmas/turmas_adicionar.html')

@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turmas():
    descricao = request.form['descricao']
    professor = request.form['professor']
    ativo = request.form['ativo']

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
              ativo = request.form['ativo']

              turma['descricao'] = descricao
              turma['professor'] = professor
              turma['ativo'] = ativo
              atualizar_turma(id_turma, turma)
              return redirect(url_for('turmas.get_turmas'))
            else:
               return redirect(url_for('turmas.get_turmas')) 
        except:
            return jsonify({'message': 'Turma não encontrada'}), 404

@turmas_blueprint.route('/turmas/delete/<int:id_turmas>', methods=['DELETE','POST'])
def delete_turma(id_turma):
        try:
            excluir_turma(id_turma)
            return redirect(url_for('turmas.get_turmas'))
        except:
            return jsonify({'message': 'Turma não encontrada'}), 404

@turmas_blueprint.route('/turmas/editar/<int:id_turma>', methods=['GET'])
def get_turma_id(id_turma):
        try:
          professor = listar_turma(id_turma)
          if professor:
            return  render_template('turmas/turmas_editar.html', professor=professor)
          else:
            return redirect(url_for('turmas.get_turmas'))
        except:
            return jsonify({'message': 'Turma não encontrada'}), 404