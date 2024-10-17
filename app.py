from flask import jsonify
from config import app,db
from professores.models import adicionar_professor

with app.app_context():
    db.create_all()

@app.route("/professores", methods=['GET'])
def add_professor():
    adicionar_professor()
    return jsonify({'message': 'Professor criado com sucesso'})
app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])