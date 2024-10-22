from config import db

class Alunos(db.Model):
    __tablename__ = "alunos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, default=0.0)
    nota_segundo_semestre = db.Column(db.Float, default=0.0)
    media_final = db.Column(db.Float, default=0.0)

    def __init__(self, nome, idade, turma, data_nascimento):
        self.nome = nome
        self.idade = idade
        self.turma = turma
        self.data_nascimento = data_nascimento

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'turma': self.turma,
            'data_nascimento': self.data_nascimento.isoformat(),
            'nota_primeiro_semestre': self.nota_primeiro_semestre,
            'nota_segundo_semestre': self.nota_segundo_semestre,
            'media_final': self.media_final
            }

def adicionar_aluno(aluno_forms):
    novo_aluno=Alunos(nome=aluno_forms['nome'], idade=aluno_forms['idade'], turma=aluno_forms['turma'], data_nascimento=aluno_forms['data_nascimento'])
    db.session.add(novo_aluno)
    db.session.commit()

def listar_alunos():
    alunos = db.session.query(Alunos).all()
    alunos_dict = [aluno.to_dict() for aluno in alunos]
    return alunos_dict

def alterar_dados(aluno_forms):
    if not 'id' in aluno_forms:
        return "Necessario o ID do Aluno"
    aluno_id = aluno_forms['id']
    aluno = db.session.query(Alunos).filter_by(id=aluno_id).first()
    if aluno is None:
        return "Aluno não existe"
    if 'nome' in aluno_forms and aluno_forms['nome']:
        aluno.nome = aluno_forms['nome']

    if 'idade' in aluno_forms and aluno_forms['idade']:
        aluno.idade = aluno_forms['idade']

    if 'turma' in aluno_forms and aluno_forms['turma']:
        aluno.turma = aluno_forms['turma']

    if 'data_nascimento' in aluno_forms and aluno_forms['data_nascimento']:
        aluno.data_nascimento = aluno_forms['data_nascimento']

    if 'nota_primeiro_semestre' in aluno_forms and aluno_forms['nota_primeiro_semestre']:
        aluno.nota_primeiro_semestre = aluno_forms['nota_primeiro_semestre']

    if 'nota_segundo_semestre' in aluno_forms and aluno_forms['nota_segundo_semestre']:
        aluno.nota_segundo_semestre = aluno_forms['nota_segundo_semestre']

    if 'media_final' in aluno_forms and aluno_forms['media_final']:
        aluno.media_final = aluno_forms['media_final']

    db.session.commit()

    return "Aluno atualizado com sucesso"

def deletar_alunos(aluno_forms):
    if not 'id' in aluno_forms:
        return "Necessario o ID do Aluno"
    aluno_id = aluno_forms['id']
    alunos_inexistentes = []
    alunos_excluidos = []
    try:
        for aluno in aluno_id:
            aluno_db = db.session.query(Alunos).filter_by(id=aluno).first()
            if aluno_db is None:
                alunos_inexistentes.append(aluno)
                continue
            db.session.delete(aluno_db)
            alunos_excluidos.append(aluno)

        return f'Aluno/s deletado/s com sucesso {alunos_excluidos}'
    except:
        pass

      

