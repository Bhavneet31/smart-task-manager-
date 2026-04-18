# 🚀 Smart Task Manager

A full-stack task management application built using Flask (backend) and HTML, CSS, JavaScript (frontend).

---

## 🔥 Features

- 🔐 User Authentication (JWT)
- 📝 Create, Update, Delete Tasks
- 📊 Task Analytics
- 📋 Dashboard UI
- 🔒 Protected APIs

---

## 🛠️ Tech Stack

### Backend:
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Flask-Bcrypt
- Flask-Limiter

### Frontend:
- HTML
- CSS
- JavaScript

### Database:
- SQLite

---
## 📂 Project Structure
smart-task-manager/
│
├── app/
│ ├── models/
│ ├── routes/
│ ├── services/
│ ├── config.py
│ └── init.py
│
├── frontend/
│ ├── index.html
│ ├── register.html
│ ├── dashboard.html
│ ├── style.css
│ └── script.js
│
├── .env
├── .gitignore
├── requirements.txt
└── run.py





## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-task-manager.git
cd smart-task-manager

###  setup backend 
python -m venv venv
venv\Scripts\Activate   # Windows
pip install -r requirements.txt
python run.py

### run Frontend 
cd frontend
python -m http.server 5500


###   🔐 API Endpoints
Auth
POST /api/auth/register → Register user
POST /api/auth/login → Login (returns JWT token)
Tasks
GET /api/tasks/ → Get all tasks
POST /api/tasks/ → Create task
PUT /api/tasks/<id> → Update task
DELETE /api/tasks/<id> → Delete task
Analytics
GET /api/analytics/ → Task statistics

### 💡 How it Works
User registers and logs in
Backend returns a JWT token
Token is stored in browser (localStorage)
All protected requests use this token
User manages tasks through dashboard

### 🚀 Future Improvements
React frontend
Better UI/UX design
Task deadlines & reminders
Deployment (Render / Vercel / AWS)


### 👨‍💻 Author

Bhavneet Singh
