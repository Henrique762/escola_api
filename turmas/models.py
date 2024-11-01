from config import db

class Turmas(db.Model):
    __tablename__ = "turmas"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    descricao = db.Column(db.String)
    professor = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False, default=False)

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

def listar_turma(id_turma):
    turma = db.session.query(Turmas).filter_by(id=id_turma).first()
    if turma is None:
        return False
    else:
        turma_dict = turma.to_dict()
        return turma_dict

def listar_turmas():
    turmas = Turmas.query.all()
    turmas_dict = [turma.to_dict() for turma in turmas]
    return turmas_dict

def adicionar_turma(turma_forms):
    nova_turma = Turmas(descricao=turma_forms['descricao'], professor=turma_forms['professor'], ativo=turma_forms['ativo'])
    db.session.add(nova_turma)
    db.session.commit()

def atualizar_turma(id_turma, dados):
    turma = Turmas.query.get(id_turma)
    if not turma:
        return 'Turma não encontrada'
    else:
        turma.descricao = dados['descricao']
        turma.professor = dados['professor']
        turma.ativo = dados['ativo']
    db.session.commit()
    return 'Turma atualizada com sucesso'

def excluir_turma(id_turma):
    turma = Turmas.query.get(id_turma)
    if not turma:
        return 'Turma não encontrado'
    db.session.delete(turma)
    db.session.commit()