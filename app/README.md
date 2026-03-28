
# 🚀 FastAPI Project

Este repositório contém uma aplicação desenvolvida com **FastAPI**, focada em alta performance, simplicidade e escalabilidade para construção de APIs modernas.

---

## 📁 Estrutura do Projeto

```bash
.
├── app/
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── api/             # Rotas da aplicação
│   ├── core/            # Configurações e utilidades
│   └── services/        # Regras de negócio
├── .venv/               # Ambiente virtual (não versionado)
├── .vscode/
│   └── launch.json      # Configuração de debug
├── requirements.txt     # Dependências do projeto
└── README.md
````

---

## ⚙️ Pré-requisitos

* Python 3.8+
* pip
* (Opcional) VS Code

---

## 🐍 Configuração do Ambiente

### 1. Criar ambiente virtual

```bash
python3 -m venv .venv
```

### 2. Ativar o ambiente

#### Linux/macOS:

```bash
source .venv/bin/activate
```

#### Windows:

```powershell
.venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Como rodar o projeto

### 🔥 Rodando via terminal

```bash
uvicorn app.main:app --reload
```

A aplicação estará disponível em:

```
http://127.0.0.1:8000
```

---

### 🧪 Documentação automática da API

* Swagger UI:

  ```
  http://127.0.0.1:8000/docs
  ```

* ReDoc:

  ```
  http://127.0.0.1:8000/redoc
  ```

---

## 🐞 Debug no VS Code

O projeto já possui configuração pronta para debug no arquivo:

```
.vscode/launch.json
```

### Configuração utilizada:

```json
{
    "name": "Python Debugger: FastAPI",
    "type": "debugpy",
    "request": "launch",
    "module": "uvicorn",
    "args": [
        "app.main:app",
        "--reload"
    ],
    "jinja": true
}
```

### ▶️ Como usar:

1. Abra o projeto no VS Code
2. Vá até a aba **Run and Debug** (Ctrl + Shift + D)
3. Selecione:

   ```
   Python Debugger: FastAPI
   ```
4. Clique em **Run**

---

## 📦 Tecnologias utilizadas

* FastAPI
* Uvicorn
* Python

---

## 📌 Boas práticas

* Utilize `.env` para variáveis de ambiente
* Nunca versionar `.venv`
* Separar regras de negócio em `services`
* Organizar rotas por domínio em `api`

---

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch:

   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações
4. Push:

   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT.

