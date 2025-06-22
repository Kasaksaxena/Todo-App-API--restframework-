# 📝 Django REST Framework Todo API

A secure and modular *To-Do List API* built using Django and Django REST Framework (DRF).  
This project allows users to log in via token-based authentication and manage their personal todos (Create, Read, Update, Delete).

---

## 🚀 Features

- 🔐 Token-based authentication (Login required)
- ✅ CRUD functionality (Create, Read, Update, Delete)
- 👤 Todos linked to individual users
- 📅 Automatically tracks created/updated timestamps
- 🛡 Auth-protected API endpoints
- 💬 Tested using Postman

---

## 📂 Tech Stack

- *Backend*: Django, Django REST Framework
- *Authentication*: DRF TokenAuth
- *Database*: SQLite (default)
- *Testing*: Postman

---

## 📦 API Endpoints

| Method | Endpoint                      | Description                | Auth Required |
|--------|-------------------------------|----------------------------|----------------|
| POST   | /api/login/                 | Obtain token via login     | ❌ No |
| GET    | /api/todos/                 | List all user todos        | ✅ Yes |
| POST   | /api/todos/                 | Create a new todo          | ✅ Yes |
| GET    | /api/todos/<uuid>/         | View a specific todo       | ✅ Yes |
| PUT    | /api/todos/<uuid>/         | Update a specific todo     | ✅ Yes |
| DELETE | /api/todos/<uuid>/         | Delete a specific todo     | ✅ Yes |

---

## 🧪 Sample Request (POST /api/todos/)
