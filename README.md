# 🗂️ Tasks Management API

This repository contains a simple and clean **FastAPI** application connected to a **PostgreSQL** database.  
It provides a fully functional RESTful API for managing tasks — including creating, reading, updating, and deleting records.  

The project is designed to be lightweight, modular, and ready for deployment on services such as **Render.com** or any Linux-based server.

---

## 🚀 Key Features

- CRUD operations for managing tasks  
- High-performance backend built with **FastAPI**  
- Database powered by **PostgreSQL**  
- Organized modular structure for scalability  
- Interactive API documentation via **Swagger UI** and **Redoc**  
- Easy deployment using **Uvicorn** or **Gunicorn**  
- Environment-based configuration through `.env`

---

## 🏗️ Project Structure

```
app/
│── main.py          # Application entry point
│── config.py        # Environment configuration
│── database.py      # Database setup
│── models.py        # SQLAlchemy ORM models
│── schemas.py       # Pydantic models for validation
│── crud.py          # CRUD operations
│── routers/
│   └── tasks.py     # API endpoints for tasks
│
requirements.txt      # Python dependencies
.env.example          # Example environment variables
README.md             # Project documentation
```

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend** | FastAPI |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Validation** | Pydantic |
| **Server** | Uvicorn / Gunicorn |
| **Deployment** | Render.com / Linux Server |

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/tasks/` | Retrieve all tasks |
| `GET` | `/tasks/{id}` | Retrieve a specific task |
| `POST` | `/tasks/` | Create a new task |
| `PUT` | `/tasks/{id}` | Update a task |
| `DELETE` | `/tasks/{id}` | Delete a task |

---

## 🧩 Example Task Object

```json
{
  "id": 1,
  "title": "Write documentation",
  "description": "Prepare a detailed README for the FastAPI project",
  "is_completed": false,
  "created_at": "2025-11-02T12:00:00Z"
}
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory of your project and define:

```
DATABASE_URL=postgresql+psycopg2://postgres:yourpassword@localhost:5432/tasks_db
APP_DEBUG=True
```


## 🧱 Local Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/fastapi-tasks.git
cd fastapi-tasks
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate      # On Linux or macOS
.venv\Scripts\activate         # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
uvicorn app.main:app --reload
```

### 5️⃣ Access the API Docs
- Swagger UI → http://127.0.0.1:8000/docs  
- Redoc → http://127.0.0.1:8000/redoc

---

## ☁️ Deployment on Render.com

1. Push your project to GitHub  
2. Create a new **Web Service** on [Render.com](https://render.com)  
3. Connect your GitHub repository  
4. Configure the settings as follows:

| Option | Value |
|--------|--------|
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |

5. Create a PostgreSQL database on Render  
6. Copy the database connection string and add it as an environment variable:

```
DATABASE_URL=postgresql+psycopg2://user:password@host:5432/dbname
```

7. Deploy and access your live API at:  
👉 `https://your-app-name.onrender.com/docs`

---


## 👨‍💻 Author

**Mahan Tarighati**  
Back-end Developer — Python | Django | FastAPI  
📧 mahan7t7@gmail.com 

---

