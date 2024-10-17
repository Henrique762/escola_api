from config import db

class Alunos(db.Model):
    __tablename__ = "alunos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)

    def __init__(self, nome, idade, turma, data_nascimento):
        self.nome = nome
        self.idade = idade
        self.turma = turma
        self.data_nascimento = data_nascimento

# def adicionar_aluno(aluno_forms):
#     novo_aluno=Alunos(nome=aluno_forms['nome'], idade=aluno_forms['idade'], turma=aluno_forms[''])
