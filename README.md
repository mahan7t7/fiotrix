#  Tasks Management API

This repository contains a simple and clean **FastAPI** application connected to a **PostgreSQL** database.  
It provides a fully functional RESTful API for managing tasks — including creating, reading, updating, and deleting records.  

The project is designed to be lightweight, modular, and production-ready for deployment on a **Linux VPS** using **Gunicorn** and **Nginx**.

---

##  Key Features

- CRUD operations for managing tasks  
- High-performance backend built with **FastAPI**  
- Database powered by **PostgreSQL**  
- Organized modular structure for scalability  
- Interactive API documentation via **Swagger UI** and **Redoc**  
- Production-ready setup using **Gunicorn**, **Uvicorn**, **Systemd** and **Nginx**  
- Environment-based configuration through `.env`

---

##  Project Structure

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

##  Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend** | FastAPI |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Validation** | Pydantic |
| **Server** | Gunicorn + Uvicorn Workers |
| **Reverse Proxy** | Nginx |
| **OS** | Ubuntu 22.04+ |

---

##  API Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/tasks/` | Retrieve all tasks |
| `GET` | `/tasks/{id}` | Retrieve a specific task |
| `POST` | `/tasks/` | Create a new task |
| `PUT` | `/tasks/{id}` | Update a task |
| `DELETE` | `/tasks/{id}` | Delete a task |

---

##  Example Task Object

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

##  Environment Variables

Create a `.env` file in the root directory of your project and define:

```
DATABASE_URL=postgresql+psycopg2://postgres:yourpassword@localhost:5432/tasks_db
APP_DEBUG=False
```



##  Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/fastapi-tasks.git
cd fastapi-tasks
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate      # On Linux or macOS
.venv\Scripts\activate         # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application Locally
```bash
uvicorn app.main:app --reload
```

### 5. Access the API Docs
- Swagger UI → http://127.0.0.1:8000/docs  
- Redoc → http://127.0.0.1:8000/redoc

---

##  VPS Deployment (Ubuntu + Gunicorn + Nginx)

###  1. Update and Install Dependencies
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-venv python3-pip postgresql nginx git -y
```

###  2. Clone the Project
```bash
cd /home/ubuntu
git clone https://github.com/mahan7t7/fiotrix.git
cd fastapi-tasks
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

###  3. Setup PostgreSQL
```bash
sudo -u postgres psql
CREATE DATABASE tasks_db;
CREATE USER fastapi_user WITH PASSWORD 'yourpassword';
ALTER ROLE fastapi_user SET client_encoding TO 'utf8';
ALTER ROLE fastapi_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE fastapi_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE tasks_db TO fastapi_user;
\q
```

Then, update `.env`:
```
DATABASE_URL=postgresql+psycopg2://fastapi_user:yourpassword@localhost:5432/tasks_db
APP_DEBUG=False
```

###  4. Start Gunicorn Service
Test manually first:
```bash
gunicorn app.main:app -w 3 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

If it runs correctly, create a **systemd service**:

`sudo nano /etc/systemd/system/fastapi.service`
```ini
[Unit]
Description=FastAPI Gunicorn Service
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/fastapi-tasks
ExecStart=/home/ubuntu/fastapi-tasks/.venv/bin/gunicorn app.main:app -w 3 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start it:
```bash
sudo systemctl daemon-reload
sudo systemctl enable fastapi.service
sudo systemctl start fastapi.service
sudo systemctl status fastapi.service
```

###  5. Configure Nginx Reverse Proxy
`sudo nano /etc/nginx/sites-available/fastapi`
```nginx
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable site and restart Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/fastapi /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```



##  Author

**Mahan Tarighati**  
Back-end Developer — Python | Django | FastAPI   
 mahan7t7@gmail.com  

---
