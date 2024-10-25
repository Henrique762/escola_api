from config import db

class Turmas(db.Model):
    __tablename__ = "turmas"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    descricao = db.Column(db.String)
    ativo = db.Column(db.Boolean, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)

    def __init__(self, descricao, professor, ativo):
        self.descricao = descricao
        self.professor = professor
        self.ativo = ativo

    def to_dict(self):
        return{
            'id': self.id,
            'descricao': self.descricao,
            'professor': self.professor,
            'ativo': self.ativo
        }

def adicionar_turma(turma_forms):
    nova_turma=Turmas(descricao=turma_forms['descricao'], professor=turma_forms['professor'], ativo=turma_forms['ativo'])
    db.session.add(nova_turma)
    db.session.commit()

def listar_turmas():
    turmas = db.session.query(Turmas).all()
    turmas_dict = [turma.to_dict() for turma in turmas]
    return turmas_dict

def alterar_dados(turma_forms):
    if not 'id' in turma_forms:
        return "Necessario o ID da Turma"
    turma_id = turma_forms['id']
    turma = db.session.query(Turmas).filter_by(id=aluno_id).first()
    if turma is None:
        return "Turma não existe"
    if 'descricao' in turma_forms and turma_forms['descricao']:
        turma.descricao = turma_forms['descricao']

    if 'professor' in turma_forms and turma_forms['professor']:
        turma.professor = turma_forms['professor'] 

    if 'ativo' in turma_forms and turma_forms['ativo']:
        turma.ativo = turma_forms['ativo']       

    db.session.commit()    

    return "Turma atualizada com sucesso"

def deletar_turmas(turma_forms):
    # turma_db = db.session.query(Turmas).filter_by(id=11).first()
    # db.session.delete(turma_db)
    # db.session.commit()
    # return "Turma Deletada"
    if not 'id' in turma_forms:
        return "Necessário o ID da Turma"
    turma_id = turma_forms['id']
    if not isinstance(turma_id, list):
        turma_id = [turma_id]
    print(turma_id)
    turmas_inexistentes = []
    turmas_excluidas = []
    #try:
    for turma in turma_id:
        turma_db = db.session.query(Turmas).filter_by(id=turma).first()
        if turma_db is None:
            print(turma_db)
            turmas_inexistentes.append(turma_db)
            return f'"Turmas não existem": {turmas_inexistentes}'
         #     continue
        # else:
        #     db.session.delete(turma_db)
        #     db.session.commit()
        #     turmas_excluidos.append(turma)
        #     return f'turma/s deletada/s com sucesso {turmas_excluidas}'
    # except:
    #     pass