
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tarefas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)  # libera CORS para o frontend acessar a API
db = SQLAlchemy(app)

# Modelo ORM
class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    status = db.Column(db.String(20), default="pendente")

    def to_dict(self):
        return {"id": self.id, "titulo": self.titulo, "descricao": self.descricao, "status": self.status}

# Criar tabelas
with app.app_context():
    db.create_all()

# Rotas
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    tarefas = Tarefa.query.order_by(Tarefa.id.desc()).all()
    return jsonify([t.to_dict() for t in tarefas])

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json(force=True)
    if not dados or "titulo" not in dados:
        return jsonify({"erro": "Campo 'titulo' é obrigatório"}), 400
    nova = Tarefa(titulo=dados["titulo"], descricao=dados.get("descricao", ""))
    db.session.add(nova)
    db.session.commit()
    return jsonify(nova.to_dict()), 201

@app.route("/tarefas/<int:id>", methods=["PUT"])
def concluir_tarefa(id):
    tarefa = Tarefa.query.get(id)
    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    tarefa.status = "concluída"
    db.session.commit()
    return jsonify(tarefa.to_dict())

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar_tarefa(id):
    tarefa = Tarefa.query.get(id)
    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({"mensagem": "Tarefa deletada!"})

if __name__ == "__main__":
    app.run(debug=True)
