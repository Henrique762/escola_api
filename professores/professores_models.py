from config import db

class Professores(db.Model):
    __tablename__ = "professores"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(50), nullable=False)
    observacoes = db.Column(db.String(200), nullable=False)

    def __init__(self, nome, idade, materia, observacoes):
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes

    def to_dict(self):
        return {'id': self.id, 
                'nome': self.nome,
                'idade': self.idade,
                'materia': self.materia,
                'observacoes': self.observacoes}
    

def listar_professor(id_professor):
    professor = db.session.query(Professores).filter_by(id=id_professor).first()
    if professor is None:
        return False
    else:
        professor_dict = professor.to_dict()
        return professor_dict
    
def listar_professores():
    professores = Professores.query.all()
    if not professores:
        return []  
    professores_dict = [professor.to_dict() for professor in professores]
    return professores_dict

def adicionar_professor(professor_forms):
    novo_professor = Professores(nome=professor_forms['nome'], idade=professor_forms['idade'], materia=professor_forms['materia'], observacoes=professor_forms['observacoes'])
    db.session.add(novo_professor)
    db.session.commit()

def atualizar_professor(id_professor, dados):
    professor = Professores.query.get(id_professor)
    if not professor:
        return 'Professor não encontrado'
    else:
        professor.nome = dados['nome']
        professor.idade = dados['idade']
        professor.materia = dados['materia']
        professor.observacoes = dados['observacoes']
    db.session.commit()
    return 'Professor atualizado com sucesso'

def excluir_professor(id_professor):
    professor = Professores.query.get(id_professor)
    if not professor:
        return 'Professor não encontrado'
    db.session.delete(professor)
    db.session.commit()
