from config import db

class Turmas(db.Model):
    __tablename__ = "turmas"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    descricao = db.Column(db.String)
    professor = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    def __init__(self, descricao, professor, ativo):
        self.descricao = descricao
        self.professor = professor
        self.ativo = ativo