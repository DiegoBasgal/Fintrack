# FinTrack

Sistema web de controle financeiro desenvolvido com Django e Django REST Framework.

## 🚀 Funcionalidades

- Cadastro de receitas e despesas
- Dashboard financeiro
- Insights automáticos
- API REST
- Autenticação de usuários

## 🧠 Arquitetura

O projeto foi estruturado utilizando separação de responsabilidades:

- Views
- Services
- Selectors
- Serializers

## 🛠️ Tecnologias

- Python
- Django
- Django REST Framework
- SQLite

## ▶️ Como executar

```bash
git clone <repo>
cd fintrack

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

## 📌 API

Endpoint:

``` id="qphf5q"
/api/transactions/
```

## 👨‍💻 Autor

Diego Basgal Gasparoto Garcia