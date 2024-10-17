from config import db

class Professores(db.Model):
    __tablename__ = "professores"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)

def adicionar_professor():
    db.session.add(Professores())
    db.session.commit()
