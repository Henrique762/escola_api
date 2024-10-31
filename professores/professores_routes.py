from flask import Blueprint, request, jsonify, render_template, redirect, url_for

from .professores_models import listar_professor, listar_professores, adicionar_professor, atualizar_professor, excluir_professor
from config import db

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route('/', methods=['GET'])
def getIndex():
  return "Meu index"


# @professores_blueprint.route('/professores', methods=['GET'])
# def get_professores():
#   professores = listar_professores()
#   return render_template('professores.html', professores=professores)

@professores_blueprint.route('/professores/adicionar', methods=['GET'])
def adicionar_professores_page():
    return render_template('professores/professores_adicionar.html')

@professores_blueprint.route('/professores', methods=['GET'])
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
