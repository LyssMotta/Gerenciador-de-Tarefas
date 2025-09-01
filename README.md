Gerenciador de Tarefas Full Stack

🚀 Projeto Gerenciador de Tarefas — Aplicação full stack construída com Python (Flask + SQLAlchemy ORM) e JavaScript (HTML + CSS + JS). Permite criar, listar, atualizar e excluir tarefas em um banco SQLite, com API REST no back-end e interface web simples e funcional no front-end.

💻 Tecnologias Utilizadas

Python com Flask para o back-end

SQLAlchemy ORM para gerenciamento do banco SQLite

HTML e CSS  para o front-end

Flask-CORS para permitir comunicação entre front-end e back-end

✨ Funcionalidades

Criar tarefas com título e descrição

Listar todas as tarefas

Atualizar tarefas (marcar como concluída)

Deletar tarefas

🏗 Estrutura do Projeto
gerenciador-tarefas/
│── backend/
│   └── app.py          # Flask + SQLAlchemy + rotas da API
│── frontend/
    ├── templates/
│       └── index.html      # Interface web
    └── static/
         ├── css/
         └── 3c1matu3-removebg-preview.png
│── requirements.txt    # Dependências Python
│── .gitignore
│── README.md


O banco SQLite (tarefas.db) é gerado automaticamente ao rodar a aplicação.

🚀 Como Rodar Localmente

Recomendado Python 3.10 ou superior

Criar e ativar um ambiente virtual:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate


Instalar dependências:

pip install -r requirements.txt


Rodar o back-end:

cd backend
python app.py


A API ficará disponível em http://127.0.0.1:5000.

Abrir o front-end:

Clique duas vezes em frontend/index.html
ou

Use um servidor local simples:

cd frontend
python -m http.server 8000
# acesse http://127.0.0.1:8000

🧪 Rotas da API

GET /tarefas → lista todas as tarefas

POST /tarefas → cria nova tarefa

{ "titulo": "Estudar", "descricao": "Flask + ORM" }


PUT /tarefas/<id> → marca tarefa como concluída

DELETE /tarefas/<id> → remove tarefa

Exemplo via curl:

curl -X POST http://127.0.0.1:5000/tarefas \
-H "Content-Type: application/json" \
-d '{"titulo":"Estudar","descricao":"Flask"}'
