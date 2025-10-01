# 📚 FastAPI + MongoDB (PyMongo, Síncrono) — Projeto Completo

Este projeto é um exemplo **completo e organizado** de API usando:

- ⚡ **FastAPI** — framework rápido e moderno para APIs REST
- 🍃 **PyMongo** — conexão **síncrona** com MongoDB (sem async e sem Motor)
- 📁 Arquitetura **limpa e separada**: Controllers (routers), Services e Models
- 🔄 Conversão automática de `_id` ↔ `id`
- ▶️ Execução direta com `python -m app.main`

---

## 📁 Estrutura do Projeto

```
fastapi_mongo_sync_clean/
├─ app/
│  ├─ main.py                 # ponto de entrada (tem if __main__)
│  ├─ db.py                   # conexão MongoDB
│  ├─ utils/
│  │  └─ io.py                # funções auxiliares
│  ├─ models/
│  │  ├─ aluno.py             # modelos de entrada/atualização
│  │  └─ curso.py
│  ├─ services/
│  │  ├─ alunos_service.py
│  │  └─ cursos_service.py
│  └─ routers/
│     ├─ alunos_controller.py
│     └─ cursos_controller.py
├─ requirements.txt
└─ .env.example
```

---

## 🚀 Passo a Passo para Rodar

### 1️⃣ Subir o MongoDB

Se quiser rodar localmente via Docker:

```bash
docker run -d --name mongo -p 27017:27017 mongo:6
```

### 2️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Rodar a Aplicação

✅ **Opção 1 — via uvicorn:**

```bash
uvicorn app.main:app --reload
```

✅ **Opção 2 — diretamente pelo arquivo principal:**

```bash
python -m app.main
```

- 📍 API disponível em: http://127.0.0.1:8000  
- 📘 Documentação Swagger: http://127.0.0.1:8000/docs

---

## 🔥 Executando com `if __main__`

O arquivo `app/main.py` já vem com:

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
```

Isso significa que você pode iniciar o servidor com:

```bash
python -m app.main
```

---

## 🔎 Endpoints Disponíveis

### 🧑‍🎓 Alunos

| Método | Endpoint                               | Descrição                       |
|-------:|----------------------------------------|----------------------------------|
| POST   | `/alunos`                              | Criar aluno                     |
| GET    | `/alunos`                              | Listar alunos                   |
| GET    | `/alunos/{id}`                         | Obter aluno por ID              |
| PATCH  | `/alunos/{id}`                         | Atualizar aluno                 |
| DELETE | `/alunos/{id}`                         | Remover aluno                   |
| PATCH  | `/alunos/{id}/matricular?curso_id={id}`| Matricular aluno em curso       |

### 📘 Cursos

| Método | Endpoint           | Descrição             |
|-------:|--------------------|-----------------------|
| POST   | `/cursos`          | Criar curso           |
| GET    | `/cursos`          | Listar cursos         |
| GET    | `/cursos/{id}`     | Obter curso por ID    |
| PATCH  | `/cursos/{id}`     | Atualizar curso       |
| DELETE | `/cursos/{id}`     | Remover curso         |

---

## 📤 Exemplos de JSON

### 📘 Criar Curso — `POST /cursos`

```json
{
  "titulo": "Algoritmos I",
  "descricao": "Introdução à análise de algoritmos e estruturas de dados."
}
```

### 📘 Atualizar Curso — `PATCH /cursos/{id}`

```json
{
  "descricao": "Conteúdo atualizado com listas, filas, pilhas e árvores."
}
```

### 📘 Resposta de Curso

```json
{
  "id": "66f04c8f6f2e0a1d1c3b2a90",
  "titulo": "Algoritmos I",
  "descricao": "Introdução à análise de algoritmos e estruturas de dados."
}
```

### 🧑‍🎓 Criar Aluno — `POST /alunos`

```json
{
  "nome": "Maria Silva",
  "email": "maria.silva@example.com",
  "curso_ids": ["66f04c8f6f2e0a1d1c3b2a90"]
}
```

### 🧑‍🎓 Atualizar Aluno — `PATCH /alunos/{id}`

```json
{
  "nome": "Maria A. Silva",
  "curso_ids": ["66f04c8f6f2e0a1d1c3b2a90", "66f0502b6f2e0a1d1c3b2aa1"]
}
```

### 🧑‍🎓 Resposta de Aluno

```json
{
  "id": "66f0513d6f2e0a1d1c3b2ab2",
  "nome": "Maria Silva",
  "email": "maria.silva@example.com",
  "curso_ids": ["66f04c8f6f2e0a1d1c3b2a90"]
}
```

---

## 🩺 Healthcheck

Verifique se a API está funcionando:

**Requisição:**

```
GET /health
```

**Resposta:**

```json
{
  "status": "ok"
}
```

---

## 🔧 Paginação

Os endpoints `GET /alunos` e `GET /cursos` suportam paginação:

```
GET /alunos?skip=0&limit=20
```

- `skip`: número de registros a pular (default: 0)  
- `limit`: número máximo de registros (default: 20)

---

## 🧪 Códigos de Status Importantes

| Código | Significado                      |
|------:|-----------------------------------|
| 200   | Sucesso                           |
| 201   | Criado com sucesso                |
| 204   | Sem conteúdo (remoção)            |
| 400   | ID inválido ou payload incorreto  |
| 404   | Recurso não encontrado            |

---

## 🛠️ Tecnologias Utilizadas

- 🐍 Python 3.10+
- ⚡ FastAPI
- 🍃 PyMongo
- 🗄️ MongoDB
- 🔥 Uvicorn

---

## 💡 Dicas Finais

- Sempre envie `curso_ids` como **lista de strings** com IDs válidos do MongoDB.  
- A API converte automaticamente `_id` para `id` em todas as respostas.  
- Se `ObjectId` for inválido → retorna **400**.  
- Se o recurso não for encontrado → retorna **404**.
