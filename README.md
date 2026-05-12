# FinTrack

Sistema web de controle financeiro desenvolvido com Django e Django REST Framework.

## 🚀 Funcionalidades

- Cadastro de receitas e despesas
- Categorização de transações
- Dashboard financeiro
- Insights automáticos
- Gráficos interativos com Chart.js
- API REST
- Autenticação de usuários
- Ambiente containerizado com Docker

## 🧠 Arquitetura

O projeto foi estruturado utilizando separação de responsabilidades:

- Views
- Services
- Selectors
- Serializers

## 🛠️ Tecnologias

- Python 3.13
- Django
- Django REST Framework
- PostgreSQL
- Docker + Docker Compose
- Bootstrap
- Chart.js

## ▶️ Como executar

### Rodando localmente (sem Docker)

### 1. Clonar projeto

```bash
git clone https://github.com/DiegoBasgal/Fintrack.git
cd fintrack
```

---

### 2. Criar ambiente virtual

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env`:

```env
DB_NAME=fintrack_db
DB_USER=postgres
DB_PASSWORD=PostMaster99
DB_HOST=localhost
DB_PORT=5432
```

---

### 5. Rodar migrations

```bash
python manage.py migrate
```

---

### 6. Criar superusuário

```bash
python manage.py createsuperuser
```

---

### 7. Executar servidor

```bash
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000
```

---

### Rodando com Docker

### Pré-requisitos

Instalar Docker Desktop.

Verificar:

```bash
docker --version
docker compose version
```

---

### Subir containers

```bash
docker compose up --build
```

---

### Rodar migrations

Em outro terminal:

```bash
docker compose exec web python manage.py migrate
```

---

### Criar superusuário

```bash
docker compose exec web python manage.py createsuperuser
```

---

### Acessar aplicação

```text
http://127.0.0.1:8000
```

---

### Parar containers

```bash
docker compose down
```

---

### Resetar banco Docker

```bash
docker compose down -v
```


## 📌 API

Endpoint:

``` id="qphf5q"
/api/transactions/
```

## 👨‍💻 Autor

Diego Basgal Gasparoto Garcia