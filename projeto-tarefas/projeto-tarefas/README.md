
# Gerenciador de Tarefas (Python + Flask + ORM + JavaScript)

Projeto simples de **CRUD de tarefas** para demonstrar:
- **Back-end** em Python com **Flask**
- **ORM** com **SQLAlchemy** (SQLite)
- **API REST** consumida por um **front-end** em JavaScript

Ideal para portfólio e entrevistas de estágio.

---

## ✨ Funcionalidades
- Criar tarefa (título e descrição)
- Listar tarefas
- Concluir tarefa
- Deletar tarefa

---

## 🧱 Arquitetura
```
projeto-tarefas/
│── backend/
│   └── app.py          # Flask + SQLAlchemy + rotas
│── frontend/
│   ├── index.html      # UI simples
│   └── script.js       # Consome a API com fetch
│── requirements.txt
│── .gitignore
│── README.md
```
O banco usado é **SQLite** (arquivo `tarefas.db` gerado automaticamente).

---

## 🚀 Como rodar (local)
> Recomendado Python 3.10+

1. Crie e ative um ambiente virtual na raiz do projeto:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Rode o back-end:
   ```bash
   cd backend
   python app.py
   ```
   A API subirá em `http://127.0.0.1:5000`.

4. Abra o front-end:
   - Clique duas vezes em `frontend/index.html` ou
   - Sirva com um servidor simples:
     ```bash
     # na pasta frontend
     python -m http.server 8000
     # acesse http://127.0.0.1:8000
     ```

> **Observação:** O CORS já está liberado no Flask via `Flask-Cors`, então o front-end (em file:// ou porta 8000) consegue consumir a API.

---

## 🧪 Rotas da API
- `GET /tarefas` → lista todas
- `POST /tarefas` → cria tarefa  
  Body JSON: `{ "titulo": "Estudar", "descricao": "ORM e JS" }`
- `PUT /tarefas/<id>` → marca como **concluída**
- `DELETE /tarefas/<id>` → remove

Exemplo via `curl`:
```bash
curl -X POST http://127.0.0.1:5000/tarefas -H "Content-Type: application/json" -d "{"titulo":"Estudar","descricao":"Flask"}"
```

---

## 📤 Como publicar no GitHub (rápido)
1. Crie um repositório chamado **gerenciador-tarefas** no GitHub (sem README).
2. Na raiz do projeto, rode:
   ```bash
   git init
   git add .
   git commit -m "Projeto: Flask + ORM + JS (CRUD de tarefas)"
   git branch -M main
   git remote add origin https://github.com/<seu-usuario>/gerenciador-tarefas.git
   git push -u origin main
   ```

### Alternativa pelo site (sem Git instalado)
- No GitHub, clique em **Add file → Upload files**, arraste a pasta toda e confirme o commit.

---

## 🎥 Dica de apresentação
- Grave um vídeo curto (1–2 min) criando, concluindo e deletando tarefas.  
- Pode usar **Loom** (mais fácil) ou **OBS Studio**.  
- Coloque o link do vídeo aqui no README (YouTube não listado ou Loom).

---

## 🧾 Licença
MIT — sinta-se à vontade para usar e melhorar.
