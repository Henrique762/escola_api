from flask import Blueprint, request, jsonify, render_template, redirect, url_for

from .professores_models import listar_professor, listar_professores, adicionar_professor, atualizar_professor, excluir_professor
from config import db

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route('/', methods=['GET'])
def getIndex():
  return render_template('index.html')

@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
  professores = listar_professores()
  return render_template('professores/professores.html', professores=professores)

@professores_blueprint.route('/professores/adicionar', methods=['GET'])
def adicionar_professores_page():
    return render_template('professores/professores_adicionar.html')

@professores_blueprint.route('/professores', methods=['POST'])
def create_professores():
    nome = request.form['nome']
    idade = request.form['idade']
    materia = request.form['materia']
    observacoes = request.form['observacoes']

    novo_professor = {'nome': nome, 
                      'idade': idade, 
                      'materia': materia, 
                      'observacoes': observacoes }
    adicionar_professor(novo_professor)
    return redirect(url_for('professores.get_professores'))

@professores_blueprint.route('/professores/<int:id_professor>', methods=['PUT', 'POST'])
def update_professor(id_professor):
        try:
            professor = listar_professor(id_professor)
            if(professor):
              nome = request.form['nome']
              idade = request.form['idade']
              materia = request.form['materia']
              observacoes = request.form['observacoes']

              professor['nome'] = nome
              professor['idade'] = idade
              professor['materia'] = materia
              professor['observacoes'] = observacoes
              atualizar_professor(id_professor, professor)
              return redirect(url_for('professores.get_professores'))
            else:
               return redirect(url_for('professores.get_professores')) 
        except:
            return jsonify({'message': 'Professor não encontrado'}), 404


@professores_blueprint.route('/professores/delete/<int:id_professor>', methods=['DELETE','POST'])
def delete_professor(id_professor):
        try:
            excluir_professor(id_professor)
            return redirect(url_for('professores.get_professores'))
        except:
            return jsonify({'message': 'Professor não encontrado'}), 404

@professores_blueprint.route('/professores/editar/<int:id_professor>', methods=['GET'])
def get_professor_id(id_professor):
        try:
          professor = listar_professor(id_professor)
          if professor:
            return  render_template('professores/professores_editar.html', professor=professor)
          else:
            return redirect(url_for('professores.get_professores'))
        except:
            return jsonify({'message': 'Professor não encontrado vbnvb'}), 404