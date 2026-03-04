# 🚀 Task Manager API

A simple and clean **RESTful API** built with **FastAPI** for managing tasks.
This project demonstrates how to build a backend service with **Python**, **SQLAlchemy**, and **SQLite**.

It supports full **CRUD operations** and includes automatically generated API documentation.

---

# 📌 Features

* Create tasks
* Retrieve all tasks
* Retrieve a single task
* Update tasks
* Delete tasks
* Automatic API documentation

---

# 🧠 What This Project Demonstrates

This project demonstrates key backend development concepts:

* REST API design
* CRUD operations
* Database integration
* ORM usage
* API documentation

---

# 🛠 Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

---

# 📂 Project Structure

task-manager-api

main.py – FastAPI application entry point
database.py – database connection configuration
models.py – SQLAlchemy models
schemas.py – request and response schemas
tasks.db – SQLite database
requirements.txt – project dependencies

---

# ▶️ How to Run the Project

Clone the repository:

git clone https://github.com/Timur-Chen/task-manager-api.git

Navigate to the project folder:

cd task-manager-api

Create virtual environment:

python -m venv venv

Activate the environment:

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn main:app --reload

---

# 📖 API Documentation

Once the server is running, open:

http://127.0.0.1:8000/docs

This interactive interface allows you to test all API endpoints.

---

# 📌 Example Task JSON

{
"title": "Learn FastAPI",
"completed": false
}

---

# 🎯 API Endpoints

GET /tasks – Get all tasks
POST /tasks – Create a new task
GET /tasks/{task_id} – Get a specific task
PUT /tasks/{task_id} – Update a task
DELETE /tasks/{task_id} – Delete a task

---

# 📈 Future Improvements

Possible improvements for the project:

* User authentication
* PostgreSQL database
* Docker support
* Pagination for tasks
* Task categories

---

# 👨‍💻 Author

Built as a backend practice project using FastAPI.
