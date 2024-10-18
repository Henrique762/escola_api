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

def adicionar_professor():
    db.session.add(Professores())
    db.session.commit()
